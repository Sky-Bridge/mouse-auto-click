#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from mouseclick import *
from chuangkou import *

def click():
    print("点击此电脑")
    cidiannao = r".\images\click.jpg"
    mc = MouseClick()
    mc.cv2_click(cidiannao)

click()
