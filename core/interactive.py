# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/29/2018 12:03 AM

def interactive(self):
    """
    本模块用于客户端与服务端的交互
    """
    while True:
        cmd = input(">>>:").strip()
        if len(cmd) == 0:
            continue
        cmd_str = cmd.split()[0]
        if hasattr(self, "cmd_%s" % cmd_str):
            func = getattr(self, "cmd_%s" % cmd_str)
            func(cmd)
        else:
            self.help()