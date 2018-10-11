# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/29/2018 12:03 AM

import os,json
from conf import settings
from core import progress_bar

def client_get(self, *args):
    """
    用来处理客户端下载功能
    """
    cmd_split = args[0].split()
    if len(cmd_split) > 1:
        filename = cmd_split[1]
        msg_dic = {
            "action": "get",
            "filename": filename,
            "overridden": True
        }
        self.client.send(json.dumps(msg_dic).encode())
        server_response = json.loads(self.client.recv(1024).decode())
        print(server_response,type(server_response))
        if server_response["file_exit"] == settings.LOGIN_STATE["file_exit"]:
            self.client.send("客户端已准备好下载".encode())
            if os.path.isfile(msg_dic["filename"]):
                f = open(filename + ".new", "wb")
            else:
                f = open(filename, "wb")
            receive_size = 0
            while receive_size < server_response["file_size"]:
                data = self.client.recv(1024)
                receive_size += len(data)
                progress_bar.progress_bar(self, receive_size, server_response["file_size"])
                f.write(data)
            else:
                print("download from server success")

        elif server_response["file_exit"] == settings.LOGIN_STATE["file_no_exit"]:
            print("%s:请求文件不存在" % server_response["file_exit"])