from fake_useragent import UserAgent

# 创建 UserAgent 对象
ua = UserAgent()

# 生成一个随机的用户代理字符串
random_user_agent = ua.random
print(random_user_agent)
