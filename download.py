import requests
from bs4 import BeautifulSoup as bs
import os
import re

url0 = 'http://papers.nips.cc/'
gResDir = 'paper'  # 存储的位置

# 下载首页
html0 = requests.get(url=url0)
html0 = bs(html0.text, 'html5lib')

# 获取所有会议次数
books_hrefs = [(li.text, li.find('a')['href']) for li in html0.find_all('li', text=re.compile('Advances'))]
books_hrefs = [(book.replace(' ', '_'), url0.rstrip('/') + href) for book, href in books_hrefs]


# 创建文件夹函数
def makedirs(indir):
    if not os.path.exists(indir):
        os.makedirs(indir)


# 为每次会议单独创建一个文件夹
[makedirs(os.path.join(gResDir, indir)) for indir, _ in books_hrefs]

# 读取每次会议，并读取该次会议下面的paper链接
for indb, (book, href) in enumerate(books_hrefs):
    html1 = requests.get(url=href)
    html1 = bs(html1.text, 'html5lib')
    papers_hrefs = [(li.text, li.find('a')['href']) for li in html1.find_all('li') if '/paper/' in li.find('a')['href']]
    resPath = os.path.join(gResDir, book)

    # 文件保存路径
    links_file_path = os.path.join(resPath, 'links.txt')

    with open(links_file_path, 'a', encoding='utf-8') as fw:
        for paper, hrefPaper in papers_hrefs:
            # 生成每篇论文的具体链接并写入文件
            paper_link = url0.rstrip('/') + hrefPaper.replace('/paper/', '/paper/')
            fw.write(paper_link + '\n')

    print(f'Links for {book} saved to {links_file_path}')
