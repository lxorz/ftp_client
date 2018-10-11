# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/29/2018 12:04 AM

import sys


def progress_bar(self, num, total):
    """
    进度条:用于显示上传与下载的进度
  :return: 无
    """
    rate = num/total
    rate_num = int(rate * 100)
    r = "\r%s%d%%" % ("|" * rate_num, rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()