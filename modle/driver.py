from selenium import webdriver
from time import sleep

# class Browser():
#     def __init__(self):
#        self.driver = webdriver.PhantomJS()
#
#     def get_driver(self):
#         return self.driver



class Chrome():
    # 配置谷歌浏览器模拟'Galaxy S5'手机打开浏览器
    mobileEmulation = {'deviceName': 'Galaxy S5'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    #驱动最大化打开谷歌浏览器
    def browser_chrome(self):
        #executable_path = 'C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'  ##马洁的谷歌浏览器驱动
        executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\\chromedriver.exe'##邵新林的谷歌浏览器驱动
        #executable_path = 'C:\Program Files (x86)\Application\\chromedriver.exe'#执行机的谷歌驱动

        self.driver=webdriver.Chrome(executable_path,
                                     chrome_options=self.options)
        # display = Display(visible=0, size=(800, 800))
        # display.start()
        self.driver.set_window_size(500,800)
        sleep(0.1)

        return self.driver
