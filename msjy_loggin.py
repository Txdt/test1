import json

import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from utils import load_cookies, save_cookies, is_login

driver = webdriver.Chrome()

load_cookies(driver)
driver.refresh()
# # 保持设置cookie, 保持登录状态
# driver.add_cookie({"name": "PHPSESSID",
#                    "value": "qirvj2bvv06m8lvrptqi7jtmk2"})
#


if is_login(driver) is False:
    url = "http://47.107.116.139/fangwei/m.php?m=Public&a=login"
    driver.get(url)
    driver.maximize_window()
    # load_cookies(driver)
    # 对验证码截图
    driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot('verify.png')
    # 第三方识别验证码
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
    else:
        print("识别失败")

    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input').send_keys("admin")
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input').send_keys("msjy123")
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input').send_keys(code)
    driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()

    save_cookies(driver)

    time.sleep(5)
    driver.quit()