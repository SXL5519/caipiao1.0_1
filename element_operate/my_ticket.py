from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import MyTicket_loc
import random
from element_position.lemi import Recharge_loc
from element_operate.base import Page_lexiu
from element_position.lexiu import MyTicket_lexiu_loc
from element_position.lexiu import Recharge_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import MyTicket_leyou_loc
from element_position.leyou import Recharge_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import MyTicket_lelun_loc
from element_position.lelun import Recharge_lelun_loc

#个人中心页面
class MyTicket(Page,MyTicket_loc,Recharge_loc):

#################################元素操作###############################################
    ############点击设置链接####################
    def setup_link(self):
        self.wait_element_located(self.driver, self.setup_link_loc)
        self.find_element(*self.setup_link_loc).click()
    #获取可用余额操作


    def available_cash_text(self):
        self.wait_element_located(self.driver, self.available_cash_loc)
        cash = self.find_element(*self.available_cash_loc).text
        if ',' in cash:
            text = cash.replace(',', '')
            print(text)
            return text

    def Recharge(self):
        self.wait_element_located(self.driver, self.recharge)
        self.find_element(*self.recharge).click()####点击充值

    def Recharge_Money(self):
        list=['50','100','200','500','1000']
        i = random.randint(0,4)
        self.find_element(*self.Recharge_money(list[i])).click()###点击充值金额
        print("点击充值"+list[i])

    def Next(self):
        self.wait_element_located(self.driver,self.next)
        self.find_element(*self.next).click()##点击下一步

    def More_payment(self):
        self.find_element(*self.more_payment).click()##点击更多支付方式

    def Account(self):
        self.wait_element_located(self.driver, self.account)
        aa=self.find_element(*self.account).text###读取账户
        return aa

    def Recharge_input(self,n):
        self.find_element(*self.recharge_input).send_keys(n)###输入充值金额

    def After_nu(self):
        self.find_element(*self.after_nu).click()##点击追号订单

    def After_nu_record(self):
        a=self.find_elements(*self.after_nu_record)
        if a:
            a[0].click()
        else:
            print('没有追号记录')
        return a

#个人中心页面
class MyTicket_lexiu(Page_lexiu,MyTicket_lexiu_loc,Recharge_lexiu_loc):

#################################元素操作###############################################
    ############点击设置链接####################
    def setup_link(self):
        self.wait_element_located(self.driver, self.setup_link_loc)
        self.find_element(*self.setup_link_loc).click()
    #获取可用余额操作


    def available_cash_text(self):
        self.wait_element_located(self.driver, self.available_cash_loc)
        cash = self.find_element(*self.available_cash_loc).text
        if ',' in cash:
            text = cash.replace(',', '')
            print(text)
            return text

    def Recharge(self):
        self.wait_element_located(self.driver, self.recharge)
        self.find_element(*self.recharge).click()####点击充值

    def Recharge_Money(self):
        list=['50','100','200','500','1000']
        i = random.randint(0,4)
        self.find_element(*self.Recharge_money(list[i])).click()###点击充值金额
        print("点击充值"+list[i])

    def Next(self):
        self.wait_element_located(self.driver,self.next)
        self.find_element(*self.next).click()##点击下一步

    def More_payment(self):
        self.find_element(*self.more_payment).click()##点击更多支付方式

    def Account(self):
        self.wait_element_located(self.driver, self.account)
        aa=self.find_element(*self.account).text###读取账户
        return aa

    def Recharge_input(self,n):
        self.find_element(*self.recharge_input).send_keys(n)###输入充值金额

    def After_nu(self):
        self.find_element(*self.after_nu).click()##点击追号订单

    def After_nu_record(self):
        a=self.find_elements(*self.after_nu_record)
        if a:
            a[0].click()
        else:
            print('没有追号记录')
        return a

class MyTicket_leyou(Page_leyou,MyTicket_leyou_loc,Recharge_leyou_loc):

#################################元素操作###############################################
    ############点击设置链接####################
    def setup_link(self):
        self.wait_element_located(self.driver, self.setup_link_loc)
        self.find_element(*self.setup_link_loc).click()
    #获取可用余额操作


    def available_cash_text(self):
        self.wait_element_located(self.driver, self.available_cash_loc)
        cash = self.find_element(*self.available_cash_loc).text
        if ',' in cash:
            text = cash.replace(',', '')
            print(text)
            return text

    def Recharge(self):
        self.wait_element_located(self.driver, self.recharge)
        self.find_element(*self.recharge).click()####点击充值

    def Recharge_Money(self):
        list=['50','100','200','500','1000']
        i = random.randint(0,4)
        self.find_element(*self.Recharge_money(list[i])).click()###点击充值金额
        print("点击充值"+list[i])

    def Next(self):
        self.wait_element_located(self.driver,self.next)
        self.find_element(*self.next).click()##点击下一步

    def More_payment(self):
        self.find_element(*self.more_payment).click()##点击更多支付方式

    def Account(self):
        self.wait_element_located(self.driver, self.account)
        aa=self.find_element(*self.account).text###读取账户
        return aa

    def Recharge_input(self,n):
        self.find_element(*self.recharge_input).send_keys(n)###输入充值金额

    def After_nu(self):
        self.find_element(*self.after_nu).click()##点击追号订单

    def After_nu_record(self):
        a=self.find_elements(*self.after_nu_record)
        if a:
            a[0].click()
        else:
            print('没有追号记录')
        return a

class MyTicket_lelun(Page_lelun,MyTicket_lelun_loc,Recharge_lelun_loc):

#################################元素操作###############################################
    ############点击设置链接####################
    def setup_link(self):
        self.wait_element_located(self.driver, self.setup_link_loc)
        self.find_element(*self.setup_link_loc).click()
    #获取可用余额操作


    def available_cash_text(self):
        self.wait_element_located(self.driver, self.available_cash_loc)
        cash = self.find_element(*self.available_cash_loc).text
        if ',' in cash:
            text = cash.replace(',', '')
            print(text)
            return text

    def Recharge(self):
        self.wait_element_located(self.driver, self.recharge)
        self.find_element(*self.recharge).click()####点击充值

    def Recharge_Money(self):
        list=['50','100','200','500','1000']
        i = random.randint(0,4)
        self.find_element(*self.Recharge_money(list[i])).click()###点击充值金额
        print("点击充值"+list[i])

    def Next(self):
        self.wait_element_located(self.driver,self.next)
        self.find_element(*self.next).click()##点击下一步

    def More_payment(self):
        self.find_element(*self.more_payment).click()##点击更多支付方式

    def Account(self):
        self.wait_element_located(self.driver, self.account)
        aa=self.find_element(*self.account).text###读取账户
        return aa

    def Recharge_input(self,n):
        self.find_element(*self.recharge_input).send_keys(n)###输入充值金额

    def After_nu(self):
        self.find_element(*self.after_nu).click()##点击追号订单

    def After_nu_record(self):
        a=self.find_elements(*self.after_nu_record)
        if a:
            a[0].click()
        else:
            print('没有追号记录')
        return a

