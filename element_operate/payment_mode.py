from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_operate.base import Page_lexiu
from element_operate.base import Page_leyou
from element_operate.base import Page_lelun

class PaymetMode(Page):

    #更多支付方式链接定位
    morecharge_loc = (By.CLASS_NAME,"j-morecharge")
    #宝付支付定位
    baofoo_loc = (By.ID,"baofoo")
    top_up=(By.CSS_SELECTOR,'body > header > div > h3')###充值文本
    def Top_up(self):###获取充值成功文本
        a=self.find_element(*self.top_up).text
        return a
    #点击更多支付方式链接
    def morecharge(self):
        self.wait_element_located(self.driver,self.morecharge_loc)
        self.find_element(*self.morecharge_loc).click()

    #点击宝付支付
    def baofoo_payment(self):
        self.wait_element_located(self.driver,self.baofoo_loc)
        self.find_element(*self.baofoo_loc).click()

class PaymetMode_lexiu(Page_lexiu):

    #更多支付方式链接定位
    morecharge_loc = (By.CLASS_NAME,"j-morecharge")
    #宝付支付定位
    baofoo_loc = (By.ID,"baofoo")
    top_up = (By.CSS_SELECTOR, 'body > header > div > h3')  ###充值文本

    def Top_up(self):  ###获取充值成功文本
        a = self.find_element(*self.top_up).text
        return a


    #点击更多支付方式链接
    def morecharge(self):
        self.wait_element_located(self.driver,self.morecharge_loc)
        self.find_element(*self.morecharge_loc).click()

    #点击宝付支付
    def baofoo_payment(self):
        self.wait_element_located(self.driver,self.baofoo_loc)
        self.find_element(*self.baofoo_loc).click()

class PaymetMode_leyou(Page_leyou):

    #更多支付方式链接定位
    morecharge_loc = (By.CLASS_NAME,"j-morecharge")
    #宝付支付定位
    baofoo_loc = (By.ID,"baofoo")
    top_up = (By.CSS_SELECTOR, 'body > header > div > h3')  ###充值文本

    def Top_up(self):  ###获取充值成功文本
        a = self.find_element(*self.top_up).text
        return a


    #点击更多支付方式链接
    def morecharge(self):
        self.wait_element_located(self.driver,self.morecharge_loc)
        self.find_element(*self.morecharge_loc).click()

    #点击宝付支付
    def baofoo_payment(self):
        self.wait_element_located(self.driver,self.baofoo_loc)
        self.find_element(*self.baofoo_loc).click()

class PaymetMode_lelun(Page_lelun):

    #更多支付方式链接定位
    morecharge_loc = (By.CLASS_NAME,"j-morecharge")
    #宝付支付定位
    baofoo_loc = (By.ID,"baofoo")
    top_up = (By.CSS_SELECTOR, 'body > header > div > h3')  ###充值文本

    def Top_up(self):  ###获取充值成功文本
        a = self.find_element(*self.top_up).text
        return a


    #点击更多支付方式链接
    def morecharge(self):
        self.wait_element_located(self.driver,self.morecharge_loc)
        self.find_element(*self.morecharge_loc).click()

    #点击宝付支付
    def baofoo_payment(self):
        self.wait_element_located(self.driver,self.baofoo_loc)
        self.find_element(*self.baofoo_loc).click()