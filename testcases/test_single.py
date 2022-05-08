from common.httphandler import HttpHander
from common.yml_util import YmlUtil
import pytest, json
http = HttpHander()
YmlUt = YmlUtil()

class TestCaseSingle:

    def get_case_all(self, case_data, header):
        if case_data["method"] == 'get':
            resp = http.get(url=case_data["url"], headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data["assert_data"] in resp

        elif case_data["method"] == 'post':
            data = case_data["param"]
            resp = http.post(url=case_data["url"], json=case_data["param"], headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data["assert_data"] in resp
        else:
            return

    @pytest.mark.parametrize('yml_path,case_id', YmlUt.read_yaml_all_tuple("case_single"))
    def test_case_all(self, yml_path, case_id):
        yml_value = YmlUt.read_yaml_values(yml_path)
        case_data = YmlUt.get_value(yml_value, case_id)
        try:
            header = YmlUt.read_yaml_values(YmlUt.read_yaml_paths("token_head")[0])["headers"]
            # print(header)
            self.get_case_all(case_data, header)
        except Exception as e:
            print(e)







