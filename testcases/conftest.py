
from common import httphandler
from common import readw
from common import yml_util
import json,pytest


@pytest.fixture(scope="session", autouse=True)
def get_code():
    http = httphandler.HttpHandler()
    read = readw.ReadW()
    url = read.read_E(0,2,6)
    resp = json.loads(http.get(url=url,headers=http.headData()))
    head_data = {'headers': http.headData(code='{}'.format(resp['code']))}
    yml_util.write_yaml(head_data)
    print("添加header参数并写入yml")
    yield
    print("清空yml")
    yml_util.clear_yaml()

# @pytest.fixture(scope = "class",autouse = 1)
# def execute_database_sql():
#     clear_yaml()
#     print("所有请求前清空yaml")
#     yield
#     print("所有请求后")