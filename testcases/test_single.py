from common.httphandler import HttpHander
from common.yml_util import YmlUtil
import pytest, json
http = HttpHander()
YmlUt = YmlUtil()

class TestCaseSingle:

    def get_case_all(self, case_data, url_map, header):
        if case_data.get("method") == 'get':
            resp = http.get(url=url_map, headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data.get("assert_data") in resp

        elif case_data.get("method") == 'post':
            data = case_data.get("param")
            resp = http.post(url=url_map, json=data, headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data.get("assert_data") in resp
        else:
            return

    @pytest.mark.parametrize('yml_path,case_id', YmlUt.read_yaml_all_tuple("case_single"))
    def test_case_all(self, yml_path, case_id):
        yml_value = YmlUt.read_yaml_values(yml_path)
        case_data = YmlUt.get_value(yml_value, case_id)
        header = YmlUt.read_yaml_values(YmlUt.read_yaml_paths("token_head")[0]).get("headers")
        host_map = YmlUt.read_yaml_values(YmlUt.read_yaml_paths("token_head")[0]).get("host_map")
        url_map = YmlUt.host_map_url(case_data, host_map)  # 服务器映射
        # print(header)
        self.get_case_all(case_data, url_map, header)









