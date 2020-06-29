# 根据关键词下载CV顶会文章列表

## 说明

根据关键词，从 https://openaccess.thecvf.com 网站下载CV顶会文章列表

# 环境

+ Python 3
+ BeautifulSoup 
+ urllib
+ re
+ request
+ os



## 使用方法

1. 指定 CONFERENCE，例如“CVPR2020 ICCV2019 ECCV2018”
2. 指定KEYWORDS，例如 “few-shot”， 可以指定多个
3. 指定DOWNLOAD_FLAG, 'True' 或者 ‘False'
4. 运行 python getPapers.py



##  结果

会在当前路径下生成一个'papers\_' + KEYWORDS[0] + '_' + CONFERENCE 文件夹

