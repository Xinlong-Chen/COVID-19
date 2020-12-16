# COVID-19
This is a project which is used to analyze the trend of COVID-19 besides China. The network-spider's data source is from Tencent news. The main technology in this project is multi-thread network spider, periodical bioinformatics publication, visual analytics, and Django. 
<br>
本项目功能为分析海外新冠疫情趋势。网络爬虫数据源为腾讯新闻。项目中所使用的主要技术为多线程爬虫，数据定时更新，数据可视化分析以及Django技术。

----
### 项目背景
新型冠状病毒感染的肺炎是一种急性感染性肺炎，2019新型冠状病毒具有很强的传染性。自2019年年底发现到2020年年初快速扩散到全球数十个国家和地区，引起大众严重的心理恐慌。至2020年5月，我国已基本控制疫情，但海外的疫情状况仍然严重，全世界都是同一个人类命运共同体，我国疫情的防控也和海外疫情状况息息相关。我国的疫情防控的主要矛盾已经从控制本土传染转移到防止境外输入上来，观察海外疫情动态已经成为人们的一个常态，也是疫情期间最受关注的一个热点问题。
<br>
本项目的目的是搭建一个集数据收集，数据存储，数据处理，数据分析为一体的操作性高，可用性好的系统。“内防扩散，外防输入”是我国现阶段疫情防控的基本措施。从传染病传播的一般性规律结合实际数据，往往更能说明当前全世界疫情防控所处的阶段项目目标任务，有关政府机关可以根据系统的数据分析结果，指定相应的“外防输入”手段，广大人民可以观察系统数据，得出自己对于整个疫情局势的判断，从而自觉采取相关的措施，减少出国以保护自己。

----
### 项目相关技术简介
- 项目过程中需要使用***代理IP池***，直接github找到相关项目即可，然后修改*COVID_19Analyse/tools/Scrapy/spider.py*中的获取代理IP地址即可。
- 项目中前端框架采用的*SB ADMIN2*，这是一个基于***bootstrap***的前端模版.
- 数据可视化分析方面采用***ECharts***实现。
- 网站搭建采用***Django***实现。
- 数据存储使用SQLite。

----
### 项目模块分析
系统主要分为三个模块，即数据可视化分析模块，Web网站模块，数据爬虫模块。
1.	数据爬虫模块：主要有两个功能：
   - 多线程爬虫的实现：使用线程池实现，根据顶层指令不同，以多线程方式调用底层的数据爬虫模块，并对数据爬虫爬到的数据的写入进行并发控制。
   - 代理IP池：该功能为GitHub开源项目，如果不使用代理IP则无法进行大规模数据的爬取。
2.	Web网站模块：主要有两个功能：
   - 用户管理：处理登陆/注册等与用户相关的请求。
   - 疫情数据管理：处理与疫情数据相关的请求.
3.	数据可视化分析模块：主要有两个功能：
   - 为用户提供网页操作界面。
   - 为用户提供上述数据的图表，以折线图，柱状图，表格等形式展现给用户。

----
### 项目启动：
1. 添加相关的代理IP池，并启动代理IP池的服务。
2. 修改*COVID_19Analyse/tools/Scrapy/spider.py*中的获取代理IP地址，使得爬虫能够支持使用代理IP。
3. 安装*requirements.txt*下所需要的相关插件。
4. 执行数据库变化指令。
```python
python manage.py makemigrations
python manage.py migrate
```
5. 执行*crontab*定时操作，添加相关任务：
```python
python manage.py crontab add 
 ```
6. 启动*Django*，查看localhost即可查看结果。
---
### 项目运行结果：
可参考：https://blog.csdn.net/hrbust_cxl/article/details/106894626
---
### 问题汇总：
Q：Step 1所说的代理IP池是个什么东西？
A：首先先弄清楚IP是什么，知道常用的反爬虫手段，及如何反制反爬虫（代理IP就是伪装一下自己，相当于你手里一堆身份证，拿着别人的身份证去买火车票），具体建议Google或者百度。

Q：Step 5的crontab是个什么东西？
A：crontab主要用于定时执行，疫情数据肯定要定时爬取啦！手动爬取多low啊！可以参考Blog：https://blog.csdn.net/hrbust_cxl/article/details/106887045

Q：为什么我crontab用不了？
A：同学你可能是Windows操作系统嗷，crontab一般是Unix系统用滴（linux或者Mac OS）

Q：我是Windows的os想跑这个项目怎么办？
A：两个解决办法。第一，仔细看urls中，有个update的url，可以手动刷新哦，你就手动刷新吧，别装逼了；第二，虚拟机，装Linux（Ubantu，Cent OS皆可）

Q：我想改一下这个项目，该如何去改呢？
A：从数据的流向分析，数据的来源已经解决，你要是想分析别的东西（比如画点别的图），现在用Django操作数据库，取出相关数据，Ajax方式发送给前端，前端使用Echarts绘图即可。
