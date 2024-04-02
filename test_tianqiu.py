import pytest
from selenium.webdriver.common.by import By

from commons.datas_util import DataUtil
from commons.pom import DealPage, AdminPage
from commons.utils import get_code


def test_admin_new_deal(admin_driver):
    # 隐式等待
    admin_driver.implicitly_wait(5)
    iframe = admin_driver.find_element(By.XPATH, '/html/frameset/frame[1]')
    admin_driver.switch_to.frame(iframe)
    assert '登录账户:admin' in admin_driver.page_source

def test_user_login_ok(anonymous_driver):
    anonymous_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
    anonymous_driver.maximize_window()
    page = DealPage(anonymous_driver)
    msg = page.login("admin", "msjy123")
    assert msg == '成功登录'


def test_user_login_fail(anonymous_driver):
    anonymous_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
    anonymous_driver.maximize_window()
    page = DealPage(anonymous_driver)
    msg = page.login("admin", "msjy123567")
    assert msg == '密码错误'


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


def test_admin(anonymous_driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    code = get_code(anonymous_driver)
    msg = admin_page.login('admin', 'msjy123', code)
    assert msg == '登录成功'


@pytest.mark.parametrize("username, password, code, assert_msg", DataUtil.get_regist_data())
def test_admin_data(anonymous_driver, username, password, code, assert_msg):
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    msg = admin_page.login(username, password, code)
    assert msg == assert_msg


def test_admin_login_1(anonymous_driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    msg = admin_page.login('', '', '')
    assert msg == '管理员帐号不能为空'


def test_admin_login_2(anonymous_driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    msg = admin_page.login('admin', '', '')
    assert msg == '管理员密码不能为空'


def test_admin_login_3(anonymous_driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    msg = admin_page.login('admin', 'msjy123', '')
    assert msg == '验证码不能为空'


def test_admin_login_4(anonymous_driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    msg = admin_page.login('admin', 'msjy123', '3422')
    assert msg == '验证码错误'


def test_admin_login_5(anonymous_driver):
    # 后台管理员登录
    # driver = webdriver.Chrome()
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    anonymous_driver.maximize_window()
    admin_page = AdminPage(anonymous_driver)
    msg = admin_page.login('', 'msjy123', '3422')
    assert msg == '管理员帐号不能为空'
