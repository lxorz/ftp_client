# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/29/2018 12:04 AM

import json
from conf import settings


def client_mkdir(self, *args):
    """实现用户在当前目录下可创建目录的功能"""
    cm_split = args[0].split()
    if len(cm_split) > 1:
        new_dir = cm_split[1]
        msg_dic = {
            "action":"mkdir",
            "new_dir":new_dir,
            "overriden":False,
        }
        self.client.send(json.dumps(msg_dic).encode())
        server_response = self.client.recv(1024)
        print(json.loads(server_response.decode()))

    else:
        print("%s:命令错误" % settings.LOGIN_STATE["cmd_error"])