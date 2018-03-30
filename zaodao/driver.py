from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from zaodao.config import *


class Driver(object):

    def __init__(self, timeout=20, head=None):

        # chromeUserSet = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
        # options.add_argument(chromeUserSet)
        # 配置谷歌浏览器为测试浏览器 并以headless模式运行
        options = webdriver.ChromeOptions()
        options.add_argument(head) if head != None else None
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, timeout)
        # 使用cookie登录
        self.user_login()

    def user_login(self):
        try:
            cookies = COOKIES
            print(INDEX_PAGE)
            self.browser.get(INDEX_PAGE)
            self.browser.add_cookie(cookies)
            self.browser.refresh()
        except:
            self.user_login()

    def get_index_page(self, url=TEST_URL):
        try:
            self.browser.get(url)
            element = self.wait.until(EC.presence_of_element_located((By.ID, "search_page"))).text
            time.sleep(1)
            return self.browser.page_source
        except TimeoutException:
            print("请求超时!正在重新发起请求...")
            self.get_index_page(url)

    def drive_close(self):
        self.browser.quit()


