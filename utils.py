# 获取保存cookies信息
import json
import time


def save_cookies(driver):
    # 保存cookie信息到本地文件
    cookies = driver.get_cookies()
    with open("cookies.json", 'w') as f:
        # dumps()放法将python对象转化为json字符串
        # loads()方法将json字符串转化为python对象
        # json数据格式是一个字符串"""json的数据"""
        f.write(json.dumps(cookies))  # json字符串转json类型


def load_cookies(driver):
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
    try:
        with open("cookies.json") as f:
            cookies = json.loads(f.read())
        for cookie in cookies:
            driver.add_cookie(cookie)
        else:
            driver.refresh()
    except:
        print("目前没有登录信息")
        pass


def is_login(driver):
    # 判断是否登录
    if '管理员登录' in driver.title:
        print('需要登录')
        return False
    else:
        print('已登录')
        driver.maximize_window()
        time.sleep(3)
        return True