# 获取保存cookies信息
import json
import time

import requests


def save_cookies(driver):
    # 保存cookie信息到本地文件
    cookies = driver.get_cookies()
    with open("cookies.json", 'w') as f:
        # dumps()放法将python对象转化为json字符串
        # loads()方法将json字符串转化为python对象
        # json数据格式是一个字符串"""json的数据"""
        f.write(json.dumps(cookies))  # json字符串转json类型


def load_cookies(driver, url):
    driver.get(url)
    try:
        with open("cookies.json") as f:
            cookies = json.loads(f.read())
        for cookie in cookies:
            driver.add_cookie(cookie)
        else:
            driver.maximize_window()
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


def get_verify(driver):
    url = 'http://upload.chaojiying.net/Upload/Processing.php'
    data = {
        "user": "baili123",
        # 密码：pass原生密码，pass2（md5加密）
        "pass2": "02BB7F3BBBAC170A2D836517AD9CC8DA",
        "sofid": "958623", # 软件ID
        "codetype": 1902
    }
    files = {"userfile": open("verify.png", "rb")}
    resp = requests.post(url=url, data=data, files=files)
    res = resp.json()
    code = ""
    if res["err_no"] == 0:
        code = res["pic_str"]
        print(f"识别成功{code}")
        return code
    else:
        print("识别失败")
        return code