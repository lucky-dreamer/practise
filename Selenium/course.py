"""
给班级同学分享视频，进行录屏时，此程序控制程序的播放和停止
"""


import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
option = ChromeOptions().add_experimental_option("excludeSwitches", ["enable-automation"])
driver = Chrome(executable_path=r"H:\chromedriver.exe", options=option)  # 初始设置


def window_latest():  # 进入最新的窗口（即提交后的）
    for handle in driver.window_handles:
        driver.switch_to.window(handle)


def main():
    driver.maximize_window()
    driver.get('https://www.yojiang.cn/lesson/index')#进入目标登录网页
    time.sleep(2)  # 小小缓冲一下
    xx = driver.find_element_by_xpath('//*[@id="user_login_zone"]/li[2]/a')
    xx.click()
    time.sleep(7)  # 扫码登陆
    window_latest()
    zcc = driver.find_element_by_xpath('//*[@id="user_login_zone"]/li[1]/div[1]/a')
    zcc.click()
    time.sleep(2)
    window_latest()
    sd = driver.find_element_by_xpath('//*[@id="rd-bought-list"]/div/div/div[2]/a')
    sd.click()
    window_latest()
    time.sleep(2)
    mulu = driver.find_element_by_xpath('//*[@id="lesson_feature"]/div/div/div/div[4]/a')
    mulu.click()
    window_latest()
    time.sleep(2)
    url_list = driver.find_elements_by_css_selector('#lesson_catalogue > ol > li > a')
    p = 54
    for i in url_list:
        hg=driver.find_elements_by_css_selector('#lesson_catalogue > ol > li > a')
        hg[p].click()
        time.sleep(1)
        active = driver.find_element_by_xpath('//*[@id="wk-video"]/button')
        active.click()
        time.sleep(3)
        o=driver.find_element_by_css_selector('body > div.dialog.confirm-dialog > div.text').text
        if '是否' in o:
            driver.find_element_by_css_selector('body > div.dialog.confirm-dialog > div.text-right > button.dialog-btn.cancle').click()
        button = driver.find_element_by_xpath('//*[@id="wk-video"]/div[5]/button[1]').get_attribute('title')
        while button =='Pause':
            time.sleep(10)
            button = driver.find_element_by_xpath('//*[@id="wk-video"]/div[5]/button[1]').get_attribute('title')
        p += 1
        continue


if __name__ == "__main__":
    main()
