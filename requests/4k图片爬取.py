import requests
from lxml import etree
import urllib3
import os
import sys
import io

if __name__ == '__main__':
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    # https://bing.ee123.net/page/1
    raw_url = "https://pic.netbian.com/4kmeinv/"
    page_num = 1

    if not os.path.exists("./bing"):
        os.mkdir('./bing')
    
    BING_PIC = []
    BING_NAME = []

    for i in range(1,3):
        #https://pic.netbian.com/4kmeinv/index_2.html
        url = raw_url+f"index_{i}.html"

        response = requests.get(headers=headers,url=raw_url)
        page_txt = response.text
        tree = etree.HTML(page_txt)
        q_list = tree.xpath('//div[@class="wrap clearfix"]//li')
        #这个就是把li整成一个列表
        for j in q_list:
            #https://pic.netbian.com/uploads/allimg/241028/001351-1730045631dfd4.jpg
            src = 'https://pic.netbian.com/'+j.xpath('./a/img/@src')[0]
            BING_PIC.append(src)
            name = j.xpath('./a/img/@alt')[0] + '.jpg'
    
    number = 0   
    for img_url in BING_PIC:
        img_data = requests.get(url=img_url,headers=headers).content
        img_path = 'bing/' + BING_NAME[number]
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(BING_NAME[number]+"finish!!!")
        number = number + 1