import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageGrab
def py_cv2(imgpath):
        img = cv2.imread(imgpath, 0)
        wd = ImageGrab.grab()
        wd.save(r'.\images\screen.jpg')
        template = cv2.imread(r'.\images\screen.jpg', 0)
        # wd.show()
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        # print(res)
        threshold = 0.9
        loc = np.where(res >= threshold)
        # print(loc)
        # print("1")
        # print(int(loc[0]),int(loc[1]))
        # print(int(loc[0]),loc[1])
        # print("2")
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), 255, 3)
        plt.imshow(img, cmap='gray')
        plt.xticks([]), plt.yticks([])
        return int(loc[0]), int(loc[1])
        # plt.show()



#imgpath = r".\images\click.jpg"
#im2 = py_cv2(imgpath)
# im3x = im2[0]+25
# im3y = im2[1]+25
# print(im3x)
# print(im3y)
# print(im2)