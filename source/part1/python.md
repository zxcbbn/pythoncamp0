#python 教程


##MOOC笔记
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
		 .  ..    .            .
		 .  ....  .......> Handler2
		 .     .
		 .....> Handler1
 
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
