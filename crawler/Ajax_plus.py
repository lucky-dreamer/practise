'''
爬取利用fetch（或者Ajax）加载(只要找到接口链接，什么加载的都能爬)的页面例如知乎首页的动态内容信息
账号密码可以配合session使用，也可以导出cookie,更强大
只知道cookie,可以在找到接口后直接用cookie验证突破所有接口！，，，分析清楚后直接cookie一次解决
功能：查找知乎首页推荐的高赞的动态
在AJax的基础上采用异步多线程的方法爬取，效率大大提高
'''
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import random
import pymysql
from multiprocessing.dummy import Pool   # multiprocessing.dummy.pool是多线程，multiprocessing是多进程
# 代理设置（阿布云付费代理体验期）        pool.map()实现并发
# proxy_host='http-dyn.abuyun.com'
# proxy_port='9020'
# proxy_user='H7Z8RC493696QSYD'
# proxy_pass='4A5E14A875CDEE9F'
# proxy_meta='http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
#         "host" : proxy_host,
#         "port" : proxy_port,
#         "user" : proxy_user,
#         "pass" : proxy_pass,
#     }
# proxies={
#     'http':proxy_meta,
#     'https':proxy_meta
# }
# 请求头设置   cookie是登陆过后的cookie,可以设置多个登陆过后的账号的cookie，每次请求随机换一个，防止被封（即cookie池）
header0 = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
               ,'cookie': '_zap=be342da1-f5c7-42eb-97c4-ae7af231bcce; d_c0="ABBvHcNGrA-PTjJh9OC96uog6IPmkNQ5WEg=|1562039312"; _xsrf=S5GRIkp1YyypyGimKW7EEokRVOK29o0L; q_c1=a7e2c970ffb44c88b6a77806be9bb7db|1570372345000|1570372345000; __utma=51854390.461069542.1570372351.1570372351.1570372351.1; __utmz=51854390.1570372351.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/ha-ha-ha-pi-86/collections; __utmv=51854390.100--|2=registration_date=20180207=1^3=entry_date=20180207=1; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; capsion_ticket="2|1:0|10:1571756758|14:capsion_ticket|44:OTliZDg1OGY5ZjhhNGUyMmIzN2FkMGVjODlmMWM0NGI=|65ca9aa2598dcbf00e6a077068ac1136a3914574ff29c318e433b84a680ba984"; z_c0="2|1:0|10:1571756771|4:z_c0|92:Mi4xTXlpMEJ3QUFBQUFBRUc4ZHcwYXNEeVlBQUFCZ0FsVk40MmljWGdBREpPQjVrR2FXWk0yd0NqMkc2SEF0ejhBRFBB|8f5fc07b3901725eaa15f130ed2fe10d5b6f2ba106e17fc84e8f272e76a59019"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1571152624,1571241115,1571241777,1571756461; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1571756774'}
header1={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
         'cookie':'_zap=be342da1-f5c7-42eb-97c4-ae7af231bcce; d_c0="ABBvHcNGrA-PTjJh9OC96uog6IPmkNQ5WEg=|1562039312"; _xsrf=S5GRIkp1YyypyGimKW7EEokRVOK29o0L; q_c1=a7e2c970ffb44c88b6a77806be9bb7db|1570372345000|1570372345000; __utma=51854390.461069542.1570372351.1570372351.1570372351.1; __utmz=51854390.1570372351.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/ha-ha-ha-pi-86/collections; __utmv=51854390.100--|2=registration_date=20180207=1^3=entry_date=20180207=1; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; capsion_ticket="2|1:0|10:1571756833|14:capsion_ticket|44:NGQ1NDIzZDg2MDc5NDQ5Y2FjNjM5OTE3MzBiZDFmMmQ=|575f9dc6d617ef2322c218e63e39e41785facd25503169e4746945fb6dca59e9"; z_c0="2|1:0|10:1571756845|4:z_c0|92:Mi4xTXlpMEJ3QUFBQUFBRUc4ZHcwYXNEeVlBQUFCZ0FsVk5MV21jWGdDUEM4M1FhVHF0aGRqNlk0eTVlMW5yMzJtQkZR|28ada350e1546ca994661382b6b3874006b94da2c611942fe3c6761496d7d5c6"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1571152624,1571241115,1571241777,1571756461; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1571756848'}
header2={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'cookie':'_zap=be342da1-f5c7-42eb-97c4-ae7af231bcce; d_c0="ABBvHcNGrA-PTjJh9OC96uog6IPmkNQ5WEg=|1562039312"; _xsrf=S5GRIkp1YyypyGimKW7EEokRVOK29o0L; q_c1=a7e2c970ffb44c88b6a77806be9bb7db|1570372345000|1570372345000; __utma=51854390.461069542.1570372351.1570372351.1570372351.1; __utmz=51854390.1570372351.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/ha-ha-ha-pi-86/collections; __utmv=51854390.100--|2=registration_date=20180207=1^3=entry_date=20180207=1; capsion_ticket="2|1:0|10:1570433684|14:capsion_ticket|44:MTg4ZmQyMjA5NGZlNDRiOGEzZjJlMDI2MDQwNTQzODc=|c44cb9615c55b5500221f9d4594849937401d95431913ab737d8f61911a61654"; z_c0="2|1:0|10:1570433804|4:z_c0|92:Mi4xTXlpMEJ3QUFBQUFBRUc4ZHcwYXNEeVlBQUFCZ0FsVk5ERG1JWGdCVHN6WG5DY1RhUGZNZGJPSTROQW13RFFfYWp3|f03fb10ee9a87926db8c93d5d511f66b0b3a9f09b2513ace436583b8ea93b1f1"; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1571152624,1571241115,1571241777,1571756461; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1571756461'}
list_x=[header0,header1,header2]  # 作为一个小的cookie池子，每次请求都随机换不同的cookie
def url_list(url_list1):
    id = 5
    based_url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?'
    for x in range(2,8):
        params={'session_token':'ad6c15368abf7824e3aa81f0e980acf5',  # cookie和session_token会变
                'mobile':'true',
                'page_number':x,
                'limit':'6',
                'action':'down',
                'after_id':id
        }
        url=based_url+urlencode(params)
        url_list1.append(url)
        id+=6


# 页面获取
def get_page(url):
    gf=requests.get(url,headers=list_x[random.randint(0,2)],timeout=100)  # proxies=proxies #  用多个cookie来爬取
    if gf.status_code==200:
        return gf.json()
    else:
        mn.append(url)   # 没返回成功则加入带爬取的列表
# 解析提取自己需要的信息


def prase_page(c):
        items = c.get('data')
        for item in items:
            item=item.get('target')
            dongtai={}
            dongtai['点赞数'] = item.get('voteup_count')
            xi=item.get('question')
            if xi:              # 这里增加一层判断，老是这个地方被检测住卡住（或者if xi is not None），可能因为网速或传输原因导致的小部分局部数据丢失（一页中的单个回答）
                dongtai['问题']=xi.get('title')
                dongtai['内容']=pq(item.get('content')).text()
                yield dongtai   # yield作用，循环一次到这里的时候，跳出函数，返回一个值，并且记住返回值的位置                   # 下一次迭代再从这个位置后面开始，，好处是值不会覆盖，不会因为键相同而被重新赋值而吃掉
                                # 先写进文件系统中，看看有没有什么问题，然后再写入数据库中


def write_in_database(ghb):    # 写入数据库中
    q = pymysql.connect(host='localhost', user='root', password='980412', port=3306, db='db_mt')
    cursor = q.cursor()
    cursor.execute('create table if not exists tb_zhihu (点赞数 int(10),问题 varchar(100) primary key,内容 text(10000)) engine="InnoDB"')
    for i in ghb:
        print(i)
        x=str(i.values()).strip('dict_values([').strip('])').split(',')  # 字符串处理好麻烦，不过最终还是勉强实现了
        if eval(x[0])>1000:
            try:
                cursor.execute('insert into tb_zhihu values(%s,%s,%s)',(x[0],x[1],x[2].replace('\\n','')))
            except:
                q.rollback()        # 如果插入失败则执行数据回滚，相当于什么也没发生
    q.commit()
    q.close()


# 获取前十页的信息
def main():
    url_list1 = []       # 空列表，用于日后存放构造好的url
    url_list(url_list1)  # 1.构造url的列表
    while url_list1:     # 只要列表不为空，即还有页面未被解析
        global mn
        mn=[]              # mn 用于存放获取页面失败的url,进行循环往复多次获取，作为中间的过渡
        json=Pool().map(get_page,url_list1)   # 2.利用pool.map并发，和多线程,把列表里的网站进行爬取
        for c in json:
            if c is not None:     # 3.爬取完了之后统一解析和4.写入数据库中 # 判断不为空才进行解析，防止报错
                ghb=prase_page(c)  # 解析网页
                write_in_database(ghb)  # 写入数据库
            continue
        url_list1 = mn     # 把没有爬取成功的列表放入待爬取区，循环往复


if __name__ == '__main__':
    main()  # 算是成功了吧！^_^
#  还可以添加一个数据去重！
# 自我理解：mn和url1 list相当于schedule,get相当于downloader,prase相当于spider，write相当于Item pipeline
# 看看Scrapy的源代码，参照别人写的好的地方
