#第二周作业Guess_the_number

##分析与拆解
###理清问题
[作业要求](https://class.coursera.org/interactivepython1-002/human_grading/view/courses/974633/assessments/29/submissions)

- 完成基本逻辑结构
	- 流程
		- 选定**随机数**出现的范围
		- 输入**猜测数**
			- 注意使**字符串**转换为**整型**，输出"Guess was xxx"
		- 随机生成随机数。
			- Hint：使用random module。
		- 比较**随机数**与**猜测数**
		- 测试
	- 所需python知识
		- 模块调用
		- print:计算机到玩家
		- random:自动生成随机数
		- input_raw:玩家到计算机
		- 强制类型转换
		- 条件与循环
- 完成逻辑结构
	- 调用simplegui完成图形界面
		- [simplegui](http://www.codeskulptor.org/docs.html#tabs-Python)
	- 循环启动游戏
	- 随机选择范围（2选1）
	- 限制尝试次数
		- 0到100，7次
		- 0到1000，10次
- 实现逻辑功能[代码](http://www.codeskulptor.org/#user39_MmdkKzh00ddELfY.py)
- 实现图形界面需要相对独立的调用[代码](http://www.codeskulptor.org/#user39_9OK4KOXIWwnvY9K.py)

		
##操作发现的问题
###simplegui不太会用
	
尝试参考[组长的 simplegui 代码](https://github.com/yzha3917/omooc.py/blob/master/guess_the_number.py)猜测调用函数方式
	
```
		frame = simplegui.create_frame('Testing', 200, 200)
		#frame.add_功能("显示名称", 函数,位置)
		frame.add_input("Lowest number", lowest,50)
		frame.add_input("Highest number", highest,50)
		frame.add_button('Its Showtime!',arange,100)
		frame.add_input("", input_guess,50)
		
		frame.start()
		new_game()
```
	
	
查看 codeskulptor 中的 docs [simplegui](http://www.codeskulptor.org/docs.html#tabs-Python)

###限制次数一开始设置有问题，对函数的互相调用理解不清晰
###simplegui在safari中显示有问题，使用chrome
###需要解决的问题
	
- [x]输入非range内的数提示
- [ ]输入字符不能转换成int的错误预防
- [ ]一次游戏结束自动在该范围进行下一次，引入延时函数


