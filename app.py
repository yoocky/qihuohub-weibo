#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weibo import APIClient

def get_access_token(app_key, app_secret, callback_url):
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    # 获取授权页面网址
    auth_url = client.get_authorize_url()
    print auth_url

    # 在浏览器中访问这个URL，会跳转到回调地址，回调地址后面跟着code，输入code
    code = raw_input('input code')
    r = client.request_access_token(code)
    access_token = r.access_token
    # token过期的UNIX时间
    expires_in = r.expires_in
    print 'access_token:', access_token
    print 'expires_in:', expires_in

    return access_token, expires_in
def init_login():
    app_key = 'xxx'
    app_secret = 'xxx'
    callback_url = 'https://api.weibo.com/oauth2/default.html'
    # access_token, expires_in = get_access_token(app_key, app_secret, callback_url)
    # 上面的语句运行一次后，可保存得到的access token，不必每次都申请
    # print "access_token = %s, expires_in = %s" % (access_token, expires_in)
    access_token = 'xxx'
    expires_in = 1697018782

    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    client.set_access_token(access_token, expires_in)
    return client


def send_pic(client,picpath,message):
    # send a weibo with img
    f = open(picpath, 'rb')
    mes = message.decode('utf-8')
    client.statuses.upload.post(status=mes, pic=f)
    f.close()  # APIClient不会自动关闭文件，需要手动关闭
    print u"发送成功！"

def send_mes(client,message):
    utext = unicode(message,"UTF-8")
    client.post.statuses__share(status=utext)
    print u"发送成功！"


if __name__ == '__main__':
    client = init_login()
    mes = "测试一下， 今天的行情大幅反转哈哈哈哈哈哈哈哈，太开心了！,可以了吗https://www.qihuohub.com"
    send_mes(client,mes)