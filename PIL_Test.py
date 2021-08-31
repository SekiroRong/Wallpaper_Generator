# -*- coding = utf-8 -*-
# @Time : 2021/8/31 9:13
# @Author : 戎昱
# @File : PIL_Test.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
import imageio
from PIL import ImageSequence,Image
img = Image.new('RGB', (3840, 2160), (255, 255, 255))
img.save('bg.png')

# originpath = 'GIF/output0.gif'
# whitepath = 'D:\pythonProject\IoT\white.gif'
# white = Image.open(whitepath)
# gif = Image.open(originpath)
# print(white.n_frames)
# frames_w = ImageSequence.Iterator(white)
# frames = ImageSequence.Iterator(gif)
#
# frames_out = []
# i = 0
# for frame_w in frames_w:
#
#     framecopy = frame_w.copy().convert('RGB')
#     framecopy.paste(frames[i], (0, 0))
#     i = i+1
#     frames_out.append(framecopy)
#
# imageio.mimsave('O.gif', frames_out, 'GIF', duration=1/30)

# frames = ImageSequence.Iterator(gif)
# frames = frameIterator(frames,img)
# outimg = next(frames)  # Handle first frame separately
# outimg.info = img.info  # H制顺序信息
# savepath = originpath.replace('.', '_resize.')
# outimg.save(savepath, save_all=True, append_images=list(frames))