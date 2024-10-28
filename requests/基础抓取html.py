import requests

if __name__ == '__main__':
    url = 'https://www.bx33661.com'
    response  = requests.get(url=url)
    res_text = response.text
    #r 是为了创建一个原始字符串（raw string）
    with open(r"E:\gitproject\Note\工程学习\Pyhton\爬虫项目\request\bxweb.html",'w',encoding='utf-8') as f:
        f.write(res_text)
