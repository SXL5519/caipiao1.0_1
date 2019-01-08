from element_operate.base import Page
from element_position.lemi import BigLotteryConfirmLottery_loc
from element_position.lemi import ConfirmLottery_loc
from element_operate.base import Page_lexiu
from element_position.lexiu import BigLotteryConfirmLottery_lexiu_loc
from element_position.lexiu import ConfirmLottery_lexiu_loc
from time import sleep
from element_operate.base import Page_leyou
from element_position.leyou import BigLotteryConfirmLottery_leyou_loc
from element_position.leyou import ConfirmLottery_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import BigLotteryConfirmLottery_lelun_loc
from element_position.lelun import ConfirmLottery_lelun_loc
class BigLotteryConfirmLottery(Page,BigLotteryConfirmLottery_loc,ConfirmLottery_loc):
######点击“追加”单选按钮
    def additional_radio_button(self):
        self.wait_element_located(self.driver,self.additional_radio_button_loc)
        self.find_element(*self.additional_radio_button_loc).click()
####大乐透点击增加投注倍数
    def l_throw_times_button_add(self):
        self.wait_element_located(self.driver, self.l_throw_times_button_add_loc)
        self.find_element(*self.l_throw_times_button_add_loc).click()
    ####大乐透点击减少投注倍数
    def l_throw_times_button_sub(self,num):
        self.throw_times_input(num)
        self.wait_element_located(self.driver,self.l_throw_times_button_sub_loc)
        self.find_element(*self.l_throw_times_button_sub_loc).click()

    ####输入增加投注倍数
    def throw_times_input(self, num):
        self.wait_element_located(self.driver, self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).send_keys(num)

class BigLotteryConfirmLottery_lexiu(Page_lexiu,BigLotteryConfirmLottery_lexiu_loc,ConfirmLottery_lexiu_loc):
######点击“追加”单选按钮
    def additional_radio_button(self):
        self.wait_element_located(self.driver,self.additional_radio_button_loc)
        self.find_element(*self.additional_radio_button_loc).click()
####大乐透点击增加投注倍数
    def l_throw_times_button_add(self):
        self.wait_element_located(self.driver, self.l_throw_times_button_add_loc)
        self.find_element(*self.l_throw_times_button_add_loc).click()
    ####大乐透点击减少投注倍数
    def l_throw_times_button_sub(self,num):
        self.throw_times_input(num)
        self.wait_element_located(self.driver,self.l_throw_times_button_sub_loc)
        self.find_element(*self.l_throw_times_button_sub_loc).click()

    ####输入增加投注倍数
    def throw_times_input(self, num):
        self.wait_element_located(self.driver, self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).send_keys(num)

class BigLotteryConfirmLottery_leyou(Page_leyou,BigLotteryConfirmLottery_leyou_loc,ConfirmLottery_leyou_loc):
######点击“追加”单选按钮
    def additional_radio_button(self):
        self.wait_element_located(self.driver,self.additional_radio_button_loc)
        self.find_element(*self.additional_radio_button_loc).click()
####大乐透点击增加投注倍数
    def l_throw_times_button_add(self):
        self.wait_element_located(self.driver, self.l_throw_times_button_add_loc)
        self.find_element(*self.l_throw_times_button_add_loc).click()
    ####大乐透点击减少投注倍数
    def l_throw_times_button_sub(self,num):
        self.throw_times_input(num)
        self.wait_element_located(self.driver,self.l_throw_times_button_sub_loc)
        self.find_element(*self.l_throw_times_button_sub_loc).click()

    ####输入增加投注倍数
    def throw_times_input(self, num):
        self.wait_element_located(self.driver, self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).send_keys(num)

class BigLotteryConfirmLottery_lelun(Page_lelun,BigLotteryConfirmLottery_lelun_loc,ConfirmLottery_lelun_loc):
######点击“追加”单选按钮
    def additional_radio_button(self):
        self.wait_element_located(self.driver,self.additional_radio_button_loc)
        self.find_element(*self.additional_radio_button_loc).click()
####大乐透点击增加投注倍数
    def l_throw_times_button_add(self):
        self.wait_element_located(self.driver, self.l_throw_times_button_add_loc)
        self.find_element(*self.l_throw_times_button_add_loc).click()
    ####大乐透点击减少投注倍数
    def l_throw_times_button_sub(self,num):
        self.throw_times_input(num)
        self.wait_element_located(self.driver,self.l_throw_times_button_sub_loc)
        self.find_element(*self.l_throw_times_button_sub_loc).click()

    ####输入增加投注倍数
    def throw_times_input(self, num):
        self.wait_element_located(self.driver, self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).send_keys(num)
