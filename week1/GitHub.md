# GitHub 教程


## Git 与 GitHub


- Git 是什么

####Git 是一个分布式版本控制系统

我们假设这样一种情境，如果你头脑中因为**某些原因**闪现出某些**想法**。如果想法很多，我们就很希望把他们保留下来，已被将来使用，使记忆外部化。假使我们想把他们记录下来，我们可以使用word，但是如果改了许多次，又间隔了一段时间。很可能你会觉得不知道从何写起，而选择推到重来。又或者机器崩溃，word提示你尝试从最近的保存副本恢复，你就只能先把所有的文字浏览一遍，难以想起到底写到哪儿，思路被迫打断。
		
那我们何不换一种思路，关注**改变**，关注我们思路发生了哪些变化，并且把为什么变化同时标记出来。也就是说把我们的**想法**以及其对应出现的**原因**都进行记录，就可以不费力的理清思路，并且也为更精准的恢复文本提供了条件。

## 本地文件夹
###文件基本操作
 
**进入目录**

<pre><code>
cd dir
<code\><pre\>

**创建目录**
<pre><code>
mkdir dir
<code\><pre\>
**删除目录**
<pre><code>
rm -rf dir
<code\><pre\>
**创建文件**
<pre><code>
touch file
<code\><pre\>

## 本地仓库

**增加一个想法**
<pre><code>
git add
<code\><pre\>

**为什么要增加这个想法**
<pre><code>
git commit
<code\><pre\>

**查看我是否有想法了**
<pre><code>
git status
<code\><pre\>

**查看以往的想法**
<pre><code>
git log
<code\><pre\>


## 远程操作
- origin/master
- git push/pull


## 参考

[Git 教程廖雪峰](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

##适用环境

OS X
