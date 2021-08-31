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

# 动态拼接壁纸生成器

* conda install pywin32 #鬼知道为什么pip不行

* 先整一张白底的图片

![](https://i.loli.net/2021/08/31/iqg1SCPZJjreK3v.png)

* 白底图片转成300帧的白底gif图![](https://i.loli.net/2021/08/31/M4ECh5qHlayRUbG.png)

* 将24张300帧的gif图嵌入白底gif图中并储存

  ```python
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
  ```

* 获取win10桌面的句柄,用gif替换桌面

  ```python
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
  ```
