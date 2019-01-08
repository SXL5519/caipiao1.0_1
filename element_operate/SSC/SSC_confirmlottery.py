from element_position.lemi import CQSSC_ConfirmLottery_loc
from element_operate.base import Page
from selenium.webdriver.common.by import By
from time import sleep
from element_position.lexiu import CQSSC_ConfirmLottery_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import CQSSC_ConfirmLottery_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import CQSSC_ConfirmLottery_lelun_loc
from element_operate.base import Page_lelun
###重庆时时彩投注确认页元素操作-----mj20171206
class CQSSCConfirmLottery(Page,CQSSC_ConfirmLottery_loc):

    def intelligently_chase_button(self):#点击智能追号按钮
        self.wait_element_located(self.driver,self.intelligently_chase_button_loc)
        self.find_element(*self.intelligently_chase_button_loc).click()
    def znzh_issue_num_input(self,n):#输入智能追号的期数
        self.wait_element_located(self.driver,self.znzh_issue_num_loc)
        self.find_element(*self.znzh_issue_num_loc).clear()
        self.find_element(*self.znzh_issue_num_loc).send_keys(n)
        return n
    def totalIssue(self):#点击总追号期数，更新修改
        self.find_element(*self.totalIssue_loc).click()
    def totalIssue_text(self):#获取总追号期数文本
        text = self.find_element(*self.totalIssue_loc).text
        return text
    def totalIssue_num(self):#获取总追号期数的数字
        total_num =self.totalIssue_text()[1:3]
        num = int(total_num)
        return num

    def submit_button(self):#点击智能追号页提交按钮
        self.wait_element_located(self.driver,self.submit_button_loc)
        self.find_element(*self.submit_button_loc).click()
    def revise_button(self):#点击智能追号页修改方案按钮
        self.find_element(*self.revise_button_loc).click()
    def revise_chase_add(self):#点击智能追号修改方案页面的连续追+按钮
        self.find_element(*self.revise_chase_add_loc).click()
    def revise_chase_sub(self):#点击智能追号修改方案页面的连续追-按钮
        self.find_element(*self.revise_chase_sub_loc).click()
    def revise_chase_input(self,n):#智能追号页输入连续追号期数
        self.find_element(*self.revise_chase_input_loc).clear()
        self.find_element(*self.revise_chase_input_loc).send_keys(n)
    def revise_times_add(self):#点击智能追号修改方案页的起始倍数的+按钮
        self.find_element(*self.revise_times_add_loc).click()
    def revise_times_sub(self):#点击智能追号修改方案页的起始倍数的-按钮
        self.find_element(*self.revise_times_sub_loc).click()
    def revise_times_input(self,n):#智能追号页输入起始倍数
        self.find_element(*self.revise_times_input_loc).clear()
        self.find_element(*self.revise_times_input_loc).send_keys(n)
    def revise_confirm(self):#点击智能追号页确认按钮
        self.find_element(*self.revise_confirm_loc).click()
        sleep(2)#等待更新方案
    def revise_cancel(self):#点击智能选号页的取消按钮
        self.find_element(*self.revise_cancel_loc).click()

class CQSSCConfirmLottery_lexiu(Page_lexiu,CQSSC_ConfirmLottery_lexiu_loc):

    def intelligently_chase_button(self):#点击智能追号按钮
        self.wait_element_located(self.driver,self.intelligently_chase_button_loc)
        self.find_element(*self.intelligently_chase_button_loc).click()
    def znzh_issue_num_input(self,n):#输入智能追号的期数
        self.wait_element_located(self.driver,self.znzh_issue_num_loc)
        self.find_element(*self.znzh_issue_num_loc).clear()
        self.find_element(*self.znzh_issue_num_loc).send_keys(n)
        return n
    def totalIssue(self):#点击总追号期数，更新修改
        self.find_element(*self.totalIssue_loc).click()
    def totalIssue_text(self):#获取总追号期数文本
        text = self.find_element(*self.totalIssue_loc).text
        return text
    def totalIssue_num(self):#获取总追号期数的数字
        total_num =self.totalIssue_text()[1:3]
        num = int(total_num)
        return num

    def submit_button(self):#点击智能追号页提交按钮
        self.wait_element_located(self.driver,self.submit_button_loc)
        self.find_element(*self.submit_button_loc).click()
    def revise_button(self):#点击智能追号页修改方案按钮
        self.find_element(*self.revise_button_loc).click()
    def revise_chase_add(self):#点击智能追号修改方案页面的连续追+按钮
        self.find_element(*self.revise_chase_add_loc).click()
    def revise_chase_sub(self):#点击智能追号修改方案页面的连续追-按钮
        self.find_element(*self.revise_chase_sub_loc).click()
    def revise_chase_input(self,n):#智能追号页输入连续追号期数
        self.find_element(*self.revise_chase_input_loc).clear()
        self.find_element(*self.revise_chase_input_loc).send_keys(n)
    def revise_times_add(self):#点击智能追号修改方案页的起始倍数的+按钮
        self.find_element(*self.revise_times_add_loc).click()
    def revise_times_sub(self):#点击智能追号修改方案页的起始倍数的-按钮
        self.find_element(*self.revise_times_sub_loc).click()
    def revise_times_input(self,n):#智能追号页输入起始倍数
        self.find_element(*self.revise_times_input_loc).clear()
        self.find_element(*self.revise_times_input_loc).send_keys(n)
    def revise_confirm(self):#点击智能追号页确认按钮
        self.find_element(*self.revise_confirm_loc).click()
        sleep(2)#等待更新方案
    def revise_cancel(self):#点击智能选号页的取消按钮
        self.find_element(*self.revise_cancel_loc).click()

class CQSSCConfirmLottery_leyou(Page_leyou,CQSSC_ConfirmLottery_leyou_loc):

    def intelligently_chase_button(self):#点击智能追号按钮
        self.wait_element_located(self.driver,self.intelligently_chase_button_loc)
        self.find_element(*self.intelligently_chase_button_loc).click()
    def znzh_issue_num_input(self,n):#输入智能追号的期数
        self.wait_element_located(self.driver,self.znzh_issue_num_loc)
        self.find_element(*self.znzh_issue_num_loc).clear()
        self.find_element(*self.znzh_issue_num_loc).send_keys(n)
        return n
    def totalIssue(self):#点击总追号期数，更新修改
        self.find_element(*self.totalIssue_loc).click()
    def totalIssue_text(self):#获取总追号期数文本
        text = self.find_element(*self.totalIssue_loc).text
        return text
    def totalIssue_num(self):#获取总追号期数的数字
        total_num =self.totalIssue_text()[1:3]
        num = int(total_num)
        return num

    def submit_button(self):#点击智能追号页提交按钮
        self.wait_element_located(self.driver,self.submit_button_loc)
        self.find_element(*self.submit_button_loc).click()
    def revise_button(self):#点击智能追号页修改方案按钮
        self.find_element(*self.revise_button_loc).click()
    def revise_chase_add(self):#点击智能追号修改方案页面的连续追+按钮
        self.find_element(*self.revise_chase_add_loc).click()
    def revise_chase_sub(self):#点击智能追号修改方案页面的连续追-按钮
        self.find_element(*self.revise_chase_sub_loc).click()
    def revise_chase_input(self,n):#智能追号页输入连续追号期数
        self.find_element(*self.revise_chase_input_loc).clear()
        self.find_element(*self.revise_chase_input_loc).send_keys(n)
    def revise_times_add(self):#点击智能追号修改方案页的起始倍数的+按钮
        self.find_element(*self.revise_times_add_loc).click()
    def revise_times_sub(self):#点击智能追号修改方案页的起始倍数的-按钮
        self.find_element(*self.revise_times_sub_loc).click()
    def revise_times_input(self,n):#智能追号页输入起始倍数
        self.find_element(*self.revise_times_input_loc).clear()
        self.find_element(*self.revise_times_input_loc).send_keys(n)
    def revise_confirm(self):#点击智能追号页确认按钮
        self.find_element(*self.revise_confirm_loc).click()
        sleep(2)#等待更新方案
    def revise_cancel(self):#点击智能选号页的取消按钮
        self.find_element(*self.revise_cancel_loc).click()

class CQSSCConfirmLottery_lelun(Page_lelun,CQSSC_ConfirmLottery_lelun_loc):

    def intelligently_chase_button(self):#点击智能追号按钮
        self.wait_element_located(self.driver,self.intelligently_chase_button_loc)
        self.find_element(*self.intelligently_chase_button_loc).click()
    def znzh_issue_num_input(self,n):#输入智能追号的期数
        self.wait_element_located(self.driver,self.znzh_issue_num_loc)
        self.find_element(*self.znzh_issue_num_loc).clear()
        self.find_element(*self.znzh_issue_num_loc).send_keys(n)
        return n
    def totalIssue(self):#点击总追号期数，更新修改
        self.find_element(*self.totalIssue_loc).click()
    def totalIssue_text(self):#获取总追号期数文本
        text = self.find_element(*self.totalIssue_loc).text
        return text
    def totalIssue_num(self):#获取总追号期数的数字
        total_num =self.totalIssue_text()[1:3]
        num = int(total_num)
        return num

    def submit_button(self):#点击智能追号页提交按钮
        self.wait_element_located(self.driver,self.submit_button_loc)
        self.find_element(*self.submit_button_loc).click()
    def revise_button(self):#点击智能追号页修改方案按钮
        self.find_element(*self.revise_button_loc).click()
    def revise_chase_add(self):#点击智能追号修改方案页面的连续追+按钮
        self.find_element(*self.revise_chase_add_loc).click()
    def revise_chase_sub(self):#点击智能追号修改方案页面的连续追-按钮
        self.find_element(*self.revise_chase_sub_loc).click()
    def revise_chase_input(self,n):#智能追号页输入连续追号期数
        self.find_element(*self.revise_chase_input_loc).clear()
        self.find_element(*self.revise_chase_input_loc).send_keys(n)
    def revise_times_add(self):#点击智能追号修改方案页的起始倍数的+按钮
        self.find_element(*self.revise_times_add_loc).click()
    def revise_times_sub(self):#点击智能追号修改方案页的起始倍数的-按钮
        self.find_element(*self.revise_times_sub_loc).click()
    def revise_times_input(self,n):#智能追号页输入起始倍数
        self.find_element(*self.revise_times_input_loc).clear()
        self.find_element(*self.revise_times_input_loc).send_keys(n)
    def revise_confirm(self):#点击智能追号页确认按钮
        self.find_element(*self.revise_confirm_loc).click()
        sleep(2)#等待更新方案
    def revise_cancel(self):#点击智能选号页的取消按钮
        self.find_element(*self.revise_cancel_loc).click()




