# -*- coding: utf-8 -*-

import paramiko

# SSH 代理服务器的地址和端口
ssh_proxy_addr = 'ip'
ssh_proxy_port = 22  # 请将端口号替换为您的 SSH 代理端口号

# 用户名和私钥文件路径
ssh_user = 'your_username'  # 替换为您的用户名
pri_key_path = 'path/to/your/private/keyfile'  # 替换为您的私钥文件路径

# 创建 SSH 客户端
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到 SSH 代理服务器
ssh_client.connect(ssh_proxy_addr, port=ssh_proxy_port, username=ssh_user, key_filename=pri_key_path)

# 可以在这里执行基于 SSH 代理的操作，例如使用 requests 库进行 HTTP 请求
# ...

# 关闭 SSH 连接
ssh_client.close()
