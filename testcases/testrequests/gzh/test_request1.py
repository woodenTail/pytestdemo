import json

import pytest

from common.parameters_util import  read_testcase_file
from common.request_util import RequestUtil


class TestRequest1:
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/gzh/get_token.yml'))
    def test_get_token(self, caseinfo):
        res = RequestUtil().analysis_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/gzh/select_flag.yml'))
    def  test_select_flag(self, caseinfo):
       res = RequestUtil().analysis_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/gzh/edit_flag.yml'))
    def test_edit_flag(self, caseinfo):
        res = RequestUtil().analysis_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/gzh/file_upload.yml'))
    def test_file_upload(self, caseinfo):
        res = RequestUtil().analysis_yaml(caseinfo)
