from selenium.webdriver.common.by import By
from element_operate.base import Page
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,WebDriverException
from element_position.lemi import EleChooseFiveChooseNum_loc
from element_position.lemi import UChooseNum_loc
import random
import time
from time import sleep
from element_operate.base import Page_lexiu
from element_position.lexiu import EleChooseFiveChooseNum_lexiu_loc
from element_position.lexiu import UChooseNum_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import EleChooseFiveChooseNum_leyou_loc
from element_position.leyou import UChooseNum_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import EleChooseFiveChooseNum_lelun_loc
from element_position.lelun import UChooseNum_lelun_loc
#11选5元素操作
class ElevenFiveChooseNumber(Page,EleChooseFiveChooseNum_loc,UChooseNum_loc):

    #点击选择展开玩法模式
    def spread_mode_button(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()

        ##########################11选5选择方法------mj20171023
        ##广东11选5 23
        ##广西11选5 24
        ##山东11选5 22
    def mode_choose(self, type, mode):
        list1 = [1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 18, 19, 24, 22, 23, 2, 4, 6, 8, 10, 12, 17, 20]
        if type == 23:  # 广东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前三组选
        if type == 24:  # 广西11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广西11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广西11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
        if type == 22:  # 山东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择山东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择山东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选六模式
            if mode == 6:
                model = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
    #点击展开“正在开奖”
    def current_period(self):
        self.wait_element_located(self.driver,self.current_period_text_loc)
        self.find_element(*self.current_period_text_loc).click()
    #点击展开“历史走势”
    def spread_historical_trend(self):
        self.wait_element_located(self.driver,self.spread_run_lottery_loc)
        self.find_element(*self.spread_run_lottery_loc).click()
    #判断“距离第xxx期截止：”文案是否存在
    def countdown_text(self):
        try:
            sleep(1)
            #self.wait_element_located(self.driver,self.countdown_text_loc)
            countdown_text=self.find_element(*self.countdown_text_loc).text
            print(countdown_text)
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")

    #######手选随机选号###----mj171031
    def hand_options(self,n):
       #随机选取n个号码
        self.wait_element_located(self.driver,self.first_num_loc)
        label_list = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list.append(i)
        return label_list
    ####选第二位数
    def second_num_choose(self,n):
        #第二位取n个号码
        self.wait_element_located(self.driver,self.second_num_loc)
        label_list1 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list1.append(i)
        return label_list1
    #选第三位数
    def third_num_choose(self,n):
        #第三位取n个号码
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver,self.third_num_loc)
        label_list2 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div2'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #乐选三选取三个号码---mj20171102
    def lexuan_choose(self,n,loc):
        self.wait_element_located(self.driver,self.l_first_num_loc)
        label_list2 = []
        for i in random.sample(range(1, 12), n):
            if len(str(i)) == 1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_%d'] i[vrq*='%s']" % (loc,label)).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #前三位选取不同的数字
    def different_three_num(self,m,n,p):
        self.wait_element_located(self.driver,self.l_first_num_loc)#第一位选号列表出现时
        label_list1 = []
        for i in random.sample(range(1, 12), m):##选取第一个数字
            if len(str(i)) == 1:
                label1 = "0" + str(i)
            else:
                label1 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_1'] i[vrq*='%s']" % label1).click()  # 第一位随机选取m个号码
            sleep(0.2)
            label_list1.append(i)
            print(label_list1)
        self.wait_element_located(self.driver, self.l_second_num_loc)  # 第二位选号列表出现时
        second = [i for i in range(1, 12) if i not in label_list1]  # 第二位可选号码
        print(second)
        # 从可选的号码中选取n个数做为第二位
        label_list2 = []
        for i in random.sample(second,n):#选取第二个数字
            if len(str(i)) == 1:
                label2 = "0" + str(i)
            else:
                label2 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_2'] i[vrq*='%s']" % label2).click()
            label_list2.append(i)
            print(label_list2)
        self.wait_element_located(self.driver, self.l_third_num_loc)  # 第三位选号列表出现时
        label_list2.extend(label_list1)
        third = [i for i in range(1, 12) if i not in label_list2]  # 第三位可选号码
        print(third)
        label_list3 = []
        for i in random.sample(third,p):#选取第三个数字
            if len(str(i)) == 1:
                label3 = "0" + str(i)
            else:
                label3 = str(i)
            self.driver.execute_script("window.scroll(0,300)")
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_3'] i[vrq*='%s']" % label3).click()
            sleep(0.2)
            label_list3.append(i)
            print(label_list3)
    ###胆拖投注---mj171101
    def dantuo_choose_num(self,n,m):##选取n个胆码
        danma_list = []
        for i in random.sample(range(1,12),n):
            #if len(str(i)) == 1:
             #   danma = "0" + str(i)
            #else:
            danma = i
            danma_list.append(danma)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%danma).click()
            sleep(0.2)
        print(danma_list)
        tuoma_option = [i for i in range(1,12) if i not in danma_list]#拖码可选的数字
        print(tuoma_option)
        tuoma_list = []

        for j in random.sample(tuoma_option,m):##选取m个拖码
            if len(str(j)) == 1:
                tuoma = "0" + str(j)
            else:
                tuoma = str(j)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s"%tuoma).click()
            sleep(0.2)
            tuoma_list.append(j)
        print(tuoma_list)
    #获取投xx注的文本
    def total_buy_text(self):
        self.wait_element_located(self.driver,self.total_buy_text_loc)
        text = self.find_element(*self.total_buy_text_loc).text
        return text
    #点击“确认选号”按钮
    def confirm_number_button(self):
        self.wait_element_located(self.driver,self.confirm_number_button_loc)
        self.find_element(*self.confirm_number_button_loc).click()
    def recommendation_choose_num(self,n):#点击推荐号码页面的号码--mj20171211
        for i in random.sample(range(2,13),n):
            self.find_element(*self.recommendation_choose_num_loc(i)).click()

    def use_recommendation(self):#点击使用推荐号码按钮
        self.find_element(*self.use_recommendation_loc).click()
    def history_trend(self):#11选5点击历史走势
        self.find_element(*self.history_trend_loc).click()

class ElevenFiveChooseNumber_lexiu(Page_lexiu,EleChooseFiveChooseNum_lexiu_loc,UChooseNum_lexiu_loc):

    #点击选择展开玩法模式
    def spread_mode_button(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()

        ##########################11选5选择方法------mj20171023
        ##广东11选5 23
        ##广西11选5 24
        ##山东11选5 22
    def mode_choose(self, type, mode):
        list1 = [1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 18, 19, 24, 22, 23, 2, 4, 6, 8, 10, 12, 17, 20]
        if type == 23:  # 广东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前三组选
        if type == 24:  # 广西11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广西11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广西11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
        if type == 22:  # 山东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择山东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择山东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选六模式
            if mode == 6:
                model = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
    #点击展开“正在开奖”
    def current_period(self):
        self.wait_element_located(self.driver,self.current_period_text_loc)
        self.find_element(*self.current_period_text_loc).click()
    #点击展开“历史走势”
    def spread_historical_trend(self):
        self.wait_element_located(self.driver,self.spread_run_lottery_loc)
        self.find_element(*self.spread_run_lottery_loc).click()
    #判断“距离第xxx期截止：”文案是否存在
    def countdown_text(self):
        try:
            sleep(1)
            #self.wait_element_located(self.driver,self.countdown_text_loc)
            countdown_text=self.find_element(*self.countdown_text_loc).text
            print(countdown_text)
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")

    #######手选随机选号###----mj171031
    def hand_options(self,n):
       #随机选取n个号码
        self.wait_element_located(self.driver,self.first_num_loc)
        label_list = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list.append(i)
        return label_list
    ####选第二位数
    def second_num_choose(self,n):
        #第二位取n个号码
        self.wait_element_located(self.driver,self.second_num_loc)
        label_list1 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list1.append(i)
        return label_list1
    #选第三位数
    def third_num_choose(self,n):
        #第三位取n个号码
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver,self.third_num_loc)
        label_list2 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div2'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #乐选三选取三个号码---mj20171102
    def lexuan_choose(self,n,loc):
        self.wait_element_located(self.driver,self.l_first_num_loc)
        label_list2 = []
        for i in random.sample(range(1, 12), n):
            if len(str(i)) == 1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_%d'] i[vrq*='%s']" % (loc,label)).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #前三位选取不同的数字
    def different_three_num(self,m,n,p):
        self.wait_element_located(self.driver,self.l_first_num_loc)#第一位选号列表出现时
        label_list1 = []
        for i in random.sample(range(1, 12), m):##选取第一个数字
            if len(str(i)) == 1:
                label1 = "0" + str(i)
            else:
                label1 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_1'] i[vrq*='%s']" % label1).click()  # 第一位随机选取m个号码
            sleep(0.2)
            label_list1.append(i)
            print(label_list1)
        self.wait_element_located(self.driver, self.l_second_num_loc)  # 第二位选号列表出现时
        second = [i for i in range(1, 12) if i not in label_list1]  # 第二位可选号码
        print(second)
        # 从可选的号码中选取n个数做为第二位
        label_list2 = []
        for i in random.sample(second,n):#选取第二个数字
            if len(str(i)) == 1:
                label2 = "0" + str(i)
            else:
                label2 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_2'] i[vrq*='%s']" % label2).click()
            label_list2.append(i)
            print(label_list2)
        self.wait_element_located(self.driver, self.l_third_num_loc)  # 第三位选号列表出现时
        label_list2.extend(label_list1)
        third = [i for i in range(1, 12) if i not in label_list2]  # 第三位可选号码
        print(third)
        label_list3 = []
        for i in random.sample(third,p):#选取第三个数字
            if len(str(i)) == 1:
                label3 = "0" + str(i)
            else:
                label3 = str(i)
            self.driver.execute_script("window.scroll(0,300)")
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_3'] i[vrq*='%s']" % label3).click()
            sleep(0.2)
            label_list3.append(i)
            print(label_list3)
    ###胆拖投注---mj171101
    def dantuo_choose_num(self,n,m):##选取n个胆码
        danma_list = []
        for i in random.sample(range(1,12),n):
            #if len(str(i)) == 1:
             #   danma = "0" + str(i)
            #else:
            danma = i
            danma_list.append(danma)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%danma).click()
            sleep(0.2)
        print(danma_list)
        tuoma_option = [i for i in range(1,12) if i not in danma_list]#拖码可选的数字
        print(tuoma_option)
        tuoma_list = []

        for j in random.sample(tuoma_option,m):##选取m个拖码
            if len(str(j)) == 1:
                tuoma = "0" + str(j)
            else:
                tuoma = str(j)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s"%tuoma).click()
            sleep(0.2)
            tuoma_list.append(j)
        print(tuoma_list)
    #获取投xx注的文本
    def total_buy_text(self):
        self.wait_element_located(self.driver,self.total_buy_text_loc)
        text = self.find_element(*self.total_buy_text_loc).text
        return text
    #点击“确认选号”按钮
    def confirm_number_button(self):
        self.wait_element_located(self.driver,self.confirm_number_button_loc)
        self.find_element(*self.confirm_number_button_loc).click()
    def recommendation_choose_num(self,n):#点击推荐号码页面的号码--mj20171211
        for i in random.sample(range(2,13),n):
            self.find_element(*self.recommendation_choose_num_loc(i)).click()

    def use_recommendation(self):#点击使用推荐号码按钮
        self.find_element(*self.use_recommendation_loc).click()
    def history_trend(self):#11选5点击历史走势
        self.find_element(*self.history_trend_loc).click()

class ElevenFiveChooseNumber_leyou(Page_leyou,EleChooseFiveChooseNum_leyou_loc,UChooseNum_leyou_loc):

    #点击选择展开玩法模式
    def spread_mode_button(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()

        ##########################11选5选择方法------mj20171023
        ##广东11选5 23
        ##广西11选5 24
        ##山东11选5 22
    def mode_choose(self, type, mode):
        list1 = [1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 18, 19, 24, 22, 23, 2, 4, 6, 8, 10, 12, 17, 20]
        if type == 23:  # 广东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前三组选
        if type == 24:  # 广西11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广西11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广西11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
        if type == 22:  # 山东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择山东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择山东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选六模式
            if mode == 6:
                model = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
    #点击展开“正在开奖”
    def current_period(self):
        self.wait_element_located(self.driver,self.current_period_text_loc)
        self.find_element(*self.current_period_text_loc).click()
    #点击展开“历史走势”
    def spread_historical_trend(self):
        self.wait_element_located(self.driver,self.spread_run_lottery_loc)
        self.find_element(*self.spread_run_lottery_loc).click()
    #判断“距离第xxx期截止：”文案是否存在
    def countdown_text(self):
        try:
            sleep(1)
            #self.wait_element_located(self.driver,self.countdown_text_loc)
            countdown_text=self.find_element(*self.countdown_text_loc).text
            print(countdown_text)
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")

    #######手选随机选号###----mj171031
    def hand_options(self,n):
       #随机选取n个号码
        self.wait_element_located(self.driver,self.first_num_loc)
        label_list = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list.append(i)
        return label_list
    ####选第二位数
    def second_num_choose(self,n):
        #第二位取n个号码
        self.wait_element_located(self.driver,self.second_num_loc)
        label_list1 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list1.append(i)
        return label_list1
    #选第三位数
    def third_num_choose(self,n):
        #第三位取n个号码
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver,self.third_num_loc)
        label_list2 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div2'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #乐选三选取三个号码---mj20171102
    def lexuan_choose(self,n,loc):
        self.wait_element_located(self.driver,self.l_first_num_loc)
        label_list2 = []
        for i in random.sample(range(1, 12), n):
            if len(str(i)) == 1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_%d'] i[vrq*='%s']" % (loc,label)).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #前三位选取不同的数字
    def different_three_num(self,m,n,p):
        self.wait_element_located(self.driver,self.l_first_num_loc)#第一位选号列表出现时
        label_list1 = []
        for i in random.sample(range(1, 12), m):##选取第一个数字
            if len(str(i)) == 1:
                label1 = "0" + str(i)
            else:
                label1 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_1'] i[vrq*='%s']" % label1).click()  # 第一位随机选取m个号码
            sleep(0.2)
            label_list1.append(i)
            print(label_list1)
        self.wait_element_located(self.driver, self.l_second_num_loc)  # 第二位选号列表出现时
        second = [i for i in range(1, 12) if i not in label_list1]  # 第二位可选号码
        print(second)
        # 从可选的号码中选取n个数做为第二位
        label_list2 = []
        for i in random.sample(second,n):#选取第二个数字
            if len(str(i)) == 1:
                label2 = "0" + str(i)
            else:
                label2 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_2'] i[vrq*='%s']" % label2).click()
            label_list2.append(i)
            print(label_list2)
        self.wait_element_located(self.driver, self.l_third_num_loc)  # 第三位选号列表出现时
        label_list2.extend(label_list1)
        third = [i for i in range(1, 12) if i not in label_list2]  # 第三位可选号码
        print(third)
        label_list3 = []
        for i in random.sample(third,p):#选取第三个数字
            if len(str(i)) == 1:
                label3 = "0" + str(i)
            else:
                label3 = str(i)
            self.driver.execute_script("window.scroll(0,300)")
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_3'] i[vrq*='%s']" % label3).click()
            sleep(0.2)
            label_list3.append(i)
            print(label_list3)
    ###胆拖投注---mj171101
    def dantuo_choose_num(self,n,m):##选取n个胆码
        danma_list = []
        for i in random.sample(range(1,12),n):
            #if len(str(i)) == 1:
             #   danma = "0" + str(i)
            #else:
            danma = i
            danma_list.append(danma)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%danma).click()
            sleep(0.2)
        print(danma_list)
        tuoma_option = [i for i in range(1,12) if i not in danma_list]#拖码可选的数字
        print(tuoma_option)
        tuoma_list = []

        for j in random.sample(tuoma_option,m):##选取m个拖码
            if len(str(j)) == 1:
                tuoma = "0" + str(j)
            else:
                tuoma = str(j)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s"%tuoma).click()
            sleep(0.2)
            tuoma_list.append(j)
        print(tuoma_list)
    #获取投xx注的文本
    def total_buy_text(self):
        self.wait_element_located(self.driver,self.total_buy_text_loc)
        text = self.find_element(*self.total_buy_text_loc).text
        return text
    #点击“确认选号”按钮
    def confirm_number_button(self):
        self.wait_element_located(self.driver,self.confirm_number_button_loc)
        self.find_element(*self.confirm_number_button_loc).click()
    def recommendation_choose_num(self,n):#点击推荐号码页面的号码--mj20171211
        for i in random.sample(range(2,13),n):
            self.find_element(*self.recommendation_choose_num_loc(i)).click()

    def use_recommendation(self):#点击使用推荐号码按钮
        self.find_element(*self.use_recommendation_loc).click()
    def history_trend(self):#11选5点击历史走势
        self.find_element(*self.history_trend_loc).click()

class ElevenFiveChooseNumber_lelun(Page_lelun,EleChooseFiveChooseNum_lelun_loc,UChooseNum_lelun_loc):

    #点击选择展开玩法模式
    def spread_mode_button(self):
        self.wait_element_located(self.driver,self.mode_choose_button_loc)
        self.find_element(*self.mode_choose_button_loc).click()

        ##########################11选5选择方法------mj20171023
        ##广东11选5 23
        ##广西11选5 24
        ##山东11选5 22
    def mode_choose(self, type, mode):
        list1 = [1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 18, 19, 24, 22, 23, 2, 4, 6, 8, 10, 12, 17, 20]
        if type == 23:  # 广东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广东11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  #胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  #胆拖模式前三组选
        if type == 24:  # 广西11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择广西11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择广西11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择广西11选5，任选六模式
            if mode == 6:
                mode = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择广西11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
        if type == 22:  # 山东11选5
            if mode == 1:
                model = "0" + str(list1[0])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ##选择山东11选5，任选二模式
            if mode == 2:
                model = "0" + str(list1[1])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  ###选择山东11选5，任选三模式
            if mode == 3:
                model = "0" + str(list1[2])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选四模式
            if mode == 4:
                model = "0" + str(list1[3])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选五模式
            if mode == 5:
                model = "0" + str(list1[4])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选六模式
            if mode == 6:
                model = str(list1[5])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 选择山东11选5，任选七模式
            if mode == 7:
                mode = str(list1[6])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，任选八模式
            if mode == 8:
                mode = str(list1[7])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前一模式
            if mode == 9:
                mode = str(list1[8])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 选择山东11选5，前二直选模式
            if mode == 10:
                mode = str(list1[9])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前二组选模式
            if mode == 11:
                mode = str(list1[10])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三直选模式
            if mode == 12:
                mode = str(list1[11])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 前三组选模式
            if mode == 13:
                mode = str(list1[12])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选三模式
            if mode == 14:
                mode = str(list1[13])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选四模式
            if mode == 15:
                mode = str(list1[14])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 乐选五模式
            ##胆拖模式
            if mode == 16:
                model = "0" + str(list1[15])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选二
            if mode == 17:
                model = "0" + str(list1[16])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选三
            if mode == 18:
                model = "0" + str(list1[17])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选四
            if mode == 19:
                model = "0" + str(list1[18])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, model)).click()  # 胆拖模式任选五
            if mode == 20:
                mode = str(list1[19])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选六
            if mode == 21:
                mode = str(list1[20])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式任选七
            if mode == 22:
                mode = str(list1[21])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前二组选
            if mode == 23:
                mode = str(list1[22])
                self.find_element(By.CSS_SELECTOR, "li[valp='%s0%s']" % (type, mode)).click()  # 胆拖模式前三组选
    #点击展开“正在开奖”
    def current_period(self):
        self.wait_element_located(self.driver,self.current_period_text_loc)
        self.find_element(*self.current_period_text_loc).click()
    #点击展开“历史走势”
    def spread_historical_trend(self):
        self.wait_element_located(self.driver,self.spread_run_lottery_loc)
        self.find_element(*self.spread_run_lottery_loc).click()
    #判断“距离第xxx期截止：”文案是否存在
    def countdown_text(self):
        try:
            sleep(1)
            #self.wait_element_located(self.driver,self.countdown_text_loc)
            countdown_text=self.find_element(*self.countdown_text_loc).text
            print(countdown_text)
            return countdown_text
        except NoSuchElementException:
            print("倒计时文案缺失")

    #######手选随机选号###----mj171031
    def hand_options(self,n):
       #随机选取n个号码
        self.wait_element_located(self.driver,self.first_num_loc)
        label_list = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list.append(i)
        return label_list
    ####选第二位数
    def second_num_choose(self,n):
        #第二位取n个号码
        self.wait_element_located(self.driver,self.second_num_loc)
        label_list1 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list1.append(i)
        return label_list1
    #选第三位数
    def third_num_choose(self,n):
        #第三位取n个号码
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)
        self.wait_element_located(self.driver,self.third_num_loc)
        label_list2 = []
        for i in random.sample(range(1,12),n):
            if len(str(i))==1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div2'] i[vrq*='%s']"%label).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #乐选三选取三个号码---mj20171102
    def lexuan_choose(self,n,loc):
        self.wait_element_located(self.driver,self.l_first_num_loc)
        label_list2 = []
        for i in random.sample(range(1, 12), n):
            if len(str(i)) == 1:
                label = "0" + str(i)
            else:
                label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_%d'] i[vrq*='%s']" % (loc,label)).click()
            sleep(0.2)
            label_list2.append(i)
        return label_list2
    #前三位选取不同的数字
    def different_three_num(self,m,n,p):
        self.wait_element_located(self.driver,self.l_first_num_loc)#第一位选号列表出现时
        label_list1 = []
        for i in random.sample(range(1, 12), m):##选取第一个数字
            if len(str(i)) == 1:
                label1 = "0" + str(i)
            else:
                label1 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_1'] i[vrq*='%s']" % label1).click()  # 第一位随机选取m个号码
            sleep(0.2)
            label_list1.append(i)
            print(label_list1)
        self.wait_element_located(self.driver, self.l_second_num_loc)  # 第二位选号列表出现时
        second = [i for i in range(1, 12) if i not in label_list1]  # 第二位可选号码
        print(second)
        # 从可选的号码中选取n个数做为第二位
        label_list2 = []
        for i in random.sample(second,n):#选取第二个数字
            if len(str(i)) == 1:
                label2 = "0" + str(i)
            else:
                label2 = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_2'] i[vrq*='%s']" % label2).click()
            label_list2.append(i)
            print(label_list2)
        self.wait_element_located(self.driver, self.l_third_num_loc)  # 第三位选号列表出现时
        label_list2.extend(label_list1)
        third = [i for i in range(1, 12) if i not in label_list2]  # 第三位可选号码
        print(third)
        label_list3 = []
        for i in random.sample(third,p):#选取第三个数字
            if len(str(i)) == 1:
                label3 = "0" + str(i)
            else:
                label3 = str(i)
            self.driver.execute_script("window.scroll(0,300)")
            self.find_element(By.CSS_SELECTOR, "div[id='codes_div_lx3_3'] i[vrq*='%s']" % label3).click()
            sleep(0.2)
            label_list3.append(i)
            print(label_list3)
    ###胆拖投注---mj171101
    def dantuo_choose_num(self,n,m):##选取n个胆码
        danma_list = []
        for i in random.sample(range(1,12),n):
            #if len(str(i)) == 1:
             #   danma = "0" + str(i)
            #else:
            danma = i
            danma_list.append(danma)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div'] i[vrq*='%s']"%danma).click()
            sleep(0.2)
        print(danma_list)
        tuoma_option = [i for i in range(1,12) if i not in danma_list]#拖码可选的数字
        print(tuoma_option)
        tuoma_list = []

        for j in random.sample(tuoma_option,m):##选取m个拖码
            if len(str(j)) == 1:
                tuoma = "0" + str(j)
            else:
                tuoma = str(j)
            self.find_element(By.CSS_SELECTOR,"div[id='codes_div1'] i[vrq*='%s"%tuoma).click()
            sleep(0.2)
            tuoma_list.append(j)
        print(tuoma_list)
    #获取投xx注的文本
    def total_buy_text(self):
        self.wait_element_located(self.driver,self.total_buy_text_loc)
        text = self.find_element(*self.total_buy_text_loc).text
        return text
    #点击“确认选号”按钮
    def confirm_number_button(self):
        self.wait_element_located(self.driver,self.confirm_number_button_loc)
        self.find_element(*self.confirm_number_button_loc).click()
    def recommendation_choose_num(self,n):#点击推荐号码页面的号码--mj20171211
        for i in random.sample(range(2,13),n):
            self.find_element(*self.recommendation_choose_num_loc(i)).click()

    def use_recommendation(self):#点击使用推荐号码按钮
        self.find_element(*self.use_recommendation_loc).click()
    def history_trend(self):#11选5点击历史走势
        self.find_element(*self.history_trend_loc).click()
