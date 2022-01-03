import os
import threading
import time

from selenium import webdriver


def fun_search(question):
    # chromedriver的绝对路径
    driver_path = r'C:\Users\DELL\Desktop\edgedriver_win64\msedgedriver.exe'

    # 初始化一个driver，并且指定chromedriver的路径
    driver = webdriver.Edge(executable_path=driver_path)
    driver.maximize_window()
    # 请求网页
    try:
        driver.get("https://www.baidu.com/")
        # 通过page_source获取网页源代码
        elem = driver.find_element_by_id('kw')
        elem.send_keys(question)
        elem.submit()
        time.sleep(20)  # 设置页面关闭时间
    except Exception as error:
        print(error)
    finally:
        driver.close()


def fun_music():
    os.startfile(r"D:\QQmusic\QQMusic1844.18.57.14\QQMusic.exe")


def fun_TIM():
    os.startfile(r"D:\QQ\Bin\QQScLauncher.exe")


def fun_calc():
    os.startfile(r"C:\Windows\System32\calc.exe")


def fun_sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def fun_total(question):
    if "播放音乐" in question or "打开qq音乐" in question:
        t1 = threading.Thread(target=fun_music)
        t1.start()

    elif "交互软件" in question or "聊天软件" in question:
        t2 = threading.Thread(target=fun_TIM)
        t2.start()

    elif "搜索" in question:
        index = question.find("搜索")
        string = question[index + 2:-1]
        t3 = threading.Thread(target=fun_search(string))
        t3.start()

    elif "计算器" in question:
        t4 = threading.Thread(target=fun_calc)
        t4.start()

    elif "睡眠" in question:
        t5 = threading.Thread(target=fun_sleep)
        t5.start()

