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
menu_frame = driver.find_element(By.XPATH, '//*[@id="menu-frame"]')
# 进入frame子页面
driver.switch_to.frame(menu_frame)
# 点击贷款管理
driver.find_element(By.XPATH, '/html/body/dl[1]/dd[1]/a').click()
time.sleep(3)
# 退出子页面
driver.switch_to.default_content()

# 点击新增
main_frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
# 进入frame子页面
driver.switch_to.frame(main_frame)
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

# 文件上传
# 点击图片上传
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button').click()
time.sleep(2)
# 点击本地上传
driver.find_element(By.XPATH, '//li[text()="本地上传"]').click()
time.sleep(3)
# 输入路径
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(r'D:\桌面\7月找工作\09-web自动化实战\test1\verify.png')
time.sleep(3)
# 点击确定  动态获取按钮，使用xpath手写
driver.find_element(By.XPATH, '//div[@class="ke-dialog-footer"]//*[@value="确定"]').click()


# 借款用途
select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select'))
time.sleep(2)
select.select_by_visible_text('婚礼筹备')

# 还款方式
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[16]/td[2]/select')
s = Select(sl1) # 创建Select对象
s.select_by_visible_text('等额本息')

# 合同范本
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select')
s = Select(sl1) # 创建Select对象
s.select_by_visible_text('付息还本合同范本【担保】')

# 转让合同范本
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select')
s = Select(sl1) # 创建Select对象
s.select_by_visible_text('付息还本合同范本【担保】')

# 借款金额
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input').clear()
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input').send_keys('200000')
time.sleep(3)

# 借款保证金
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input').clear()
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input').send_keys('100000')
time.sleep(2)
# 投标类型
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[21]/td[2]/select')
s = Select(sl1) # 创建Select对象
s.select_by_visible_text('按份额')
time.sleep(1)


# 分成多少份
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[24]/td[2]/input').clear()
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[24]/td[2]/input').send_keys('20')
time.sleep(3)

# 最高买多少份
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[25]/td[2]/input').clear()
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[25]/td[2]/input').send_keys('13')


# 借款期限
driver.find_element(By.XPATH, '//*[@id="repay_time"]').clear()
driver.find_element(By.XPATH, '//*[@id="repay_time"]').send_keys('24')
s1 = driver.find_element(By.XPATH, '//*[@id="repay_time_type"]')
s = Select(sl1)
s.select_by_value('1')

# 年利率
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[27]/td[2]/input').send_keys('3')

# 筹标期限
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input').send_keys('20')

# 可否使用红包
s1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[29]/td[2]/select')
s = Select(sl1)
s.select_by_value('1')
time.sleep(3)
# 贷款描述 frame
# 进入子页面
frame1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[30]/td[2]/div/div/div[2]/iframe')
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH, '/html/body').send_keys("kjsdjfioaoef，世纪东方框架时空裂缝婉拒我金额非")
# 推出子页面
driver.switch_to.default_content()

time.sleep(3)
# 进入frame子页面
driver.switch_to.frame(main_frame)
# 风险等级
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[31]/td[2]/select')
s = Select(sl1)
s.select_by_value('2')

# 风险控制

time.sleep(3)
# 借款状态
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]').click()
# 开始时间 //*[@id="start_time"]
start_time = driver.find_element(By.XPATH, '//input[@name="start_time"]')
driver.execute_script('arguments.value="2024-03-28 18:00:09"', start_time)

# 排序


time.sleep(3)
# 退出子页面
driver.switch_to.default_content()

input("进入调试：")


time.sleep(3)
driver.quit()