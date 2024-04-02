from selenium.webdriver import Chrome, Firefox, Ie, Safari


def get_webdriver(name: str = 'chrome'):
    name = name.lower()
    name = name.replace(" ", "")
    if name == 'chrome':
        return Chrome()
    elif name == 'firefox':
        return Firefox()
    elif name == 'ie':
        return Ie()
    elif name == 'safari':
        return Safari()

