from requests import Session
from user_agent import generate_user_agent
from common.recursion import GetDictParam


session =Session()
class HttpHander:
    def head_data(self, data: dict = None):
        head_data = {}
        headers = {
                'User-Agent': generate_user_agent(),
                'content-type': 'application/json;charset=UTF-8'
        }
        head_data.update(headers)
        if data:
            head_data.update(data)
        return head_data


    def get(self, url, headers: dict = None):
        '''get请求'''

        resp = session.get(url=url, headers=headers).text
        return resp

    def post(self,url, data=None, json=None, headers: dict = None):
        '''post请求'''

        if json:
            resp = session.post(url=url, json=json, headers=headers).text
            return resp
        resp = session.post(url=url, data=data, headers=headers).text
        return resp

# if __name__ == '__main__':
#     url_k = "Https://account.kaola.com/user/ajax/getUserProfile.html"
#     http = HttpHandler()
#     resp = http.get(url_k)
#     print(resp)