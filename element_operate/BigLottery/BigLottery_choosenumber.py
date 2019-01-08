from element_operate.base import Page
from element_position.lemi import LChooseNum_loc
from element_position.lemi import UChooseNum_loc
import random
from selenium.webdriver.common.by import By
from time import sleep
from element_operate.base import Page_lexiu
from element_position.lexiu import LChooseNum_lexiu_loc
from element_position.lexiu import UChooseNum_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import LChooseNum_leyou_loc
from element_position.leyou import UChooseNum_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import LChooseNum_lelun_loc
from element_position.lelun import UChooseNum_lelun_loc
class BigLotteryChooseNum(Page,LChooseNum_loc,UChooseNum_loc):
    ################################################################################################################
    #大乐透的选择胆拖模式玩法操作、大乐透机选操作在双色球选号的元素操作页类名为UnionLottoChooseNumber
    #
    ################################################################################################################
    def bule_history_choose(self,n):##点击历史趋势中的蓝球号码
        for i in range(2,n+2):
            self.find_element(*self.bule_history_choose_loc(i)).click()
            sleep(2)
    #大乐透拖胆玩法，鼠标拖动操作
    # 鼠标向下拖动
    def l_drag_down(self):
        target = self.find_element(*self.l_bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 鼠标向上拖动
    def l_drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        ########################################大 乐 透 手 选 ，随 机 选 取 红 球 操 作############################################################
        ####从35个红球中随机选取5个红球操作
    def l_red_label5(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取18个红球操作
    def l_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取19个红球操作
    def l_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ########################################大 乐 透 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ####大乐透取消选中18个红球操作
    def l_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        print(red_label_list)
        for i in red_label_list:
            re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从12个蓝球中选取2个蓝球的操作
    def l_bule_label2(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            bule_label_list.append(bule_label)
        print(bule_label_list)
        return bule_label_list
    ###从12个蓝球中选取12个蓝球的操作


    def l_bule_label12(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 12):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            sleep(0.2)
            bule_label_list.append(bule_label)
        #print(bule_label_list)#调试用
        return bule_label_list
##########################################大 乐 透 手 选 胆 拖 玩 法 ， 选 球 操 作##############################################
    #前区选取1个胆码，5个拖码
    def l_red_one_five(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，2个拖码
    def l_red_four_two(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click() #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取2个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取1个胆码，18个拖码
    def l_red_one_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，18个拖码
    def l_red_four_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取18个球
        self.l_drag_down()  # 鼠标向下拖动
        sleep(5)
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选5个胆码，19个拖码，获取提示信息文本
    def l_red_five_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()  ##红球胆码超过4个提示
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取19个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
        self.out_of_num()##红球胆码超过18个提示
    ##########大乐透胆拖玩法手选蓝球操作#
    ###后区选择1个胆码，11个拖码
    def l_bule_one_eleven(self):
        self.l_drag_down()
        self.wait_element_located(self.driver,self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" %bule_label).click()  # 随机选取一个红球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 11): # 从可选的拖码中选取11个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" %bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用
    ###后区选择1个胆码，2个拖码
    def l_bule_one_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取一个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        self.l_drag_down()
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

####选择2个后区胆码，获取提示信息文本
    def l_bule_two_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取两个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##超出限制提示
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

        # 获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver, self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)
        #print(outOfNumtoast)#调试用
        return outOfNumtoast

class BigLotteryChooseNum_lexiu(Page_lexiu,LChooseNum_lexiu_loc,UChooseNum_lexiu_loc):
    ################################################################################################################
    #大乐透的选择胆拖模式玩法操作、大乐透机选操作在双色球选号的元素操作页类名为UnionLottoChooseNumber
    #
    ################################################################################################################
    def bule_history_choose(self,n):##点击历史趋势中的蓝球号码
        for i in range(2,n+2):
            self.find_element(*self.bule_history_choose_loc(i)).click()
            sleep(2)
    #大乐透拖胆玩法，鼠标拖动操作
    # 鼠标向下拖动
    def l_drag_down(self):
        target = self.find_element(*self.l_bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 鼠标向上拖动
    def l_drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        ########################################大 乐 透 手 选 ，随 机 选 取 红 球 操 作############################################################
        ####从35个红球中随机选取5个红球操作
    def l_red_label5(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取18个红球操作
    def l_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取19个红球操作
    def l_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ########################################大 乐 透 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ####大乐透取消选中18个红球操作
    def l_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        print(red_label_list)
        for i in red_label_list:
            re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从12个蓝球中选取2个蓝球的操作
    def l_bule_label2(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            bule_label_list.append(bule_label)
        print(bule_label_list)
        return bule_label_list
    ###从12个蓝球中选取12个蓝球的操作


    def l_bule_label12(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 12):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            sleep(0.2)
            bule_label_list.append(bule_label)
        #print(bule_label_list)#调试用
        return bule_label_list
##########################################大 乐 透 手 选 胆 拖 玩 法 ， 选 球 操 作##############################################
    #前区选取1个胆码，5个拖码
    def l_red_one_five(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，2个拖码
    def l_red_four_two(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click() #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取2个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取1个胆码，18个拖码
    def l_red_one_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，18个拖码
    def l_red_four_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取18个球
        self.l_drag_down()  # 鼠标向下拖动
        sleep(5)
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选5个胆码，19个拖码，获取提示信息文本
    def l_red_five_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()  ##红球胆码超过4个提示
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取19个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
        self.out_of_num()##红球胆码超过18个提示
    ##########大乐透胆拖玩法手选蓝球操作#
    ###后区选择1个胆码，11个拖码
    def l_bule_one_eleven(self):
        self.l_drag_down()
        self.wait_element_located(self.driver,self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" %bule_label).click()  # 随机选取一个红球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 11): # 从可选的拖码中选取11个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" %bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用
    ###后区选择1个胆码，2个拖码
    def l_bule_one_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取一个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        self.l_drag_down()
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

####选择2个后区胆码，获取提示信息文本
    def l_bule_two_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取两个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##超出限制提示
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

        # 获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver, self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)
        #print(outOfNumtoast)#调试用
        return outOfNumtoast

class BigLotteryChooseNum_leyou(Page_leyou,LChooseNum_leyou_loc,UChooseNum_leyou_loc):
    ################################################################################################################
    #大乐透的选择胆拖模式玩法操作、大乐透机选操作在双色球选号的元素操作页类名为UnionLottoChooseNumber
    #
    ################################################################################################################
    def bule_history_choose(self,n):##点击历史趋势中的蓝球号码
        for i in range(2,n+2):
            self.find_element(*self.bule_history_choose_loc(i)).click()
            sleep(2)
    #大乐透拖胆玩法，鼠标拖动操作
    # 鼠标向下拖动
    def l_drag_down(self):
        target = self.find_element(*self.l_bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 鼠标向上拖动
    def l_drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        ########################################大 乐 透 手 选 ，随 机 选 取 红 球 操 作############################################################
        ####从35个红球中随机选取5个红球操作
    def l_red_label5(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取18个红球操作
    def l_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取19个红球操作
    def l_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ########################################大 乐 透 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ####大乐透取消选中18个红球操作
    def l_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        print(red_label_list)
        for i in red_label_list:
            re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从12个蓝球中选取2个蓝球的操作
    def l_bule_label2(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            bule_label_list.append(bule_label)
        print(bule_label_list)
        return bule_label_list
    ###从12个蓝球中选取12个蓝球的操作


    def l_bule_label12(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 12):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            sleep(0.2)
            bule_label_list.append(bule_label)
        #print(bule_label_list)#调试用
        return bule_label_list
##########################################大 乐 透 手 选 胆 拖 玩 法 ， 选 球 操 作##############################################
    #前区选取1个胆码，5个拖码
    def l_red_one_five(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，2个拖码
    def l_red_four_two(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click() #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取2个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取1个胆码，18个拖码
    def l_red_one_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，18个拖码
    def l_red_four_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取18个球
        self.l_drag_down()  # 鼠标向下拖动
        sleep(5)
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选5个胆码，19个拖码，获取提示信息文本
    def l_red_five_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()  ##红球胆码超过4个提示
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取19个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
        self.out_of_num()##红球胆码超过18个提示
    ##########大乐透胆拖玩法手选蓝球操作#
    ###后区选择1个胆码，11个拖码
    def l_bule_one_eleven(self):
        self.l_drag_down()
        self.wait_element_located(self.driver,self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" %bule_label).click()  # 随机选取一个红球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 11): # 从可选的拖码中选取11个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" %bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用
    ###后区选择1个胆码，2个拖码
    def l_bule_one_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取一个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        self.l_drag_down()
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

####选择2个后区胆码，获取提示信息文本
    def l_bule_two_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取两个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##超出限制提示
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

        # 获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver, self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)
        #print(outOfNumtoast)#调试用
        return outOfNumtoast

class BigLotteryChooseNum_lelun(Page_lelun,LChooseNum_lelun_loc,UChooseNum_lelun_loc):
    ################################################################################################################
    #大乐透的选择胆拖模式玩法操作、大乐透机选操作在双色球选号的元素操作页类名为UnionLottoChooseNumber
    #
    ################################################################################################################
    def bule_history_choose(self,n):##点击历史趋势中的蓝球号码
        for i in range(2,n+2):
            self.find_element(*self.bule_history_choose_loc(i)).click()
            sleep(2)
    #大乐透拖胆玩法，鼠标拖动操作
    # 鼠标向下拖动
    def l_drag_down(self):
        target = self.find_element(*self.l_bottom_element_loc)  # 向下
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 鼠标向上拖动
    def l_drag_up(self):
        target = self.find_element(*self.above_element_loc)  # 向上
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        ########################################大 乐 透 手 选 ，随 机 选 取 红 球 操 作############################################################
        ####从35个红球中随机选取5个红球操作
    def l_red_label5(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取18个红球操作
    def l_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ####从35个红球中随机选取19个红球操作
    def l_red_label19(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        #print(red_label_list)#调试用
        return red_label_list
    ########################################大 乐 透 手 选 ，随 机 选 取 蓝 球 操 作############################################################
    ####大乐透取消选中18个红球操作
    def l_rechoose_red_label18(self):
        red_label_list = []
        for i in random.sample(range(1, 36), 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % red_label).click()
            red_label_list.append(red_label)
        print(red_label_list)
        for i in red_label_list:
            re_red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='redlabel'] i[vrq='%s']" % re_red_label).click()
        print("已取消所选号码")
        return red_label_list
    ###从12个蓝球中选取2个蓝球的操作
    def l_bule_label2(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            bule_label_list.append(bule_label)
        print(bule_label_list)
        return bule_label_list
    ###从12个蓝球中选取12个蓝球的操作


    def l_bule_label12(self):
        bule_label_list = []
        for i in random.sample(range(1, 13), 12):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "label[name='bluelabel'] i[vbq='%s']" % bule_label).click()
            sleep(0.2)
            bule_label_list.append(bule_label)
        #print(bule_label_list)#调试用
        return bule_label_list
##########################################大 乐 透 手 选 胆 拖 玩 法 ， 选 球 操 作##############################################
    #前区选取1个胆码，5个拖码
    def l_red_one_five(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()#随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，2个拖码
    def l_red_four_two(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click() #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取2个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取1个胆码，18个拖码
    def l_red_one_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 1):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  #随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取6个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选取4个胆码，18个拖码
    def l_red_four_eighteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 4):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" %red_label).click()  # 随机选取一个红球胆码
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码,调试用
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取18个球
        self.l_drag_down()  # 鼠标向下拖动
        sleep(5)
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 18):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" %red_label).click()
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
    #前区选5个胆码，19个拖码，获取提示信息文本
    def l_red_five_nineteen(self):
        self.wait_element_located(self.driver, self.DanMa_loc)  # 当胆码选号列表可见时，执行下步操作
        red_dan_label_list = []
        for i in random.sample(range(1, 36), 5):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danredq'] i[vrq='%s']" % red_label).click()  # 随机选取一个红球胆码
            sleep(0.2)
            red_dan_label_list.append(i)
        #print(red_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()  ##红球胆码超过4个提示
        Tuo_Ma = [i for i in range(1, 36) if i not in red_dan_label_list]  # 拖码可选号码
        # 从可选的拖码中选取19个球
        self.l_drag_down()  # 鼠标向下拖动
        self.wait_element_located(self.driver, self.TuoMa_loc)  # 当拖码选号列表可见时，执行下步操作
        red_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 19):
            if len(str(i)) == 1:
                red_label = "0" + str(i)
            else:
                red_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoredq'] i[vrq='%s']" % red_label).click()
            sleep(0.2)
            red_tuo_label_list.append(i)
        #print(red_tuo_label_list)  # 打印所选拖码，调试用
        self.out_of_num()##红球胆码超过18个提示
    ##########大乐透胆拖玩法手选蓝球操作#
    ###后区选择1个胆码，11个拖码
    def l_bule_one_eleven(self):
        self.l_drag_down()
        self.wait_element_located(self.driver,self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" %bule_label).click()  # 随机选取一个红球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 11): # 从可选的拖码中选取11个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" %bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用
    ###后区选择1个胆码，2个拖码
    def l_bule_one_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 1):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取一个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        self.l_drag_down()
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

####选择2个后区胆码，获取提示信息文本
    def l_bule_two_two(self):
        self.l_drag_down()
        self.wait_element_located(self.driver, self.DanTuo_Dan_bule_loc)
        bule_dan_label_list = []
        for i in random.sample(range(1, 13), 2):
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='danblueq'] i[vbq='%s']" % bule_label).click()  # 随机选取两个蓝球胆码
            bule_dan_label_list.append(i)
        #print(bule_dan_label_list)  # 打印可选胆码，调试用
        self.out_of_num()##超出限制提示
        Tuo_Ma = [i for i in range(1, 13) if i not in bule_dan_label_list]  # 拖码可选号码
        self.l_drag_down()
        self.wait_element_located(self.driver, self.Dantuo_Tuo_bule_loc)  # 当拖码选号列表可见时，执行下步操作
        bule_tuo_label_list = []
        for i in random.sample(Tuo_Ma, 2):  # 从可选的拖码中选取2个球
            if len(str(i)) == 1:
                bule_label = "0" + str(i)
            else:
                bule_label = str(i)
            self.find_element(By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='%s']" % bule_label).click()
            bule_tuo_label_list.append(i)
        #print(bule_tuo_label_list)  # 打印所选拖码，调试用

        # 获取选取红球个数超过规则个数时，toast提示信息的文本信息
    def out_of_num(self):
        self.wait_element_located(self.driver, self.out_toast_loc)
        outOfNumtoast = self.find_element(*self.out_toast_loc).text
        sleep(2)
        #print(outOfNumtoast)#调试用
        return outOfNumtoast