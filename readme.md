[TOC]



# 拼接壁纸生成器

你是否觉得壁纸有些单调乏味。

今日心血来潮做了一个拼接壁纸生成器，可以把低分辨率的图片自动拼接起来形成风格独特的壁纸。

## 设计思路

### 1.读取图片文件

### 2.kmeans聚类

利用kmeans将图片按照长宽分为3类，将大小相似的图片拼接在同一排，提升拼接的美观性。
![在这里插入图片描述](https://img-blog.csdnimg.cn/8fba7637a02a4013abb73ac445cd2c3a.png#pic_center)

### 3.拼接并储存

## 使用教程

### 1.安装所需库

```
sklearn
numpy
matplotlib
skimage
```

### 2.设定壁纸参数

其中所需图片数量与生成的壁纸数及分辨率成正比吗，与你所使用的图片分辨率成反比，建议选用分辨率低于壁纸分辨率一半的图片。
![在这里插入图片描述](https://img-blog.csdnimg.cn/2a636c663192410396ddba3bce08bbb0.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTExMTYxMw==,size_16,color_FFFFFF,t_70#pic_center)
### 3.查看拼接成果

![在这里插入图片描述](https://img-blog.csdnimg.cn/a7ff8a0bf4b149d9afd6f9ddae73b6e1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTExMTYxMw==,size_16,color_FFFFFF,t_70#pic_center)
## 代码下载

那么哪里才能获得代码呢？

欢迎前往我的github里面下载：

https://github.com/SekiroRong/Wallpaper_Generator

欢迎与我交流学习。
