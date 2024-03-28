import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from utils import is_login, save_cookies, load_cookies

# 实例化一个驱动
driver = Chrome()
url = "http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053"

# # 保存登录状态
# load_cookies(driver, url)
# driver.refresh()

# 1.1访问借款页面
# http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053
# 判断是否登录
# if is_login is False:
driver.get(url)
driver.maximize_window()
time.sleep(2)
# 1.2账号密码登录
driver.find_element(By.XPATH, '//*[@id="deal-intro"]/div[2]/div[8]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="login-email-address"]').send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys('msjy123')
driver.find_element(By.XPATH, '//*[@id="ajax-login-submit"]').click()
# save_cookies(driver)
time.sleep(2)
msg = driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
assert msg == '成功登录'
# 点击确定
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
time.sleep(2)
# 1.3输入金额
driver.find_element(By.XPATH, '//*[@id="J_BIDMONEY"]').send_keys('1000000')

# 1.4点击立即投资
driver.find_element(By.XPATH, '//*[@id="tz_link"]').click()
# 1.5输入支付密码（不同的用户密码也不同，admin（msiy123））
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="J_bid_password"]').send_keys('msjy123')
# 1.6点击确定
driver.find_element(By.XPATH, '//*[@id="J_bindpassword_btn"]').click()
# 1.7获取系统提示信息，断言：（投标成功！）
time.sleep(1)
msg = driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
assert msg == '投标成功！'
# 点击确定
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
# input('进入调试：')

time.sleep(3)
driver.quit()

