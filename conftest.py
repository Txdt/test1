import json

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from commons.driver import get_webdriver
from commons.pom import DealPage, AdminPage
from commons.utils import get_code


@pytest.fixture
def anonymous_driver():
    driver = get_webdriver()
    yield driver


@pytest.fixture(scope="session")
def user_driver():
    driver = Chrome()
    driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
    driver.maximize_window()
    page = DealPage(driver)
    msg = page.login("admin", "msjy123")
    assert msg == '成功登录'
    yield driver


@pytest.fixture
def clear_deal_page(user_driver):
    user_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')


@pytest.fixture(scope='session')
def admin_driver():
    driver = get_webdriver()
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login')
    driver.maximize_window()
    # 加载cookies
    with open('datas/admin_cookies.json') as f:
        _data = f.read()
        if _data:
            cookies = json.loads(_data)
        else:
            cookies = []
    for cookie in cookies:
        driver.add_cookie(cookie)
    # 刷新页面
    driver.refresh()
    if not driver.title != '码尚金融 - 管理员登录':
        admin_page = AdminPage(driver)
        code = get_code(driver)  # 验证码识别
        msg = admin_page.login('admin', 'msjy123', code)
        assert msg == '登录成功'
    yield driver
    # 在后置中写入保存cookies
    cookies = driver.get_cookies()
    with open("datas/admin_cookies.json", 'w') as f:
        f.write(json.dumps(cookies))
