import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from commons.pom import DealPage, AdminPage
from commons.utils import get_code


@pytest.fixture
def driver():
    return Chrome()


# 把登录成功为前置任务
@pytest.fixture(scope='session')
def user_driver():
    driver = Chrome()
    driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
    driver.maximize_window()
    page = DealPage(driver)
    msg = page.login('admin', 'msjy123')
    assert msg == '成功登录'
    return driver


# 支付密码正确
def test_user_deal_ok(user_driver):
    # driver = webdriver.Chrome()
    # driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
    # driver.maximize_window()
    page = DealPage(user_driver)
    pay_msg = page.pay('100', 'msjy123')
    assert pay_msg == '投标成功！'
    # driver.quit()


def test_user_deal_fail(user_driver):
    # driver = webdriver.Chrome()
    # driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
    # driver.maximize_window()
    page = DealPage(user_driver)
    pay_msg = page.pay('200', 'msjy12345')
    assert pay_msg == '支付密码错误'


def test_admin(driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    driver.maximize_window()
    admin_page = AdminPage(driver)
    code = get_code(driver)
    admin_page.login('admin', 'msjy123', code)
    assert driver.title == '码尚金融 - 管理员登录'
