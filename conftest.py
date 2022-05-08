
from common.httphandler import HttpHander
from common.yml_util import YmlUtil
import json, pytest
http = HttpHander()
YmlUt = YmlUtil()


@pytest.fixture(scope="class", autouse=True)
# 作用域-每个方法
def get_tocken():
    case_data = YmlUt.read_yaml_values(yml_path=YmlUt.read_yaml_paths("token_get")[0])["token_get_data"]
    resp = json.loads(http.get(url=case_data["url"],headers=http.head_data()))
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

