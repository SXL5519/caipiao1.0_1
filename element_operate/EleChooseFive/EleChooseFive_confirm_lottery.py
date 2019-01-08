from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import EleChooseFiveConfirmLottery_loc
from element_position.lemi import ConfirmLottery_loc
from selenium.common.exceptions import NoSuchElementException
from element_operate.base import Page_lexiu
from element_position.lexiu import EleChooseFiveConfirmLottery_lexiu_loc
from element_position.lexiu import ConfirmLottery_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import EleChooseFiveConfirmLottery_leyou_loc
from element_position.leyou import ConfirmLottery_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import EleChooseFiveConfirmLottery_lelun_loc
from element_position.lelun import ConfirmLottery_lelun_loc

###11选5投注确认页元素操作
class EleChooseFiveConfirmLottery(Page,EleChooseFiveConfirmLottery_loc,ConfirmLottery_loc):
    #获取倒计时文案
    def countdown_text(self):
        try:
            countdown_text = self.find_element(*self.countdown_text_loc).text
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")
    #点击机选一注
    def machine_choose_one(self):
        self.wait_element_located(self.driver,self.machine_choose_one_loc)
        self.find_element(*self.machine_choose_one_loc).click()
    #点击机选五注
    def machine_choose_five(self):
        self.wait_element_located(self.driver,self.machine_choose_five_loc)
        self.find_element(*self.machine_choose_five_loc).click()
    #点击继续选号按钮
    def continue_choose_num(self):
        self.wait_element_located(self.driver,self.continue_choose_num_loc)
        self.find_element(*self.continue_choose_num_loc).click()
    def delete_one_button(self):
        self.wait_element_located(self.driver,self.delete_one_button_loc)
        self.find_element(*self.delete_one_button_loc).click()
    #获取投注注数、追号期数、投注倍数文本
    def lottery_chase_throw_text(self):
        lottery_text = self.find_element(*self.lottery_chase_throw_text_loc).text
        return lottery_text
    #点击追xxx期
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()
        except NoSuchElementException:
            print("追期按钮缺失")
    ###############################################################################mj171020
    #输入追xxx期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    #点击追期的-按钮
    def chase_sub_button(self):
        try:
            self.find_element(*self.chase_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
    #点击追期的+按钮
    def chase_add_button(self):
        try:
            self.find_element(*self.chase_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
    #输入投xx倍
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    #点击投注倍数的+按钮
    def throw_times_add_button(self):
        try:
            self.find_element(*self.throw_add_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的+按钮缺失")
    #点击投注倍数的-按钮
    def throw_times_sub_button(self):
        try:
            self.find_element(*self.throw_sub_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的—按钮缺失")
    #点击提交订单给站主
    def submit_order_button(self):
        self.wait_element_located(self.driver,self.submit_order_button_loc)
        self.find_element(*self.submit_order_button_loc).click()
    ##11选5确认投注页的 追2期、追5期、追10期、追20期、追50期元素操作与双色球元素操作相同，文件名为confirm_lottery.py/操作类名为ConfirmLottery
    # “确认支付”、确认支付页的“X”按钮操作与双色球确认投注页元素操作一致
    def Ele_five_select_number(self):#获取11选5投注确认页的投注号码--mj20171211
        list = []
        a=self.find_element(*self.select_num_loc).text##读取选择的号码
        print("投注页的号码是：%s"%a)
        a1=a.replace('[','')
        a2=a1.replace(']',' ')
        list.append(a2)
        print(list)
        return list

class EleChooseFiveConfirmLottery_lexiu(Page_lexiu,EleChooseFiveConfirmLottery_lexiu_loc,ConfirmLottery_lexiu_loc):
    #获取倒计时文案
    def countdown_text(self):
        try:
            countdown_text = self.find_element(*self.countdown_text_loc).text
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")
    #点击机选一注
    def machine_choose_one(self):
        self.wait_element_located(self.driver,self.machine_choose_one_loc)
        self.find_element(*self.machine_choose_one_loc).click()
    #点击机选五注
    def machine_choose_five(self):
        self.wait_element_located(self.driver,self.machine_choose_five_loc)
        self.find_element(*self.machine_choose_five_loc).click()
    #点击继续选号按钮
    def continue_choose_num(self):
        self.wait_element_located(self.driver,self.continue_choose_num_loc)
        self.find_element(*self.continue_choose_num_loc).click()
    def delete_one_button(self):
        self.wait_element_located(self.driver,self.delete_one_button_loc)
        self.find_element(*self.delete_one_button_loc).click()
    #获取投注注数、追号期数、投注倍数文本
    def lottery_chase_throw_text(self):
        lottery_text = self.find_element(*self.lottery_chase_throw_text_loc).text
        return lottery_text
    #点击追xxx期
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()
        except NoSuchElementException:
            print("追期按钮缺失")
    ###############################################################################mj171020
    #输入追xxx期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    #点击追期的-按钮
    def chase_sub_button(self):
        try:
            self.find_element(*self.chase_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
    #点击追期的+按钮
    def chase_add_button(self):
        try:
            self.find_element(*self.chase_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
    #输入投xx倍
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    #点击投注倍数的+按钮
    def throw_times_add_button(self):
        try:
            self.find_element(*self.throw_add_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的+按钮缺失")
    #点击投注倍数的-按钮
    def throw_times_sub_button(self):
        try:
            self.find_element(*self.throw_sub_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的—按钮缺失")
    #点击提交订单给站主
    def submit_order_button(self):
        self.wait_element_located(self.driver,self.submit_order_button_loc)
        self.find_element(*self.submit_order_button_loc).click()
    ##11选5确认投注页的 追2期、追5期、追10期、追20期、追50期元素操作与双色球元素操作相同，文件名为confirm_lottery.py/操作类名为ConfirmLottery
    # “确认支付”、确认支付页的“X”按钮操作与双色球确认投注页元素操作一致
    def Ele_five_select_number(self):#获取11选5投注确认页的投注号码--mj20171211
        list = []
        a=self.find_element(*self.select_num_loc).text##读取选择的号码
        print("投注页的号码是：%s"%a)
        a1=a.replace('[','')
        a2=a1.replace(']',' ')
        list.append(a2)
        print(list)
        return list

class EleChooseFiveConfirmLottery_leyou(Page_leyou,EleChooseFiveConfirmLottery_leyou_loc,ConfirmLottery_leyou_loc):
    #获取倒计时文案
    def countdown_text(self):
        try:
            countdown_text = self.find_element(*self.countdown_text_loc).text
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")
    #点击机选一注
    def machine_choose_one(self):
        self.wait_element_located(self.driver,self.machine_choose_one_loc)
        self.find_element(*self.machine_choose_one_loc).click()
    #点击机选五注
    def machine_choose_five(self):
        self.wait_element_located(self.driver,self.machine_choose_five_loc)
        self.find_element(*self.machine_choose_five_loc).click()
    #点击继续选号按钮
    def continue_choose_num(self):
        self.wait_element_located(self.driver,self.continue_choose_num_loc)
        self.find_element(*self.continue_choose_num_loc).click()
    def delete_one_button(self):
        self.wait_element_located(self.driver,self.delete_one_button_loc)
        self.find_element(*self.delete_one_button_loc).click()
    #获取投注注数、追号期数、投注倍数文本
    def lottery_chase_throw_text(self):
        lottery_text = self.find_element(*self.lottery_chase_throw_text_loc).text
        return lottery_text
    #点击追xxx期
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()
        except NoSuchElementException:
            print("追期按钮缺失")
    ###############################################################################mj171020
    #输入追xxx期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    #点击追期的-按钮
    def chase_sub_button(self):
        try:
            self.find_element(*self.chase_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
    #点击追期的+按钮
    def chase_add_button(self):
        try:
            self.find_element(*self.chase_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
    #输入投xx倍
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    #点击投注倍数的+按钮
    def throw_times_add_button(self):
        try:
            self.find_element(*self.throw_add_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的+按钮缺失")
    #点击投注倍数的-按钮
    def throw_times_sub_button(self):
        try:
            self.find_element(*self.throw_sub_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的—按钮缺失")
    #点击提交订单给站主
    def submit_order_button(self):
        self.wait_element_located(self.driver,self.submit_order_button_loc)
        self.find_element(*self.submit_order_button_loc).click()
    ##11选5确认投注页的 追2期、追5期、追10期、追20期、追50期元素操作与双色球元素操作相同，文件名为confirm_lottery.py/操作类名为ConfirmLottery
    # “确认支付”、确认支付页的“X”按钮操作与双色球确认投注页元素操作一致
    def Ele_five_select_number(self):#获取11选5投注确认页的投注号码--mj20171211
        list = []
        a=self.find_element(*self.select_num_loc).text##读取选择的号码
        print("投注页的号码是：%s"%a)
        a1=a.replace('[','')
        a2=a1.replace(']',' ')
        list.append(a2)
        print(list)
        return list

class EleChooseFiveConfirmLottery_lelun(Page_lelun,EleChooseFiveConfirmLottery_lelun_loc,ConfirmLottery_lelun_loc):
    #获取倒计时文案
    def countdown_text(self):
        try:
            countdown_text = self.find_element(*self.countdown_text_loc).text
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")
    #点击机选一注
    def machine_choose_one(self):
        self.wait_element_located(self.driver,self.machine_choose_one_loc)
        self.find_element(*self.machine_choose_one_loc).click()
    #点击机选五注
    def machine_choose_five(self):
        self.wait_element_located(self.driver,self.machine_choose_five_loc)
        self.find_element(*self.machine_choose_five_loc).click()
    #点击继续选号按钮
    def continue_choose_num(self):
        self.wait_element_located(self.driver,self.continue_choose_num_loc)
        self.find_element(*self.continue_choose_num_loc).click()
    def delete_one_button(self):
        self.wait_element_located(self.driver,self.delete_one_button_loc)
        self.find_element(*self.delete_one_button_loc).click()
    #获取投注注数、追号期数、投注倍数文本
    def lottery_chase_throw_text(self):
        lottery_text = self.find_element(*self.lottery_chase_throw_text_loc).text
        return lottery_text
    #点击追xxx期
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()
        except NoSuchElementException:
            print("追期按钮缺失")
    ###############################################################################mj171020
    #输入追xxx期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    #点击追期的-按钮
    def chase_sub_button(self):
        try:
            self.find_element(*self.chase_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
    #点击追期的+按钮
    def chase_add_button(self):
        try:
            self.find_element(*self.chase_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
    #输入投xx倍
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    #点击投注倍数的+按钮
    def throw_times_add_button(self):
        try:
            self.find_element(*self.throw_add_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的+按钮缺失")
    #点击投注倍数的-按钮
    def throw_times_sub_button(self):
        try:
            self.find_element(*self.throw_sub_button_loc).click()
        except NoSuchElementException:
            print("投注倍数的—按钮缺失")
    #点击提交订单给站主
    def submit_order_button(self):
        self.wait_element_located(self.driver,self.submit_order_button_loc)
        self.find_element(*self.submit_order_button_loc).click()
    ##11选5确认投注页的 追2期、追5期、追10期、追20期、追50期元素操作与双色球元素操作相同，文件名为confirm_lottery.py/操作类名为ConfirmLottery
    # “确认支付”、确认支付页的“X”按钮操作与双色球确认投注页元素操作一致
    def Ele_five_select_number(self):#获取11选5投注确认页的投注号码--mj20171211
        list = []
        a=self.find_element(*self.select_num_loc).text##读取选择的号码
        print("投注页的号码是：%s"%a)
        a1=a.replace('[','')
        a2=a1.replace(']',' ')
        list.append(a2)
        print(list)
        return list
