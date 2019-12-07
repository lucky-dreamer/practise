"""
超星尔雅刷课程序，实现自动控制视频的播放停止，遍历播放
作者：Lucky
"""
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
option = ChromeOptions().add_experimental_option("excludeSwitches", ["enable-automation"])
driver = Chrome(executable_path=r"H:\chromedriver.exe", options=option)  # 初始设置
def window_latest():# 进入最新的窗口（即提交后的）
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
def main():
    driver.maximize_window()
    driver.get('http://passport2.chaoxing.com/login?fid=2016&refer=http://i.mooc.chaoxing.com/space/index.shtml')#进入目标登录网页
    time.sleep(3)  # 小小缓冲一下
    xx = driver.find_element_by_id("unameId")
    xx.click()
    xx.send_keys("13102327270")
    time.sleep(3)
    acc = driver.find_element_by_id("passwordId")
    acc.click()
    acc.send_keys("mt1913252329")
    time.sleep(3)
    zcc = driver.find_element_by_xpath("//*[@id='numcode']")
    zcc.click()
    time.sleep(5)
    ccc = driver.find_element_by_css_selector("input.zl_btn_right")
    ccc.click()  # 找到相应输入框的位置，点击输入，最后提交
    window_latest()
    time.sleep(3)
    driver.switch_to.frame("frame_content")  # 进入元素真实所在的框架
    nb = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]/div[1]/a[1]")
    nb.click()  # 点击进入自己的第一个尔雅课程
    time.sleep(3)
    window_latest()
    url_list = driver.find_elements_by_css_selector("body > div.main > div.left > div.content1.roundcorner > div.timeline > div > div > h3 > span.articlename > a")
    i = 0
    print(url_list)
    for item in url_list:
        nng = driver.find_elements_by_css_selector("body > div.main > div.left > div.content1.roundcorner > div.timeline > div > div > h3 > span.articlename > a")
        # 由于窗口刷新后列报里面的链接会失效，所以要重新找，新建一个列表，此列表用于点击进入课程
        nng[i].click()  # 用i来控制遍历
        i += 1
        window_latest()
        time.sleep(3)
        try:  # 链接里有视频的
            driver.switch_to.frame("iframe")  # 进入嵌套的第一层框架
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 进入嵌套的第二层框架
            bb = driver.find_element_by_id("ext-gen1038")  # 找到视频所在点击处的真实位置
            bb.click()  # 进行视频播放
        except(Exception):  # 链接里没有视频的
            driver.close()
            window_latest()
            time.sleep(3)
            driver.switch_to.frame("frame_content")
            nb = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]/div[1]/a[1]")
            nb.click()  # 点击进入自己的第一个尔雅课程
            time.sleep(3)
            window_latest()
            continue
        try:  # 正常播放含有答题的视频
            bbbb = driver.find_element_by_class_name("x-container ans-timelineobjects x-container-default").get_attribute("style")#找到判断是否弹出题目的节点
            while bbbb == "overflow: auto; visibility: hidden;":  # 如果没弹出题目
                time.sleep(10)
                bbbb = driver.find_element_by_xpath("//*[@id='ext-comp-1035']").get_attribute("style")  # 每十秒抓取一次，看是否弹出题目
            window_latest()
            driver.switch_to.frame("iframe")  # 进入嵌套的第一层框架
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 进入嵌套的第二层框架
            cv = driver.find_element_by_css_selector("input[value='true']")
            cv.click()
            time.sleep(3)
            z = driver.find_element_by_xpath("//*[@id='ext-gen1045']")  # 提交
            time.sleep(2)
            z.click()
            bbk = driver.find_element_by_xpath("//*[@id='video']/div[4]/button[1]/span[2]").text  # 判断视频是否终止
            while bbk!="重播":
                time.sleep(10)
                bbk = driver.find_element_by_xpath("//*[@id='video']/div[4]/button[1]/span[2]").text  # 每十秒判断一次
            else:
                driver.close()
                window_latest()
                time.sleep(3)
                driver.switch_to.frame("frame_content")
                nb = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]/div[1]/a[1]")
                nb.click()  # 点击进入自己的第一个尔雅课程
                time.sleep(3)
                window_latest()
        except:  # 播放不含有题目的视频
            window_latest()
            driver.switch_to.frame("iframe")  # 进入嵌套的第一层框架
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 进入嵌套的第二层框架
            bbn = driver.find_element_by_xpath("//*[@id='video']/div[4]/button[1]/span[2]").text
            while bbn != "重播":
                time.sleep(10)
                bbn = driver.find_element_by_xpath("//*[@id='video']/div[4]/button[1]/span[2]").text
            else:
                driver.close()
                window_latest()
                time.sleep(3)
                driver.switch_to.frame("frame_content")
                nb = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]/div[1]/a[1]")
                nb.click()
                time.sleep(3)
                window_latest()
if __name__ == "__main__":
    main()