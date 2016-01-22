# 管道

- 课程中接触到的位置
- 探索
- 该概念对应的中文/英文


## 课程中接触到的位置

5:22 秒开始

> Linux 命令还有一个好处在于，它可以使用`管道`。
> 
> 也就是**前一个命令的输出可以作为后一个命令的输入**

**例子**

统计/home/han目录(包含子目录)下 的所有js文件:

```
	ls -lR /home/han | grep js | wc -l
```

先使用 `ls` 命令列出 /home/han 下的文件。再把这个**输出**作为下一个命令 `grep`的**输入**



## 探索

在肖凯老师推荐的 Linux 相关书籍 [The Linux Command Line](http://billie66.github.io/TLCL/index.html) 中英文双语版-PDF-2015-01-16 中，搜索**管道** 。搜索到 **重定向** 这一章节

以下为书中解释：

> The ability of commands to read data from standard input and send to standard output is utilized by a shell feature called pipelines. Using the pipe operator “|”(vertical bar), the standard output of one command can be piped into the standard input of another:

```
command1 | command2
```

因此说 pipeline 的目的就是从**标准输入**中读取信息并发送到**标准输出**，那么是不是这个过程就是**重定向**呢？

跳转到**重定向**这一章

> In this lesson we are going to unleash what may be the coolest feature of the command line. It’s called I/O redirection. The “I/O”stands for input/output and with this facility you can redirect the input and output of commands to and from files, as well as connect multiple commands together into powerful command pipelines. 




## 中英对照

管道对应 Pipes，或者 pipelines

- [Pipes: A Brief Introduction](http://www.linfo.org/pipes.html)