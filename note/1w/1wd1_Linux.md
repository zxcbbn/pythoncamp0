# 1wd1 Linux 笔记

## 目录

- Linux 在数据科学领域的重要性
- Linux 基础
- 新概念解释


## Linux 在数据科学领域的重要性

很多互联网公司的工作环境基于 Linux，尤其是再处理非常多的数据的时候。比如常见的 Spark，Hadoop

## Linux 基础

### 文件操作

- 创建目录:mkdir （make directory）
- 删除:rm 
- 删除非空目录:rm -rf file 
- 移动:mv
- 复制:cp (复制目录:cp -r )
- 找到文件/目录位置:cd 
- 显示当前目录下的文件: ls 
- 搜寻文件或目录: find 
	- find ./ -name "core*" 
- 查看文件:cat vi more

### 大型数据文件操作

- head -n 3 data.csv 
- tail -n 3 data.csv 
- 使用grep查询文件内容
	- grep 'data' todo.txt
- wc -l file 统计行数
- wc -w file 统计单词数
- wc -c file 统计字符数
- 统计/home/han目录(包含子目录)下 的所有js文件:
	- ls -lR /home/han | grep js | wc -l

	
## 新概念





