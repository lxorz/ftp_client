# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/29/2018 12:02 AM

"""
客户端接口
"""

import os,sys


dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir)

from core import main

if __name__ == "__main__":
    main.run()