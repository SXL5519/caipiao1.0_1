from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_operate.base import Page_lexiu
from element_operate.base import Page_leyou
from element_operate.base import Page_lelun
class ChooseBank(Page):

    # “招商银行”卡支付定位
    merchants_pay_loc = (By.CSS_SELECTOR, "li[data-id='4020001']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")

    #点击选择“招商银行”支付
    def merchants_pay(self):
        self.wait_element_located(self.driver,self.merchants_pay_loc)
        self.find_element(*self.merchants_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()

class ChooseBank_lexiu(Page_lexiu):

    # “招商银行”卡支付定位
    merchants_pay_loc = (By.CSS_SELECTOR, "li[data-id='4020001']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")

    #点击选择“招商银行”支付
    def merchants_pay(self):
        self.wait_element_located(self.driver,self.merchants_pay_loc)
        self.find_element(*self.merchants_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()

class ChooseBank_leyou(Page_leyou):

    # “招商银行”卡支付定位
    merchants_pay_loc = (By.CSS_SELECTOR, "li[data-id='4020001']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")

    #点击选择“招商银行”支付
    def merchants_pay(self):
        self.wait_element_located(self.driver,self.merchants_pay_loc)
        self.find_element(*self.merchants_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()

class ChooseBank_lelun(Page_lelun):

    # “招商银行”卡支付定位
    merchants_pay_loc = (By.CSS_SELECTOR, "li[data-id='4020001']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")

    #点击选择“招商银行”支付
    def merchants_pay(self):
        self.wait_element_located(self.driver,self.merchants_pay_loc)
        self.find_element(*self.merchants_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()
    