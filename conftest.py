
from common.httphandler import HttpHander
from common.yml_util import YmlUtil
import json, pytest
http = HttpHander()
YmlUt = YmlUtil()

# test测试服，对应host_test.yml||pre预发布，对应host_pre.yml||None线上，对应token_get_online
host_map = "test"

@pytest.fixture(scope="class", autouse=True)
# 作用域-每个方法
def get_tocken():
    YmlUt.write_yaml({"host_map": host_map})
    case_data = YmlUt.read_yaml_values(YmlUt.read_yaml_paths("host_{}".format(host_map))[0])["token_get"] \
        if host_map else YmlUt.read_yaml_values(YmlUt.read_yaml_paths("data_online")[0])["token_get"]
    resp = json.loads(http.get(url=case_data["url"], headers=http.head_data()))
    head_data = {'headers': http.head_data({"token": '{}'.format(resp['code'])})}
    YmlUt.write_yaml(head_data)
    print("添加header参数并写入yml")

    yield
    print("清空yml")
    YmlUt.clear_yaml()

# @pytest.fixture(scope = "module",autouse = True)
# def execute_database_sql():
#     print("每个模块前")
#     yield
#     print("每个模块后")

