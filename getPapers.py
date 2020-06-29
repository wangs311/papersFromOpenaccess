'''
@Descripttion: find papers whose title contains keywords
@version: 
@Author: wangshuo
@Date: 2020-06-29 09:45:06
@LastEditors: wangshuo
@LastEditTime: 2020-06-29 15:54:44
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import os

# CVPR ICCV ECCV
CONFERENCE = 'CVPR2020'
# 关键字可以添加多个
KEYWORDS = ['few-shot', 'few']
# 是否下载
DOWNLOAD_FLAG = False

# 跳转地址前缀
PREFIX = 'https://openaccess.thecvf.com/'
URL = PREFIX + CONFERENCE.upper()
# 保存路径
SAVEPATH = 'papers_' + KEYWORDS[0] + '_' + CONFERENCE
# 保存文件前缀
FILEPREFIX = '['+ CONFERENCE +']'
# windows命名不包含以下字符
DICT_REP = {
    ':': ' ',
    '?': ' ',
    '<': ' ',
    '>': ' ',
    '|': ' '
}


def main():
    # 请求HTML
    html = urlopen(URL).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    
    # 找到所有class为ptitle的标签 
    paper_titles = soup.find_all('dt', {"class": "ptitle"})
    paper_all_nums = len(paper_titles)

    # 创建文件夹
    if not os.path.exists(SAVEPATH):
        os.mkdir(SAVEPATH)

    # 用于存放文章标题
    titles_list = []
    # 用于存放文章链接
    links_list = []
    # 计数器
    papers_num = 0

    for i in range(paper_all_nums):
        paper_title = paper_titles[i].get_text()
        # 遍历，是否包含关键字
        for kw in KEYWORDS:
            if paper_title.lower().find(kw) != -1:
                papers_num += 1
                titles_list.append(paper_title)
                # 文件名
                file_name = FILEPREFIX +  rep(paper_title) + '.pdf'
                # 保存路径
                file_path = os.path.join(SAVEPATH, file_name)
                # 文章链接
                pdf_url = PREFIX + paper_titles[i].next_sibling.next_sibling.next_sibling.next_sibling.a['href']
                links_list.append(pdf_url)
                
                # 下载文章
                if DOWNLOAD_FLAG:
                    r = requests.get(pdf_url)
                    print(papers_num, paper_title)
                    with open(file_path , 'wb') as f:
                        f.write(r.content)
                # 避免重复
                break

    save_txt(titles_list, links_list, nums=papers_num)


def rep(rawstr, dict_rep=DICT_REP):
    '''
    @Author: wangshuo
    @description: replace strs in title
    '''
    for i in dict_rep:
        rawstr = rawstr.replace(i, dict_rep[i])
    return rawstr


def save_txt(titles, links, nums):
    '''
    @Author: wangshuo
    @description: generate a paper list
    '''
    content = ''
    for i in range(nums):
        line = '  ' + str(i+1) + '. [' + titles[i] + '](' + links[i] + ')' + '\n'
        content += line
    file_path = os.path.join(SAVEPATH, 'papers_list.md') 
    with open(file_path , 'w') as f:
        f.write(content)
        

if __name__ == "__main__":
    main()