import pytest

from common.request_util import RequestUtil
from common.yaml_util import read_testcase_file


class TestRequest1:
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/get_token.yml'))
    def test_get_token(self,caseinfo):
        res = RequestUtil('base','base_gzh_url').analysis_yaml(caseinfo)
        print(res.text)

    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/select_flag.yml'))
    def  test_get2(self, caseinfo):
       res = RequestUtil('base','base_gzh_url').analysis_yaml(caseinfo)
       print(res.text)

    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/edit_flag.yml'))
    def test_edit_flag(self, caseinfo):
        res = RequestUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)
        print(res.text)

    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcases/testrequests/file_upload.yml'))
    def test_file_upload(self, caseinfo):
        res = RequestUtil('base', 'base_gzh_url').analysis_yaml(caseinfo)
        print(res.text)