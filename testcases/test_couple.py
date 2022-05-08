from common.httphandler import HttpHander
from common.yml_util import YmlUtil
import pytest, json
http = HttpHander()
YmlUt = YmlUtil()

class TestCaseAUD:

    def get_case_all(self, yml_path, case_id, case_data, header):
        if case_data["method"] == 'get':
            resp = http.get(url=case_data["url"], headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data["assert_data"] in resp
            if "output_name" in case_data.keys():
                output_key = case_data["output_index"]
                YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)

        elif case_data["method"] == 'post':
            if "insert_value" in case_data.keys():
                case_data_in = YmlUt.get_value(YmlUt.insert_value(yml_path, case_data), case_id)
                print(case_data_in)
                resp = http.post(url=case_data["url"], json=case_data_in["param"], headers=header)
                print(resp)
                if "assert_data" in case_data.keys():
                    assert case_data["assert_data"] in resp
                if "output_name" in case_data.keys():
                    output_key = case_data["output_index"]
                    YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)

            else:
                resp = http.post(url=case_data["url"], json=case_data["param"], headers=header)
                print(resp)
                if "assert_data" in case_data.keys():
                    assert case_data["assert_data"] in resp
                if "output_name" in case_data.keys():
                    output_key = case_data["output_index"]
                    YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)

        elif case_data["method"] == 'put':
            file_path = YmlUt.get_photo_path(case_data["file_name"])
            resp = http.put(url=case_data["url"], file_path=file_path, headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data["assert_data"] in resp
            if "output_name" in case_data.keys():
                output_key = case_data["output_index"]
                YmlUt.output_value(json.loads(resp), case_data["output_name"], output_key)

        elif case_data["method"] == 'delete':
            if "insert_value" in case_data.keys():
                case_data_in = YmlUt.get_value(YmlUt.insert_value(yml_path, case_data), case_id)
                print(case_data_in)
                resp = http.delete(url=case_data_in["url"], headers=header)
                print(resp)
                if "assert_data" in case_data.keys():
                    assert case_data["assert_data"] in resp

            resp = http.delete(url=case_data["url"], headers=header)
            print(resp)
            if "assert_data" in case_data.keys():
                assert case_data["assert_data"] in resp

        else:
            return

    @pytest.mark.parametrize('yml_path,case_id', YmlUt.read_yaml_all_tuple("case_couple"))
    def test_case_all(self, yml_path, case_id):
        yml_value = YmlUt.read_yaml_values(yml_path)
        case_data = YmlUt.get_value(yml_value, case_id)
        try:
            header = YmlUt.read_yaml_values(YmlUt.read_yaml_paths("token_head")[0])["headers"]
            print(header)
            self.get_case_all(yml_path, case_id, case_data, header)
        except Exception as e:
            print(e)
