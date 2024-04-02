import json

import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://47.107.116.139/fangwei/m.php?m=Public&a=login"
driver.get(url)
driver.maximize_window()

# # 保持设置cookie, 保持登录状态
# driver.add_cookie({"name": "PHPSESSID",
#                    "value": "qirvj2bvv06m8lvrptqi7jtmk2"})
#
# driver.refresh()


# 获取所有的cookies信息
cookies = driver.get_cookies()  # [{'domain': '47.107.116.139', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'bvlarhbu80bj64h1flf0n8e583'}]
print(cookies)
for cookie in cookies:
    driver.add_cookie(cookie)
else:
    driver.refresh()


time.sleep(5)
driver.quit()