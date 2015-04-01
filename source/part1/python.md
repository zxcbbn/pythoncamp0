#python 教程


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

### items:直接取values


```
d.items()
```
##知识清单

- 地板除 // 舍弃小数部分 & 常规除


##重要思维清单

- **功能间的转换**一定有标记，同样的结束一个功能也必须有标记
	- 函数:开始，停止缩进结束
- 先把抽象的功能实现，再试图“好看”。**先能用，再考虑好用**
> You will interact with your program using an input field and several buttons. For this project, we will ignore the canvas and print the computer's responses in the console. Building an initial version of your project that prints information in the console is a development strategy that you should use in later projects as well. Focusing on getting the logic of the program correct before trying to make it display the information in some “nice” way on the canvas usually saves lots of time since debugging logic errors in graphical output can be tricky.

- Event-driven programming model
	- 程序不再是一股脑儿的运行而是随着操作者的控制**一步一步**的进行
		- 有利于更改错误：弱耦合，模块化
		- 流程化方便操作
- 可读性，好看非常重要：确保几个月后自己能看懂，确保其他人能看懂
	- [Python代码编写格式规范](https://github.com/OpenMindClub/OMOOC.py/wiki/Python_Style_Guide)
	- **善用注释**是非常好的习惯



	
##环境配置问题

###[多python版本共存问题](http://tbb.co/managing-python-on-os-x-with-pyenv/)
