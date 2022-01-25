#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from mouseclick import *
from chuangkou import *



def shimen():
    global  is_start
    is_start = True
    i = 0
    count =0
    while is_start:
        time.sleep(2)
        i=i+1
        print("第%i次循环师门任务！" %i)
        # 点击师门任务4个字
        shimenrenwucv = r".\images\smrw.jpg"
        mc = MouseClick()
        mc.cv2_click(shimenrenwucv)

        # 点击师门任务4个字
        shimenrenwu = r".\images\shimenrenwu.jpg"
        mc = MouseClick()
        mc.cv2_click(shimenrenwu)

        # 点击购买2个字
        goumai = r".\images\goumai.jpg"
        mc = MouseClick()
        mc.cv2_click(goumai)

        # 点击购买2个字
        goumai2 = r".\images\goumai2.jpg"
        mc = MouseClick()
        mc.cv2_click(goumai2)

        # 点击交付召唤灵5个字
        jiaofuzhaohuanling = r".\images\jiaofuzhaohuanling.jpg"
        mc = MouseClick()
        mc.cv2_click(jiaofuzhaohuanling)

        # 点击上交2个字
        shangjiao = r".\images\shangjiao.jpg"
        mc = MouseClick()
        mc.cv2_click(shangjiao)

        # 点击上交2个字
        shangjiao2 = r".\images\shangjiao2.jpg"
        mc = MouseClick()
        mc.cv2_click(shangjiao2)

        # 点击去完成3个字
        quwancheng = r".\images\quwancheng.jpg"
        mc = MouseClick()
        mc.cv2_click(quwancheng)

        # 点击师门2个字
        shimen1 = r".\images\shimen1.jpg"
        mc = MouseClick()
        mc.cv2_click(shimen1)


        # 点击使用2个字
        shiyong = r".\images\shiyong.jpg"
        mc = MouseClick()
        mc.cv2_click(shiyong)


        # 点击阴曹地府4个字
        yincaodifu = r".\images\yincaodifu.jpg"
        mc = MouseClick()
        mc.cv2_click(yincaodifu)

        # 点击花果山3个字
        huaguoshan = r".\images\huaguoshan.jpg"
        mc = MouseClick()
        mc.cv2_click(huaguoshan)

        # 点击龙宫2个字
        longgong = r".\images\longgong.jpg"
        mc = MouseClick()
        mc.cv2_click(longgong)

        # 点击化生寺3个字
        huashengsi = r".\images\huashengsi.jpg"
        mc = MouseClick()
        mc.cv2_click(huashengsi)

        # 点击女儿村3个字
        nvercun = r".\images\nvercun.jpg"
        mc = MouseClick()
        mc.cv2_click(nvercun)

        # 点击师傅请3个字
        shifuqing = r".\images\shifuqing.jpg"
        mc = MouseClick()
        mc.cv2_click(shifuqing)

        #  师门问答
        shimenwenda1 = r".\images\shimenwenda1.jpg"
        chengyaojin = r".\images\chengyaojin.jpg"
        try:
            q1 = py_cv2(shimenwenda1)
            if q1[0] != 0:
                mc = MouseClick()
                mc.cv2_click(chengyaojin)
        except:
            pass

        #师门X
        shimenX = r".\images\shimenX.jpg"
        mc = MouseClick()
        mc.cv2_click(shimenX)

        # 点击师门-2个字
        shimen2 = r".\images\shimen-.jpg"
        mc = MouseClick()
        mc.cv2_click(shimen2)

        quxiao =  r".\images\quxiao.jpg"
        try:
            q1 = py_cv2(quxiao)
            if q1[0] != 0:
                print("识别到战斗中，休息30秒再次识别!")
                time.sleep(30)
        except:
            pass


def zhuagui():
    global  is_start
    is_start = True
    i = 0
    count =0
    while is_start:
        time.sleep(2)
        i=i+1
        print("第%i次循环抓鬼任务！" %i)


        # 点击抓鬼任务
        zhuaguirenwu1 = r".\images\zhuaguirenwu1.jpg"
        mc = MouseClick()
        mc.cv2_click(zhuaguirenwu1)

        # # 点击活动2个字
        # huodong2 = r".\images\huodong2.jpg"
        # mc = MouseClick()
        # mc.cv2_click(huodong2)

        # 点击抓鬼参加
        zhuaguirenwu = r".\images\zhuaguirenwu.jpg"
        mc = MouseClick()
        mc.cv2_click(zhuaguirenwu,350 , 50)

        # 点击抓鬼参加
        zhuagui = r".\images\zhuagui.jpg"
        mc = MouseClick()
        mc.cv2_click(zhuagui)

        quxiao =  r".\images\quxiao.jpg"
        try:
            q1 = py_cv2(quxiao)
            if q1[0] != 0:
                print("识别到战斗中，休息30秒再次识别!")
                time.sleep(30)
        except:
            pass

        # 点击确定
        queding = r".\images\queding.jpg"
        mc = MouseClick()
        mc.cv2_click(queding)

        guanbiyingyong =  r".\images\guanbiyingyong.jpg"
        try:
            q1 = py_cv2(guanbiyingyong)
            if q1[0] != 0:
                print("识别到游戏被退出，开始执行游戏重启!")
                #time.sleep(30)
                print(time.time())
                # 点击关闭应用
                guanbiyingyong = r".\images\guanbiyingyong.jpg"
                mc = MouseClick()
                mc.cv2_click(guanbiyingyong)

                menghuanxiyou = r".\images\menghuanxiyou.jpg"
                mc = MouseClick()
                mc.cv2_click(menghuanxiyou)

                dengluyouxi = r".\images\dengluyouxi.jpg"
                mc = MouseClick()
                time.sleep(50)
                mc.cv2_click(dengluyouxi)

                cha = r".\images\cha.jpg"
                mc = MouseClick()
                mc.cv2_click(cha)

                cha2 = r".\images\cha2.jpg"
                mc = MouseClick()
                mc.cv2_click(cha2)
        except:
                pass




def renwulian():
    global  is_start
    is_start = True
    i = 0
    count =0
    while is_start:
        time.sleep(2)
        i=i+1
        print("第%i次循环任务链任务！" %i)


        # 点击经验任务链
        jingyanrenwulian = r".\images\jingyanrenwulian.jpg"
        mc = MouseClick()
        mc.cv2_click(jingyanrenwulian)

        # 点击经验任务链2
        jingyanrenwulian2 = r".\images\jingyanrenwulian2.jpg"
        mc = MouseClick()
        mc.cv2_click(jingyanrenwulian2)

        # 点击开始战斗
        kaishizhandou = r".\images\kaishizhandou.jpg"
        mc = MouseClick()
        mc.cv2_click(kaishizhandou)

        # 点击上交
        shangjiao = r".\images\shangjiao.jpg"
        mc = MouseClick()
        mc.cv2_click(shangjiao)

        # 点击上交
        shangjiao2 = r".\images\shangjiao2.jpg"
        mc = MouseClick()
        mc.cv2_click(shangjiao2)

        # 点击购买
        goumai = r".\images\goumai.jpg"
        mc = MouseClick()
        mc.cv2_click(goumai)

        # 点击经验链
        jingyanlian = r".\images\jingyanlian.jpg"
        mc = MouseClick()
        mc.cv2_click(jingyanlian)

        quxiao =  r".\images\quxiao.jpg"
        try:
            q1 = py_cv2(quxiao)
            if q1[0] != 0:
                print("识别到战斗中，休息30秒再次识别!")
                time.sleep(30)
        except:
            pass

def stop():
    global  is_start
    is_start = False
    print("停止")




if __name__ == "__main__":
    global is_start
    # 创建主窗口
    root = tk.Tk()
    root.title("梦幻西游手游辅助")
    root.minsize(300, 250)
    root.maxsize(300, 250)
    # 创建按钮
    button_shimen = tk.Button(root, text=u"师门", command=lambda: MyThread(shimen), width = 15,height = 2)
    button_shimen.place(relx=0.2, rely=0.15, width=200)
    button_shimen.pack()

    # 创建按钮
    button_shimen = tk.Button(root, text=u"抓鬼", command=lambda: MyThread(zhuagui), width = 15,height = 2)
    button_shimen.place(relx=0.2, rely=0.15, width=200)
    button_shimen.pack()

    # 创建按钮
    button_shimen = tk.Button(root, text=u"任务链", command=lambda: MyThread(renwulian), width = 15,height = 2)
    button_shimen.place(relx=0.2, rely=0.15, width=200)
    button_shimen.pack()

    button_tingzhi = tk.Button(root,text=u"停止", command=lambda: MyThread(stop), width = 15,height = 2)
    button_tingzhi.place(relx=0.4, rely=0.85, width=200)
    button_tingzhi.pack()

    root.mainloop()

