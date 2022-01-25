
import threading
import tkinter as tk

class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)

# class chuangkou:
#     def stop(self):
#         global is_start
#         is_start = False
#         print("停止")

    # # 创建主窗口
    # root = tk.Tk()
    # root.title("梦幻西游手游辅助")
    # root.minsize(300, 250)
    # root.maxsize(300, 250)
    # # 创建按钮
    # button_shimen = tk.Button(root, text=u"师门", command=lambda: MyThread(shimen, window_size), width = 15,height = 2)
    # button_shimen.place(relx=0.2, rely=0.15, width=200)
    # button_shimen.pack()
    #
    # button_bangpai = tk.Button(root, text="帮派", command=lambda: MyThread(bang_pai, window_size), width = 15,height = 2)
    # button_bangpai.place(relx=0.2, rely=0.35, width=200)
    # button_bangpai.pack()
    #
    # button_baotu = tk.Button(root, text="宝图", command=lambda: MyThread(baotu,window_size), width = 15,height = 2)
    # button_baotu.place(relx=0.4, rely=0.55, width=200)
    # button_baotu.pack()
    #
    # button_zhuagui = tk.Button(root, text="带队抓鬼", command=lambda: MyThread(zhua_gui, window_size), width = 15,height = 2)
    # button_zhuagui.place(relx=0.4, rely=0.65, width=100)
    # button_zhuagui.pack()
    #
    # button_tingzhi = tk.Button(root,text=u"停止", command=lambda: MyThread(stop), width = 15,height = 2)
    # button_tingzhi.place(relx=0.4, rely=0.85, width=200)
    # button_tingzhi.pack()
    #
    # root.mainloop()