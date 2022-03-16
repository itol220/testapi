from requests import Session
from user_agent import generate_user_agent

from common.yml_util import write_yaml, clear_yaml
from common.recursion import GetDictParam

class HttpHandler(GetDictParam):

    def headData(self,**kwargs):

        head_data = {}
        headers= {
                'User-Agent': generate_user_agent(),
                'content-type': 'application/json;charset=UTF-8'
        }
        head_data.update(headers)
        if kwargs:
            head_data.update(kwargs)
        return head_data


    def get(self, url, parm=None,headers=None):
        '''get请求'''
        session = Session()
        resp = session.get(url=url, headers=headers).text
        return resp

    def post(self, url, data=None, json=None, headers=None):
        '''post请求'''
        session =Session()
        if json is not None:
            resp = session.post(url, json=json, headers=headers).text
            return resp
        resp = session.post(url, data=data, headers=headers).text
        return resp


# if __name__ == '__main__':
#     url_k = "Https://account.kaola.com/user/ajax/getUserProfile.html"
#     http = HttpHandler()
#     resp = http.get(url_k)
#     print(resp)