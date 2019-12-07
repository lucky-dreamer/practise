"""
作者：Lucky
功能：爬虫知乎，获得高价值，点赞数高的内容
1.登陆，获取登陆后的cookie,通过审查元素的network找到cookie，以后在请求头设置cookie
获取的是登陆后的页面，不用重复登陆。。。中途用浏览器登陆了的话，cookie会改变
2.请求头设置ua标识防止被屏蔽
3.有条件的话再设置一个代理，防止爬虫被封
"""
import requests
def get_text(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
               ,'Cookie':'_zap=be342da1-f5c7-42eb-97c4-ae7af231bcce; d_c0="ABBvHcNGrA-PTjJh9OC96uog6IPmkNQ5WEg=|1562039312"; _xsrf=S5GRIkp1YyypyGimKW7EEokRVOK29o0L; tgw_l7_route=66cb16bc7f45da64562a077714739c11; capsion_ticket="2|1:0|10:1570372265|14:capsion_ticket|44:NmRiZmJhMDQ2YzFjNDk3MTlhNmU1NmIzNjhlNWM4N2U=|355734bec2941e6fc5a2a7875543f6b57fa3c0319d31e7f996042ef39083a8f2"; z_c0="2|1:0|10:1570372274|4:z_c0|92:Mi4xTXlpMEJ3QUFBQUFBRUc4ZHcwYXNEeVlBQUFCZ0FsVk5za2lIWGdBSFNiMk5qSXU1Z2NxZkN5Y0FldmR5ckNUZ1R3|23927ef9578c1697680ee820840548fb2be42325e7384b3b4c3c7ae177f7243c"; q_c1=a7e2c970ffb44c88b6a77806be9bb7db|1570372345000|1570372345000; __utma=51854390.461069542.1570372351.1570372351.1570372351.1; __utmb=51854390.0.10.1570372351; __utmc=51854390; __utmz=51854390.1570372351.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/ha-ha-ha-pi-86/collections; __utmv=51854390.100--|2=registration_date=20180207=1^3=entry_date=20180207=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1570340565,1570341908,1570342687,1570372264; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1570372814; tst=r'}

    s=requests.get(url,headers=headers,timeout=30)
    text=s.text
    print(text)

def main():
    url="https://www.zhihu.com/"
    get_text(url)

if __name__=="__main__":
    main()