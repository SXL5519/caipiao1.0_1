from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import SubmitOrderSuccess_loc
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from element_operate.base import Page_lexiu
from element_position.lexiu import SubmitOrderSuccess_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import SubmitOrderSuccess_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import SubmitOrderSuccess_lelun_loc
class LessPaySucess(Page,SubmitOrderSuccess_loc):

    #获取支付成功文本定位
    recharge_sucess_loc = (By.CSS_SELECTOR,".'f_17x'")
    pay_fail_loc = (By.CLASS_NAME,"c_333")


    #获取充值成功文本
    def recharge_sucess(self):
        #sucess_text = self.find_element(*self.recharge_sucess_loc)[1].text
        sucess_text = self.find_elements(By.CSS_SELECTOR,"span.f_17x")[1].text
        return sucess_text
    #获取支付成功文本
    def judge_pay_sucess(self):
        try:
            success_text = self.find_element(*self.submit_order_success_text_loc).text
            print(success_text)
            print("支付成功")
        except NoSuchElementException :

            fail_text = self.find_element(*self.pay_fail_loc).text
            print(fail_text)
            print("支付失败")


    def assect_pay(self):
        sleep(1)
        self.wait_element_located(self.driver, self.submit_order_success_text_loc)
        a=self.find_element(*self.submit_order_success_text_loc).text##读取支付状态文本
        return a

class LessPaySucess_lexiu(Page_lexiu,SubmitOrderSuccess_lexiu_loc):

    #获取支付成功文本定位
    recharge_sucess_loc = (By.CSS_SELECTOR,".'f_17x'")
    pay_fail_loc = (By.CLASS_NAME,"c_333")


    #获取充值成功文本
    def recharge_sucess(self):
        #sucess_text = self.find_element(*self.recharge_sucess_loc)[1].text
        sucess_text = self.find_elements(By.CSS_SELECTOR,"span.f_17x")[1].text
        return sucess_text
    #获取支付成功文本
    def judge_pay_sucess(self):
        try:
            success_text = self.find_element(*self.submit_order_success_text_loc).text
            print(success_text)
            print("支付成功")
        except NoSuchElementException :

            fail_text = self.find_element(*self.pay_fail_loc).text
            print(fail_text)
            print("支付失败")


    def assect_pay(self):
        sleep(1)
        self.wait_element_located(self.driver, self.submit_order_success_text_loc)
        a=self.find_element(*self.submit_order_success_text_loc).text##读取支付状态文本
        return a

class LessPaySucess_leyou(Page_leyou,SubmitOrderSuccess_leyou_loc):

    #获取支付成功文本定位
    recharge_sucess_loc = (By.CSS_SELECTOR,".'f_17x'")
    pay_fail_loc = (By.CLASS_NAME,"c_333")


    #获取充值成功文本
    def recharge_sucess(self):
        #sucess_text = self.find_element(*self.recharge_sucess_loc)[1].text
        sucess_text = self.find_elements(By.CSS_SELECTOR,"span.f_17x")[1].text
        return sucess_text
    #获取支付成功文本
    def judge_pay_sucess(self):
        try:
            success_text = self.find_element(*self.submit_order_success_text_loc).text
            print(success_text)
            print("支付成功")
        except NoSuchElementException :

            fail_text = self.find_element(*self.pay_fail_loc).text
            print(fail_text)
            print("支付失败")


    def assect_pay(self):
        sleep(1)
        self.wait_element_located(self.driver, self.submit_order_success_text_loc)
        a=self.find_element(*self.submit_order_success_text_loc).text##读取支付状态文本
        return a

class LessPaySucess_lelun(Page_lelun,SubmitOrderSuccess_lelun_loc):

    #获取支付成功文本定位
    recharge_sucess_loc = (By.CSS_SELECTOR,".'f_17x'")
    pay_fail_loc = (By.CLASS_NAME,"c_333")


    #获取充值成功文本
    def recharge_sucess(self):
        #sucess_text = self.find_element(*self.recharge_sucess_loc)[1].text
        sucess_text = self.find_elements(By.CSS_SELECTOR,"span.f_17x")[1].text
        return sucess_text
    #获取支付成功文本
    def judge_pay_sucess(self):
        try:
            success_text = self.find_element(*self.submit_order_success_text_loc).text
            print(success_text)
            print("支付成功")
        except NoSuchElementException :

            fail_text = self.find_element(*self.pay_fail_loc).text
            print(fail_text)
            print("支付失败")


    def assect_pay(self):
        sleep(1)
        self.wait_element_located(self.driver, self.submit_order_success_text_loc)
        a=self.find_element(*self.submit_order_success_text_loc).text##读取支付状态文本
        return a
