<!--
 * @Descripttion: 
 * @version: 
 * @Author: wangshuo
 * @Date: 2020-06-29 15:42:44
 * @LastEditors: wangshuo
 * @LastEditTime: 2020-07-28 11:01:40
--> 
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

1. 指定 *CONFERENCE*，例如 'CVPR2020 ICCV2019 ECCV2018'
2. 指定 *KEYWORDS*，例如 'few-shot'， 可以指定多个
3. 指定 *DOWNLOAD_FLAG*, 表示下载与否，'True' 或者 'False'
4. 运行 *python getPapers.py*



##  结果

会在当前路径下生成一个'papers\_' + KEYWORDS[0] + '_' + CONFERENCE 文件夹，如果*DOWNLOAD_FLAG* 设置为True, 文件夹中还会包含文章的PDF文件，以及对应的paper\_list.md，如果*DOWNLOAD_FLAG* 设置为False，则只有paper\_list.md

## Blog

https://blog.csdn.net/wangs1996/article/details/107019413