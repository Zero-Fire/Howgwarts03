# -*- coding: utf-8 -*-
import requests
class TestDemo():
    #setup_class方法获取token
    def setup_class(self):
        rul1 = " https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param1 = {
            "corpid": "ww25c8f6bf8deb47a1",
            "corpsecret": "ZKwB0dlOgBYYeRiBgzOM9igwDONc7XwADzL4pA-cV6M"
        }
        r = requests.request(method="GET",url = rul1,params = param1)
        # print(r.json())
        #获取类变量token，方便全局调用
        self.access_token = r.json()['access_token']
        assert r.json()['errcode'] == 0
    def test_create_mark(self):
        rul2 = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        data = {
            "tagname":"添加标签",
            "tagid": 2
        }
        params2 = {
            "access_token" : self.access_token
        }
        try:
            r1 = requests.request(method="POST",url = rul2, json = data, params = params2 )
        except Exception as e:
            print(e)
        print(r1.json())
        assert r1.json()['errmsg'] == 'created'
    def test_updata_mark(self):
        url3 = "https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        data1 = {
            "tagid": 2,
            "tagname": "更新标签"
        }
        params3 = {
            "access_token" : self.access_token
        }
        try:
            r3 = requests.request(method="POST",url = url3,json = data1,params = params3)
        except Exception as e:
            print(e)
        print(r3.json())
        assert r3.json()['errmsg'] == 'updated'

    def test_delete_mark(self):
        url4 = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params4 = {
            "access_token" : self.access_token,
            "tagid": 2
        }
        try:
            r4 = requests.request(method="GET",url = url4,params = params4)
        except Exception as e:
            print(e)
        print(r4.json())
        assert  r4.json()['errmsg'] == 'deleted'
