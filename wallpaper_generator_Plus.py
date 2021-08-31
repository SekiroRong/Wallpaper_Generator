# -*- coding = utf-8 -*-
# @Time : 2021/8/30 18:06
# @Author : 戎昱
# @File : wallpaper_generator_Plus.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
import imageio
import pyglet
import win32gui, win32ui, win32con
import os
from tqdm import tqdm
from PIL import ImageSequence,Image

img_path = "GIF"  # GIF Path
dir_path = "H:\gif_dirs.txt"  # Direction Path
save_path = 'H:\wallpapers' # 壁纸最终储存的位置
whitepath = 'D:\pythonProject\IoT\white.gif'

# 读取目录下文件
f = open(dir_path, "w")
files = os.listdir(img_path)
for file in files:
    f.write(img_path + '/' + file + '\n')
f.close()

f = open(dir_path, "r")
dirs = f.readlines()
f.close()
length = len(dirs)

# img = Image.new('RGB', (2560, 1440), (255, 255, 255))
# # img.show()
# # img.save('white.jpg')

class myGIF:
    def __init__(self, filename):
        self.filename = filename
        # animation = pyglet.resource.animation(self.filename)
        # self.sprite = pyglet.sprite.Sprite(animation)
        # print(self.sprite.width,self.sprite.height)
        gif = Image.open(self.filename)
        self.Iterater = ImageSequence.Iterator(gif)
        self.width = gif.width
        self.height = gif.height
        print(self.width,self.height)

    def get_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
        print(self.pos_x,self.pos_y)

gifs = []
for i in range(length):
    gifs.append(myGIF(dirs[i][0:-1]))

x = 0
y = 0
layer = 0
for i in range(length):
    gifs[i].get_pos(x,y)
    if not layer:
        x = x + gifs[i].width
    if layer == 1:
        y = gifs[i-5].height
        x = x + min(gifs[i-6].width,gifs[i-1].width)
        print(min(gifs[i - 6].width, gifs[i].width))
    elif layer == 2:
        y = gifs[i - 5].height + gifs[i - 11].height
        x = x + min(gifs[i - 6].width, gifs[i].width)
        print(min(gifs[i - 6].width, gifs[i].width))
    elif layer == 3:
        y = gifs[i - 5].height + gifs[i - 11].height + gifs[i - 17].height
        x = x + min(gifs[i - 6].width, gifs[i].width)
        print(min(gifs[i - 6].width, gifs[i].width))

    if x>3840:
        x = 0
        layer = layer + 1
        y = gifs[i - 5].height
        if layer == 2:
            y = y + gifs[i - 11].height
            if layer == 3:
                y = y + gifs[i - 17].height
    # y = y + gif.sprite.height

frames_out = []
white = Image.open(whitepath)
frames_w = ImageSequence.Iterator(white)
n = 0
for frame_w in tqdm(frames_w,ncols=300):
    framecopy = frame_w.copy().convert('RGB')
    for i in range(length):
        framecopy.paste(gifs[i].Iterater[n], (gifs[i].pos_x, gifs[i].pos_y))
    n = n+1
    frames_out.append(framecopy)

imageio.mimsave('O.gif', frames_out, 'GIF', duration=1/30)
