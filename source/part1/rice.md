#RICE课程笔记
##MOOC笔记part1
### Programming Tips
- 注意使用 module 要 import
- 善用 codeskulptor 的 DOC。可以使用搜索功能
- codeskulptor 中代码的不同颜色，表示不同的功能（Sublime Text 有同样的功能）
- 注重代码的可读性
	- 使用注释解释 '''/#
	- 变量名尽可能有意义
	- 限制单行的长度

### Rock-paper-scissor-lizard-Spork

转化成数字关系，利用数字的差来表明逻辑

### Event-driven programming

Linear programming model & Event-driven programming model

1. ####Linear programming model

```
start - A - B - C - D - E - F...END
```
2. ####Event-driven programming model

```
start - Interactive - wait(event):"quit" END
							(handler)	
```

- **Events**
	- Input
		- button
		- text_box input
	- Keyboard
		- key down
		- key up
	- Mouse
		- click
		- drag
	- Timer
- **Event Queue**

```
		 .        . 
		 . eventi .
		 . ...... . 
		 ..........  
		 . event2 . <....
		 ..........     .
		 . event1 .     . 
		 ..........     .
		  ..            .
		  ..   ..........    
		  ..   .          
		  \/   .
		 ...wait<............... 
		 .  /\ ....            . 
		 .  ..    |            .
		 .  ....  ------> Handler2
		 .     .
		 ----> Handler1
 
```

### Local vs Global variables 
已知
### simplegui

program structure

- Globals（state）
- helper functions
- classes
- Define event handlers
- creat a frame
- Register event handlers
- start frame & timers

### Input field
使用 simplegui 创建 input
### Visualizing events
使用 tutorial 模式更深入理解
###Programming Tips 2
- 使用 global variables 需要声明
- x = function() x为函数的返回值
- 每一个操作输出操作的内容，使每一次操作都得到反馈
- 逻辑关系能简化就化到最简

### Guess the number
解释mini project


##MOOC笔记part2

### Mouse input
 frame.set_mouseclick_handler(position) 注意一个两个实数的**元组**
 
 讲解实例：如何点绘图形，改变颜色
 
 - 位置获取
 - 鼠标使用
 - 图形绘制

### List methods

####创建列表
列表:注意元素的序列是从0开始计数


```
lst = [1,232,43434,3534,a,b,c]
```
####对当前列表操作 
in:判断某元素是否在列表里


```
232 in lst ------->  T/F
 元素
```
index:说明元素在列表中的位置

```
lst.index(232) ------>   3
          元素         位置
```
####修改列表
修改单一元素

```
lst[2] = 444
   位置    修改值 
```
append:增加元素到列表的最末位


```
lst.append(777) ....> lst = [1,232,43434,3534,a,b,c,777]
```
pop:删除append的元素


```
lst.pop(7)     .....>          777
     移除第几个元素          移除的元素是什么
```

remove:删除名称在列表中的元素

```
lst.remove(232)
```
### List example
通过列表增加删除元素控制绘制

### Iteration
不能对迭代的列表进行完全的操作么，可以建立新列表

### Dictionary

本质是一个映射，列表的映射只针对数字

key -> value


####创建字典

```
d = {1:   2,        3:4}
    key values
```

#### items:直接取values


```
d.items()
```
### Image

Load images:具体内容看 simplegui 的 doc

```
load_image(URL)
```
draw image


```
canvas.draw_image(im,src_center,src_size,dst_center,dst_size)

```
### Visualizing iteration


### Programming tips

####列表易出现的问题
注意范围从0开始
####列表和字典
字典是没有顺序的，字典可以直接添加（没有范围可言），字典的key应该是不可变元素

### Object-oriented programming1
介绍**类**的概念
### Object-oriented programming2
####bounce_ball_example

- define a ball domain
- define another domain to hold the ball

####advantages of object_oriented_programming

- To separate things into class
	- In our example is to separate the behaivour of the ball and the domain（概念清楚的重要性：李笑来）简而言之是抽象化一个object的行为
- To implement your code to performs new functions easily

###Working with objects

tuple需要了解一下元组的概念
