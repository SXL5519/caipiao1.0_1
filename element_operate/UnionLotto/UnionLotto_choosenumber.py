import random
from time import sleep
from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import UChooseNum_loc,LChooseNum_loc
from selenium.common.exceptions import NoSuchElementException
from element_operate.base import Page_lexiu
from element_position.lexiu import UChooseNum_lexiu_loc,LChooseNum_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import UChooseNum_leyou_loc,LChooseNum_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import UChooseNum_lelun_loc,LChooseNum_lelun_loc

class UnionLottoChooseNumber(Page,UChooseNum_loc,LChooseNum_loc):
    ################################元素操作##############################################
    #鼠标向下拖动
    def drag_down(self):
        target = self.find_element(*self.bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #鼠标向上拖动
    def drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    ##选择胆拖模式
    def DanTuo_mode(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()#点击选择模式
        self.wait_element_located(self.driver,self.UnionLotto_type_DanTuo_loc)
        self.find_element(*self.UnionLotto_type_DanTuo_loc).click()#选择双色球胆拖模式
    ######双色球 历史开奖#########
    def History(self):
        self.find_element(*self.history).click()
    def click_history(self):#点击展开的历史开奖
        self.find_element(*self.spread_run_lottery_loc).click()
    ##点击清除所选号码
    def clear_number(self):
        try:
            self.find_element(*self.clear_number_icon_loc).click()
        except NoSuchElementException:
            print("选号页，清除按钮缺失")
    #############################################双 色 球 手 选  ， 随 机 选 取 红 球 操 作 ####################################
    #从33个红球中随机选取6个红球
    def u_red_label6(self):
        red_label_list = []
        for i in random.sample(range(1,34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            #选取红球操作
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    ###从33个红球中随机选取18个红球
    def u_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1,34),18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    #双色球取消选中的18个球
    def u_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 34), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        for i in red_label_list:
            if len(str(i)) == 1:
                re_red_label = "0" + str(i)
            else:
                re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" %re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从33个红球中随机选取19个红球
    def u_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1,34),19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list

    ########################################双 色 球 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ########随机点击1个蓝球操作###################
    def u_bule_label1(self):
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),1):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list
    #随机选取16个蓝球操作
    def u_bule_label16(self):
        bule_label_list = []
        for i in random.sample(range(1,17),16):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            #选取16个蓝球
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            bule_label_list.append(i)
            #打印出选取的16个蓝球的号码
        #print(bule_label_list)#调试用
        return bule_label_list

 ######################################双 色 球 手 选 胆 拖 玩 法 ，元 素 操 作############################################
    ####双色球胆拖玩法，随机选取1个胆码，6个拖码操作
    def u_red_one_six(self):
        self.wait_element_located(self.driver,self.DanMa_loc)#当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1,34),1):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)#打印可选胆码，调试用
        Tuo_Ma =[i for i in range(1,34) if i not in red_dan_label_list]#拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()#鼠标向下拖动
        self.wait_element_located(self.driver,self.TuoMa_loc)#当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma,6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='tuoredq'] i[vrq='%s']"%red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)#打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，2个拖码操作
    def u_red_five_two(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，18个拖码操作
    def u_red_five_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用

    ####双色球胆拖玩法，随机选取6个胆码，19个拖码操作
    def u_red_six_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##红球胆码超过5个提示
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码,调试用
        self.out_of_num()  # 拖码超过指定数量提示
    ####双色球胆拖玩法，选取一个蓝球操作
    def u_bule_one(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" % red_label).click()
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    ####双色球胆拖玩法，选取16个蓝球操作
    def u_bule_sixteen(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 16):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" %red_label).click()
            sleep(0.2)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    #获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver,self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)#等待2秒，toast提示信息自动消失
        return outOfNumtoast

    #点击“机选”按钮
    def machine_choose_button(self):
        self.wait_element_located(self.driver,self.machine_choose_button_loc)
        self.find_element(*self.machine_choose_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.wait_element_located(self.driver,self.machine_choose_one_button_loc)
        self.find_element(*self.machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.wait_element_located(self.driver,self.machine_choose_five_button_loc)
        self.find_element(*self.machine_choose_five_button_loc).click()
    #点击“机选十注”按钮
    def machine_choose_ten_button(self):
        self.wait_element_located(self.driver,self.machine_choose_ten_button_loc)
        self.find_element(*self.machine_choose_ten_button_loc).click()

    ###################确认选号按钮############################
    def Confirm_button(self):
        self.wait_element_located(self.driver,self.confirm_button_loc)##等待确认选号按钮可见时，再执行点击操作
        self.find_element(*self.confirm_button_loc).click()

    ##################点击 双色球-普通按钮#######################
    def UnionLotto_type_choose(self):
        self.find_element(*self.mode_choose_button_loc).click()

    def Select_bule(self):
        a=self.find_element(*self.select_bule).text##读取选中蓝球号码
        self.wait_element_located(self.driver, self.bule_loc)
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
                # 选取蓝球操作
            if bule_label==a:
                print("已经选中了")
                if a=='01':
                    bule_label = int(bule_label)+1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
                else:
                    bule_label=int(bule_label)-1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
            else:
                self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                bule_label_list.append(i)
            return bule_label_list

    def There_clock(self):
        self.find_element(*self.there_clock).click()###点击右上角。。。

    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Recommended_number(self):
        self.find_element(*self.recommended_number).click()#点击使用推荐号码

    def Recommended_nu(self):
        list=[]
        a=self.find_elements(*self.recommended_nu)##读取推荐号码list
        for i in range(len(a)):
            aa=self.find_element(*self.Recommended_nus(i+1)).text##在List中将号码遍历出来
            list.append(int(aa))##将遍历出来的号码放入list
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:###list号码以小到大排序
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Many_pause(self):
        self.find_element(*self.many_pause).click()##点击多期机选

    def Many_pause_nu(self):
        list=[5,10,20,50]
        a=random.sample(list,1)
        n=a[0]
        self.find_element(*self.many_pause_nu(n)).click()###随机选择多期机选中的期号
        return n

    def Many_pause_confirm(self):
        self.find_element(*self.many_pause_confirm).click()##点击多期机选中的提交订单

    def History_red(self,q):
        for n in range(1,q+1):
            sleep(2)
            self.find_element(*self.history_red(n)).click()#点击历史走势红球

    def Red_movements(self):
        self.find_element(*self.red_movements).click()##点击红球走势

    def Bule_movements(self):
        self.find_element(*self.bule_movements).click()##点击蓝球走势

    def History_bule(self,q):
        for n in range(1,q):
            sleep(2)
            self.find_element(*self.history_bule(n)).click()#点击历史走势，蓝球
    def many_machine_choose(self,n):#多期机选号码--mj20171208
        self.find_element(*self.many_pause_nu(n)).click()  ###随机选择多期机选中的期号
        return n
    def many_machine_choose_text(self):#获取多期机选页的注数倍数文本
        text=self.find_element(*self.many_text_loc).text
        return text
    def many_choose_input(self,n):#多期机选页输入追号期数
        self.find_element(*self.many_choose_input_loc).clear()
        self.find_element(*self.many_choose_input_loc).send_keys(n)
        return n
    def many_choose_add(self):#点击多期机选页的+按钮
        self.find_element(*self.many_choose_add_loc).click()
    def many_choose_sub(self):#点击多期机选页的-按钮
        self.find_element(*self.many_choose_sub_loc).click()
    def many_chase_radio(self):#点击多期机选页面的追加单选按钮
        self.find_element(*self.many_chase_radio_loc).click()

    def u_bule_label1_too(self):###随机选择2个蓝球
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),2):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    def Lottery_information_unionlotto(self):
        self.find_element(*self.lottery_information_unionlotto).click()###点击开奖信息中的双色球

    def Lucky_number(self):
        self.find_element(*self.lucky_number).click()##点击幸运选号

    def Birthday_pick(self):
        self.find_element(*self.birthday_pick).click()###生日选号

    def Phone_pick(self):
        self.find_element(*self.phone_pick).click()##手机号选号

    def QQ_pick(self):
        self.find_element(*self.qq_pick).click()##qq选号

class UnionLottoChooseNumber_lexiu(Page_lexiu,UChooseNum_lexiu_loc,LChooseNum_lexiu_loc):
    ################################元素操作##############################################
    #鼠标向下拖动
    def drag_down(self):
        target = self.find_element(*self.bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #鼠标向上拖动
    def drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    ##选择胆拖模式
    def DanTuo_mode(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()#点击选择模式
        self.wait_element_located(self.driver,self.UnionLotto_type_DanTuo_loc)
        self.find_element(*self.UnionLotto_type_DanTuo_loc).click()#选择双色球胆拖模式
    ######双色球 历史开奖#########
    def History(self):
        self.find_element(*self.history).click()
    def click_history(self):#点击展开的历史开奖
        self.find_element(*self.spread_run_lottery_loc).click()
    ##点击清除所选号码
    def clear_number(self):
        try:
            self.find_element(*self.clear_number_icon_loc).click()
        except NoSuchElementException:
            print("选号页，清除按钮缺失")
    #############################################双 色 球 手 选  ， 随 机 选 取 红 球 操 作 ####################################
    #从33个红球中随机选取6个红球
    def u_red_label6(self):
        red_label_list = []
        for i in random.sample(range(1,34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            #选取红球操作
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    ###从33个红球中随机选取18个红球
    def u_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1,34),18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    #双色球取消选中的18个球
    def u_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 34), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        for i in red_label_list:
            if len(str(i)) == 1:
                re_red_label = "0" + str(i)
            else:
                re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" %re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从33个红球中随机选取19个红球
    def u_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1,34),19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list

    ########################################双 色 球 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ########随机点击1个蓝球操作###################
    def u_bule_label1(self):
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),1):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list
    #随机选取16个蓝球操作
    def u_bule_label16(self):
        bule_label_list = []
        for i in random.sample(range(1,17),16):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            #选取16个蓝球
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            bule_label_list.append(i)
            #打印出选取的16个蓝球的号码
        #print(bule_label_list)#调试用
        return bule_label_list

 ######################################双 色 球 手 选 胆 拖 玩 法 ，元 素 操 作############################################
    ####双色球胆拖玩法，随机选取1个胆码，6个拖码操作
    def u_red_one_six(self):
        self.wait_element_located(self.driver,self.DanMa_loc)#当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1,34),1):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)#打印可选胆码，调试用
        Tuo_Ma =[i for i in range(1,34) if i not in red_dan_label_list]#拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()#鼠标向下拖动
        self.wait_element_located(self.driver,self.TuoMa_loc)#当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma,6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='tuoredq'] i[vrq='%s']"%red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)#打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，2个拖码操作
    def u_red_five_two(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，18个拖码操作
    def u_red_five_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用

    ####双色球胆拖玩法，随机选取6个胆码，19个拖码操作
    def u_red_six_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##红球胆码超过5个提示
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码,调试用
        self.out_of_num()  # 拖码超过指定数量提示
    ####双色球胆拖玩法，选取一个蓝球操作
    def u_bule_one(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" % red_label).click()
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    ####双色球胆拖玩法，选取16个蓝球操作
    def u_bule_sixteen(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 16):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" %red_label).click()
            sleep(0.2)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    #获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver,self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)#等待2秒，toast提示信息自动消失
        return outOfNumtoast

    #点击“机选”按钮
    def machine_choose_button(self):
        self.wait_element_located(self.driver,self.machine_choose_button_loc)
        self.find_element(*self.machine_choose_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.wait_element_located(self.driver,self.machine_choose_one_button_loc)
        self.find_element(*self.machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.wait_element_located(self.driver,self.machine_choose_five_button_loc)
        self.find_element(*self.machine_choose_five_button_loc).click()
    #点击“机选十注”按钮
    def machine_choose_ten_button(self):
        self.wait_element_located(self.driver,self.machine_choose_ten_button_loc)
        self.find_element(*self.machine_choose_ten_button_loc).click()

    ###################确认选号按钮############################
    def Confirm_button(self):
        self.wait_element_located(self.driver,self.confirm_button_loc)##等待确认选号按钮可见时，再执行点击操作
        self.find_element(*self.confirm_button_loc).click()

    ##################点击 双色球-普通按钮#######################
    def UnionLotto_type_choose(self):
        self.find_element(*self.mode_choose_button_loc).click()

    def Select_bule(self):
        a=self.find_element(*self.select_bule).text##读取选中蓝球号码
        self.wait_element_located(self.driver, self.bule_loc)
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
                # 选取蓝球操作
            if bule_label==a:
                print("已经选中了")
                if a=='01':
                    bule_label = int(bule_label)+1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
                else:
                    bule_label=int(bule_label)-1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
            else:
                self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                bule_label_list.append(i)
            return bule_label_list

    def There_clock(self):
        self.find_element(*self.there_clock).click()###点击右上角。。。

    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Recommended_number(self):
        self.find_element(*self.recommended_number).click()#点击使用推荐号码

    def Recommended_nu(self):
        list=[]
        a=self.find_elements(*self.recommended_nu)##读取推荐号码list
        for i in range(len(a)):
            aa=self.find_element(*self.Recommended_nus(i+1)).text##在List中将号码遍历出来
            list.append(int(aa))##将遍历出来的号码放入list
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:###list号码以小到大排序
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Many_pause(self):
        self.find_element(*self.many_pause).click()##点击多期机选

    def Many_pause_nu(self):
        list=[5,10,20,50]
        a=random.sample(list,1)
        n=a[0]
        self.find_element(*self.many_pause_nu(n)).click()###随机选择多期机选中的期号
        return n

    def Many_pause_confirm(self):
        self.find_element(*self.many_pause_confirm).click()##点击多期机选中的提交订单

    def History_red(self,q):
        for n in range(1,q+1):
            sleep(2)
            self.find_element(*self.history_red(n)).click()#点击历史走势红球

    def Red_movements(self):
        self.find_element(*self.red_movements).click()##点击红球走势

    def Bule_movements(self):
        self.find_element(*self.bule_movements).click()##点击蓝球走势

    def History_bule(self,q):
        for n in range(1,q):
            sleep(2)
            self.find_element(*self.history_bule(n)).click()#点击历史走势，蓝球
    def many_machine_choose(self,n):#多期机选号码--mj20171208
        self.find_element(*self.many_pause_nu(n)).click()  ###随机选择多期机选中的期号
        return n
    def many_machine_choose_text(self):#获取多期机选页的注数倍数文本
        text=self.find_element(*self.many_text_loc).text
        return text
    def many_choose_input(self,n):#多期机选页输入追号期数
        self.find_element(*self.many_choose_input_loc).clear()
        self.find_element(*self.many_choose_input_loc).send_keys(n)
        return n
    def many_choose_add(self):#点击多期机选页的+按钮
        self.find_element(*self.many_choose_add_loc).click()
    def many_choose_sub(self):#点击多期机选页的-按钮
        self.find_element(*self.many_choose_sub_loc).click()
    def many_chase_radio(self):#点击多期机选页面的追加单选按钮
        self.find_element(*self.many_chase_radio_loc).click()

    def u_bule_label1_too(self):###随机选择2个蓝球
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),2):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    def Lottery_information_unionlotto(self):
        self.find_element(*self.lottery_information_unionlotto).click()###点击开奖信息中的双色球

class UnionLottoChooseNumber_leyou(Page_leyou,UChooseNum_leyou_loc,LChooseNum_leyou_loc):
    ################################元素操作##############################################
    #鼠标向下拖动
    def drag_down(self):
        target = self.find_element(*self.bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #鼠标向上拖动
    def drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    ##选择胆拖模式
    def DanTuo_mode(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()#点击选择模式
        self.wait_element_located(self.driver,self.UnionLotto_type_DanTuo_loc)
        self.find_element(*self.UnionLotto_type_DanTuo_loc).click()#选择双色球胆拖模式
    ######双色球 历史开奖#########
    def History(self):
        self.find_element(*self.history).click()
    def click_history(self):#点击展开的历史开奖
        self.find_element(*self.spread_run_lottery_loc).click()
    ##点击清除所选号码
    def clear_number(self):
        try:
            self.find_element(*self.clear_number_icon_loc).click()
        except NoSuchElementException:
            print("选号页，清除按钮缺失")
    #############################################双 色 球 手 选  ， 随 机 选 取 红 球 操 作 ####################################
    #从33个红球中随机选取6个红球
    def u_red_label6(self):
        red_label_list = []
        for i in random.sample(range(1,34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            #选取红球操作
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    ###从33个红球中随机选取18个红球
    def u_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1,34),18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    #双色球取消选中的18个球
    def u_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 34), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        for i in red_label_list:
            if len(str(i)) == 1:
                re_red_label = "0" + str(i)
            else:
                re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" %re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从33个红球中随机选取19个红球
    def u_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1,34),19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list

    ########################################双 色 球 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ########随机点击1个蓝球操作###################
    def u_bule_label1(self):
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),1):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list
    #随机选取16个蓝球操作
    def u_bule_label16(self):
        bule_label_list = []
        for i in random.sample(range(1,17),16):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            #选取16个蓝球
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            bule_label_list.append(i)
            #打印出选取的16个蓝球的号码
        #print(bule_label_list)#调试用
        return bule_label_list

 ######################################双 色 球 手 选 胆 拖 玩 法 ，元 素 操 作############################################
    ####双色球胆拖玩法，随机选取1个胆码，6个拖码操作
    def u_red_one_six(self):
        self.wait_element_located(self.driver,self.DanMa_loc)#当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1,34),1):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)#打印可选胆码，调试用
        Tuo_Ma =[i for i in range(1,34) if i not in red_dan_label_list]#拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()#鼠标向下拖动
        self.wait_element_located(self.driver,self.TuoMa_loc)#当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma,6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='tuoredq'] i[vrq='%s']"%red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)#打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，2个拖码操作
    def u_red_five_two(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，18个拖码操作
    def u_red_five_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用

    ####双色球胆拖玩法，随机选取6个胆码，19个拖码操作
    def u_red_six_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##红球胆码超过5个提示
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码,调试用
        self.out_of_num()  # 拖码超过指定数量提示
    ####双色球胆拖玩法，选取一个蓝球操作
    def u_bule_one(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" % red_label).click()
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    ####双色球胆拖玩法，选取16个蓝球操作
    def u_bule_sixteen(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 16):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" %red_label).click()
            sleep(0.2)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    #获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver,self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)#等待2秒，toast提示信息自动消失
        return outOfNumtoast

    #点击“机选”按钮
    def machine_choose_button(self):
        self.wait_element_located(self.driver,self.machine_choose_button_loc)
        self.find_element(*self.machine_choose_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.wait_element_located(self.driver,self.machine_choose_one_button_loc)
        self.find_element(*self.machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.wait_element_located(self.driver,self.machine_choose_five_button_loc)
        self.find_element(*self.machine_choose_five_button_loc).click()
    #点击“机选十注”按钮
    def machine_choose_ten_button(self):
        self.wait_element_located(self.driver,self.machine_choose_ten_button_loc)
        self.find_element(*self.machine_choose_ten_button_loc).click()

    ###################确认选号按钮############################
    def Confirm_button(self):
        self.wait_element_located(self.driver,self.confirm_button_loc)##等待确认选号按钮可见时，再执行点击操作
        self.find_element(*self.confirm_button_loc).click()

    ##################点击 双色球-普通按钮#######################
    def UnionLotto_type_choose(self):
        self.find_element(*self.mode_choose_button_loc).click()

    def Select_bule(self):
        a=self.find_element(*self.select_bule).text##读取选中蓝球号码
        self.wait_element_located(self.driver, self.bule_loc)
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
                # 选取蓝球操作
            if bule_label==a:
                print("已经选中了")
                if a=='01':
                    bule_label = int(bule_label)+1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
                else:
                    bule_label=int(bule_label)-1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
            else:
                self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                bule_label_list.append(i)
            return bule_label_list

    def There_clock(self):
        self.find_element(*self.there_clock).click()###点击右上角。。。

    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Recommended_number(self):
        self.find_element(*self.recommended_number).click()#点击使用推荐号码

    def Recommended_nu(self):
        list=[]
        a=self.find_elements(*self.recommended_nu)##读取推荐号码list
        for i in range(len(a)):
            aa=self.find_element(*self.Recommended_nus(i+1)).text##在List中将号码遍历出来
            list.append(int(aa))##将遍历出来的号码放入list
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:###list号码以小到大排序
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Many_pause(self):
        self.find_element(*self.many_pause).click()##点击多期机选

    def Many_pause_nu(self):
        list=[5,10,20,50]
        a=random.sample(list,1)
        n=a[0]
        self.find_element(*self.many_pause_nu(n)).click()###随机选择多期机选中的期号
        return n

    def Many_pause_confirm(self):
        self.find_element(*self.many_pause_confirm).click()##点击多期机选中的提交订单

    def History_red(self,q):
        for n in range(1,q+1):
            sleep(2)
            self.find_element(*self.history_red(n)).click()#点击历史走势红球

    def Red_movements(self):
        self.find_element(*self.red_movements).click()##点击红球走势

    def Bule_movements(self):
        self.find_element(*self.bule_movements).click()##点击蓝球走势

    def History_bule(self,q):
        for n in range(1,q):
            sleep(2)
            self.find_element(*self.history_bule(n)).click()#点击历史走势，蓝球
    def many_machine_choose(self,n):#多期机选号码--mj20171208
        self.find_element(*self.many_pause_nu(n)).click()  ###随机选择多期机选中的期号
        return n
    def many_machine_choose_text(self):#获取多期机选页的注数倍数文本
        text=self.find_element(*self.many_text_loc).text
        return text
    def many_choose_input(self,n):#多期机选页输入追号期数
        self.find_element(*self.many_choose_input_loc).clear()
        self.find_element(*self.many_choose_input_loc).send_keys(n)
        return n
    def many_choose_add(self):#点击多期机选页的+按钮
        self.find_element(*self.many_choose_add_loc).click()
    def many_choose_sub(self):#点击多期机选页的-按钮
        self.find_element(*self.many_choose_sub_loc).click()
    def many_chase_radio(self):#点击多期机选页面的追加单选按钮
        self.find_element(*self.many_chase_radio_loc).click()

    def u_bule_label1_too(self):###随机选择2个蓝球
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),2):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    def Lottery_information_unionlotto(self):
        self.find_element(*self.lottery_information_unionlotto).click()###点击开奖信息中的双色球

class UnionLottoChooseNumber_lelun(Page_lelun,UChooseNum_lelun_loc,LChooseNum_lelun_loc):
    ################################元素操作##############################################
    #鼠标向下拖动
    def drag_down(self):
        target = self.find_element(*self.bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #鼠标向上拖动
    def drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    ##选择胆拖模式
    def DanTuo_mode(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()#点击选择模式
        self.wait_element_located(self.driver,self.UnionLotto_type_DanTuo_loc)
        self.find_element(*self.UnionLotto_type_DanTuo_loc).click()#选择双色球胆拖模式
    ######双色球 历史开奖#########
    def History(self):
        self.find_element(*self.history).click()
    def click_history(self):#点击展开的历史开奖
        self.find_element(*self.spread_run_lottery_loc).click()
    ##点击清除所选号码
    def clear_number(self):
        try:
            self.find_element(*self.clear_number_icon_loc).click()
        except NoSuchElementException:
            print("选号页，清除按钮缺失")
    #############################################双 色 球 手 选  ， 随 机 选 取 红 球 操 作 ####################################
    #从33个红球中随机选取6个红球
    def u_red_label6(self):
        red_label_list = []
        for i in random.sample(range(1,34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            #选取红球操作
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    ###从33个红球中随机选取18个红球
    def u_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1,34),18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list
    #双色球取消选中的18个球
    def u_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 34), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        for i in red_label_list:
            if len(str(i)) == 1:
                re_red_label = "0" + str(i)
            else:
                re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" %re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从33个红球中随机选取19个红球
    def u_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1,34),19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"label[name='redlabel'] i[vrq='%s']"%red_label).click()
            red_label_list.append(i)
        #print(red_label_list)#调试用
        return red_label_list

    ########################################双 色 球 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ########随机点击1个蓝球操作###################
    def u_bule_label1(self):
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),1):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list
    #随机选取16个蓝球操作
    def u_bule_label16(self):
        bule_label_list = []
        for i in random.sample(range(1,17),16):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            #选取16个蓝球
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            bule_label_list.append(i)
            #打印出选取的16个蓝球的号码
        #print(bule_label_list)#调试用
        return bule_label_list

 ######################################双 色 球 手 选 胆 拖 玩 法 ，元 素 操 作############################################
    ####双色球胆拖玩法，随机选取1个胆码，6个拖码操作
    def u_red_one_six(self):
        self.wait_element_located(self.driver,self.DanMa_loc)#当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1,34),1):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)#打印可选胆码，调试用
        Tuo_Ma =[i for i in range(1,34) if i not in red_dan_label_list]#拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()#鼠标向下拖动
        self.wait_element_located(self.driver,self.TuoMa_loc)#当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma,6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='tuoredq'] i[vrq='%s']"%red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)#打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，2个拖码操作
    def u_red_five_two(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    ####双色球胆拖玩法，随机选取5个胆码，18个拖码操作
    def u_red_five_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 5):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用

    ####双色球胆拖玩法，随机选取6个胆码，19个拖码操作
    def u_red_six_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 34), 6):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##红球胆码超过5个提示
        Tuo_Ma = [i for i in range(1, 34) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i))==1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码,调试用
        self.out_of_num()  # 拖码超过指定数量提示
    ####双色球胆拖玩法，选取一个蓝球操作
    def u_bule_one(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" % red_label).click()
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    ####双色球胆拖玩法，选取16个蓝球操作
    def u_bule_sixteen(self):
        self.wait_element_located(self.driver,self.DT_bule_loc)#胆拖玩法蓝球列表可见时
        bule_label_list = []
        for i in random.sample(range(1, 17), 16):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
                # 选取蓝球操作
            self.find_element(By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='%s']" %red_label).click()
            sleep(0.2)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    #获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver,self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)#等待2秒，toast提示信息自动消失
        return outOfNumtoast

    #点击“机选”按钮
    def machine_choose_button(self):
        self.wait_element_located(self.driver,self.machine_choose_button_loc)
        self.find_element(*self.machine_choose_button_loc).click()
    #点击“机选一注”按钮
    def machine_choose_one_button(self):
        self.wait_element_located(self.driver,self.machine_choose_one_button_loc)
        self.find_element(*self.machine_choose_one_button_loc).click()
    #点击“机选五注”按钮
    def machine_choose_five_button(self):
        self.wait_element_located(self.driver,self.machine_choose_five_button_loc)
        self.find_element(*self.machine_choose_five_button_loc).click()
    #点击“机选十注”按钮
    def machine_choose_ten_button(self):
        self.wait_element_located(self.driver,self.machine_choose_ten_button_loc)
        self.find_element(*self.machine_choose_ten_button_loc).click()

    ###################确认选号按钮############################
    def Confirm_button(self):
        self.wait_element_located(self.driver,self.confirm_button_loc)##等待确认选号按钮可见时，再执行点击操作
        self.find_element(*self.confirm_button_loc).click()

    ##################点击 双色球-普通按钮#######################
    def UnionLotto_type_choose(self):
        self.find_element(*self.mode_choose_button_loc).click()

    def Select_bule(self):
        a=self.find_element(*self.select_bule).text##读取选中蓝球号码
        self.wait_element_located(self.driver, self.bule_loc)
        bule_label_list = []
        for i in random.sample(range(1, 17), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
                # 选取蓝球操作
            if bule_label==a:
                print("已经选中了")
                if a=='01':
                    bule_label = int(bule_label)+1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
                else:
                    bule_label=int(bule_label)-1
                    self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                    bule_label_list.append(i)
            else:
                self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vrq='%s']" % bule_label).click()
                bule_label_list.append(i)
            return bule_label_list

    def There_clock(self):
        self.find_element(*self.there_clock).click()###点击右上角。。。

    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Recommended_number(self):
        self.find_element(*self.recommended_number).click()#点击使用推荐号码

    def Recommended_nu(self):
        list=[]
        a=self.find_elements(*self.recommended_nu)##读取推荐号码list
        for i in range(len(a)):
            aa=self.find_element(*self.Recommended_nus(i+1)).text##在List中将号码遍历出来
            list.append(int(aa))##将遍历出来的号码放入list
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:###list号码以小到大排序
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Many_pause(self):
        self.find_element(*self.many_pause).click()##点击多期机选

    def Many_pause_nu(self):
        list=[5,10,20,50]
        a=random.sample(list,1)
        n=a[0]
        self.find_element(*self.many_pause_nu(n)).click()###随机选择多期机选中的期号
        return n

    def Many_pause_confirm(self):
        self.find_element(*self.many_pause_confirm).click()##点击多期机选中的提交订单

    def History_red(self,q):
        for n in range(1,q+1):
            sleep(2)
            self.find_element(*self.history_red(n)).click()#点击历史走势红球

    def Red_movements(self):
        self.find_element(*self.red_movements).click()##点击红球走势

    def Bule_movements(self):
        self.find_element(*self.bule_movements).click()##点击蓝球走势

    def History_bule(self,q):
        for n in range(1,q):
            sleep(2)
            self.find_element(*self.history_bule(n)).click()#点击历史走势，蓝球
    def many_machine_choose(self,n):#多期机选号码--mj20171208
        self.find_element(*self.many_pause_nu(n)).click()  ###随机选择多期机选中的期号
        return n
    def many_machine_choose_text(self):#获取多期机选页的注数倍数文本
        text=self.find_element(*self.many_text_loc).text
        return text
    def many_choose_input(self,n):#多期机选页输入追号期数
        self.find_element(*self.many_choose_input_loc).clear()
        self.find_element(*self.many_choose_input_loc).send_keys(n)
        return n
    def many_choose_add(self):#点击多期机选页的+按钮
        self.find_element(*self.many_choose_add_loc).click()
    def many_choose_sub(self):#点击多期机选页的-按钮
        self.find_element(*self.many_choose_sub_loc).click()
    def many_chase_radio(self):#点击多期机选页面的追加单选按钮
        self.find_element(*self.many_chase_radio_loc).click()

    def u_bule_label1_too(self):###随机选择2个蓝球
        self.wait_element_located(self.driver,self.bule_loc)
        bule_label_list =[]
        for i in random.sample(range(1,17),2):
            if len(str(i))==1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
        #选取蓝球操作
            self.find_element(By.CSS_SELECTOR,"label[name='bluelabel'] i[vrq='%s']"%bule_label).click()
            sleep(1)
            bule_label_list.append(i)
        #print(bule_label_list)#调试用
        return bule_label_list

    def Lottery_information_unionlotto(self):
        self.find_element(*self.lottery_information_unionlotto).click()###点击开奖信息中的双色球

