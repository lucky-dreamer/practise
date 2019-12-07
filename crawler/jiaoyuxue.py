import requests
import bs4
import urllib
def get_text(url):
    s=requests.get(url,timeout=30)
    text=s.text
    return text
def writefill(km,url0):
    txttt = get_text(url0)
    gdd = bs4.BeautifulSoup(txttt, "lxml")
    vcx = gdd.find("div", class_="artBcon")
    pic = vcx.find("img")
    picture = pic["src"]
    w = urllib.request.urlopen(picture)
    asc = open("G:\case\picture\pic" +str(km) +".jpg","wb")
    data = w.read()
    asc.write(data)
    asc.close()
def main():
    km = 0
    ks=100
    url="http://nmg.huatu.com/2018/1220/1556223.html?tdsourcetag=s_pcqq_aiomsg"
    jj=get_text(url)
    bs = bs4.BeautifulSoup(jj, "lxml")
    bv=bs.find("div",class_="artBcon")
    bn=bv.find_all("tr")
    kl=[]
    name=2014
    for dd in bn[9:14]:
        mn=dd.find_all("a")
        kl.append((str(name),mn[0]["href"],mn[1]["href"]))
        name+=1
    for dj in kl:
        for hg in dj[1:3]:
            txt = get_text(hg)
            vb=bs4.BeautifulSoup(txt,"lxml")
            qb=vb.find("div",class_="coursePage")
            qua=qb.find_all("li")
            mum=qua[-2].find("a").text.strip()
            ds=eval(mum)
            writefill(ks,hg)
            ks+=100
            for jf in range(1,ds):
                km += 1
                url0=hg[0:-5]+"_"+str(jf+1)+".html"
                writefill(km,url0)
if __name__=="__main__":
    main()

