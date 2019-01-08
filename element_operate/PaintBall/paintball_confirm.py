from element_operate.base import Page
from element_position.lemi import PaintBallConfirm_loc
from selenium.webdriver.common.by import By
from time import sleep
import random
from element_operate.base import Page_lexiu
from element_position.lexiu import PaintBallConfirm_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import PaintBallConfirm_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import PaintBallConfirm_lelun_loc
class PaintBallConfirm(Page,PaintBallConfirm_loc):
    def Add_event(self):
        self.wait_element_located(self.driver,self.add_event)
        self.find_element(*self.add_event).click()#####点击编辑/添加赛事按钮

    def Add_event_rqspf(self):
        self.wait_element_located(self.driver,self.add_event2)
        self.find_element(*self.add_event2).click()#####点击编辑/添加赛事按钮

    def N_del(self,n):
        self.wait_element_located(self.driver,self.n_del(n))
        self.find_element(*self.n_del(n)).click()####点击清除第n场赛事

    def Del_n(self,n):
        self.wait_element_located(self.driver, self.del_n(n))
        self.find_element(*self.del_n(n)).click()  ####点击清除第n场赛事

    def DXF_del_n(self,n):
        self.wait_element_located(self.driver,self.Dxf_del_n(n))
        self.find_element(*self.Dxf_del_n(n)).click()

    def Pf_del_icon(self):
        #target = self.find_element(*self.iagree)  ####定位我满18岁了
        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.pf_del_icon).click()  ####点击删除全部选号按钮

    def Btn_less(self):
        self.wait_element_located(self.driver,self.btn_less)
        self.find_element(*self.btn_less).click()####点击倍数 -

    def Btn_add(self):
        self.find_element(*self.btn_add).click()####点击倍数 +

    def Times_input(self,n):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).clear()
        self.find_element(*self.times_input).send_keys(n)####倍数输入框输入n

    def Times_input_click(self):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).click()###点击倍数输入框

    def Pf_bouns(self):
        self.find_element(*self.pf_bonus).click()####点击奖金优化
    def optimize_award(self):
        optimize_text=self.find_element(*self.optimize_award_page_text_loc).text
        print(optimize_text)
        return optimize_text
    def Pf_pass(self):
        self.wait_element_located(self.driver,self.pf_pass)
        self.find_element(*self.pf_pass).click()###点击过关方式
    #---------------------------------------------------mj20171109
    def throw_times_text(self):
        throw_times_text=self.find_element(*self.times_input).text
        print(throw_times_text)
        return throw_times_text
    def throw_times(self,times):
        self.wait_element_located(self.driver,self.throw_times_loc(times))
        self.find_element(*self.throw_times_loc(times)).click()##点击选择投注倍数

    def Pf_pass_nu(self):
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print(nn)
        for i in range(len(nn)):
            if i == len(nn) - 1:
                nn[i].click()
            else:
                nn[i].click()
                nn[i].click()
        j = random.randint(0, len(nn) - 1)
        b = nn[j].text
        print(b)
        nn[j].click()  ##点击J对应的过关方式
        self.Pf_pass()  ###点击收起
        return b

    def Pf_pass_text(self):
        nn = self.find_element(*self.pf_pass).text  ###读取显示的过关方式
        print(nn)
        return nn

    def Times_number(self,n):
        self.find_element(*self.times_number(n)).click()###点击N倍

    def Times_display(self):
        aa=self.find_element(*self.times_display).text###获取确认页面倍数显示文本
        return aa

    def NN(self):
        aa=self.find_elements(*self.nn)
        return len(aa)

    def C_nn(self):
        aa = self.find_elements(*self.nn)
        aa[0].click()

    def A_nn(self):
        a=self.find_elements(*self.a_nn)
        return  len(a)

    def Dxf_nn(self):
        a=self.find_elements(*self.dxf_nn)
        return len(a)

    iagree = (By.ID, 'iagree')

    def down_bf(self):
        # js = "var q=document.body.scrollTop=100000"
        # self.driver.execute_script(js)  ###鼠标拉到顶部
        ##js = "window.scroll(0,1000000)"
        # self.driver.execute_script(js)
        target = self.find_element(*self.iagree)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def submit_order(self):#点击奖金优化页面的【提交订单给站主】--mj20171214
        self.wait_element_located(self.driver,self.submit_order_loc)
        self.find_element(*self.submit_order_loc).click()
    def optimize_add_money_input(self,n):##修改奖金优化金额
        self.wait_element_located(self.driver,self.optimize_add_money_input_loc)
        self.find_element(*self.optimize_add_money_input_loc).clear()
        self.find_element(*self.optimize_add_money_input_loc).send_keys(n)
    def maximum_text(self):#获取理论最大收益，文本
        self.wait_element_located(self.driver,self.maximum_text_loc)
        text = self.find_element(*self.maximum_text_loc).text
        return text
    def restroe_button(self):#点击还原选项按钮
        self.find_element(*self.restroe_button_loc).click()
    def choose_all_pass_nu(self):#选中所有的过关方式
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print('过关方式列表%s'%nn)
        for i in range(0,len(nn)-1):
                nn[i].click()
        self.Pf_pass()  ###点击收起

class PaintBallConfirm_lexiu(Page_lexiu,PaintBallConfirm_lexiu_loc):
    def Add_event(self):
        self.wait_element_located(self.driver,self.add_event)
        self.find_element(*self.add_event).click()#####点击编辑/添加赛事按钮

    def Add_event_rqspf(self):
        self.wait_element_located(self.driver,self.add_event2)
        self.find_element(*self.add_event2).click()#####点击编辑/添加赛事按钮

    def N_del(self,n):
        self.wait_element_located(self.driver,self.n_del(n))
        self.find_element(*self.n_del(n)).click()####点击清除第n场赛事

    def Del_n(self,n):
        self.wait_element_located(self.driver, self.del_n(n))
        self.find_element(*self.del_n(n)).click()  ####点击清除第n场赛事

    def DXF_del_n(self, n):
        self.wait_element_located(self.driver, self.Dxf_del_n(n))
        self.find_element(*self.Dxf_del_n(n)).click()

    def Pf_del_icon(self):
        target = self.find_element(*self.iagree)  ####定位我满18岁了
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.pf_del_icon).click()  ####点击删除全部选号按钮

    def Btn_less(self):
        self.wait_element_located(self.driver,self.btn_less)
        self.find_element(*self.btn_less).click()####点击倍数 -

    def Btn_add(self):
        self.find_element(*self.btn_add).click()####点击倍数 +

    def Times_input(self,n):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).clear()
        self.find_element(*self.times_input).send_keys(n)####倍数输入框输入n

    def Times_input_click(self):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).click()###点击倍数输入框

    def Pf_bouns(self):
        self.find_element(*self.pf_bonus).click()####点击奖金优化
    def optimize_award(self):
        optimize_text=self.find_element(*self.optimize_award_page_text_loc).text
        print(optimize_text)
        return optimize_text
    def Pf_pass(self):
        self.wait_element_located(self.driver,self.pf_pass)
        self.find_element(*self.pf_pass).click()###点击过关方式
    #---------------------------------------------------mj20171109
    def throw_times_text(self):
        throw_times_text=self.find_element(*self.times_input).text
        print(throw_times_text)
        return throw_times_text
    def throw_times(self,times):
        self.wait_element_located(self.driver,self.throw_times_loc(times))
        self.find_element(*self.throw_times_loc(times)).click()##点击选择投注倍数

    def Pf_pass_nu(self):
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print(nn)
        for i in range(len(nn)):
            if i == len(nn) - 1:
                nn[i].click()
            else:
                nn[i].click()
                nn[i].click()
        j = random.randint(0, len(nn) - 1)
        b = nn[j].text
        print(b)
        nn[j].click()  ##点击J对应的过关方式
        self.Pf_pass()  ###点击收起
        return b

    def Pf_pass_text(self):
        nn = self.find_element(*self.pf_pass).text  ###读取显示的过关方式
        print(nn)
        return nn

    def Times_number(self,n):
        self.find_element(*self.times_number(n)).click()###点击N倍

    def Times_display(self):
        aa=self.find_element(*self.times_display).text###获取确认页面倍数显示文本
        return aa

    def NN(self):
        aa=self.find_elements(*self.nn)
        return len(aa)

    def C_nn(self):
        aa = self.find_elements(*self.nn)
        aa[0].click()

    def A_nn(self):
        a=self.find_elements(*self.a_nn)
        return  len(a)

    def Dxf_nn(self):
        a=self.find_elements(*self.dxf_nn)
        return len(a)

    iagree = (By.ID, 'iagree')

    def down_bf(self):
        # js = "var q=document.body.scrollTop=100000"
        # self.driver.execute_script(js)  ###鼠标拉到顶部
        ##js = "window.scroll(0,1000000)"
        # self.driver.execute_script(js)
        target = self.find_element(*self.iagree)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def submit_order(self):#点击奖金优化页面的【提交订单给站主】--mj20171214
        self.wait_element_located(self.driver,self.submit_order_loc)
        self.find_element(*self.submit_order_loc).click()
    def optimize_add_money_input(self,n):##修改奖金优化金额
        self.wait_element_located(self.driver,self.optimize_add_money_input_loc)
        self.find_element(*self.optimize_add_money_input_loc).clear()
        self.find_element(*self.optimize_add_money_input_loc).send_keys(n)
    def maximum_text(self):#获取理论最大收益，文本
        self.wait_element_located(self.driver,self.maximum_text_loc)
        text = self.find_element(*self.maximum_text_loc).text
        return text
    def restroe_button(self):#点击还原选项按钮
        self.find_element(*self.restroe_button_loc).click()
    def choose_all_pass_nu(self):#选中所有的过关方式
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print('过关方式列表%s'%nn)
        for i in range(0,len(nn)-1):
                nn[i].click()
        self.Pf_pass()  ###点击收起

class PaintBallConfirm_leyou(Page_leyou,PaintBallConfirm_leyou_loc):
    def Add_event(self):
        self.wait_element_located(self.driver,self.add_event)
        self.find_element(*self.add_event).click()#####点击编辑/添加赛事按钮

    def Add_event_rqspf(self):
        self.wait_element_located(self.driver,self.add_event2)
        self.find_element(*self.add_event2).click()#####点击编辑/添加赛事按钮

    def N_del(self,n):
        self.wait_element_located(self.driver,self.n_del(n))
        self.find_element(*self.n_del(n)).click()####点击清除第n场赛事

    def Del_n(self,n):
        self.wait_element_located(self.driver, self.del_n(n))
        self.find_element(*self.del_n(n)).click()  ####点击清除第n场赛事

    def DXF_del_n(self, n):
        self.wait_element_located(self.driver, self.Dxf_del_n(n))
        self.find_element(*self.Dxf_del_n(n)).click()

    def Pf_del_icon(self):
        target = self.find_element(*self.iagree)  ####定位我满18岁了
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.pf_del_icon).click()  ####点击删除全部选号按钮

    def Btn_less(self):
        self.wait_element_located(self.driver,self.btn_less)
        self.find_element(*self.btn_less).click()####点击倍数 -

    def Btn_add(self):
        self.find_element(*self.btn_add).click()####点击倍数 +

    def Times_input(self,n):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).clear()
        self.find_element(*self.times_input).send_keys(n)####倍数输入框输入n

    def Times_input_click(self):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).click()###点击倍数输入框

    def Pf_bouns(self):
        self.find_element(*self.pf_bonus).click()####点击奖金优化
    def optimize_award(self):
        optimize_text=self.find_element(*self.optimize_award_page_text_loc).text
        print(optimize_text)
        return optimize_text
    def Pf_pass(self):
        self.wait_element_located(self.driver,self.pf_pass)
        self.find_element(*self.pf_pass).click()###点击过关方式
    #---------------------------------------------------mj20171109
    def throw_times_text(self):
        throw_times_text=self.find_element(*self.times_input).text
        print(throw_times_text)
        return throw_times_text
    def throw_times(self,times):
        self.wait_element_located(self.driver,self.throw_times_loc(times))
        self.find_element(*self.throw_times_loc(times)).click()##点击选择投注倍数

    def Pf_pass_nu(self):
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print(nn)
        for i in range(len(nn)):
            if i == len(nn) - 1:
                nn[i].click()
            else:
                nn[i].click()
                nn[i].click()
        j = random.randint(0, len(nn) - 1)
        b = nn[j].text
        print(b)
        nn[j].click()  ##点击J对应的过关方式
        self.Pf_pass()  ###点击收起
        return b

    def Pf_pass_text(self):
        nn = self.find_element(*self.pf_pass).text  ###读取显示的过关方式
        print(nn)
        return nn

    def Times_number(self,n):
        self.find_element(*self.times_number(n)).click()###点击N倍

    def Times_display(self):
        aa=self.find_element(*self.times_display).text###获取确认页面倍数显示文本
        return aa

    def NN(self):
        aa=self.find_elements(*self.nn)
        return len(aa)

    def C_nn(self):
        aa = self.find_elements(*self.nn)
        aa[0].click()

    def A_nn(self):
        a=self.find_elements(*self.a_nn)
        return  len(a)

    def Dxf_nn(self):
        a=self.find_elements(*self.dxf_nn)
        return len(a)

    def BF_nn(self):
        a=self.find_elements(*self.Bf_nn)
        return len(a)

    iagree = (By.ID, 'iagree')

    def down_bf(self):
        # js = "var q=document.body.scrollTop=100000"
        # self.driver.execute_script(js)  ###鼠标拉到顶部
        ##js = "window.scroll(0,1000000)"
        # self.driver.execute_script(js)
        target = self.find_element(*self.iagree)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def submit_order(self):#点击奖金优化页面的【提交订单给站主】--mj20171214
        self.wait_element_located(self.driver,self.submit_order_loc)
        self.find_element(*self.submit_order_loc).click()
    def optimize_add_money_input(self,n):##修改奖金优化金额
        self.wait_element_located(self.driver,self.optimize_add_money_input_loc)
        self.find_element(*self.optimize_add_money_input_loc).clear()
        self.find_element(*self.optimize_add_money_input_loc).send_keys(n)
    def maximum_text(self):#获取理论最大收益，文本
        self.wait_element_located(self.driver,self.maximum_text_loc)
        text = self.find_element(*self.maximum_text_loc).text
        return text
    def restroe_button(self):#点击还原选项按钮
        self.find_element(*self.restroe_button_loc).click()
    def choose_all_pass_nu(self):#选中所有的过关方式
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print('过关方式列表%s'%nn)
        for i in range(0,len(nn)-1):
                nn[i].click()
        self.Pf_pass()  ###点击收起

class PaintBallConfirm_lelun(Page_lelun,PaintBallConfirm_lelun_loc):
    def Add_event(self):
        self.wait_element_located(self.driver,self.add_event)
        self.find_element(*self.add_event).click()#####点击编辑/添加赛事按钮

    def Add_event_rqspf(self):
        self.wait_element_located(self.driver,self.add_event2)
        self.find_element(*self.add_event2).click()#####点击编辑/添加赛事按钮

    def N_del(self,n):
        self.wait_element_located(self.driver,self.n_del(n))
        self.find_element(*self.n_del(n)).click()####点击清除第n场赛事

    def Del_n(self,n):
        self.wait_element_located(self.driver, self.del_n(n))
        self.find_element(*self.del_n(n)).click()  ####点击清除第n场赛事

    def DXF_del_n(self, n):
        self.wait_element_located(self.driver, self.Dxf_del_n(n))
        self.find_element(*self.Dxf_del_n(n)).click()

    def Pf_del_icon(self):
        #target = self.find_element(*self.iagree)  ####定位我满18岁了
        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.pf_del_icon).click()  ####点击删除全部选号按钮

    def Btn_less(self):
        self.wait_element_located(self.driver,self.btn_less)
        self.find_element(*self.btn_less).click()####点击倍数 -

    def Btn_add(self):
        self.find_element(*self.btn_add).click()####点击倍数 +

    def Times_input(self,n):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).clear()
        self.find_element(*self.times_input).send_keys(n)####倍数输入框输入n

    def Times_input_click(self):
        self.wait_element_located(self.driver,self.times_input)
        self.find_element(*self.times_input).click()###点击倍数输入框

    def Pf_bouns(self):
        self.find_element(*self.pf_bonus).click()####点击奖金优化
    def optimize_award(self):
        optimize_text=self.find_element(*self.optimize_award_page_text_loc).text
        print(optimize_text)
        return optimize_text
    def Pf_pass(self):
        self.wait_element_located(self.driver,self.pf_pass)
        self.find_element(*self.pf_pass).click()###点击过关方式
    #---------------------------------------------------mj20171109
    def throw_times_text(self):
        throw_times_text=self.find_element(*self.times_input).text
        print(throw_times_text)
        return throw_times_text
    def throw_times(self,times):
        self.wait_element_located(self.driver,self.throw_times_loc(times))
        self.find_element(*self.throw_times_loc(times)).click()##点击选择投注倍数

    def Pf_pass_nu(self):
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print(nn)
        for i in range(len(nn)):
            if i == len(nn) - 1:
                nn[i].click()
            else:
                nn[i].click()
                nn[i].click()
        j = random.randint(0, len(nn) - 1)
        b = nn[j].text
        print(b)
        nn[j].click()  ##点击J对应的过关方式
        self.Pf_pass()  ###点击收起
        return b

    def Pf_pass_text(self):
        nn = self.find_element(*self.pf_pass).text  ###读取显示的过关方式
        print(nn)
        return nn

    def Times_number(self,n):
        self.find_element(*self.times_number(n)).click()###点击N倍

    def Times_display(self):
        aa=self.find_element(*self.times_display).text###获取确认页面倍数显示文本
        return aa

    def NN(self):
        aa=self.find_elements(*self.nn)
        return len(aa)

    def C_nn(self):
        aa = self.find_elements(*self.nn)
        aa[0].click()

    def A_nn(self):
        a=self.find_elements(*self.a_nn)
        return  len(a)

    def Dxf_nn(self):
        a=self.find_elements(*self.dxf_nn)
        return len(a)

    iagree = (By.ID, 'iagree')

    def down_bf(self):
        # js = "var q=document.body.scrollTop=100000"
        # self.driver.execute_script(js)  ###鼠标拉到顶部
        ##js = "window.scroll(0,1000000)"
        # self.driver.execute_script(js)
        target = self.find_element(*self.iagree)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def submit_order(self):#点击奖金优化页面的【提交订单给站主】--mj20171214
        self.wait_element_located(self.driver,self.submit_order_loc)
        self.find_element(*self.submit_order_loc).click()
    def optimize_add_money_input(self,n):##修改奖金优化金额
        self.wait_element_located(self.driver,self.optimize_add_money_input_loc)
        self.find_element(*self.optimize_add_money_input_loc).clear()
        self.find_element(*self.optimize_add_money_input_loc).send_keys(n)
    def maximum_text(self):#获取理论最大收益，文本
        self.wait_element_located(self.driver,self.maximum_text_loc)
        text = self.find_element(*self.maximum_text_loc).text
        return text
    def restroe_button(self):#点击还原选项按钮
        self.find_element(*self.restroe_button_loc).click()
    def choose_all_pass_nu(self):#选中所有的过关方式
        nn = self.find_elements(*self.pf_pass_nu())  ##过关方式列表
        print('过关方式列表%s'%nn)
        for i in range(0,len(nn)-1):
                nn[i].click()
        self.Pf_pass()  ###点击收起
