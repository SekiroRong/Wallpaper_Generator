# -*- coding = utf-8 -*-
# @Time : 2021/8/18 10:08
# @Author : 戎昱
# @File : wallpaper_generator.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # mpimg 用于读取图片
import os
import numpy as np
import random
from sklearn.cluster import KMeans
import skimage.io as io

# 文件目录
img_path = "H:\ins"  # Image Path
dir_path = "H:\dirs.txt"  # Direction Path
save_path = 'H:\wallpapers' # 壁纸最终储存的位置

# 参数
Max = 9  # 一行最多的图片数
nums = 20  # 生成的壁纸总数
resolution = '4K' # 壁纸分辨率 可选4k，2K和1080 建议所拼接图片的长宽不超过所选分辨率的一半

# 读取目录下文件
f = open(dir_path, "w")
files = os.listdir(img_path)
for file in files:
    f.write(img_path + '\\' + file + '\n')
f.close()

f = open(dir_path, "r")
dirs = f.readlines()
f.close()
length = len(dirs)
X = np.zeros((length,2))
for i in range(length):
    img = mpimg.imread(dirs[i][0:-1])
    X[i] = [img.shape[0],img.shape[1]]

# 利用kmeans聚类把图片分为L，M，S三类
kmeans = KMeans(3, random_state=0)
kmeans.fit(X)  # 训练模型
labels = kmeans.predict(X)  # 预测分类

#抽取三种标签各一例
rd1 = random.randint(0,length-1)
lb1 = labels[rd1]
rd2 = random.randint(0,length-1)
while labels[rd2] == lb1:
    rd2 = random.randint(0, length - 1)
lb2 = labels[rd2]
rd3 = random.randint(0,length-1)
while labels[rd3] == lb1 or labels[rd3] == lb2:
    rd3 = random.randint(0, length - 1)
lb3 = labels[rd3]

img1 = mpimg.imread(dirs[rd1][0:-1])
img2 = mpimg.imread(dirs[rd2][0:-1])
img3 = mpimg.imread(dirs[rd3][0:-1])

space1 = img1.shape[0]*img1.shape[1]
space2 = img2.shape[0]*img2.shape[1]
space3 = img3.shape[0]*img3.shape[1]

if space1 > space2 and space1 > space3:
    L = lb1
    M = lb2
    S = lb3
elif space2 > space1 and space2 > space3:
    L = lb2
    M = lb1
    S = lb3
elif space3 > space2 and space3 > space1:
    L = lb3
    M = lb2
    S = lb1

# 显示kmeans结果
# print(labels)
# plt.scatter(X[:,0], X[:,1], c=labels, s=40, cmap='viridis')
# plt.show()

if resolution == '4K':
    w = 3840
    h = 2160
elif resolution == '2K':
    w = 2560
    h = 1440
else:
    w = 1920
    h = 1080
L_index = 0
for num in range(nums):
    output = np.zeros((h, w, 3))
    used = np.zeros(length)
    L_height = 0  # 一行最小高度
    Height = 0
    Width = 0
    size = 0
    for i in range(Max):
        for j in range(Max):
            if Width == w:
                Width = 0
                Height = Height + L_height
                break
            selected = random.randint(0,length-1)
            while labels[selected] == L:
                if not L_index:
                    L_index = 1
                    break
                else:
                    selected = random.randint(0, length - 1)
            if not j:
                size = labels[selected]
            while used[selected] or labels[selected] != size:
                selected = random.randint(0, length - 1)
            used[selected] = 1
            img = mpimg.imread(dirs[selected][0:-1])
            width = Width + img.shape[1]
            height = Height + img.shape[0]
            if width > w:
                width = w
                img = img[:,:w-Width,:]
            if height > h:
                height = h
                img = img[:h-Height, :, :]
            output[Height:height, Width:width, :] = img.copy()
            Width = Width + img.shape[1]
            if not j:
                L_height = img.shape[0]
            elif img.shape[0] < L_height:
                L_height = img.shape[0]
            if j == Max-1:
                Width = 0
                Height = Height + L_height
    output=np.array(output,dtype=np.uint8)   #将pj1数组元素数据类型的改为"uint8"
    plt.imshow(output)   #查看图片
    plt.show()
    io.imsave(save_path + '\\' + str(num)+'.jpg', output)  # 保存拼接后的图片
    print(str(num)+'.jpg' + ' saved')