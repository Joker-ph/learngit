from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
def check_and_install_webdriver():
    options = ChromeOptions()     #实例化一个ChromeOptions对象
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  #以键值对的形式加入参数
    # 检查是否已经安装了 Chrome WebDriver
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)

    # driver.get('http://www.whxunw.com/exam/login.thtml')
    driver.get('http://www.baidu.com')
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.find_element('xpath','//*[@id="kw"]').send_keys('你好')
    driver.find_element('xpath','//*[@id="su"]').click()
    time.sleep(10)
check_and_install_webdriver()