from element_operate.base import Page
from element_position.lemi import ConfirmLottery_loc
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException,WebDriverException
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from element_operate.base import Page_lexiu
from element_position.lexiu import ConfirmLottery_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import ConfirmLottery_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import ConfirmLottery_lelun_loc

###投注确认页元素操作#####
class ConfirmLottery(Page,ConfirmLottery_loc):
    #################################元素操作######################################
    #获取投注确认页的“提交订单给站主”的文本
    def confirm_num_page_text(self):#---mj20171207修改
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)
        confirm_cathectic = self.find_element(*self.submit_order_to_station_owner_button_loc).text
        return confirm_cathectic
    #点击“继续选号”按钮
    def continue_choose_num_button(self):
        self.find_element(*self.continue_choose_num_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.find_element(*self.Machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.find_element(*self.Machine_choose_five_button_loc).click()
    #点击“重新选号链接”
    def re_selection_num(self):
        self.wait_element_located(self.driver,self.re_selection_num_loc)#重新选号链接可见时，进行点击操作
        self.find_element(*self.re_selection_num_loc).click()
    #点击“清除所有选号”按钮
    def delete_all_num_button(self):
        self.wait_element_located(self.driver,self.delete_all_num_button_loc)
        self.find_element(*self.delete_all_num_button_loc).click()
    #点击“清除单个选号”
    def delete_one_num_button(self):
        self.wait_element_located(self.driver,self.delete_one_num_button_loc)
        self.find_element(*self.delete_one_num_button_loc).click()

    ##############################mj20171206
    def del_n(self, n):
        self.wait_element_located(self.driver, self.del_n_loc(n))
        self.find_element(*self.del_n_loc(n)).click()  ####点击清除第n个投注
    # 获取投注确认页共有多少笔投注
    def event_count(self):
        aa = self.find_elements(*self.event_field_loc)
        return len(aa)
    ##############################mj20171206############################
    #点击“确定清除所有选号”按钮
    def confirm_delete_button(self):
        self.wait_element_located(self.driver,self.confirm_delete_button_loc)
        self.find_element(*self.confirm_delete_button_loc).click()
    #点击“取消清除所有选号”按钮
    def cancel_delete_button(self):
        self.wait_element_located(self.driver,self.cancel_delete_button_loc)
        self.find_element(*self.cancel_delete_button_loc).click()
    ##点击“追xx期”
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()  # 点击追XX期
        except NoSuchElementException:
            print("追xx期按钮缺失")
            raise
    ##点击中奖停追
    def stop_chase_win_radio(self):
        try:
            self.find_element(*self.stop_chase_win_radio_loc).click()  # 点击中奖停追单选按钮
        except NoSuchElementException:
            print("中奖停追按钮缺失")
            raise
    ######点击“追两期”按钮
    def chase_ticket_button_two(self):
        try:
            self.find_element(*self.chase_ticket_button_two_loc).click()#点击追2期
        except NoSuchElementException:
            print("追2期按钮缺失")
            raise
    ####点击“追5期”
    def chase_ticket_button_five(self):
        try:
            self.find_element(*self.chase_ticket_button_five_loc).click()#点击追5期
        except NoSuchElementException:
            print("追5期按钮缺失")
            raise
    ####点击“追10期”
    def chase_ticket_button_ten(self):
        try:
            self.find_element(*self.chase_ticket_button_ten_loc).click()#点击追10期
        except NoSuchElementException:
            print("追10期按钮缺失")
            raise
    ###点击“追20期”
    def chase_ticket_button_twenty(self):
        try:
            self.find_element(*self.chase_ticket_button_twenty_loc).click()  # 点击追20期
        except NoSuchElementException:
            print("追20期按钮缺失")
            raise
    ####点击“追50期”
    def chase_ticket_button_fifty(self):
        try:
            self.find_element(*self.chase_ticket_button_fifty_loc).click()  # 点击追50期
        except NoSuchElementException:
            print("追50期按钮缺失")
            raise
    ###输入追XX期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    ####输入增加投注倍数
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    ###获取投注注数文本
    def lottery_number_text(self):
        self.wait_element_located(self.driver,self.lottery_number_text_loc)
        lottery_number = self.find_element(*self.lottery_number_text_loc).text
        return lottery_number
    ###获取所追期数
    def chase_time_text(self):
        self.wait_element_located(self.driver,self.chase_times_text_loc)
        chase_times = self.find_element(*self.chase_times_text_loc).text
        return chase_times
    #####获取投注倍数
    def throw_time_text(self):
        self.wait_element_located(self.driver, self.throw_times_text_loc)
        throw_times = self.find_element(*self.throw_times_text_loc).text
        return throw_times
    ####双色球点击增加追期数
    def u_chase_ticket_add_button(self):
        try:
            self.find_element(*self.chase_ticket_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
            raise
    ###双色球点击减少追期数
    def u_chase_ticket_sub_button(self):
        try:
            self.find_element(*self.chase_ticket_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
            raise
    ####双色球点击增加投注倍数
    def u_throw_times_button_add(self):
        try:
            self.find_element(*self.u_throw_times_button_add_loc).click()
        except NoSuchElementException:
            print("投注倍数+按钮缺失")
            raise
    ####双色球点击减少投注倍数
    def u_throw_times_button_sub(self):
        try:
            self.find_element(*self.u_throw_times_button_sub_loc).click()
        except NoSuchElementException:
            print("投注倍数-按钮缺失")
            raise
    ######点击“提交订单给站主”按钮
    def submit_order_to_station_owner_button(self):
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)#显示等待提交按钮出现，进行点击操作
        self.find_element(*self.submit_order_to_station_owner_button_loc).click()
    ###订单金额超过100000元的时候，弹出提示信息
    def out_max_pay(self):
        self.wait_element_located(self.driver,self.toast_loc)#显示等待，等待提示信息出现再进行获取文本操作
        out_max_pay_text=self.find_element(*self.toast_loc).text
        sleep(2)
        print(out_max_pay_text)
        return out_max_pay_text
    # #所投期停止销售时，弹出提示信息“该期已截止销售”
    # def stop_sale_toast(self):
    #     try:
    #         stop_sale_text = self.find_element(*self.toast_loc).text
    #         print(stop_sale_text)
    #         self.find_element(self.)
    #     except NoSuchElementException:
    #         print("该期在售")
    #####点击“确认并支付”按钮
    def confirm_and_pay_button(self):
        try:
            self.wait_element_located(self.driver, self.confirm_and_pay_button_loc)
            self.find_element(*self.confirm_and_pay_button_loc).click()###点击确认支付
        except TimeoutException:
            self.find_element(*self.submit_frequently).click()##提示提交频繁，点击知道了
    #点击确认支付页面的x按钮
    def cancel_pay_button(self):
        self.wait_element_located(self.driver, self.cancel_pay_button_loc)
        self.find_element(*self.cancel_pay_button_loc).click()

    def User_agreement(self):
        self.find_element(*self.user_agreement).click()##点击用户协议

    def User_know(self):
        self.find_element(*self.user_know).click()##点击用户协议，我知道了

    def Risk(self):
        self.find_element(*self.risk).click()###点击购彩风险

    def Risk_know(self):
        self.find_element(*self.risk_know).click()##点击购彩风险，我知道了

    def Select_number(self):
        list=[]
        a=self.find_element(*self.select_red).text##读取选择的红球
        b=self.find_element(*self.select_blue).text##读取蓝球
        c=a+' '+b##在2个字符串中间添加空格
        list.append(c)
        print(list)
        return list

    def Del_x(self):
        self.find_element(*self.del_X).click()###点击左侧X按钮
    def lottery_confirm_num_page_text(self):#获取投注确认页文本---mj20171207
        self.wait_element_located(self.driver,self.confirm_num_page_text_loc)
        lottery_text = self.find_element(*self.confirm_num_page_text_loc).text
        return lottery_text

    def n_event_count(self):   ###随机点击1注X按钮
        aa = self.find_elements(*self.event_field_loc)
        i=random.randint(0,len(aa)-1)
        aa[i].click()
        print("删除第%d注"%(i+1))

    def Unionlotto_History_buy(self):
        self.find_element(*self.unionlotto_History_buy).click()##点击历史开奖信息中的最近开奖信息

    def Buy_unionlotto(self):
        self.find_element(*self.buy_unionlotto).click()###点击投注双色球

    def Choose_color(self):
        self.find_element(*self.choose_color).click()##幸运选号，点击选择彩种入口

    def Choose_note(self):
        self.find_element(*self.choose_note).click()##幸运选号，点击选择注数入口

    def Lucky_unionlotto(self,driver):###选择双色球
        driver.click_and_hold(self.find_element(*self.lucky_unionlotto)).move_to_element(self.find_element(*self.lucky_lottery)).release().perform()
        #driver.drag_and_drop(self.find_element(*self.lucky_lottery), self.find_element(*self.lucky_unionlotto)).perform()##实现鼠标拖拽


    def Complete(self):
        self.find_element(*self.complete).click()###点击完成

###投注确认页元素操作#####
class ConfirmLottery_lexiu(Page_lexiu,ConfirmLottery_lexiu_loc):
    #################################元素操作######################################
    #获取投注确认页的“提交订单给站主”的文本
    def confirm_num_page_text(self):#---mj20171207修改
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)
        confirm_cathectic = self.find_element(*self.submit_order_to_station_owner_button_loc).text
        return confirm_cathectic
    #点击“继续选号”按钮
    def continue_choose_num_button(self):
        self.find_element(*self.continue_choose_num_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.find_element(*self.Machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.find_element(*self.Machine_choose_five_button_loc).click()
    #点击“重新选号链接”
    def re_selection_num(self):
        self.wait_element_located(self.driver,self.re_selection_num_loc)#重新选号链接可见时，进行点击操作
        self.find_element(*self.re_selection_num_loc).click()
    #点击“清除所有选号”按钮
    def delete_all_num_button(self):
        self.wait_element_located(self.driver,self.delete_all_num_button_loc)
        self.find_element(*self.delete_all_num_button_loc).click()
    #点击“清除单个选号”
    def delete_one_num_button(self):
        self.wait_element_located(self.driver,self.delete_one_num_button_loc)
        self.find_element(*self.delete_one_num_button_loc).click()

    ##############################mj20171206
    def del_n(self, n):
        self.wait_element_located(self.driver, self.del_n_loc(n))
        self.find_element(*self.del_n_loc(n)).click()  ####点击清除第n个投注
    # 获取投注确认页共有多少笔投注
    def event_count(self):
        aa = self.find_elements(*self.event_field_loc)
        return len(aa)
    ##############################mj20171206############################
    #点击“确定清除所有选号”按钮
    def confirm_delete_button(self):
        self.wait_element_located(self.driver,self.confirm_delete_button_loc)
        self.find_element(*self.confirm_delete_button_loc).click()
    #点击“取消清除所有选号”按钮
    def cancel_delete_button(self):
        self.wait_element_located(self.driver,self.cancel_delete_button_loc)
        self.find_element(*self.cancel_delete_button_loc).click()
    ##点击“追xx期”
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()  # 点击追XX期
        except NoSuchElementException:
            print("追xx期按钮缺失")
            raise
    ##点击中奖停追
    def stop_chase_win_radio(self):
        try:
            self.find_element(*self.stop_chase_win_radio_loc).click()  # 点击中奖停追单选按钮
        except NoSuchElementException:
            print("中奖停追按钮缺失")
            raise
    ######点击“追两期”按钮
    def chase_ticket_button_two(self):
        try:
            self.find_element(*self.chase_ticket_button_two_loc).click()#点击追2期
        except NoSuchElementException:
            print("追2期按钮缺失")
            raise
    ####点击“追5期”
    def chase_ticket_button_five(self):
        try:
            self.find_element(*self.chase_ticket_button_five_loc).click()#点击追5期
        except NoSuchElementException:
            print("追5期按钮缺失")
            raise
    ####点击“追10期”
    def chase_ticket_button_ten(self):
        try:
            self.find_element(*self.chase_ticket_button_ten_loc).click()#点击追10期
        except NoSuchElementException:
            print("追10期按钮缺失")
            raise
    ###点击“追20期”
    def chase_ticket_button_twenty(self):
        try:
            self.find_element(*self.chase_ticket_button_twenty_loc).click()  # 点击追20期
        except NoSuchElementException:
            print("追20期按钮缺失")
            raise
    ####点击“追50期”
    def chase_ticket_button_fifty(self):
        try:
            self.find_element(*self.chase_ticket_button_fifty_loc).click()  # 点击追50期
        except NoSuchElementException:
            print("追50期按钮缺失")
            raise
    ###输入追XX期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    ####输入增加投注倍数
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    ###获取投注注数文本
    def lottery_number_text(self):
        self.wait_element_located(self.driver,self.lottery_number_text_loc)
        lottery_number = self.find_element(*self.lottery_number_text_loc).text
        return lottery_number
    ###获取所追期数
    def chase_time_text(self):
        self.wait_element_located(self.driver,self.chase_times_text_loc)
        chase_times = self.find_element(*self.chase_times_text_loc).text
        return chase_times
    #####获取投注倍数
    def throw_time_text(self):
        self.wait_element_located(self.driver, self.throw_times_text_loc)
        throw_times = self.find_element(*self.throw_times_text_loc).text
        return throw_times
    ####双色球点击增加追期数
    def u_chase_ticket_add_button(self):
        try:
            self.find_element(*self.chase_ticket_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
            raise
    ###双色球点击减少追期数
    def u_chase_ticket_sub_button(self):
        try:
            self.find_element(*self.chase_ticket_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
            raise
    ####双色球点击增加投注倍数
    def u_throw_times_button_add(self):
        try:
            self.find_element(*self.u_throw_times_button_add_loc).click()
        except NoSuchElementException:
            print("投注倍数+按钮缺失")
            raise
    ####双色球点击减少投注倍数
    def u_throw_times_button_sub(self):
        try:
            self.find_element(*self.u_throw_times_button_sub_loc).click()
        except NoSuchElementException:
            print("投注倍数-按钮缺失")
            raise
    ######点击“提交订单给站主”按钮
    def submit_order_to_station_owner_button(self):
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)#显示等待提交按钮出现，进行点击操作
        self.find_element(*self.submit_order_to_station_owner_button_loc).click()
    ###订单金额超过100000元的时候，弹出提示信息
    def out_max_pay(self):
        self.wait_element_located(self.driver,self.toast_loc)#显示等待，等待提示信息出现再进行获取文本操作
        out_max_pay_text=self.find_element(*self.toast_loc).text
        sleep(2)
        print(out_max_pay_text)
        return out_max_pay_text
    # #所投期停止销售时，弹出提示信息“该期已截止销售”
    # def stop_sale_toast(self):
    #     try:
    #         stop_sale_text = self.find_element(*self.toast_loc).text
    #         print(stop_sale_text)
    #         self.find_element(self.)
    #     except NoSuchElementException:
    #         print("该期在售")
    #####点击“确认并支付”按钮
    def confirm_and_pay_button(self):
        try:
            self.wait_element_located(self.driver, self.confirm_and_pay_button_loc)
            self.find_element(*self.confirm_and_pay_button_loc).click()###点击确认支付
        except TimeoutException:
            self.find_element(*self.submit_frequently).click()##提示提交频繁，点击知道了
    #点击确认支付页面的x按钮
    def cancel_pay_button(self):
        self.wait_element_located(self.driver, self.cancel_pay_button_loc)
        self.find_element(*self.cancel_pay_button_loc).click()

    def User_agreement(self):
        self.find_element(*self.user_agreement).click()##点击用户协议

    def User_know(self):
        self.find_element(*self.user_know).click()##点击用户协议，我知道了

    def Risk(self):
        self.find_element(*self.risk).click()###点击购彩风险

    def Risk_know(self):
        self.find_element(*self.risk_know).click()##点击购彩风险，我知道了

    def Select_number(self):
        list=[]
        a=self.find_element(*self.select_red).text##读取选择的红球
        b=self.find_element(*self.select_blue).text##读取蓝球
        c=a+' '+b##在2个字符串中间添加空格
        list.append(c)
        print(list)
        return list

    def Del_x(self):
        self.find_element(*self.del_X).click()###点击左侧X按钮
    def lottery_confirm_num_page_text(self):#获取投注确认页文本---mj20171207
        self.wait_element_located(self.driver,self.confirm_num_page_text_loc)
        lottery_text = self.find_element(*self.confirm_num_page_text_loc).text
        return lottery_text

    def n_event_count(self):   ###随机点击1注X按钮
        aa = self.find_elements(*self.event_field_loc)
        i=random.randint(0,len(aa)-1)
        aa[i].click()
        print("删除第%d注"%(i+1))

    def Unionlotto_History_buy(self):
        self.find_element(*self.unionlotto_History_buy).click()##点击历史开奖信息中的最近开奖信息

    def Buy_unionlotto(self):
        self.find_element(*self.buy_unionlotto).click()###点击投注双色球

    def Choose_color(self):
        self.find_element(*self.choose_color).click()##幸运选号，点击选择彩种入口

    def Choose_note(self):
        self.find_element(*self.choose_note).click()##幸运选号，点击选择注数入口

    def Lucky_unionlotto(self,driver):###选择双色球
        driver.click_and_hold(self.find_element(*self.lucky_unionlotto)).move_to_element(self.find_element(*self.lucky_lottery)).release().perform()
        #driver.drag_and_drop(self.find_element(*self.lucky_lottery), self.find_element(*self.lucky_unionlotto)).perform()##实现鼠标拖拽


    def Complete(self):
        self.find_element(*self.complete).click()###点击完成

class ConfirmLottery_leyou(Page_leyou,ConfirmLottery_leyou_loc):
    #################################元素操作######################################
    #获取投注确认页的“提交订单给站主”的文本
    def confirm_num_page_text(self):#---mj20171207修改
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)
        confirm_cathectic = self.find_element(*self.submit_order_to_station_owner_button_loc).text
        return confirm_cathectic
    #点击“继续选号”按钮
    def continue_choose_num_button(self):
        self.find_element(*self.continue_choose_num_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.find_element(*self.Machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.find_element(*self.Machine_choose_five_button_loc).click()
    #点击“重新选号链接”
    def re_selection_num(self):
        self.wait_element_located(self.driver,self.re_selection_num_loc)#重新选号链接可见时，进行点击操作
        self.find_element(*self.re_selection_num_loc).click()
    #点击“清除所有选号”按钮
    def delete_all_num_button(self):
        self.wait_element_located(self.driver,self.delete_all_num_button_loc)
        self.find_element(*self.delete_all_num_button_loc).click()
    #点击“清除单个选号”
    def delete_one_num_button(self):
        self.wait_element_located(self.driver,self.delete_one_num_button_loc)
        self.find_element(*self.delete_one_num_button_loc).click()

    ##############################mj20171206
    def del_n(self, n):
        self.wait_element_located(self.driver, self.del_n_loc(n))
        self.find_element(*self.del_n_loc(n)).click()  ####点击清除第n个投注
    # 获取投注确认页共有多少笔投注
    def event_count(self):
        aa = self.find_elements(*self.event_field_loc)
        return len(aa)
    ##############################mj20171206############################
    #点击“确定清除所有选号”按钮
    def confirm_delete_button(self):
        self.wait_element_located(self.driver,self.confirm_delete_button_loc)
        self.find_element(*self.confirm_delete_button_loc).click()
    #点击“取消清除所有选号”按钮
    def cancel_delete_button(self):
        self.wait_element_located(self.driver,self.cancel_delete_button_loc)
        self.find_element(*self.cancel_delete_button_loc).click()
    ##点击“追xx期”
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()  # 点击追XX期
        except NoSuchElementException:
            print("追xx期按钮缺失")
            raise
    ##点击中奖停追
    def stop_chase_win_radio(self):
        try:
            self.find_element(*self.stop_chase_win_radio_loc).click()  # 点击中奖停追单选按钮
        except NoSuchElementException:
            print("中奖停追按钮缺失")
            raise
    ######点击“追两期”按钮
    def chase_ticket_button_two(self):
        try:
            self.find_element(*self.chase_ticket_button_two_loc).click()#点击追2期
        except NoSuchElementException:
            print("追2期按钮缺失")
            raise
    ####点击“追5期”
    def chase_ticket_button_five(self):
        try:
            self.find_element(*self.chase_ticket_button_five_loc).click()#点击追5期
        except NoSuchElementException:
            print("追5期按钮缺失")
            raise
    ####点击“追10期”
    def chase_ticket_button_ten(self):
        try:
            self.find_element(*self.chase_ticket_button_ten_loc).click()#点击追10期
        except NoSuchElementException:
            print("追10期按钮缺失")
            raise
    ###点击“追20期”
    def chase_ticket_button_twenty(self):
        try:
            self.find_element(*self.chase_ticket_button_twenty_loc).click()  # 点击追20期
        except NoSuchElementException:
            print("追20期按钮缺失")
            raise
    ####点击“追50期”
    def chase_ticket_button_fifty(self):
        try:
            self.find_element(*self.chase_ticket_button_fifty_loc).click()  # 点击追50期
        except NoSuchElementException:
            print("追50期按钮缺失")
            raise
    ###输入追XX期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    ####输入增加投注倍数
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    ###获取投注注数文本
    def lottery_number_text(self):
        self.wait_element_located(self.driver,self.lottery_number_text_loc)
        lottery_number = self.find_element(*self.lottery_number_text_loc).text
        return lottery_number
    ###获取所追期数
    def chase_time_text(self):
        self.wait_element_located(self.driver,self.chase_times_text_loc)
        chase_times = self.find_element(*self.chase_times_text_loc).text
        return chase_times
    #####获取投注倍数
    def throw_time_text(self):
        self.wait_element_located(self.driver, self.throw_times_text_loc)
        throw_times = self.find_element(*self.throw_times_text_loc).text
        return throw_times
    ####双色球点击增加追期数
    def u_chase_ticket_add_button(self):
        try:
            self.find_element(*self.chase_ticket_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
            raise
    ###双色球点击减少追期数
    def u_chase_ticket_sub_button(self):
        try:
            self.find_element(*self.chase_ticket_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
            raise
    ####双色球点击增加投注倍数
    def u_throw_times_button_add(self):
        try:
            self.find_element(*self.u_throw_times_button_add_loc).click()
        except NoSuchElementException:
            print("投注倍数+按钮缺失")
            raise
    ####双色球点击减少投注倍数
    def u_throw_times_button_sub(self):
        try:
            self.find_element(*self.u_throw_times_button_sub_loc).click()
        except NoSuchElementException:
            print("投注倍数-按钮缺失")
            raise
    ######点击“提交订单给站主”按钮
    def submit_order_to_station_owner_button(self):
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)#显示等待提交按钮出现，进行点击操作
        self.find_element(*self.submit_order_to_station_owner_button_loc).click()
    ###订单金额超过100000元的时候，弹出提示信息
    def out_max_pay(self):
        self.wait_element_located(self.driver,self.toast_loc)#显示等待，等待提示信息出现再进行获取文本操作
        out_max_pay_text=self.find_element(*self.toast_loc).text
        sleep(2)
        print(out_max_pay_text)
        return out_max_pay_text
    # #所投期停止销售时，弹出提示信息“该期已截止销售”
    # def stop_sale_toast(self):
    #     try:
    #         stop_sale_text = self.find_element(*self.toast_loc).text
    #         print(stop_sale_text)
    #         self.find_element(self.)
    #     except NoSuchElementException:
    #         print("该期在售")
    #####点击“确认并支付”按钮
    def confirm_and_pay_button(self):
        try:
            self.wait_element_located(self.driver, self.confirm_and_pay_button_loc)
            self.find_element(*self.confirm_and_pay_button_loc).click()###点击确认支付
        except :
            self.find_element(*self.submit_frequently).click()##提示提交频繁，点击知道了

    #点击确认支付页面的x按钮
    def cancel_pay_button(self):
        self.wait_element_located(self.driver, self.cancel_pay_button_loc)
        self.find_element(*self.cancel_pay_button_loc).click()

    def User_agreement(self):
        self.find_element(*self.user_agreement).click()##点击用户协议

    def User_know(self):
        self.find_element(*self.user_know).click()##点击用户协议，我知道了

    def Risk(self):
        self.find_element(*self.risk).click()###点击购彩风险

    def Risk_know(self):
        self.find_element(*self.risk_know).click()##点击购彩风险，我知道了

    def Select_number(self):
        list=[]
        a=self.find_element(*self.select_red).text##读取选择的红球
        b=self.find_element(*self.select_blue).text##读取蓝球
        c=a+' '+b##在2个字符串中间添加空格
        list.append(c)
        print(list)
        return list

    def Del_x(self):
        self.find_element(*self.del_X).click()###点击左侧X按钮
    def lottery_confirm_num_page_text(self):#获取投注确认页文本---mj20171207
        self.wait_element_located(self.driver,self.confirm_num_page_text_loc)
        lottery_text = self.find_element(*self.confirm_num_page_text_loc).text
        return lottery_text

    def n_event_count(self):   ###随机点击1注X按钮
        aa = self.find_elements(*self.event_field_loc)
        i=random.randint(0,len(aa)-1)
        aa[i].click()
        print("删除第%d注"%(i+1))

    def Unionlotto_History_buy(self):
        self.find_element(*self.unionlotto_History_buy).click()##点击历史开奖信息中的最近开奖信息

    def Buy_unionlotto(self):
        self.find_element(*self.buy_unionlotto).click()###点击投注双色球

    def Choose_color(self):
        self.find_element(*self.choose_color).click()##幸运选号，点击选择彩种入口

    def Choose_note(self):
        self.find_element(*self.choose_note).click()##幸运选号，点击选择注数入口

    def Lucky_unionlotto(self,driver):###选择双色球
        driver.click_and_hold(self.find_element(*self.lucky_unionlotto)).move_to_element(self.find_element(*self.lucky_lottery)).release().perform()
        #driver.drag_and_drop(self.find_element(*self.lucky_lottery), self.find_element(*self.lucky_unionlotto)).perform()##实现鼠标拖拽


    def Complete(self):
        self.find_element(*self.complete).click()###点击完成


class ConfirmLottery_lelun(Page_lelun,ConfirmLottery_lelun_loc):
    #################################元素操作######################################
    #获取投注确认页的“提交订单给站主”的文本
    def confirm_num_page_text(self):#---mj20171207修改
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)
        confirm_cathectic = self.find_element(*self.submit_order_to_station_owner_button_loc).text
        return confirm_cathectic
    #点击“继续选号”按钮
    def continue_choose_num_button(self):
        self.find_element(*self.continue_choose_num_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.find_element(*self.Machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.find_element(*self.Machine_choose_five_button_loc).click()
    #点击“重新选号链接”
    def re_selection_num(self):
        self.wait_element_located(self.driver,self.re_selection_num_loc)#重新选号链接可见时，进行点击操作
        self.find_element(*self.re_selection_num_loc).click()
    #点击“清除列表”按钮
    def delete_all_num_button(self):
        self.wait_element_located(self.driver,self.delete_all_num_button_loc)
        self.find_element(*self.delete_all_num_button_loc).click()
    #点击“清除单个选号”
    def delete_one_num_button(self):
        self.wait_element_located(self.driver,self.delete_one_num_button_loc)
        self.find_element(*self.delete_one_num_button_loc).click()

    ##############################mj20171206
    def del_n(self, n):
        self.wait_element_located(self.driver, self.del_n_loc(n))
        self.find_element(*self.del_n_loc(n)).click()  ####点击清除第n个投注
    # 获取投注确认页共有多少笔投注
    def event_count(self):
        aa = self.find_elements(*self.event_field_loc)
        return len(aa)
    ##############################mj20171206############################
    #点击“确定清除所有选号”按钮
    def confirm_delete_button(self):
        self.wait_element_located(self.driver,self.confirm_delete_button_loc)
        self.find_element(*self.confirm_delete_button_loc).click()
    #点击“取消清除所有选号”按钮
    def cancel_delete_button(self):
        self.wait_element_located(self.driver,self.cancel_delete_button_loc)
        self.find_element(*self.cancel_delete_button_loc).click()
    ##点击“追xx期”
    def chase_ticket_button(self):
        try:
            self.find_element(*self.chase_ticket_button_loc).click()  # 点击追XX期
        except NoSuchElementException:
            print("追xx期按钮缺失")
            raise
    ##点击中奖停追
    def stop_chase_win_radio(self):
        try:
            self.find_element(*self.stop_chase_win_radio_loc).click()  # 点击中奖停追单选按钮
        except NoSuchElementException:
            print("中奖停追按钮缺失")
            raise
    ######点击“追两期”按钮
    def chase_ticket_button_two(self):
        try:
            self.find_element(*self.chase_ticket_button_two_loc).click()#点击追2期
        except NoSuchElementException:
            print("追2期按钮缺失")
            raise
    ####点击“追5期”
    def chase_ticket_button_five(self):
        try:
            self.find_element(*self.chase_ticket_button_five_loc).click()#点击追5期
        except NoSuchElementException:
            print("追5期按钮缺失")
            raise
    ####点击“追10期”
    def chase_ticket_button_ten(self):
        try:
            self.find_element(*self.chase_ticket_button_ten_loc).click()#点击追10期
        except NoSuchElementException:
            print("追10期按钮缺失")
            raise
    ###点击“追20期”
    def chase_ticket_button_twenty(self):
        try:
            self.find_element(*self.chase_ticket_button_twenty_loc).click()  # 点击追20期
        except NoSuchElementException:
            print("追20期按钮缺失")
            raise
    ####点击“追50期”
    def chase_ticket_button_fifty(self):
        try:
            self.find_element(*self.chase_ticket_button_fifty_loc).click()  # 点击追50期
        except NoSuchElementException:
            print("追50期按钮缺失")
            raise
    ###输入追XX期
    def chase_ticket_input(self,num):
        self.wait_element_located(self.driver,self.chase_ticket_button_loc)
        self.find_element(*self.chase_ticket_button_loc).clear()
        self.find_element(*self.chase_ticket_button_loc).send_keys(num)
    ####输入增加投注倍数
    def throw_times_input(self,num):
        self.wait_element_located(self.driver,self.throw_times_input_loc)
        self.find_element(*self.throw_times_input_loc).clear()
        self.find_element(*self.throw_times_input_loc).send_keys(num)
    ###获取投注注数文本
    def lottery_number_text(self):
        self.wait_element_located(self.driver,self.lottery_number_text_loc)
        lottery_number = self.find_element(*self.lottery_number_text_loc).text
        return lottery_number
    ###获取所追期数
    def chase_time_text(self):
        self.wait_element_located(self.driver,self.chase_times_text_loc)
        chase_times = self.find_element(*self.chase_times_text_loc).text
        return chase_times
    #####获取投注倍数
    def throw_time_text(self):
        self.wait_element_located(self.driver, self.throw_times_text_loc)
        throw_times = self.find_element(*self.throw_times_text_loc).text
        return throw_times
    ####双色球点击增加追期数
    def u_chase_ticket_add_button(self):
        try:
            self.find_element(*self.chase_ticket_add_button_loc).click()
        except NoSuchElementException:
            print("追期+按钮缺失")
            raise
    ###双色球点击减少追期数
    def u_chase_ticket_sub_button(self):
        try:
            self.find_element(*self.chase_ticket_sub_button_loc).click()
        except NoSuchElementException:
            print("追期-按钮缺失")
            raise
    ####双色球点击增加投注倍数
    def u_throw_times_button_add(self):
        try:
            self.find_element(*self.u_throw_times_button_add_loc).click()
        except NoSuchElementException:
            print("投注倍数+按钮缺失")
            raise
    ####双色球点击减少投注倍数
    def u_throw_times_button_sub(self):
        try:
            self.find_element(*self.u_throw_times_button_sub_loc).click()
        except NoSuchElementException:
            print("投注倍数-按钮缺失")
            raise
    ######点击“提交订单给站主”按钮
    def submit_order_to_station_owner_button(self):
        self.wait_element_located(self.driver,self.submit_order_to_station_owner_button_loc)#显示等待提交按钮出现，进行点击操作
        self.find_element(*self.submit_order_to_station_owner_button_loc).click()
    ###订单金额超过100000元的时候，弹出提示信息
    def out_max_pay(self):
        self.wait_element_located(self.driver,self.toast_loc)#显示等待，等待提示信息出现再进行获取文本操作
        out_max_pay_text=self.find_element(*self.toast_loc).text
        sleep(2)
        print(out_max_pay_text)
        return out_max_pay_text
    # #所投期停止销售时，弹出提示信息“该期已截止销售”
    # def stop_sale_toast(self):
    #     try:
    #         stop_sale_text = self.find_element(*self.toast_loc).text
    #         print(stop_sale_text)
    #         self.find_element(self.)
    #     except NoSuchElementException:
    #         print("该期在售")
    #####点击“确认并支付”按钮
    def confirm_and_pay_button(self):
        try:
            self.wait_element_located(self.driver, self.confirm_and_pay_button_loc)
            self.find_element(*self.confirm_and_pay_button_loc).click()###点击确认支付
        except TimeoutException:
            self.find_element(*self.submit_frequently).click()##提示提交频繁，点击知道了
    #点击确认支付页面的x按钮
    def cancel_pay_button(self):
        self.wait_element_located(self.driver, self.cancel_pay_button_loc)
        self.find_element(*self.cancel_pay_button_loc).click()

    def User_agreement(self):
        self.find_element(*self.user_agreement).click()##点击用户协议

    def User_know(self):
        self.find_element(*self.user_know).click()##点击用户协议，我知道了

    def Risk(self):
        self.find_element(*self.risk).click()###点击购彩风险

    def Risk_know(self):
        self.find_element(*self.risk_know).click()##点击购彩风险，我知道了

    def Select_number(self):
        list=[]
        a=self.find_element(*self.select_red).text##读取选择的红球
        b=self.find_element(*self.select_blue).text##读取蓝球
        c=a+' '+b##在2个字符串中间添加空格
        list.append(c)
        print(list)
        return list

    def Del_x(self):
        self.find_element(*self.del_X).click()###点击左侧X按钮
    def lottery_confirm_num_page_text(self):#获取投注确认页文本---mj20171207
        self.wait_element_located(self.driver,self.confirm_num_page_text_loc)
        lottery_text = self.find_element(*self.confirm_num_page_text_loc).text
        return lottery_text

    def n_event_count(self):   ###随机点击1注X按钮
        aa = self.find_elements(*self.event_field_loc)
        i=random.randint(0,len(aa)-1)
        aa[i].click()
        print("删除第%d注"%(i+1))

    def Unionlotto_History_buy(self):
        self.find_element(*self.unionlotto_History_buy).click()##点击历史开奖信息中的最近开奖信息

    def Buy_unionlotto(self):
        self.find_element(*self.buy_unionlotto).click()###点击投注双色球

    def Choose_color(self):
        self.find_element(*self.choose_color).click()##幸运选号，点击选择彩种入口

    def Choose_note(self):
        self.find_element(*self.choose_note).click()##幸运选号，点击选择注数入口

    def Lucky_unionlotto(self,driver):###选择双色球
        driver.click_and_hold(self.find_element(*self.lucky_unionlotto)).move_to_element(self.find_element(*self.lucky_lottery)).release().perform()
        #driver.drag_and_drop(self.find_element(*self.lucky_lottery), self.find_element(*self.lucky_unionlotto)).perform()##实现鼠标拖拽


    def Complete(self):
        self.find_element(*self.complete).click()###点击完成




