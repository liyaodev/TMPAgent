# -*- coding: utf-8 -*-

import socks
import requests
from requests import SOCKSProxy

proxy_addr = 'ip'
proxy_port = 22
proxy_user = 'centos'
proxy_pwd = 'your_password'
pri_key_file = 'D:\Soft\mobaxterm\ip.pem'

url = 'https://www.example.com'  # 替换为您要访问的网址

# 创建一个SOCKS5代理
proxy = SOCKSProxy(
    socks_version=5, 
    host=proxy_addr, 
    port=proxy_port, 
    username=proxy_user, 
    password=proxy_pwd
)
# response = requests.get(url, proxies=dict(http=proxy, https=proxy))

socks.set_default_proxy(socks.SOCKS5, proxy_addr, proxy_port)
socket = socks.socksocket()
socket.set_proxy(socks.SOCKS5, proxy_addr, proxy_port, keyfile=pri_key_file)
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10, sock=socket)
print(response.text)

