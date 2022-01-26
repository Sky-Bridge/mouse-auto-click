#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from mouseclick import *
from chuangkou import *


# 简单演示，复杂点的可看menghuan.py
def click():
    print("点击此电脑")
    cidiannao = r".\images\click.jpg"
    mc = MouseClick()
    mc.cv2_click(cidiannao, offset_x=5, offset_y=5)  # 如果不设置offset，默认鼠标偏移为5, 如果有需要，可以改成随机偏移量


click()