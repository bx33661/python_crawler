import requests
import json

if __name__ == '__main__':
    post_api = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    query_word = input("请输入你要查询的单词")
    data  = {
        'kw':query_word
    }
    response = requests.post(url = post_api,data=data,headers=headers)
    res = response.json()
    filename = query_word+ '.json'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(json.dumps(res,indent=4,ensure_ascii=False))
    print('finish!!!!')