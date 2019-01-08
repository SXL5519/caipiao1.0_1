from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_operate.base import Page_lexiu
from element_operate.base import Page_leyou
from element_operate.base import Page_lelun


class BaofooPayment(Page):

    #储蓄卡支付方式定位
    deposit_pay_loc = (By.CSS_SELECTOR,"li[data-type*='deposit']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")



    #选择储蓄卡支付
    def deposit_pay(self):
        self.wait_element_located(self.driver,self.deposit_pay_loc)
        self.find_element(*self.deposit_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()

class BaofooPayment_lexiu(Page_lexiu):

    #储蓄卡支付方式定位
    deposit_pay_loc = (By.CSS_SELECTOR,"li[data-type*='deposit']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")



    #选择储蓄卡支付
    def deposit_pay(self):
        self.wait_element_located(self.driver,self.deposit_pay_loc)
        self.find_element(*self.deposit_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()

class BaofooPayment_leyou(Page_leyou):

    #储蓄卡支付方式定位
    deposit_pay_loc = (By.CSS_SELECTOR,"li[data-type*='deposit']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")



    #选择储蓄卡支付
    def deposit_pay(self):
        self.wait_element_located(self.driver,self.deposit_pay_loc)
        self.find_element(*self.deposit_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()

class BaofooPayment_lelun(Page_lelun):

    #储蓄卡支付方式定位
    deposit_pay_loc = (By.CSS_SELECTOR,"li[data-type*='deposit']")
    #“下一步”按钮定位
    next_step_loc = (By.CLASS_NAME,"input")



    #选择储蓄卡支付
    def deposit_pay(self):
        self.wait_element_located(self.driver,self.deposit_pay_loc)
        self.find_element(*self.deposit_pay_loc).click()
    #点击“下一步”按钮
    def next_step(self):
        self.wait_element_located(self.driver,self.next_step_loc)
        self.find_element(*self.next_step_loc).click()


