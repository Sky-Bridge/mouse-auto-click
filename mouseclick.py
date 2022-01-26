import win32con
import win32api, win32gui
import random
import time
from py_cv2 import *



class MouseClick():
    def __init__(self):
       self.wdname = u'梦幻西游 - 星云引擎'

    def resolution(self):  # 获取屏幕分辨率
        return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

    def get_window_info(self, wdname):  #  获取程序窗口名
        # wdname = u'梦幻西游 - 星云引擎'
        handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
        # print(handle)
        if handle == 0:
            # text.insert('end', '提示：请打开梦幻西游\n')
            # text.see('end')  # 自动显示底部
            # print(wdname)
            # print("请将窗口保持在前台")
            return None
        else:
            # print("窗口句柄为：" + str(handle))
            return win32gui.GetWindowRect(handle)

    def move_click(self, x, y, t=0):  # 移动鼠标并点击左键
        win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
        if t == 0:
            time.sleep(random.random() * 2 + 1)  # sleep一下
        else:
            time.sleep(t)
        return 0

    def cv2_click(self, imgpath, offset_x=25, offset_y=25):   # 鼠标默认偏移25xp
        try:
            im2 = py_cv2(imgpath)
            im3x = im2[1] + offset_x
            im3y = im2[0] + offset_y
            self.move_click(im3x, im3y)
        except TypeError:
            print("未找到图片对应坐标点！")
            return 0




