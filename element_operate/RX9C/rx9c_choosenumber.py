from element_position.lemi import RX9C_choosenumber_loc
from element_operate.base import Page
import random
from time import sleep
from element_position.lexiu import RX9C_choosenumber_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import RX9C_choosenumber_leyou_loc
from element_operate.base import Page_lexiu
from element_position.lelun import RX9C_choosenumber_lelun_loc
from element_operate.base import Page_lelun
class RX9C_choosenumber(Page,RX9C_choosenumber_loc):
    def Games_nu(self):###选择全部的赛事结果
        list=[0,1,3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in range(len(a)):
                if i>1:
                    target = self.find_element(*self.games_vs(i-1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                for j in list:
                    self.find_element(*self.games_result(i,j)).click()
            return 1


    def rx9c_top(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Games_nus(self,n,q):###选择7场赛事对应的一个赛事结果
        list = [0, 1, 3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in random.sample(range(len(a)),n):
                if i>1:
                    target = self.find_element(*self.games_vs(i - 1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                else:
                    self.rx9c_top()
                for j in random.sample(list,q):
                    self.find_element(*self.games_result(i,j)).click()
            return 1

    def Clear(self):
        self.find_element(*self.clear).click()###

    def Confirm_pick(self):
        self.find_element(*self.confirm_pick).click()###点击确认选号

    def Rx9c_play(self):
        a=self.find_element(*self.rx9c_play).text###读取任选9长文本
        return a

    def Term(self):
        self.find_element(*self.term).click()##点击期数

    def Term_t(self):
        sleep(1)
        a=self.find_element(*self.term).text##读取显示期数文本
        return a

    def Term_next(self):
        a=self.find_elements(*self.term_all)
        if len(a)==0:
            print('只有一期赛事')
            return 0
        else:
            for i in range(1,len(a)+1):
                b=a[i].text
                a[i].click()
                return b

    def Cont_choose(self):
        self.find_element(*self.cont_choose).click()###点击继续选号

class RX9C_choosenumber_lexiu(Page_lexiu,RX9C_choosenumber_lexiu_loc):
    def Games_nu(self):###选择全部的赛事结果
        list=[0,1,3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in range(len(a)):
                if i>1:
                    target = self.find_element(*self.games_vs(i-1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                for j in list:
                    self.find_element(*self.games_result(i,j)).click()
            return 1


    def rx9c_top(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Games_nus(self,n,q):###选择7场赛事对应的一个赛事结果
        list = [0, 1, 3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in random.sample(range(len(a)),n):
                if i>1:
                    target = self.find_element(*self.games_vs(i - 1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                else:
                    self.rx9c_top()
                for j in random.sample(list,q):
                    self.find_element(*self.games_result(i,j)).click()
            return 1

    def Clear(self):
        self.find_element(*self.clear).click()###

    def Confirm_pick(self):
        self.find_element(*self.confirm_pick).click()###点击确认选号

    def Rx9c_play(self):
        a=self.find_element(*self.rx9c_play).text###读取任选9长文本
        return a

    def Term(self):
        self.find_element(*self.term).click()##点击期数

    def Term_t(self):
        sleep(1)
        a=self.find_element(*self.term).text##读取显示期数文本
        return a

    def Term_next(self):
        a=self.find_elements(*self.term_all)
        if len(a)==0:
            print('只有一期赛事')
            return 0
        else:
            for i in range(1,len(a)+1):
                b=a[i].text
                a[i].click()
                return b

    def Cont_choose(self):
        self.find_element(*self.cont_choose).click()###点击继续选号

class RX9C_choosenumber_leyou(Page_leyou,RX9C_choosenumber_leyou_loc):
    def Games_nu(self):###选择全部的赛事结果
        list=[0,1,3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in range(len(a)):
                if i>1:
                    target = self.find_element(*self.games_vs(i-1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                for j in list:
                    self.find_element(*self.games_result(i,j)).click()
            return 1


    def rx9c_top(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Games_nus(self,n,q):###选择7场赛事对应的一个赛事结果
        list = [0, 1, 3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in random.sample(range(len(a)),n):
                if i>1:
                    target = self.find_element(*self.games_vs(i - 1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                else:
                    self.rx9c_top()
                for j in random.sample(list,q):
                    self.find_element(*self.games_result(i,j)).click()
            return 1

    def Clear(self):
        self.find_element(*self.clear).click()###

    def Confirm_pick(self):
        self.find_element(*self.confirm_pick).click()###点击确认选号

    def Rx9c_play(self):
        a=self.find_element(*self.rx9c_play).text###读取任选9长文本
        return a

    def Term(self):
        self.find_element(*self.term).click()##点击期数

    def Term_t(self):
        sleep(1)
        a=self.find_element(*self.term).text##读取显示期数文本
        return a

    def Term_next(self):
        a=self.find_elements(*self.term_all)
        if len(a)==0:
            print('只有一期赛事')
            return 0
        else:
            for i in range(1,len(a)+1):
                b=a[i].text
                a[i].click()
                return b

    def Cont_choose(self):
        self.find_element(*self.cont_choose).click()###点击继续选号

class RX9C_choosenumber_lelun(Page_lelun,RX9C_choosenumber_lelun_loc):
    def Games_nu(self):###选择全部的赛事结果
        list=[0,1,3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in range(len(a)):
                if i>1:
                    target = self.find_element(*self.games_vs(i-1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                for j in list:
                    self.find_element(*self.games_result(i,j)).click()
            return 1


    def rx9c_top(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Games_nus(self,n,q):###选择7场赛事对应的一个赛事结果
        list = [0, 1, 3]
        a=self.find_elements(*self.games_nu)###读取赛事场次数量
        if len(a)>0:
            self.rx9c_top()
            for i in random.sample(range(len(a)),n):
                if i>1:
                    target = self.find_element(*self.games_vs(i - 1))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                else:
                    self.rx9c_top()
                for j in random.sample(list,q):
                    self.find_element(*self.games_result(i,j)).click()
            return 1

    def Clear(self):
        self.find_element(*self.clear).click()###

    def Confirm_pick(self):
        self.find_element(*self.confirm_pick).click()###点击确认选号

    def Rx9c_play(self):
        a=self.find_element(*self.rx9c_play).text###读取任选9长文本
        return a

    def Term(self):
        self.find_element(*self.term).click()##点击期数

    def Term_t(self):
        sleep(1)
        a=self.find_element(*self.term).text##读取显示期数文本
        return a

    def Term_next(self):
        a=self.find_elements(*self.term_all)
        if len(a)==0:
            print('只有一期赛事')
            return 0
        else:
            for i in range(1,len(a)+1):
                b=a[i].text
                a[i].click()
                return b

    def Cont_choose(self):
        self.find_element(*self.cont_choose).click()###点击继续选号
