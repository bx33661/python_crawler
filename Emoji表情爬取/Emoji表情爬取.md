## Emoji表情爬取

> 由于我最近对emoji表情 十分喜欢 ，于是我想着能不能把一个中文站emoji表情爬一下
>
> 只需要使用`bs4`

### 包导入

导入三个包

```python
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
```

最后一个我比较喜欢使用，就是随机给你生成一个UA，不用自己再找了

```python
pip install fake_useragent
```



### 基本设置

![image-20241101141100199](https://gitee.com/bx33661/image/raw/master/path/image-20241101141100199.png)

```python
url = 'https://emoji8.com/zh-hans/'
headers = {
    'User-Agent': UserAgent().random
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
```

主要是设置爬取站的url，发送response，解析html



### 爬取操作

```python
emoji = soup.select('.content > ul  ')
a_emoji = emoji[0].select('li > a')
# 提取每个 a 标签的 href 内容
hrefs = [a['href'] for a in a_emoji]
```

感觉最难的就是准确地分析html结构

![image-20241101141238848](https://gitee.com/bx33661/image/raw/master/path/image-20241101141238848.png)

我们发现每个页面还有子页面，就提取每个子页面的后缀

```python
with open('./emoji.txt', 'w', encoding='utf-8') as f:
    for href in hrefs:
        url = 'https://emoji8.com' + href
        resq = requests.get(url, headers=headers)
        resq.encoding = 'utf-8'
        html = resq.text
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.select('.content > section > ul')
        span_elements = soup.find_all('span', class_='emoji')
        emojis = [span.text for span in span_elements]
        for emoji in emojis:
            f.write(emoji)
        f.write('\n')
```

创建一个txt文件，把爬取内容保存其中

![image-20241101141455299](https://gitee.com/bx33661/image/raw/master/path/image-20241101141455299.png)

还是提取内容，获得具体表情内容

这里没有把具体内容的名称，和具体分类的标题爬下来

![image-20241101141624705](https://gitee.com/bx33661/image/raw/master/path/image-20241101141624705.png)

有些不能显示，还没查清原因