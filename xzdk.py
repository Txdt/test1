# 需要重新获取驱动
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from msjy_loggin import driver

# 进入贷款管理页面
frame = driver.find_element(By.XPATH, '/html/frameset/frame[1]')
# 进入frame子页面
driver.switch_to.frame(frame)
# 点击贷款管理
driver.find_element(By.XPATH, '//*[@id="navs"]/ul/li[2]/a').click()
time.sleep(3)
# 退出子页面
driver.switch_to.default_content()

# 点击全部贷款
frame = driver.find_element(By.XPATH, '//*[@id="menu-frame"]')
# 进入frame子页面
driver.switch_to.frame(frame)
# 点击贷款管理
driver.find_element(By.XPATH, '/html/body/dl[1]/dd[1]/a').click()
time.sleep(3)
# 退出子页面
driver.switch_to.default_content()

# 点击新增
frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
# 进入frame子页面
driver.switch_to.frame(frame)
# 点击贷款管理
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/input[1]').click()
# 点击颜色框输入值
driver.find_element(By.XPATH, '//*[@id="colorpickerField"]').send_keys('f00')
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input').clear()
time.sleep(1)
# 借款编号
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input').send_keys('dk666')
# 贷款名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input').send_keys('华龙苑南里')
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input').send_keys('华南里')
# 出现会员名
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]').send_keys('beifan')
time.sleep(2)
# 选中会员名
driver.find_element(By.XPATH, '//strong[text()="beifan"]').click()
# 复选框
driver.find_element(By.XPATH, '//*[@id="citys_box"]/div[1]/div[2]/input[1]').click()
driver.find_element(By.XPATH, '//*[@id="citys_box"]/div[1]/div[2]/input[3]').click()
# input('调试出发，需要结束：')
# 分类
select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select'))
time.sleep(2)
select.select_by_value('1')
# 担保机构
select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[9]/td[2]/select'))
time.sleep(2)
select.select_by_value('2031')

# 担保范围
select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[10]/td[2]/select'))
time.sleep(2)
select.select_by_visible_text('本金')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="guarantor_margin_amt_box"]/td[2]/input').clear()
driver.find_element(By.XPATH, '//*[@id="guarantor_margin_amt_box"]/td[2]/input').send_keys('100000')
driver.find_element(By.XPATH, '//*[@id="guarantor_amt_box"]/td[2]/input').clear()
driver.find_element(By.XPATH, '//*[@id="guarantor_amt_box"]/td[2]/input').send_keys('200000')
driver.find_element(By.XPATH, '//*[@id="guarantor_pro_fit_amt_box"]/td[2]/input').clear()
driver.find_element(By.XPATH, '//*[@id="guarantor_pro_fit_amt_box"]/td[2]/input').send_keys('300000')
time.sleep(2)
# 借款用途
select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select'))
time.sleep(2)
select.select_by_visible_text('婚礼筹备')

# 文件上传
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//li[text()="本地上传"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(r'D:\桌面\7月找工作\09-web自动化实战\test1\verify.png')
time.sleep(3)
driver.find_element(By.XPATH, '//div[@class="ke-dialog-footer"]//*[@value="确定"]').click()


time.sleep(3)
# 退出子页面
driver.switch_to.default_content()


time.sleep(3)
driver.quit()