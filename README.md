# COVID-19
This is a project which is used to analyze the trend of COVID-19 besides China. The network-spider's data source is from Tencent news. The main technology in this project is multi-thread network spider, periodical bioinformatics publication, visual analytics, and Django. 
本项目功能为分析海外新冠疫情趋势。网络爬虫数据源为腾讯新闻。项目中所使用的主要技术为多线程爬虫，数据定时更新，数据可视化分析以及Django技术。

项目过程中需要使用***代理IP池***，直接github找到相关项目即可，然后修改*COVID_19Analyse/tools/Scrapy/spider.py*中的获取代理IP地址即可。
项目中前端框架采用的*SB ADMIN2*，这是一个基于***bootstrap***的前端模版.
数据可视化分析方面采用***ECharts***实现。
网站搭建采用***Django***实现。
数据存储使用SQLite。

----
### 项目启动：
1. 添加相关的代理IP池，并启动代理IP池的服务。
2. 修改*COVID_19Analyse/tools/Scrapy/spider.py*中的获取代理IP地址，使得爬虫能够支持使用代理IP。
3. 安装*requirements.txt*下所需要的相关插件。
4. 在终端执行*crontab*定时操作，添加相关任务：
(```)
python manage.py crontab add 
(```)
5. 启动*Django*，查看127.0.0.1即可查看结果。
