from element_position.lemi import CQSSC_ChooseNumber_loc
from element_operate.base import Page
import random
from element_position.lexiu import CQSSC_ChooseNumber_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import CQSSC_ChooseNumber_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import CQSSC_ChooseNumber_lelun_loc
from element_operate.base import Page_lelun
class CQSSC_ChooseNumber(Page,CQSSC_ChooseNumber_loc):
    #点击玩法模式
    def play_mode(self):
        self.wait_element_located(self.driver,self.play_mode_loc)
        self.find_element(*self.play_mode_loc).click()
    #选择点击一星玩法
    def one_star(self):
        self.wait_element_located(self.driver,self.one_star_loc)
        self.find_element(*self.one_star_loc).click()
    #点击二星直选
    def two_star(self):
        self.wait_element_located(self.driver, self.two_star_loc)
        self.find_element(*self.two_star_loc).click()
    #点击三星直选
    def three_star(self):
        self.wait_element_located(self.driver, self.three_star_loc)
        self.find_element(*self.three_star_loc).click()
    #点击五星直选
    def five_star(self):
        self.wait_element_located(self.driver, self.five_star_loc)
        self.find_element(*self.five_star_loc).click()
    #点击大小单双
    def big_little(self):
        self.wait_element_located(self.driver, self.big_or_little_loc)
        self.find_element(*self.big_or_little_loc).click()

    #万位随机选选号
    def wanwei_random(self,num):
        for i in random.sample(range(0,10),num):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print('万位选择:%d'%i)
    #点击万位所有的号码
    def wanwei_all(self):
        for i in range(0,10):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print()
    # 千位随机选选号
    def qianwei_random(self, num):
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(1, i)).click()
            print('千位选择:%d'%i)
    # 点击千位所有的号码
    def qianwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(1, i)).click()
    #点击百位随机选取一个号码
    def baiwei_random(self,num):
        baiwei = ''
        for i in random.sample(range(0,10),num):
            self.find_element(*self.choose_number_loc(2,i)).click()
            print('百位选择：%d'%i)
            baiwei = baiwei + str(i)
        return baiwei
    #点击百位所有号码
    def baiwei_all(self):
        for i in range(0,10):
            self.find_element(*self.choose_number_loc(2,i)).click()
    # 点击十位位随机选取一个号码
    def shiwei_random(self, num):
        shiwei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(3, i)).click()
            print('十位选择：%d' % i)
            shiwei = shiwei + str(i)
        return shiwei
    # 点击十位所有号码
    def shiwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(3, i)).click()
    # 点击个位随机选取一个号码
    def gewei_random(self, num):
        gewei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(4, i)).click()
            print('个位选择：%d' % i)
            gewei =gewei + str(i)
        return gewei
    # 点击个位所有号码
    def gewei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(4, i)).click()
    #大小单双玩法点击随机点击十位的号码
    def ds_shiwei_random(self,num):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(5,i)).click()
            aa = self.find_element(*self.choose_number_loc(5,i)).text
            print('十位选择的是：%s'%aa)
    #大小单双玩法点击十位所有的号码
    def ds_shiwei_all(self):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(5,i)).click()
    #大小单双玩法随机选取个位号码
    def ds_gewei_random(self,num):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(6,i)).click()
            aa = self.find_element(*self.choose_number_loc(6,i)).text
            print('个位选择的是：%s'%aa)
    # 大小单双玩法点击个位所有的号码
    def ds_gewei_all(self):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(6, i)).click()
    def three_star_select(self,baiwei,shiwei,gewei):
        baiwei = self.baiwei_random(baiwei)#百位选号
        shiwei = self.shiwei_random(shiwei)#十位选号
        gewei = self.gewei_random(gewei)#个位选号
        select_num = baiwei+' | ' + shiwei +' | '+ gewei
        return select_num
    def history_trend(self):#点击历史趋势
        self.wait_element_located(self.driver,self.history_trend_loc)
        self.find_element(*self.history_trend_loc).click()

class CQSSC_ChooseNumber_lexiu(Page_lexiu,CQSSC_ChooseNumber_lexiu_loc):
    #点击玩法模式
    def play_mode(self):
        self.wait_element_located(self.driver,self.play_mode_loc)
        self.find_element(*self.play_mode_loc).click()
    #选择点击一星玩法
    def one_star(self):
        self.wait_element_located(self.driver,self.one_star_loc)
        self.find_element(*self.one_star_loc).click()
    #点击二星直选
    def two_star(self):
        self.wait_element_located(self.driver, self.two_star_loc)
        self.find_element(*self.two_star_loc).click()
    #点击三星直选
    def three_star(self):
        self.wait_element_located(self.driver, self.three_star_loc)
        self.find_element(*self.three_star_loc).click()
    #点击五星直选
    def five_star(self):
        self.wait_element_located(self.driver, self.five_star_loc)
        self.find_element(*self.five_star_loc).click()
    #点击大小单双
    def big_little(self):
        self.wait_element_located(self.driver, self.big_or_little_loc)
        self.find_element(*self.big_or_little_loc).click()

    #万位随机选选号
    def wanwei_random(self,num):
        for i in random.sample(range(0,10),num):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print('万位选择:%d'%i)
    #点击万位所有的号码
    def wanwei_all(self):
        for i in range(0,10):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print()
    # 千位随机选选号
    def qianwei_random(self, num):
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(1, i)).click()
            print('千位选择:%d'%i)
    # 点击千位所有的号码
    def qianwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(1, i)).click()
    #点击百位随机选取一个号码
    def baiwei_random(self,num):
        baiwei = ''
        for i in random.sample(range(0,10),num):
            self.find_element(*self.choose_number_loc(2,i)).click()
            print('百位选择：%d'%i)
            baiwei = baiwei + str(i)
        return baiwei
    #点击百位所有号码
    def baiwei_all(self):
        for i in range(0,10):
            self.find_element(*self.choose_number_loc(2,i)).click()
    # 点击十位位随机选取一个号码
    def shiwei_random(self, num):
        shiwei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(3, i)).click()
            print('十位选择：%d' % i)
            shiwei = shiwei + str(i)
        return shiwei
    # 点击十位所有号码
    def shiwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(3, i)).click()
    # 点击个位随机选取一个号码
    def gewei_random(self, num):
        gewei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(4, i)).click()
            print('个位选择：%d' % i)
            gewei =gewei + str(i)
        return gewei
    # 点击个位所有号码
    def gewei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(4, i)).click()
    #大小单双玩法点击随机点击十位的号码
    def ds_shiwei_random(self,num):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(5,i)).click()
            aa = self.find_element(*self.choose_number_loc(5,i)).text
            print('十位选择的是：%s'%aa)
    #大小单双玩法点击十位所有的号码
    def ds_shiwei_all(self):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(5,i)).click()
    #大小单双玩法随机选取个位号码
    def ds_gewei_random(self,num):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(6,i)).click()
            aa = self.find_element(*self.choose_number_loc(6,i)).text
            print('个位选择的是：%s'%aa)
    # 大小单双玩法点击个位所有的号码
    def ds_gewei_all(self):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(6, i)).click()
    def three_star_select(self,baiwei,shiwei,gewei):
        baiwei = self.baiwei_random(baiwei)#百位选号
        shiwei = self.shiwei_random(shiwei)#十位选号
        gewei = self.gewei_random(gewei)#个位选号
        select_num = baiwei+' | ' + shiwei +' | '+ gewei
        return select_num
    def history_trend(self):#点击历史趋势
        self.wait_element_located(self.driver,self.history_trend_loc)
        self.find_element(*self.history_trend_loc).click()

class CQSSC_ChooseNumber_leyou(Page_leyou,CQSSC_ChooseNumber_leyou_loc):
    #点击玩法模式
    def play_mode(self):
        self.wait_element_located(self.driver,self.play_mode_loc)
        self.find_element(*self.play_mode_loc).click()
    #选择点击一星玩法
    def one_star(self):
        self.wait_element_located(self.driver,self.one_star_loc)
        self.find_element(*self.one_star_loc).click()
    #点击二星直选
    def two_star(self):
        self.wait_element_located(self.driver, self.two_star_loc)
        self.find_element(*self.two_star_loc).click()
    #点击三星直选
    def three_star(self):
        self.wait_element_located(self.driver, self.three_star_loc)
        self.find_element(*self.three_star_loc).click()
    #点击五星直选
    def five_star(self):
        self.wait_element_located(self.driver, self.five_star_loc)
        self.find_element(*self.five_star_loc).click()
    #点击大小单双
    def big_little(self):
        self.wait_element_located(self.driver, self.big_or_little_loc)
        self.find_element(*self.big_or_little_loc).click()

    #万位随机选选号
    def wanwei_random(self,num):
        for i in random.sample(range(0,10),num):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print('万位选择:%d'%i)
    #点击万位所有的号码
    def wanwei_all(self):
        for i in range(0,10):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print()
    # 千位随机选选号
    def qianwei_random(self, num):
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(1, i)).click()
            print('千位选择:%d'%i)
    # 点击千位所有的号码
    def qianwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(1, i)).click()
    #点击百位随机选取一个号码
    def baiwei_random(self,num):
        baiwei = ''
        for i in random.sample(range(0,10),num):
            self.find_element(*self.choose_number_loc(2,i)).click()
            print('百位选择：%d'%i)
            baiwei = baiwei + str(i)
        return baiwei
    #点击百位所有号码
    def baiwei_all(self):
        for i in range(0,10):
            self.find_element(*self.choose_number_loc(2,i)).click()
    # 点击十位位随机选取一个号码
    def shiwei_random(self, num):
        shiwei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(3, i)).click()
            print('十位选择：%d' % i)
            shiwei = shiwei + str(i)
        return shiwei
    # 点击十位所有号码
    def shiwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(3, i)).click()
    # 点击个位随机选取一个号码
    def gewei_random(self, num):
        gewei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(4, i)).click()
            print('个位选择：%d' % i)
            gewei =gewei + str(i)
        return gewei
    # 点击个位所有号码
    def gewei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(4, i)).click()
    #大小单双玩法点击随机点击十位的号码
    def ds_shiwei_random(self,num):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(5,i)).click()
            aa = self.find_element(*self.choose_number_loc(5,i)).text
            print('十位选择的是：%s'%aa)
    #大小单双玩法点击十位所有的号码
    def ds_shiwei_all(self):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(5,i)).click()
    #大小单双玩法随机选取个位号码
    def ds_gewei_random(self,num):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(6,i)).click()
            aa = self.find_element(*self.choose_number_loc(6,i)).text
            print('个位选择的是：%s'%aa)
    # 大小单双玩法点击个位所有的号码
    def ds_gewei_all(self):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(6, i)).click()
    def three_star_select(self,baiwei,shiwei,gewei):
        baiwei = self.baiwei_random(baiwei)#百位选号
        shiwei = self.shiwei_random(shiwei)#十位选号
        gewei = self.gewei_random(gewei)#个位选号
        select_num = baiwei+' | ' + shiwei +' | '+ gewei
        return select_num
    def history_trend(self):#点击历史趋势
        self.wait_element_located(self.driver,self.history_trend_loc)
        self.find_element(*self.history_trend_loc).click()

class CQSSC_ChooseNumber_lelun(Page_lelun,CQSSC_ChooseNumber_lelun_loc):
    #点击玩法模式
    def play_mode(self):
        self.wait_element_located(self.driver,self.play_mode_loc)
        self.find_element(*self.play_mode_loc).click()
    #选择点击一星玩法
    def one_star(self):
        self.wait_element_located(self.driver,self.one_star_loc)
        self.find_element(*self.one_star_loc).click()
    #点击二星直选
    def two_star(self):
        self.wait_element_located(self.driver, self.two_star_loc)
        self.find_element(*self.two_star_loc).click()
    #点击三星直选
    def three_star(self):
        self.wait_element_located(self.driver, self.three_star_loc)
        self.find_element(*self.three_star_loc).click()
    #点击五星直选
    def five_star(self):
        self.wait_element_located(self.driver, self.five_star_loc)
        self.find_element(*self.five_star_loc).click()
    #点击大小单双
    def big_little(self):
        self.wait_element_located(self.driver, self.big_or_little_loc)
        self.find_element(*self.big_or_little_loc).click()

    #万位随机选选号
    def wanwei_random(self,num):
        for i in random.sample(range(0,10),num):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print('万位选择:%d'%i)
    #点击万位所有的号码
    def wanwei_all(self):
        for i in range(0,10):
            self.find_element(*self.wanwei_choose_number_loc(i)).click()
            print()
    # 千位随机选选号
    def qianwei_random(self, num):
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(1, i)).click()
            print('千位选择:%d'%i)
    # 点击千位所有的号码
    def qianwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(1, i)).click()
    #点击百位随机选取一个号码
    def baiwei_random(self,num):
        baiwei = ''
        for i in random.sample(range(0,10),num):
            self.find_element(*self.choose_number_loc(2,i)).click()
            print('百位选择：%d'%i)
            baiwei = baiwei + str(i)
        return baiwei
    #点击百位所有号码
    def baiwei_all(self):
        for i in range(0,10):
            self.find_element(*self.choose_number_loc(2,i)).click()
    # 点击十位位随机选取一个号码
    def shiwei_random(self, num):
        shiwei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(3, i)).click()
            print('十位选择：%d' % i)
            shiwei = shiwei + str(i)
        return shiwei
    # 点击十位所有号码
    def shiwei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(3, i)).click()
    # 点击个位随机选取一个号码
    def gewei_random(self, num):
        gewei = ''
        for i in random.sample(range(0, 10), num):
            self.find_element(*self.choose_number_loc(4, i)).click()
            print('个位选择：%d' % i)
            gewei =gewei + str(i)
        return gewei
    # 点击个位所有号码
    def gewei_all(self):
        for i in range(0, 10):
            self.find_element(*self.choose_number_loc(4, i)).click()
    #大小单双玩法点击随机点击十位的号码
    def ds_shiwei_random(self,num):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(5,i)).click()
            aa = self.find_element(*self.choose_number_loc(5,i)).text
            print('十位选择的是：%s'%aa)
    #大小单双玩法点击十位所有的号码
    def ds_shiwei_all(self):
        num_list = [9,0,1,2]#大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(5,i)).click()
    #大小单双玩法随机选取个位号码
    def ds_gewei_random(self,num):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in random.sample(num_list,num):
            self.find_element(*self.choose_number_loc(6,i)).click()
            aa = self.find_element(*self.choose_number_loc(6,i)).text
            print('个位选择的是：%s'%aa)
    # 大小单双玩法点击个位所有的号码
    def ds_gewei_all(self):
        num_list = [9, 0, 1, 2]  # 大小单双的定位参数
        for i in num_list:
            self.find_element(*self.choose_number_loc(6, i)).click()
    def three_star_select(self,baiwei,shiwei,gewei):
        baiwei = self.baiwei_random(baiwei)#百位选号
        shiwei = self.shiwei_random(shiwei)#十位选号
        gewei = self.gewei_random(gewei)#个位选号
        select_num = baiwei+' | ' + shiwei +' | '+ gewei
        return select_num
    def history_trend(self):#点击历史趋势
        self.wait_element_located(self.driver,self.history_trend_loc)
        self.find_element(*self.history_trend_loc).click()
