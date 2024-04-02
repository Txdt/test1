from selenium import webdriver
from selenium.webdriver.common.by import By

from commons.pom import DealPage, AdminPage
from commons.utils import get_code

driver = webdriver.Chrome()
driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
driver.maximize_window()
page = DealPage(driver)
page.find_element(*DealPage.btn_login).click()  # 点击登录元素
page.find_element(*DealPage.ipt_username).send_keys('admin')  # 输入用户名
page.find_element(*DealPage.ipt_password).send_keys('msjy123')  # 输入密码
page.find_element(*DealPage.btn_login_submit).click()  # 点击登录按钮
msg = page.find_element(*DealPage.login_msg).text  # 返回登录信息
assert msg == '成功登录'
page.find_element(*DealPage.login_button).click()  # 登录确认
page.find_element(*DealPage.input_money).send_keys('100')  # 输入金额
page.find_element(*DealPage.button_touzi).click()  # 点击投资
page.find_element(*DealPage.pay_password).send_keys('msjy123')  # 输入支付密码
page.find_element(*DealPage.pay_password_button).click()  # 点击立即投资
pay_msg = page.find_element(*DealPage.pay_msg).text  # 返回投资信息
# input("")
# assert msg == '投标成功！'
page.find_element(*DealPage.pay_msg_button).click()  # 返回投资信息确认
driver.quit()

# 后台管理员登录
driver = webdriver.Chrome()
driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
driver.maximize_window()
admin_page = AdminPage(driver)
admin_page.find_element(*AdminPage.ipt_username).send_keys('admin')  # 输入用户名
admin_page.find_element(*AdminPage.ipt_password).send_keys('msjy123')  # 输入密码
driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot('verify.png')
code = get_code(driver)
admin_page.find_element(*AdminPage.ipt_code).send_keys(code)  # 输入验证码
# input("")
admin_page.find_element(*AdminPage.login_button).click()  # 点击登录
# input("")
# assert driver.title == '管理员登录'


driver.quit()