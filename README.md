# mouse-auto-click
这是一个自动完成重复枯燥任务的py文件，最开始用来自动完成梦幻西游的师门任务等重复操作,后来，后来没玩了，好像没完全写完，不记得了（当时研究好久hhh）
操作原理为截取软件屏幕，然后通过openCV找到与提前截下来的图片做对比，找到坐标点，然后鼠标点击
（中间抄了点大佬的代码，应该没问题把，如有问题可联系我删除！XD）

使用方式
使用方法很简单，简单例子🌰可参考main.py
复杂一点的可参考我之前用的menghuan.py



> pip install -r requirements.txt
导入mouseclick.py和chuangkou.py

按照自己的操作逻辑，提前截好要点击的图，然后写为一个函数，再调用就行


目前已知问题为只能前台操作，无法后台，有大佬懂的可以告知下如何改为后台


新手练手之作，如有不足，请多多包涵

