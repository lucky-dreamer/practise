"""
功能：搜索想找的专业的短期实习
由于已经原网站已经改成ajax异步加载，所以以下代码已经不再可用，需维护"，用抓包的方法进行爬取"""
import requests
import bs4
import time
class Findjob:
    def __init__(self, r,page,js):
        self.r=r
        self.page=page
        self.js=js
    def get_text(self,url):
        s=requests.get(url,timeout=30)
        text=s.text
        print(text)
        return text
    def get_pages_url(self):
        for sb in range(self.page):
            url = "https://www.shixiseng.com/" + "interns?page="+ str(sb + 1)+ "&keyword=" + self.r
            x = self.get_text(url)
            bs = bs4.BeautifulSoup(x, "lxml")
            hh = bs.find("ul", class_="position-list")
            g = hh.find_all("li", class_="position-item clearfix font")
            girl = []
            i = 0
            for s in g:
                q = s.find("div", class_="info1 clearfix")
                v = q.find("a")
                c = v["href"]
                print(c)
                name = i
                i += 1
                girl.append((name, c))
        return girl
    def get_and_print_exactly_content(self,girl):
        for interm in girl:
            ur = interm[1]
            url_1 = "https://www.shixiseng.com" + ur
            text_1 = self.get_text(url_1)
            jj = bs4.BeautifulSoup(text_1, "lxml")
            head = jj.find("div", class_="new_job_name").text.strip()
            # message=jj.find("div",class_="job_msg").text.strip()
            tt = jj.find("div", class_="job_detail").text.strip()
            company = jj.find("div", class_="com_intro").text.strip()
            print(head)
            # print(message)
            print(tt)
            print("")
            print(company)
            self.js.append((head, tt, "", company))
            print("##################################################################################")
        print("搜索完成")
    def check_more(self,file_name,if_1):
        if if_1 == "y":
            key = input("请输入需要排除的关键字：")
            print("完成筛选")
            for hk in self.js:
                if key in hk[0]:
                    continue
                else:
                    self.write_file(file_name,hk)
        else:
            for ak in self.js:
                self.write_file(file_name, ak)
    def write_file(self,fil_name,content):
        asc = open("G:\case\practise\ "+fil_name, "a", encoding="utf-8")
        asc.writelines(content[0])
        asc.writelines("\n")
        asc.writelines(content[1])
        asc.writelines("\n")
        asc.writelines(content[2])
        asc.writelines("\n")
        asc.writelines(content[3])
        asc.writelines("\n")
        asc.writelines(" ")
        asc.writelines("\n")
        asc.close()
def main():
    r=input("请输入您想找的实习信息的相关专业:")     # 输入专业
    page=eval(input("每一页有9条实习招聘信息，请您输入想要查看多少页："))    # 输入想查看的数据量
    js=[]              # 存放的详细招聘信息的列表
    try:
        job=Findjob(r,page,js)   # 调用类
        girl=job.get_pages_url()  # 找到所有每个信息的各自的url,存放在girl列表里
        job.get_and_print_exactly_content(girl)   # 解析girl列表里的数据，并且输出招聘信息给用户看
    except AttributeError:        # 排除输入的错误
        print("搜索完成")
        print("只匹配到以上信息\n您输入的页数超过数据量，如需重新搜索，请尝试减少页数")
    except ConnectionError:       # 排除网络连接的错误
        print("网络连接有问题")
    # except:                        # 出现了没涉及到的BUG，联系我改进
    #     print("程序异常，请联系开发人员")
    file_name = input("请给存入数据的文件命名：（格式：xxx.txt）")   # 给存入信息的文件命名
    if_1 = input("请问上述搜索结果需要进一步筛选吗？（输入y/n）：")   # 在已输出的信息的基础上，排除题目关键字，详细进行筛选
    job.check_more(file_name,if_1)    # 写入文件操作
    print("已完成存储，后续请用Word打开进行处理与阅读")   # 完成！
    time.sleep(3)
if __name__=="__main__":
    main()