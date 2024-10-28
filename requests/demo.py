import requests
url = "https://pic.netbian.com/uploads/allimg/241028/001351-1730045631dfd4.jpg"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
reponse = requests.get(url=url,headers=headers)
content = reponse.content

with open('./demo.jpg','wb') as fp:
            fp.write(content)
            print("finish!!!")