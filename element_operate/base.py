from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Page():

    base_url="http://mtest.xiaomicache.com/"#乐米测试环境
    #base_url = "http://192.168.2.204:10093/"#本地环境
    #初始化方法
    def __init__(self,driver,url=base_url):
        self.driver = driver
        self.url = url
        self.time=2

    #打开相应网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.time)

    #二次封装元素定位的方法
    def find_element(self,*loc):

        return self.driver.find_element(*loc)
    #二次封装显示等待的方法
    def wait_element_located(self,driver,locator):
        wait = WebDriverWait(driver,20)
        wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)



class Page_lexiu():

    base_url="http://mtest.lexuncp.com/"#乐秀测试环境
    #base_url = "http://192.168.2.204:10093/"#本地环境
    #初始化方法
    def __init__(self,driver,url=base_url):
        self.driver = driver
        self.url = url
        self.time=2

    #打开相应网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.time)

    #二次封装元素定位的方法
    def find_element(self,*loc):

        return self.driver.find_element(*loc)
    #二次封装显示等待的方法
    def wait_element_located(self,driver,locator):
        wait = WebDriverWait(driver,20)
        wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

class Page_leyou():

    base_url="http://mtest.leyoucp.com/"#乐优测试环境
    #base_url = "http://192.168.2.204:10093/"#本地环境
    #初始化方法
    def __init__(self,driver,url=base_url):
        self.driver = driver
        self.url = url
        self.time=2

    #打开相应网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.time)

    #二次封装元素定位的方法
    def find_element(self,*loc):

        return self.driver.find_element(*loc)
    #二次封装显示等待的方法
    def wait_element_located(self,driver,locator):
        wait = WebDriverWait(driver,20)
        wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

class Page_lelun():

    base_url="http://mtest.leluncp.com/"#乐优测试环境
    #base_url = "http://192.168.2.204:10093/"#本地环境
    #初始化方法
    def __init__(self,driver,url=base_url):
        self.driver = driver
        self.url = url
        self.time=2

    #打开相应网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.time)

    #二次封装元素定位的方法
    def find_element(self,*loc):

        return self.driver.find_element(*loc)
    #二次封装显示等待的方法
    def wait_element_located(self,driver,locator):
        wait = WebDriverWait(driver,20)
        wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)





