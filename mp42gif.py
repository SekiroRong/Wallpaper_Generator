# -*- coding = utf-8 -*-
# @Time : 2021/8/30 15:19
# @Author : 戎昱
# @File : mp42gif.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
from moviepy.editor import *
clip=(VideoFileClip(r"H:\myVideo\MOV_CINEMA_CLIP_010_20210831122003869.mp4").subclip(0,0.4))
clip.write_gif("D:\pythonProject\IoT\output.gif")
print("转换完成了")

# import os
# import imageio
#
#
# def create_gif(path, gif_name):
#     frames = []
#     for i in range(300):
#         frames.append(imageio.imread(path))
#     # Save them as frames into a gif
#     imageio.mimsave(gif_name, frames, 'GIF', duration=1/30)
#
#     return
#
#
# def main():
#     path = r"D:\pythonProject\IoT\bg.png"
#     gif_name = 'D:\pythonProject\IoT\white.gif'
#     create_gif(path, gif_name)
#
#
# if __name__ == "__main__":
#     main()