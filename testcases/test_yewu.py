from common.httphandler import HttpHander
from common.yml_util import YmlUtil
import pytest, json
http = HttpHander()
YmlUt = YmlUtil()

class TestQdcx:

    def get_case_resp(self, yml_name, case_id, case_data, header):
        if case_data["method"] == 'get':
            resp = http.get(url=case_data["url"], headers=header)
            print(resp)
            assert case_data["assert_data"] in resp
            if "output_name" in case_data.keys():
                output_key = case_data["output_value"]
                YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)

        else:
            data = case_data["param"]
            if "insert_value" in case_data.keys():
                insert_value = YmlUt.read_yaml_values("token_head")[case_data["insert_value"]]
                print(insert_value)
                yml_value_in = YmlUt.read_yaml_values(yml_name, {"insert_value": insert_value})
                case_data_in = YmlUt.get_value(yml_value_in, case_id)
                print(case_data_in)
                resp = http.post(url=case_data["url"], json=case_data_in["param"], headers=header)
                assert case_data["assert_data"] in resp
                if "output_name" in case_data.keys():
                    output_key = case_data["output_value"]
                    YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)

            else:
                resp = http.post(url=case_data["url"], json=case_data["param"], headers=header)
                assert case_data["assert_data"] in resp
                if "output_name" in case_data.keys():
                    output_key = case_data["output_value"]
                    print(resp)
                    YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)


    @pytest.mark.parametrize('yml_name,case_id', YmlUt.read_yaml_all_tuple("case_"))
    def test_case_all(self, yml_name, case_id):
        try:
            header = YmlUt.read_yaml_values("token_head")["headers"]
            print(header)
            yml_value = YmlUt.read_yaml_values(yml_name)
            case_data = YmlUt.get_value(yml_value, case_id)
            self.get_case_resp(yml_name, case_id, case_data, header)
        except Exception as e:
            print(e)








