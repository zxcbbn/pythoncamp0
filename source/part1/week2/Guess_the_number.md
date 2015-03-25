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
- 完成全部逻辑结构
	- 调用simplegui完成图形界面
	- 循环启动游戏
	- 随机选择范围（2选1）
	- 限制尝试次数
		- 0到100，7次
		- 0到1000，10次
