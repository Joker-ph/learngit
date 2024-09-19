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
    driver.get('http://www.whxunw.com/exam/login.thtml')
    driver.maximize_window()
    driver.implicitly_wait(3)
    while True:
        try:
            driver.find_elements('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div')
            #
            choose = driver.find_elements('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[1]')
            choose.click()
            time.sleep(1)
            be_sure = driver.find_elements('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/button')
            be_sure.click()
            time.sleep(1)
            close = driver.find_elements('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/button')
            close.click()
        except:
            time.sleep(10)
check_and_install_webdriver()
