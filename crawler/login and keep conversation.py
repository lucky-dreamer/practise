"""
1.在登陆入口用错误的密码试一遍，通过审查元素的network找到真正的登陆接口
2.分析表单form，设置会话，以后在会话的基础上操作，不用重复登陆。
再利用账号密码登陆，在同一个会话基础上获得登陆后的源代码，进行后续操作
3.请求头设置ua标识防止被屏蔽
“豆瓣的各种元素都直接铺在源代码上边，很容易就拿到各种数据；
！！分析方法：审查元素，然后复制能在审查元素上看到的元素，在源代码上搜索看能否搜到，如果能，就是普通静态页面，直接爬取”
"""
import requests
f=requests.session()  # 调用会话，待会儿登陆后可以在同一个会话基础上操作就好
data={'name':'15648106113','password':'MT1913252329'}  # 设置登陆信息
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
login=f.post('https://accounts.douban.com/j/mobile/login/basic',headers=headers,data=data) # post提交表单登陆
print(login.status_code)   # 查看是否登陆成功
print(f.get('https://www.douban.com/',headers=headers).text)   # 输出登陆页面的源代码