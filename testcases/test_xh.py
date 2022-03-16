from common import httphandler
from common import readw
from common import yml_util
import json,pytest


http = httphandler.HttpHandler()
read = readw.ReadW()

class TestQdcx():

    def test_sdf(self):
        # 'for循环驱动'
        for item in range(2,6):
            if read.read_E(0, item, 8) == 'get':
                resp = http.get(url=read.read_E(0,item,6),headers=yml_util.read_yaml('headers'))
                print(resp)
                assert read.read_E(0,item,9) in resp
            else:
                resp = http.post(url=read.read_E(0, item, 6), data=read.read_E(0, item, 7), headers=yml_util.read_yaml('headers'))
                print(resp)
                assert read.read_E(0,item,9) in resp



