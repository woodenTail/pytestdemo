import re

import requests

from common.request_util import RequestUtil
from common.yaml_util import write_extract_file, read_extract_file


class TestRequests2:
    access_token = ""
    csrf_token = ""

    def test_phpwind_start(self):
        url = "/phpwind"

        res = RequestUtil('base','base_php_url').send_request(method='get', url=url)
        data = res.text
        #通过正则表达式取值
        obj = re.search('name="csrf_token" value="(.*?)"', data)
        extract_data = {'csrf_token': obj.group(1)}
        write_extract_file(extract_data)

    def test_login(self):
        url = "/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username":"wangsan",
            "password" :"123456",
            "csrf_token": "{{csrf_token}}",
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers = {
            "Accept":"application/json, text/javascript, /; q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        # res = TestRequests.session.request("post",url, data=data, headers=headers)
        res = RequestUtil('base','base_php_url').send_request('post', url, data=data,  headers=headers)
        print(res.text)