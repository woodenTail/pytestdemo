import json
import re

import jsonpath as jsonpath
import requests

from common import yaml_util
from common.yaml_util import read_config_file, read_extract_file, write_extract_file
from debug_talk import DebugTalk


class RequestUtil:

    session = requests.session()

    def __init__(self, base, base_url):
        self.base_url = read_config_file(base, base_url)
        self.last_header = {}

    #规范功能测试yaml文件的写法
    def analysis_yaml(self, caseinfo):
        #1.必须有的四个一级关键字：name,base_url,request,validate
        caseinfo_keys = dict(caseinfo).keys()
        if 'name' in caseinfo_keys and 'base_url' in caseinfo_keys and 'request' in caseinfo_keys\
                and 'validate' in caseinfo_keys:
            #2.在request一级关键字下必须包含两个二级关键字，method、URL
            request_keys = dict(caseinfo['request']).keys()

            if 'method' in request_keys and 'url' in request_keys:
                headers = None
                method = caseinfo['request']['method']
                del caseinfo['request']['method']
                url = caseinfo['request']['url']
                del caseinfo['request']['url']

                if jsonpath.jsonpath(caseinfo, '$..headers'):
                    headers = caseinfo['request']['headers']
                    del caseinfo['request']['headers']
                files = None
                if jsonpath.jsonpath(caseinfo, '$..files'):
                    files = caseinfo['request']['files']
                    for key,value in dict(files).items():
                        files[key] = open(value,'rb')
                    del caseinfo['request']['files']

                res = self.send_request(method=method,
                                        url=url,
                                        headers=headers,files=files,
                                        **caseinfo['request'])
                return_data = res.json()
                return_text = res.text

                #提取接口关联的变量,既要支持正则表达式，又要支持json提取
                if 'extract' in caseinfo_keys:
                    for key,value in dict(caseinfo['extract']).items():
                        # 正则提取
                        if '(.+?)' in value or '(.*?)' in value:
                            ze_value = re.search(value, return_text)
                            if ze_value:
                                extract_data = {key: ze_value.group(1)}
                                write_extract_file(extract_data)
                        else: #json提取
                            if value in return_data:
                                extract_data = {key: return_data[value]}
                                write_extract_file(extract_data)
                # 断言的封装
                yq_result = caseinfo['validate']
                self.validate_result(yq_result, return_data, res.status_code)
                return res
            else:
                print('在request一级关键字下必须包含两个二级关键字，method、URL')
        else:
            print('必须有的四个一级关键字：name,base_url,request,validate')

    #统一替换的方法
    # def replace_value(self, data):
    #     if data and isinstance(data,dict):#如果类型是字典
    #         str_data = json.dumps(data)
    #     else:
    #         str_data = data
    #
    #     for a in range(1, str_data.count('{{') + 1):
    #         if "{{" in str_data and "}}" in str_data:
    #             old_value = str_data[str_data.index("{{"):str_data.index("}}") + 2]
    #             print('=========',old_value[2:-2])
    #             new_value = read_extract_file(old_value[2:-2])
    #
    #             str_data = str_data.replace(old_value, new_value)
    #             print(str_data)
    #     #还原数据类型
    #     if(data and isinstance(data, dict)):
    #         data = json.loads(str_data)
    #     else:
    #         data = str_data
    #     return data

    # 热加载替换解析
    def replace_load(self, data):
        if data and isinstance(data, dict):  # 如果类型是字典
            str_data = json.dumps(data)
        else:
            str_data = data

        for a in range(1, str_data.count('${') + 1):
            if "${" in str_data and "}" in str_data:
                old_value = str_data[str_data.index("${"):str_data.index("}") + 1]
                #反射（通过一个函数的字符串直接去调用这个方法）
                fun_name = old_value[2:old_value.index('(')]
                args_value = old_value[old_value.index('(')+1: old_value.index(')')]
                # print(args_value.split(','))
                #加*表示对list进行解析
                new_value = getattr(DebugTalk(), fun_name)(*args_value.split(','))
                str_data = str_data.replace(old_value, str(new_value))
        # 还原数据类型
        if (data and isinstance(data, dict)):
            data = json.loads(str_data)
        else:
            data = str_data
        return data

    def send_request(self, method, url,headers=None, **kwargs):
        self.base_url = self.base_url + self.replace_load(url);
        self.last_method = str(method).lower()
        #处理请求头
        if headers and isinstance(headers,dict):
            self.last_header = self.replace_load(headers)
        #处理请求数据，可能是params，data，json
        for key,value in kwargs.items():
            if key in ['params','data','json']:
                # #替换{{}}格式
                # value = self.replace_value(value)
                #替换${}格式
                value = self.replace_load(value)
                kwargs[key] = value
                print(kwargs[key])

        res = RequestUtil.session.request(method=self.last_method, url=self.base_url,
                                          headers=self.last_header, **kwargs)
        return res;

    def validate_result(self, yq_result, sj_result, status_code):
        #断言是否成功的标记
        flag = 0
        if yq_result and  isinstance(yq_result, list):
            for yq in yq_result:
                for key,value in dict(yq).items():
                    #判断断言方式
                    if key == 'equals':
                        for assert_key,assert_value in dict(value).items():
                            if assert_key == 'status_code':
                                if status_code != assert_value:
                                    flag = flag +1
                                    print("断言失败"+assert_key+"不等于"+str(assert_value))
                            else:
                                key_list = jsonpath.jsonpath(sj_result,'$..%s'%assert_key)
                                if key_list:
                                    if assert_value not in key_list:
                                        flag = flag + 1
                                        print("断言失败" + assert_key + "不等于" + str(assert_value))
                                else:
                                    flag = flag + 1
                                    print("断言失败:返回结果中不存在" + assert_key)
                    elif key=='contains':
                        if value not in json.dumps(sj_result):
                            flag = flag + 1
                            print("断言失败:返回结果中不包含字符串" + value)
                    else:
                        print("不支持此断言方式")
                    # print(key,value)

        assert flag ==0

if __name__ == '__main__':
    # dic = {'method': 'get', 'url': '/cgi-bin/token', 'data': {'grant_type': 'client_credential', 'appid': 'wx74a8627810cfa308', 'secret': 'e40a02f9d79a8097df497e6aaf93ab80'}}
    # print(dic.pop('method'))
    # print(dic)
    # del dic['url']

    data =  {"tag":{"id":8558, "name":"木鸢${get_random_number(10000,99999)}"}}
    res = RequestUtil('base','base_gzh_url').replace_load(data)
    print(res)
