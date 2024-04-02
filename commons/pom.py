from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # 定义驱动

    def wait(self, func):
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际文本内容
                return txt.replace(' ', '')  # 条件成立返回实际值
            else:
                return True  # 直接返回成功，不需要获取文本内容
        self.wait(f)  # 调用类方法触发显示等待
        return self.driver.find_element(by, value)  # 最终返回元素


class DealPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver  # 定义驱动
    # 点击定位登录元素
    btn_login = (By.XPATH, '//*[@id="deal-intro"]/div[2]/div[8]/a')
    # 定位用户名元素
    ipt_username = (By.XPATH, '//*[@id="login-email-address"]')
    # 定位密码元素
    ipt_password = (By.XPATH, '//*[@id="login-password"]')
    # 点击登录按钮
    btn_login_submit = (By.XPATH, '//*[@id="ajax-login-submit"]')
    # 返回的登录信息
    login_msg = (By.XPATH, '//*[starts-with(@id, "fanwe_")]/table/tbody/tr/td[2]/div[2]')
    # 返回的登录信息确认按钮
    login_button = (By.XPATH, '//*[starts-with(@id, "fanwe_")]/table/tbody/tr/td[2]/div[3]/input[1]')
    # 输入投资金额
    input_money = (By.XPATH, '//*[@id="J_BIDMONEY"]')
    # 立即投资按钮
    button_touzi = (By.XPATH, '//*[@id="tz_link"]')
    # 输入支付密码
    pay_password = (By.XPATH, '//*[@id="J_bid_password"]')
    # 输入密码后确认按钮
    pay_password_button = (By.XPATH, '//*[@id="J_bindpassword_btn"]')
    # 提示投资信息
    pay_msg = (By.XPATH, '//*[starts-with(@id, "fanwe_")]/table/tbody/tr/td[2]/div[2]')
    # 确认投资信息按钮
    pay_msg_button = (By.XPATH, '//*[starts-with(@id, "fanwe_")]/table/tbody/tr/td[2]/div[3]/input[1]')

    # def wait(self, func):
    #     return WebDriverWait(self.driver, 5).until(func)
    #
    # # 重写定位元素的方法
    # def find_element(self, by, value, need_text=False):
    #     def f(driver):  # 自定义需要等待的元素方法f
    #         txt = driver.find_element(by, value).text
    #         if need_text:  # 如果需要实际文本内容
    #             return txt  # 条件成立返回实际值
    #         else:
    #             return True  # 直接返回成功，不需要获取文本内容
    #     self.wait(f)  # 调用类方法触发显示等待
    #     return self.driver.find_element(by, value)  # 最终返回元素

    def login(self, username, password):
        self.find_element(*self.btn_login).click()  # 点击登录元素
        self.find_element(*self.ipt_username).send_keys(username)  # 输入用户名
        self.find_element(*self.ipt_password).send_keys(password)  # 输入密码
        self.find_element(*self.btn_login_submit).click()  # 点击登录按钮
        msg = self.find_element(*self.login_msg).text  # 返回登录信息
        self.find_element(*self.login_button).click()
        return msg

    def pay(self, money, pay_password):
        self.find_element(*self.input_money).send_keys(money)  # 输入金额
        self.find_element(*self.button_touzi).click()  # 点击投资
        self.find_element(*self.pay_password).send_keys(pay_password)  # 输入支付密码
        self.find_element(*self.pay_password_button).click()  # 点击立即投资
        pay_msg = self.find_element(*self.pay_msg).text  # 返回投资信息
        # input("")
        # assert msg == '投标成功！'
        self.find_element(*self.pay_msg_button).click()  # 返回投资信息确认
        return pay_msg


class AdminPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver  # 定义驱动
    # 定位用户名元素
    ipt_username = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
    # 定位密码元素
    ipt_password = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
    # 验证码
    ipt_code = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
    # 登录按钮
    login_button = (By.XPATH, '//*[@id="login_btn"]')
    # 登录信息
    login_msg = (By.XPATH, '//*[@id="login_msg"]')

    def login(self, username, password, code):
        self.find_element(*self.ipt_username).send_keys(username)  # 输入用户名
        self.find_element(*self.ipt_password).send_keys(password)  # 输入密码
        self.find_element(*self.ipt_code).send_keys(code)  # 输入验证码
        self.find_element(*self.login_button).click()  # 点击登录
        return self.find_element(*self.login_msg, need_text=True).text  # 登录信息

    # def wait(self, func):
    #     return WebDriverWait(self.driver, 5).until(func)
    #
    # # 重写定位元素的方法
    # def find_element(self, by, value, need_text=False):
    #     def f(driver):  # 自定义需要等待的元素方法f
    #         txt = driver.find_element(by, value).text
    #         if need_text:  # 如果需要实际文本内容
    #             return txt  # 条件成立返回实际值
    #         else:
    #             return True  # 直接返回成功，不需要获取文本内容
    #     self.wait(f)  # 调用类方法触发显示等待
    #     return self.driver.find_element(by, value)  # 最终返回元素
