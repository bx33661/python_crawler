

> UA检测：UA（User-Agent）检测是指服务器通过检查HTTP请求头中的User-Agent字段来识别和区分不同的客户端（如浏览器、爬虫等）。User-Agent字段包含了客户端的相关信息，如浏览器类型、操作系统等。通过UA检测，服务器可以采取不同的响应策略，例如阻止某些爬虫访问，或者为不同的浏览器提供优化的内容。





**百度翻译利用**

```python
import requests
import json

if __name__ == '__main__':
    post_api = 'https://fanyi.baidu.com/sug'
    headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
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
```



输出结果---`hello.json`

```python
{
    "errno": 0,
    "data": [
        {
            "k": "hello",
            "v": "int. 打招呼; 哈喽，喂; 你好，您好; 表示问候 n. “喂”的招呼声或问候声 vi. 喊“喂"
        },
        {
            "k": "hellos",
            "v": "n. 喂( hello的名词复数 )"
        },
        {
            "k": "hellow",
            "v": "（通常的招呼语）嗨， （打电话用）喂！， （英）（表示惊讶）哎哟"
        },
        {
            "k": "hello girl",
            "v": "女话务员; 女电话接线员"
        },
        {
            "k": "hello kitty",
            "v": "n. 卡通世界中; 有这样一只小猫; 没有嘴巴; 脸蛋圆圆的"
        }
    ],
    "logid": 1688304474
}
```

