# Bayes' theorem

## 目录
- 定义
- 应用范围

## 定义

### 严谨定义

维基百科定义

> In probability theory and statistics, Bayes' theorem (alternatively Bayes' law or Bayes' rule) describes the probability of an event, based on conditions that might be related to the event.

### 直观感觉


## 数学表达

\\[
  P(A|B) = \frac{P(B|A)P(A)}{P(B)}\
\\]



## 参考资料

- Wikipedia：[Bayes' theorem ](https://en.wikipedia.org/wiki/Bayes%27_theorem)
- Quora：[What is an intuitive explanation of Bayes' Rule?](https://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule)
- [bayes ](https://www.youtube.com/watch\?v\=HHIz-gR4xHo)

## 翻译与笔记

Quora：[What is an intuitive explanation of Bayes' Rule?](https://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule)
### 翻译[^4]
[^4]: By Mike Kayser, Natural Language Processor


假设一家商店卖大小两种派。并且非常奇特的是，他们允许你一部分一部分的买他们的派（比如你买个四分之一或者一半什么的）。(要说为什么这么奇怪)，可能这家店是由某些疯子或者数学专业的毕业生经营的吧。

你的朋友 Fred 让你帮他买半个小号的派。你到了商店发现那家商店小号的派卖光了。太糟糕了。然而他们商店大号的派还有很多。还不错，你依然可以帮 Fred 买到派。但是等等，（如果要买半个小号的派）那么同样的分量应该是大号的派的多少部分呢？

显然，这取决于大号派与小号派的尺寸差别。假设大的派是小号派的2倍。那么半个小号派在份量上就等于四分之一个大号派。

然我们看下面的图：

![](https://qph.is.quoracdn.net/main-qimg-72d77135cf14b7e6d3f1eddcb657deaa?convert_to_webp=true)

这幅图包含一个**红色的**圆圈，一个**蓝色的**圆圈，还有这两个圆圈重合的紫色的部分，以及灰色的背景。

假设你想知道红色圆圈有几分之几是紫色的，但是一些人告诉你的是蓝色圆圈中紫色部分的比例。那么，这就和刚刚的情况很类似，你想要半个小号的派但是在只有大号派的情况下不知道你要的派在大号派中的比例。想要解决这个问题，你就需要定量的知道**红色与蓝色部分的相对大小关系**。假设红色圆圈的大小是蓝色圆圈的**两倍**，那么你所知道的（蓝色圆圈中紫色部分的比例）就应该除以**二**。

以上的内容事实上就是**贝叶斯定理**! 此外，`在真实的世界中`我们更多的讨论『事件发生的可能性』而不是『圆圈中某个部分的比例』。

我们可以看一个与之相关的真实世界中的例子。假设你和你的朋友正字申请大学。你的朋友说"80% MIT 接收的学生的平均高中成绩都至少是 B++ 。我的成绩是 B+。那么根据统计学的铁律，我应该有很大的机会!"真的么？让我们回到我们的好多圈圈的图，让我们稍微修改一下以符合实际的情况。

![](https://qph.is.quoracdn.net/main-qimg-3157d847ed780e514f390a959abff6e3?convert_to_webp=true)

现在我们的黑色的区域是"去年申请麻省理工学院的人数"，小的蓝的圆圈表现的是"入学的人数"，红色的圆圈是"得到 B+ 的麻省理工学院的申请人"