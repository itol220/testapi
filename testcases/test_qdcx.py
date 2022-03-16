
from common import httphandler
from common import readw
from common import yml_util
import json,pytest


http = httphandler.HttpHandler()
read = readw.ReadW()

class TestQdcx:


    def test_sy(self):
        resp = http.get(url=read.read_E(0,2,6),headers=yml_util.read_yaml('headers'))
        print(resp)
        assert read.read_E(0,2,9) in resp

    def test_sx(self):
        resp = http.get(url=read.read_E(0, 5, 6), headers=yml_util.read_yaml('headers'))
        print(resp)
        assert read.read_E(0,5,9) in resp

    def test_ss(self):
        resp = http.post(url=read.read_E(0,3,6),data = read.read_E(0,3,7),headers=yml_util.read_yaml('headers'))
        print(resp)
        assert read.read_E(0,3,9) in resp

    def test_sz(self):
        resp = http.post(url=read.read_E(0,4,6),data = read.read_E(0,4,7),headers=yml_util.read_yaml('headers'))
        print(resp)
        assert read.read_E(0,4,9) in resp

# if __name__ == '__main__':
#     pytest.main([])
    # test = TestQdcx()
    # test.setup_class()
    # test.test_sy()
    # test.test_sx()
    # test.test_ss()
    # test.test_sz()
    # test.teardown_class()