import json
import random

import requests

from common.request_util import RequestUtil
from common.yaml_util import write_extract_file, read_extract_file


class TestRequests1:
    access_token = ""
    csrf_token = ""
    session = requests.session() #获得请求的session对象

    # def test_get(self):
    #
    #     url = "/cgi-bin/token"
    #     params = {
    #         "grant_type":"client_credential",
    #         "appid": "wx74a8627810cfa308",
    #         "secret": "e40a02f9d79a8097df497e6aaf93ab80"
    #     }
    #     res = RequestUtil().send_request('test_get','get', url, params=params)
    #     # res = requests.get(url,params)
    #     data = res.json()
    #     # 把中间变量写入extract.yml文件
    #     extract_data = {'access_token': data['access_token']}
    #     write_extract_file(extract_data)
    #     print(res.text)
    #
    # def  test_get2(self):
    #     url = "/cgi-bin/tags/get?access_token"
    #     params = {
    #         "access_token":"{{access_token}}"
    #     }
    #     res = RequestUtil().send_request('test_get2','get', url, params=params)
    #     print(res.text)
    #
    # def test_post2(self):
    #     url = "/cgi-bin/tags/update?access_token={{access_token}}"
    #     data = {"tag":{"id":8558, "name":"木鸢"+str(random.randint(1,100000))}}
    #
    #     res = RequestUtil().send_request('test_post2','post', url, data=json.dumps(data))
    #     print(res.text)
    #
    # def test_file_upload(self):
    #     url = "/cgi-bin/media/uploadimg?access_token={{access_token}}"
    #     data = {
    #         "media":open("d:\\1.png", "rb")
    #     }
    #     res = RequestUtil().send_request('test_file_upload','post', url, files=data)
    #     print(res.text)

