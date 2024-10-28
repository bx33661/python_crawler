import requests
import sys

if __name__ == '__main__':
    url = 'https://www.baidu.com/s?ie=UTF-8&&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    question = input('查询的内容')
    param = {
        'wd':question
    }
    response = requests.get(url=url, headers=headers,params=param)
    res_text = response.text
    with open(r"E:\gitproject\Note\工程学习\Pyhton\爬虫项目\request\baidu_query1.html", 'w', encoding='utf-8') as f:
        f.write(res_text)