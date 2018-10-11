# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/29/2018 12:03 AM

import json
from conf import settings


def client_cd(self, *args):
    """实现客户端在服务随意切换目录的功能，但只能访问自己的家目录"""
    cmd_split = args[0].split()
    if len(cmd_split) > 1:
        cd_dir = cmd_split[1]
        msg_dic = {
            "action": "cd",
            "cd_dir": cd_dir,
        }
        self.client.send(json.dumps(msg_dic).encode())
        server_response = self.client.recv(1024)
        print(server_response.decode())
    else:
        print("%s:命令错误" % settings.LOGIN_STATE["cmd_error"])