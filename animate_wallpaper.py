# -*- coding = utf-8 -*-
# @Time : 2021/8/30 18:55
# @Author : 戎昱
# @File : animate_wallpaper.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
import pyglet
import win32gui, win32ui, win32con

class AnimationSrn:
    def __init__(self):

        parenthwnd = self.getScreenHandle()
        print(parenthwnd)
        left, top, right, bottom = win32gui.GetWindowRect(parenthwnd)
        print(left, top, right, bottom)
        # self.size = (right - left, bottom - top)
        self.size = (3840, 2160)
        self.gifpath = 'O.gif'

    def getScreenHandle(self):
        hwnd = win32gui.FindWindow("Progman", "Program Manager")
        win32gui.SendMessageTimeout(hwnd, 0x052C, 0, None, 0, 0x03E8)
        hwnd_WorkW = None
        while 1:
            hwnd_WorkW = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
            if not hwnd_WorkW:
                continue
            hView = win32gui.FindWindowEx(hwnd_WorkW, None, "SHELLDLL_DefView", None)
            if not hView:
                continue
            h = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
            while h:
                win32gui.SendMessage(h, 0x0010, 0, 0);  # WM_CLOSE
                h = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
            break
        return hwnd

        # return win32gui.GetDesktopWindow()


    def putGifScreen(self):
        parenthwnd = self.getScreenHandle()
        # 使用pyglet加载动画
        # print ("1ll", parenthwnd)
        animation = pyglet.image.load_animation(self.gifpath)  # 使用pyglet 加载一个gif 动图
        sprite = pyglet.sprite.Sprite(animation)  # 创建一个动画
        # 创建一个新的窗口
        # 创建-个窗口, 并将其设置为图像大小
        newwin = pyglet.window.Window(width=3840,
                                      height=2160,
                                      style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)
        # 将默认的背景图的父窗口改为新创建的窗口
        # print(win._hwnd)
        win32gui.SetParent(newwin._hwnd, parenthwnd)

        @newwin.event  # 事件处理程序的函数装饰器.用來显示图像
        def on_draw():
            newwin.clear()
            sprite.draw()

        pyglet.app.run()


if __name__ == '__main__':
    AnimationSrn().putGifScreen()
