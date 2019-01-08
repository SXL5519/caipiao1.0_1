from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import ConfirmPay_loc
from element_operate.base import Page_lexiu
from element_position.lexiu import ConfirmPay_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import ConfirmPay_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import ConfirmPay_lelun_loc
class ConfirmPay(Page,ConfirmPay_loc):

    #点击“确认支付”按钮
    def confirm_pay(self):
        self.wait_element_located(self.driver,self.confirm_pay_loc)
        self.find_element(*self.confirm_pay_loc).click()

    def Pay_true(self):
        self.wait_element_located(self.driver, self.pay_true)
        aa=self.find_element(*self.pay_true).text##读取支付成功文本
        print(aa)
        return aa

    def Shut_down(self):
        self.find_element(*self.shut_down).click()##点击关闭

class ConfirmPay_lexiu(Page_lexiu,ConfirmPay_lexiu_loc):

    #点击“确认支付”按钮
    def confirm_pay(self):
        self.wait_element_located(self.driver,self.confirm_pay_loc)
        self.find_element(*self.confirm_pay_loc).click()

    def Pay_true(self):
        self.wait_element_located(self.driver, self.pay_true)
        aa=self.find_element(*self.pay_true).text##读取支付成功文本
        print(aa)
        return aa

    def Shut_down(self):
        self.find_element(*self.shut_down).click()##点击关闭

class ConfirmPay_leyou(Page_leyou,ConfirmPay_leyou_loc):

    #点击“确认支付”按钮
    def confirm_pay(self):
        self.wait_element_located(self.driver,self.confirm_pay_loc)
        self.find_element(*self.confirm_pay_loc).click()

    def Pay_true(self):
        self.wait_element_located(self.driver, self.pay_true)
        aa=self.find_element(*self.pay_true).text##读取支付成功文本
        print(aa)
        return aa

    def Shut_down(self):
        self.find_element(*self.shut_down).click()##点击关闭

class ConfirmPay_lelun(Page_lelun,ConfirmPay_lelun_loc):

    #点击“确认支付”按钮
    def confirm_pay(self):
        self.wait_element_located(self.driver,self.confirm_pay_loc)
        self.find_element(*self.confirm_pay_loc).click()

    def Pay_true(self):
        self.wait_element_located(self.driver, self.pay_true)
        aa=self.find_element(*self.pay_true).text##读取支付成功文本
        print(aa)
        return aa

    def Shut_down(self):
        self.find_element(*self.shut_down).click()##点击关闭