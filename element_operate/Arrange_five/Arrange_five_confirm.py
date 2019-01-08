import random
from element_position.lemi import ConfirmLottery_loc,Arrang_five_pick,UChooseNum_loc
from element_operate.base import Page
from element_position.lexiu import ConfirmLottery_lexiu_loc,Arrang_five_pick_lexiu,UChooseNum_lexiu_loc
from element_operate.base import Page_lexiu
from time import sleep
from element_position.leyou import ConfirmLottery_leyou_loc,Arrang_five_pick_leyou,UChooseNum_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import ConfirmLottery_lelun_loc,Arrang_five_pick_lelun,UChooseNum_lelun_loc
from element_operate.base import Page_lelun

class ArrangeFiveConfirmLottery(Page,ConfirmLottery_loc,Arrang_five_pick,UChooseNum_loc):
################################点击继续选号按钮######################################171018
    def Coun_nu(self):
        self.find_element(*self.coun_nu).click()

    ##############点击机选5注###############
    def Pause_five(self):
        self.find_element(*self.coun_five).click()

    ##############点击机选1注###############
    def Pause_one(self):
        self.find_element(*self.coun_one).click()

    #################读取投注的注数#########
    def Test_note_nu(self):
        nu=self.find_element(*self.note).text
        return (nu)

    def Tnote_nu(self):
        nu=self.find_element(*self.note_n).text
        return (nu)

    #############点击选择号码左侧X按钮
    def Del_none(self,n):
        nu = int(self.Test_note_nu())
        for j in range(n):
            for i in random.sample(range(1, nu + 1), 1):
                if i == 10:
                    target = self.find_element(*self.iagree)
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                self.find_element(*self.del_one(i)).click()
                print('删除第%d行数据' % i)
            nu = nu - 1

    ###############点击N注所选号码
    def Note_none(self, n):
        nu = int(self.Test_note_nu())
        for i in random.sample(range(1, nu + 1), n):
            self.find_element(*self.note_one(i)).click()  # 点击i注选择的号码
            self.find_element(*self.clear_number_icon_loc).click()  # 点击清除选号图标
            self.find_element(*self.machine_choose_button_loc).click()  ###点击机选
            self.find_element(*self.machine_choose_five_button_loc).click()  ###点击机选5注

    def Iagree(self):
            self.find_element(*self.iagree).click()#点击我已满18岁

    def Know(self):
        self.find_element(*self.know).click()#点击我知道了

    def Choose_station(self):
        self.find_element(*self.choose_station_loc).click()###点击投注站入口

##########################修改倍数###################################1020（未合）
    def Multiple_less(self):
        self.wait_element_located(self.driver, self.multiple_less)
        self.find_element(*self.multiple_less).click()##########点击倍数 -号

    def Multiple_input(self,n):
        self.wait_element_located(self.driver, self.multiple_input)
        self.find_element(*self.multiple_input).clear()##清空文本内容
        self.find_element(*self.multiple_input).send_keys(n)###输入 n

    def Multiple_add(self):
        self.wait_element_located(self.driver, self.multiple_add)
        self.find_element(*self.multiple_add).click()  ##########点击倍数 +号

    def Test_multiple_show(self):
        #self.wait_element_located(self.driver, self.multiple)
        nu=self.find_element(*self.multiple).text ##########读取倍数
        return nu

    def Tmultiple_show(self):
        #self.wait_element_located(self.driver, self.multiple)
        nu=self.find_element(*self.multiple_n).text ##########读取倍数
        return nu

    def Test_period_show(self):
        self.wait_element_located(self.driver, self.period)
        nu = self.find_element(*self.period).text  ##########读取倍数
        return nu

    def A_period(self):
        self.wait_element_located(self.driver, self.a_period)
        self.find_element(*self.a_period).click()  #########点击期数+

    def L_period(self):
        self.wait_element_located(self.driver,self.l_period)
        self.find_element(*self.l_period).click()######点击期数 -

class ArrangeFiveConfirmLottery_lexiu(Page_lexiu,ConfirmLottery_lexiu_loc,Arrang_five_pick_lexiu,UChooseNum_lexiu_loc):
################################点击继续选号按钮######################################171018
    def Coun_nu(self):
        self.find_element(*self.coun_nu).click()

    ##############点击机选5注###############
    def Pause_five(self):
        self.find_element(*self.coun_five).click()

    ##############点击机选1注###############
    def Pause_one(self):
        self.find_element(*self.coun_one).click()

    #################读取投注的注数#########
    def Test_note_nu(self):
        nu=self.find_element(*self.note).text
        return (nu)

    #############点击选择号码左侧X按钮
    def Del_none(self,n):
        nu = int(self.Test_note_nu())
        for j in range(n):
            for i in random.sample(range(1, nu + 1), 1):
                if i == 10:
                    target = self.find_element(*self.iagree)
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                self.find_element(*self.del_one(i)).click()
                print('删除第%d行数据' % i)
            nu = nu - 1

    ###############点击N注所选号码
    def Note_none(self, n):
        nu = int(self.Test_note_nu())
        for i in random.sample(range(1, nu + 1), n):
            self.find_element(*self.note_one(i)).click()  # 点击i注选择的号码
            self.find_element(*self.clear_number_icon_loc).click()  # 点击清除选号图标
            self.find_element(*self.machine_choose_button_loc).click()  ###点击机选
            self.find_element(*self.machine_choose_five_button_loc).click()  ###点击机选5注

    def Iagree(self):
            self.find_element(*self.iagree).click()#点击我已满18岁

    def Know(self):
        self.find_element(*self.know).click()#点击我知道了

    def Choose_station(self):
        self.find_element(*self.choose_station_loc).click()###点击投注站入口

##########################修改倍数###################################1020（未合）
    def Multiple_less(self):
        self.wait_element_located(self.driver, self.multiple_less)
        self.find_element(*self.multiple_less).click()##########点击倍数 -号

    def Multiple_input(self,n):
        self.wait_element_located(self.driver, self.multiple_input)
        self.find_element(*self.multiple_input).clear()##清空文本内容
        self.find_element(*self.multiple_input).send_keys(n)###输入 n

    def Multiple_add(self):
        self.wait_element_located(self.driver, self.multiple_add)
        self.find_element(*self.multiple_add).click()  ##########点击倍数 +号

    def Test_multiple_show(self):
        #self.wait_element_located(self.driver, self.multiple)
        nu=self.find_element(*self.multiple).text ##########读取倍数
        return nu

    def Test_period_show(self):
        self.wait_element_located(self.driver, self.period)
        nu = self.find_element(*self.period).text  ##########读取倍数
        return nu

    def A_period(self):
        self.wait_element_located(self.driver, self.a_period)
        self.find_element(*self.a_period).click()  #########点击期数+

    def L_period(self):
        self.wait_element_located(self.driver,self.l_period)
        self.find_element(*self.l_period).click()######点击期数 -

class ArrangeFiveConfirmLottery_leyou(Page_leyou,ConfirmLottery_leyou_loc,Arrang_five_pick_leyou,UChooseNum_leyou_loc):
################################点击继续选号按钮######################################171018
    def Coun_nu(self):
        self.find_element(*self.coun_nu).click()

    ##############点击机选5注###############
    def Pause_five(self):
        self.find_element(*self.coun_five).click()

    ##############点击机选1注###############
    def Pause_one(self):
        self.find_element(*self.coun_one).click()

    #################读取投注的注数#########
    def Test_note_nu(self):
        nu=self.find_element(*self.note).text
        return (nu)

    #############点击选择号码左侧X按钮
    def Del_none(self,n):
        nu = int(self.Test_note_nu())
        for j in range(n):
            for i in random.sample(range(1, nu + 1), 1):
                if i == 10:
                    target = self.find_element(*self.iagree)
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                self.find_element(*self.del_one(i)).click()
                print('删除第%d行数据' % i)
            nu = nu - 1

    ###############点击N注所选号码
    def Note_none(self, n):
        nu = int(self.Test_note_nu())
        for i in random.sample(range(1, nu + 1), n):
            self.find_element(*self.note_one(i)).click()  # 点击i注选择的号码
            self.find_element(*self.clear_number_icon_loc).click()  # 点击清除选号图标
            self.find_element(*self.machine_choose_button_loc).click()  ###点击机选
            self.find_element(*self.machine_choose_five_button_loc).click()  ###点击机选5注

    def Iagree(self):
            self.find_element(*self.iagree).click()#点击我已满18岁

    def Know(self):
        self.find_element(*self.know).click()#点击我知道了

    def Choose_station(self):
        self.find_element(*self.choose_station_loc).click()###点击投注站入口

##########################修改倍数###################################1020（未合）
    def Multiple_less(self):
        self.wait_element_located(self.driver, self.multiple_less)
        self.find_element(*self.multiple_less).click()##########点击倍数 -号

    def Multiple_input(self,n):
        self.wait_element_located(self.driver, self.multiple_input)
        self.find_element(*self.multiple_input).clear()##清空文本内容
        self.find_element(*self.multiple_input).send_keys(n)###输入 n

    def Multiple_add(self):
        self.wait_element_located(self.driver, self.multiple_add)
        self.find_element(*self.multiple_add).click()  ##########点击倍数 +号

    def Test_multiple_show(self):
        #self.wait_element_located(self.driver, self.multiple)
        nu=self.find_element(*self.multiple).text ##########读取倍数
        return nu

    def Test_period_show(self):
        self.wait_element_located(self.driver, self.period)
        nu = self.find_element(*self.period).text  ##########读取倍数
        return nu

    def A_period(self):
        self.wait_element_located(self.driver, self.a_period)
        self.find_element(*self.a_period).click()  #########点击期数+

    def L_period(self):
        self.wait_element_located(self.driver,self.l_period)
        self.find_element(*self.l_period).click()######点击期数 -

class ArrangeFiveConfirmLottery_lelun(Page_lelun,ConfirmLottery_lelun_loc,Arrang_five_pick_lelun,UChooseNum_lelun_loc):
################################点击继续选号按钮######################################171018
    def Coun_nu(self):
        self.find_element(*self.coun_nu).click()

    ##############点击机选5注###############
    def Pause_five(self):
        self.find_element(*self.coun_five).click()

    ##############点击机选1注###############
    def Pause_one(self):
        self.find_element(*self.coun_one).click()

    #################读取投注的注数#########
    def Test_note_nu(self):
        nu=self.find_element(*self.note).text
        return (nu)

    #############点击选择号码左侧X按钮
    def Del_none(self,n):
        nu = int(self.Test_note_nu())
        for j in range(n):
            for i in random.sample(range(1, nu + 1), 1):
                if i == 10:
                    target = self.find_element(*self.iagree)
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                self.find_element(*self.del_one(i)).click()
                print('删除第%d行数据' % i)
            nu = nu - 1

    ###############点击N注所选号码
    def Note_none(self, n):
        nu = int(self.Test_note_nu())
        for i in random.sample(range(1, nu + 1), n):
            self.find_element(*self.note_one(i)).click()  # 点击i注选择的号码
            self.find_element(*self.clear_number_icon_loc).click()  # 点击清除选号图标
            self.find_element(*self.machine_choose_button_loc).click()  ###点击机选
            self.find_element(*self.machine_choose_five_button_loc).click()  ###点击机选5注

    def Iagree(self):
            self.find_element(*self.iagree).click()#点击我已满18岁

    def Know(self):
        self.find_element(*self.know).click()#点击我知道了

    def Choose_station(self):
        self.find_element(*self.choose_station_loc).click()###点击投注站入口

##########################修改倍数###################################1020（未合）
    def Multiple_less(self):
        self.wait_element_located(self.driver, self.multiple_less)
        self.find_element(*self.multiple_less).click()##########点击倍数 -号

    def Multiple_input(self,n):
        self.wait_element_located(self.driver, self.multiple_input)
        self.find_element(*self.multiple_input).clear()##清空文本内容
        self.find_element(*self.multiple_input).send_keys(n)###输入 n

    def Multiple_add(self):
        self.wait_element_located(self.driver, self.multiple_add)
        self.find_element(*self.multiple_add).click()  ##########点击倍数 +号

    def Test_multiple_show(self):
        #self.wait_element_located(self.driver, self.multiple)
        nu=self.find_element(*self.multiple).text ##########读取倍数
        return nu

    def Test_period_show(self):
        self.wait_element_located(self.driver, self.period)
        nu = self.find_element(*self.period).text  ##########读取倍数
        return nu

    def A_period(self):
        self.wait_element_located(self.driver, self.a_period)
        self.find_element(*self.a_period).click()  #########点击期数+

    def L_period(self):
        self.wait_element_located(self.driver,self.l_period)
        self.find_element(*self.l_period).click()######点击期数 -