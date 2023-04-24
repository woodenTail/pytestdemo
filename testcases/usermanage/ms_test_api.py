import json

import allure
import pytest
import requests
import yaml

#读取yaml
def read_yaml(yaml_path):
    with open(yaml_path, mode="r",encoding="utf-8") as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


@allure.epic("项目名称：木鸢自动化测试项目")
@allure.feature("模块名称：用户管理模块")
class TestApi:
    #
    # def setup_class(self):
    #     print("在每个类之前执行，创建日志对象，创建数据库连接等")
    #
    # def teardown_class(self):
    #     print("在每个类之后执行")
    #
    # def setup(self):
    #     print("在每个用例之前执行，web自动化，打开浏览器，加载网页，日志开始等")
    #
    # def teardown(self):
    #     print("在每个日志之后执行")

    @allure.story("接口名称：测试_百里")
    @allure.title("测试用例标题：test_baili")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("测试用例描述1")
    @pytest.mark.smoke
    def test_baili(self, excute_sql,user_setup):
        allure.dynamic.description("测试用例描述2")
        #增加步骤
        for a in range(1,10):
            with allure.step("测试用例步骤"+str(a)):
                print("步骤"+str(a)+"执行的脚本")
        print("测试1" )
        #附件的定制
        with open ("d:\\1.png",mode="rb") as f:
         allure.attach(body=f.read(), name="错误截图", attachment_type=allure.attachment_type.PNG)

        #接口自动化测试
        allure.attach(body="https://api.weixin.qq.com/cgi-bin/token",name="请求地址", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body="get",name="请求方式",attachment_type=allure.attachment_type.TEXT)
        data ={
            "grant_type":"client_credential",
            "appid":"wx6b11b3efd1cdc290",
            "secret":"106a9c6157c4db5f6029918738f9529d"
        }
        allure.attach(body=json.dumps(data),name="请求数据",attachment_type=allure.attachment_type.TEXT)
        rep = requests.get(url="https://api.weixin.qq.com/cgi-bin/token",params=data)
        allure.attach(body=rep.text, name="响应数据", attachment_type=allure.attachment_type.TEXT)


    @allure.story("接口名称：木鸢")
    @pytest.mark.parametrize("caseinfo",read_yaml("./testcases/usermanage/get_token_case.yml"))
    @pytest.mark.smoke
    def test_muyuan(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['desc'])
        allure.attach(body=caseinfo['request']['url'])
        allure.attach(body=caseinfo['request']['url'], name="请求地址",
                      attachment_type=allure.attachment_type.TEXT)
        data = caseinfo['request']['data']
        allure.attach(body="get", name="请求方式", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=json.dumps(data), name="请求数据", attachment_type=allure.attachment_type.TEXT)
        rep = requests.get(caseinfo['request']['url'], params=data)
        allure.attach(body=rep.text, name="响应数据", attachment_type=allure.attachment_type.TEXT)

        print(caseinfo)

    @allure.story("接口名称：查询商品")
    @pytest.mark.parametrize("name,age",[['百里',13],['星瑶',11],['木鸢',10]])
    @pytest.mark.productmanage
    def test_product_manage_weiwei(self, name,age):
        print("测试2",name,age)