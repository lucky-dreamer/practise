"""
功能：根据您的需求爬取搜狗直播的主播的封面
作者：Lucky
"""
import requests
import bs4
import urllib
def get_text(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    s=requests.get(url,headers=headers,timeout=30)
    text=s.text
    return text
def main():
    r=input("请输入想看第几页的主播的封面^-^:")
    url="http://show.sogou.com/meinv/"+"?page="+r
    x=get_text(url)
    bs=bs4.BeautifulSoup(x,"lxml")
    hh=bs.find("div",class_="box")
    g=hh.find_all("li",class_="box-list-item")
    girl=[]
    i=0
    for s in g:
        q=s.find("div",class_="imginfo imginfoA")
        v=q.find("img")
        name=i
        i+=1
        picture=v["data-original"]
        girl.append((name,picture))
    print(girl)
    for sd in girl:
        w=urllib.request.urlopen(sd[1])
        name=str(sd[0])+".jpg"
        asc=open("G:\case\picture-s\pic"+name,"wb")
        data = w.read()
        asc.write(data)
        asc.close()
        print("已经完成爬取{}张".format(sd[0]))
if __name__=="__main__":
    main()