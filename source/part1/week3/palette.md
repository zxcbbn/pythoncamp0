#可回放的点彩画板

##要求

###程序  
+ 三种形状画笔可选: 三角/方形/圆形
+ 颜色可定义: 颜色名 或是 RGB 声明
+ 每次 鼠标 点击画板任意一处,都绘制一个当前画笔可用彩色形状
+ 可记录1024次点彩绘制行为
+ 可回放整个记录的绘制行为

###教程

- 向 6个月前的自己认真描述
- 这个游戏整体怎么设计最简单?
- 有哪些理解上的坑,如何能理解之?
- 各种坑怎么证明自个儿的理解是对的?


##思路

###绘制图形

- 有关绘制图形参考mouse input以及list examples；以点击的鼠标坐标为中心
- 查看doc
	- canvas.draw_circle
	- canvas.draw_polygon
- 增加图形以及颜色按键

###回放

按顺序记录每次的点按，辅以每次点按的时间间隔即可

- 创建列表，将每次点按存储在新列表中
	- 需要记录的内容
		- 位置
		- 形状
		- 颜色

###回放速度调节

- 调整每一步的时间间隔

###输出为文件





##折腾流程

###绘制图像

以鼠标点按的坐标为基准(x,y)

####圆形
```
import simplegui

def draw_handler(canvas):
    canvas.draw_circle([x,y], 15, 1, "Black" color)
#                     使用鼠标点按的坐标  设置为常数       使用颜色列表调用
frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()
```
####三角形


```
import simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(x, y+10), (x-6, y), (x+6, y)], 12, color)

frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()
```

###正方形


```
import simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(x-5,y-5),(x+5,y-5),(x+5,y+5),(x-5,y+5)], 12, color)

frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()
```

####第一版
[链接](http://www.codeskulptor.org/#user39_nUjQ9vmBCE4QByZ.py)

###问题1

- 现象：选择变换颜色或图形之后后，之前绘制的图像也变了颜色，图像
- 分析：可能是global变量的缘故
- 尝试：试图取消global，可是发现无法调用；考虑使用列表，令序号变化即可.**失败**
- 分析2：由于每次都会遍历整个pos_list因此颜色必然会重新绘制，所以要改变颜色
	- 列表的理解不深入
	- for的遍历理解不够，只知道是for in

######本地试验


```
#列表 test
		list = [((1,2),2,3),(4,7,8)]
		print list[0][0][1]
#for test
		list = [((1,2),2,3),(4,7,8)]
		for num in list:
			print num
```

####第二版

[链接](http://www.codeskulptor.org/#user39_L8qHa0Lw6vAjMCi.py)

###问题2

- 现象：方形三角形绘制出现问题
- 分析：列表理解不清楚；**无果**
- 分析2：img_pos[0][1] 写错了。。。直接复制粘贴错误。
- 现象：换图形，全换掉

####第三版

[链接](http://www.codeskulptor.org/#user39_L7kTg1YnYZph1Ai.py)

###记录

- 创建列表：查看doc
- 每次点击时增加元素

```
#init
record_list = []
#event handler
def click(pos):
    record_list.append([pos,shape,color_select])
# register event handler
frame.set_mouseclick_handler(click)

```

###回放

- 清空之前所画的
	- 可以通过输出列表中第一个元素解决
- 把记录按步骤调出，记录1024次
	- 列表长度len(list)

###回放速度

参考[Timer-driven Ball Motion](http://www.codeskulptor.org/#user39_48WqmctPSK_0.py)

####第四版
[链接](http://www.codeskulptor.org/#user39_YqGQcZJOnIYZgA9.py)

###问题3

- 回放有问题：只能一次性



