# crawler

>这个部分主要使用,requests库，和一些xpath语法，都是些无验证的网站

---

### UA头

> UA检测：UA（User-Agent）检测是指服务器通过检查HTTP请求头中的User-Agent字段来识别和区分不同的客户端（如浏览器、爬虫等）。User-Agent字段包含了客户端的相关信息，如浏览器类型、操作系统等。通过UA检测，服务器可以采取不同的响应策略，例如阻止某些爬虫访问，或者为不同的浏览器提供优化的内容。

```python
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
```



### **百度翻译利用**

这个主要是利用百度翻译的api，用post传参，获得返回的json数据

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

----

### FakeUA

这个重点主要是使用了一个xpath，

```python
//*[@id="liste"]/ul
```

匹配结果如下：

> 1.从根目录开始
>
> 2.匹配id为“liste”的节点
>
> 3.匹配上述节点下的`ul`标签

![image-20241028124849497](https://gitee.com/bx33661/image/raw/master/path/image-20241028124849497.png)

然后在此基础上，进行文本匹配

```python
//*[@id="liste"]/ul/li/a/text()1
```

![image-20241028125440168](https://gitee.com/bx33661/image/raw/master/path/image-20241028125440168.png)

//*[@id="view_photoList"]/div[1]

----

### 爬取图片

这个主要参看项目源代码了，一个要点就是如何把文件输入输出

这里利用xpath把li标签整合到一起，利用循环一个一个扒下来

![3d1fc0fce6ef3256ceef9e74c74babe](https://gitee.com/bx33661/image/raw/master/path/3d1fc0fce6ef3256ceef9e74c74babe.png)

最终效果

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241028174615273.png" alt="image-20241028174615273" style="zoom:50%;" />果：

主要使用content

关于`content`的例子，就是把图片的二进制码

```python
import requests
url = "https://pic.netbian.com/uploads/allimg/241028/001351-1730045631dfd4.jpg"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
reponse = requests.get(url=url,headers=headers)
content = reponse.content
print(content)
```

`content = reponse.content` 从响应对象中提取内容，并将其存储在 [`content`](vscode-file://vscode-app/d:/BaiduNetdiskDownload/Microsoft VS Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html) 变量中。[`reponse.content`](vscode-file://vscode-app/d:/BaiduNetdiskDownload/Microsoft VS Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html) 返回的是响应的二进制内容，这在处理图片或其他非文本数据时非常有用

把图片输出的话，就是把二进制写入jpg等图片文件

```python
with open('./demo.jpg','wb') as fp:
            fp.write(content)
            print("finish!!!")
```

![image-20241028174210350](https://gitee.com/bx33661/image/raw/master/path/image-20241028174210350.png)



### `fakeUA `库的使用

具体可以看`fkUA库.md`这个笔记

我贴一个实战过程中使用的例子：

```python
ua = UserAgent()
random_user_agent = ua.random
headers = {
    "User-Agent": random_user_agent
}
response = requests.get(url, headers=headers)
```

