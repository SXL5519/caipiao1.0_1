from element_operate.base import Page
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_position.lemi import UChooseNum_loc
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from selenium.webdriver.common.by import By
from time import sleep
import time
import random
from element_position.lemi import SingleFootChooseNumber_loc
from element_position.lemi import HaobcChooseNumber_loc
from element_position.lexiu import SingleFootChooseNumber_lexiu_loc
from element_position.lexiu import HaobcChooseNumber_lexiu_loc
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lexiu
from element_position.leyou import SingleFootChooseNumber_leyou_loc
from element_position.leyou import HaobcChooseNumber_leyou_loc
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_leyou
from element_position.lelun import SingleFootChooseNumber_lelun_loc
from element_position.lelun import HaobcChooseNumber_lelun_loc
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lelun


class SingleFootChooseNumber(PaintBallChooseNumber,SingleFootChooseNumber_loc,HaobcChooseNumber_loc):
    def Play_dgp(self):#点击单关配模式
        self.wait_element_located(self.driver,self.dgp_lottery_loc)
        self.find_element(*self.dgp_lottery_loc).click()

    def Play_dgp_text(self):#获取单关配页面的单关配的文字
        self.wait_element_located(self.driver,self.dgp_text_loc)
        text=self.find_element(*self.dgp_text_loc).text
        return text
#############竞足单关，胜平负玩法选号页面的元素操作#############
    def jzdg_spf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(1, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_spf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_spf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.spf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    def jzdg_spf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞彩足球点击编辑赛事，对应的选号方法
    def jzdg_spf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
##############竞足单关，让球胜平负玩法选号页面的元素操作
    def jzdg_rqspf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(2, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_rqspf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_rqspf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.rqspf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0

    def jzdg_rqspf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #竞彩足球点击所有编辑赛事，对应的选号方法
    def jzdg_rqspf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
####################竞足单关，2x1玩法选号页面元素操作###########################
    def jzdg_two_choose_one_choose_means(self, num, time, n, number=0):
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                event_list.append(i)
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def jzdg_two_choose_one_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in event_time:
                print("wo shi zui bang de ")
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.two_choose_one_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
    def jzdg_two_choose_one_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_edit_event(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Text_nu_pbs(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list

        # 获取有多少天赛事的list

    def Event_time_pbs(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def This_open_pbs(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def top_more_pbs(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Session_2(self, n):
        self.top_more_pbs()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def pull_down(self):
        target = self.find_element(*self.cdxf_icon(1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Confirm_more(self):
        self.find_element(*self.confirm_more_pbs).click()  #####点击展开更多页面的确定

    def Confirm_more_sfc(self):
        self.find_element(*self.confirm_more_sfc).click()  #####点击展开更多页面的确定

    def choosenumber_pas(self):  ####竞足单关展开更多页面显示赛事结果
        list = []
        #self.wait_element_located(self.driver, self.more_pbs)
        nn = self.find_elements(*self.more_pbs)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '9002':
                    self.Cjqs_pbs()
                elif list[j] == '9003':
                    self.Cbf_pbs()
                elif list[j] == '9004':
                    self.Cbqc_pbs()
                elif list[j]=='9005':
                    self.Cspf_pbs()
                elif list[j]=='10003':
                    self.Csfc_jzdg()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Cspf_pbs(self):
        list5=['1','0','3']
        for n in list5:
            target = self.find_element(*self.cspf_pbs_icon(1))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            self.find_element(*self.cspf_pbs_icon(n)).click()###点击胜平负

    def Cjqs_pbs(self):
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7']
        for n in list1:
            self.find_element(*self.cjqs_pbs_icon(n)).click()  # 点击胜平负/

    def Cbf_pbs(self):
        list2 = ['10', '20', '21', '30', '31', '32', '40', '41', '42', '50', '51', '52', '90', '00', '11', '22',
                 '33',
                 '99', '01', '02', '12', '03', '13', '23', '04', '14', '24', '05', '15', '25', '09']
        for n in list2:
            self.find_element(*self.cbf_pbs_icon(n)).click()  ##点击比分

    def Cbqc_pbs(self):
        list3 = ['30', '31', '33', '13', '11', '10', '03', '01', '00']
        for n in list3:
            self.find_element(*self.cbqc_pbs_icon(n)).click()  ##点击猜半全场

    def Csfc_jzdg(self):
        list4=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list4:
            self.find_elements(*self.csfc_jczq_icon(n)).clcik()##点胜分差

    def Paintball_single_mix(self):  ###点击混合玩法显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_mix(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_mixs(self, q):  ###随机点击混合玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        print("第%d天，第%d场赛事" %((i+1),n))
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_mix_nus_X(self,x):##点击混合玩法X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_mix(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Emptying_pbs(self):
        self.find_element(*self.emptying_pbs).click()###点击清空按钮

    def Paintball_single_bf(self):##点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bf(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bfs(self, q):  ###随机点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bf_nus_X(self,x):##选择比分玩法X场赛事结果
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                if n>1:
                                    target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bf(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_zjq(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    if i > 0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(1, 9):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-4
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    c=c-4
                                    self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS_pbs(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus(self, q):  ###随机点击总进球玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if n == 1:
                                self.top_more()  ###鼠标拉到顶部
                                c = random.randint(1, 4)  ###随机取C的值
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus_X(self,x):###点击总进球玩法X场比赛
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            self.top_more()
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                self.know()
                                print("第%d场，成功点击知道了"%n)
                                q = q + 1
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    c = random.randint(1, 4)  ###随机取C的值
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q=q+1
                                    print(q)
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    c = random.randint(1, 4)
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqc(self):  ###点击半全场显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqcs(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bqc_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bqc(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def Dgp_tan(self):
        self.find_element(*self.dgp_tan()).click()####点击单关配选号页弹框

    def Paintball_single_dgp(self):###选择单关配玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    self.top_more()
                    self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 8):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-3
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                        target = self.find_element(*self.VS_dgp(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def VSS_dgp(self,a):
        list=[]
        q=self.find_elements(*self.VSS(a))
        for i in range(len(q)):
            z=q[i].get_attribute('data-match')
            list.append(z)
        print(list)
        return list

    def Dgp_vs(self):
        na = self.Event_time_pbs()
        i=random.sample(len(na),1)
        a=na[i]
        self.VSS_dgp(a)

    def Paintball_single_dgps(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                if z>0:
                    self.Know_dgp()
                    print('成功点击提示信息“单关配只能选择一场赛事”')
                else:
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            if n == 1:
                                self.top_more_pbs()  ###鼠标拉到顶部
                                print('第%d天第%d场赛事' %(i+1,n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.Session_2(i + 1)
                            else:
                                js = "var q=document.body.scrollTop=10000"
                                self.driver.execute_script(js)
                                #self.wait_element_located(self.driver, self.VS_dgp(a, n-1))
                                target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                print('第%d天第%d场赛事' % (i + 1, n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.top_more_pbs()
                                self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2

    def Paintball_single_dgpss(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            print('第%d天第%d场赛事' %(i+1,n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            print('第%d天第%d场赛事' % (i + 1, n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2


    def Know_dgp(self):
        self.find_element(*self.know_dgp).click()###点击我知道了

    def Paintball_single_dgp_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q < x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>0:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                            else:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                                time.sleep(1)
                                self.Session_2(i + 1)
                        else:
                            break
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def jzdg_play_instruct(self):##竞足单关点击玩法说明--mj20171215
        self.wait_element_located(self.driver,self.jzdg_play_instruct_loc)
        self.find_element(*self.jzdg_play_instruct_loc).click()

class SingleFootChooseNumber_lexiu(PaintBallChooseNumber_lexiu,SingleFootChooseNumber_lexiu_loc,HaobcChooseNumber_lexiu_loc):
    def Play_dgp(self):#点击单关配模式
        self.wait_element_located(self.driver,self.dgp_lottery_loc)
        self.find_element(*self.dgp_lottery_loc).click()

    def Play_dgp_text(self):#获取单关配页面的单关配的文字
        self.wait_element_located(self.driver,self.dgp_text_loc)
        text=self.find_element(*self.dgp_text_loc).text
        return text
#############竞足单关，胜平负玩法选号页面的元素操作#############
    def jzdg_spf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(1, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_spf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(1)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_spf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.spf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            print("暂无赛事，前往单关配")
            return 0
    def jzdg_spf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞彩足球点击编辑赛事，对应的选号方法
    def jzdg_spf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
##############竞足单关，让球胜平负玩法选号页面的元素操作
    def jzdg_rqspf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(2, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_rqspf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_rqspf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.rqspf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0

    def jzdg_rqspf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #竞彩足球点击所有编辑赛事，对应的选号方法
    def jzdg_rqspf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
####################竞足单关，2x1玩法选号页面元素操作###########################
    def jzdg_two_choose_one_choose_means(self, num, time, n, number=0):
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                event_list.append(i)
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def jzdg_two_choose_one_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in event_time:
                print("wo shi zui bang de ")
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.two_choose_one_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
    def jzdg_two_choose_one_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_edit_event(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Text_nu_pbs(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[:-1])
            list.append(nnu)
        print(list)
        return list

        # 获取有多少天赛事的list

    def Event_time_pbs(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def This_open_pbs(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def top_more_pbs(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Session_2(self, n):
        self.top_more_pbs()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def pull_down(self):
        target = self.find_element(*self.cdxf_icon(1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Confirm_more(self):
        self.find_element(*self.confirm_more_pbs).click()  #####点击展开更多页面的确定

    def Confirm_more_sfc(self):
        self.find_element(*self.confirm_more_sfc).click()  #####点击展开更多页面的确定

    def choosenumber_pas(self):  ####竞足单关展开更多页面显示赛事结果
        list = []
        #self.wait_element_located(self.driver, self.more_pbs)
        nn = self.find_elements(*self.more_pbs)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '9002':
                    self.Cjqs_pbs()
                elif list[j] == '9003':
                    self.Cbf_pbs()
                elif list[j] == '9004':
                    self.Cbqc_pbs()
                elif list[j]=='9005':
                    self.Cspf_pbs()
                elif list[j]=='10003':
                    self.Csfc_jzdg()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def choosenumber_pasa(self):  ####竞足单关展开更多页面显示赛事结果
        list = []
        #self.wait_element_located(self.driver, self.more_pbs)
        nn = self.find_elements(*self.more_pbs)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in random.sample(range(len(list)),1):
                if list[j] == '9002':
                    self.Cjqs_pbsx()
                elif list[j] == '9003':
                    self.Cbf_pbsx()
                elif list[j] == '9004':
                    self.Cbqc_pbsx()
                elif list[j]=='9005':
                    self.Cspf_pbsx()
                elif list[j]=='10003':
                    self.Csfc_jzdgx()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Cspf_pbs(self):
        list5=['1','0','3']
        for n in list5:
            target = self.find_element(*self.cspf_pbs_icon(1))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            self.find_element(*self.cspf_pbs_icon(n)).click()###点击胜平负

    def Cspf_pbsx(self):
        list5=['1','0','3']
        for n in random.sample(list5,1):
            target = self.find_element(*self.cspf_pbs_icon(1))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            self.find_element(*self.cspf_pbs_icon(n)).click()###点击胜平负

    def Cjqs_pbs(self):
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7']
        for n in list1:
            self.find_element(*self.cjqs_pbs_icon(n)).click()  # 点击胜平负/

    def Cjqs_pbsx(self):
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7']
        for n in random.sample(list1,1):
            self.find_element(*self.cjqs_pbs_icon(n)).click()  # 点击胜平负/

    def Cbf_pbs(self):
        list2 = ['10', '20', '21', '30', '31', '32', '40', '41', '42', '50', '51', '52', '90', '00', '11', '22',
                 '33',
                 '99', '01', '02', '12', '03', '13', '23', '04', '14', '24', '05', '15', '25', '09']
        for n in list2:
            self.find_element(*self.cbf_pbs_icon(n)).click()  ##点击比分

    def Cbf_pbsx(self):
        list2 = ['10', '20', '21', '30', '31', '32', '40', '41', '42', '50', '51', '52', '90', '00', '11', '22',
                 '33',
                 '99', '01', '02', '12', '03', '13', '23', '04', '14', '24', '05', '15', '25', '09']
        for n in random.sample(list2,1):
            self.find_element(*self.cbf_pbs_icon(n)).click()  ##点击比分

    def Cbqc_pbs(self):
        list3 = ['30', '31', '33', '13', '11', '10', '03', '01', '00']
        for n in list3:
            self.find_element(*self.cbqc_pbs_icon(n)).click()  ##点击猜半全场

    def Cbqc_pbsx(self):
        list3 = ['30', '31', '33', '13', '11', '10', '03', '01', '00']
        for n in random.sample(list3,1):
            self.find_element(*self.cbqc_pbs_icon(n)).click()  ##点击猜半全场

    def Csfc_jzdg(self):
        list4=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list4:
            self.find_elements(*self.csfc_jczq_icon(n)).clcik()##点胜分差

    def Csfc_jzdgx(self):
        list4=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in random.sample(list4,1):
            self.find_elements(*self.csfc_jczq_icon(n)).clcik()##点胜分差

    def Paintball_single_mix(self):  ###点击混合玩法显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_mix(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_mixs(self, q):  ###随机点击混合玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        print("第%d天，第%d场赛事" %((i+1),n))
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2


    def Paintball_single_mix_nus_X(self,x):##点击混合玩法X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_mix(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_mix_nus_a(self,x):##点击混合玩法X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_mix(a, n)).click()
                                self.choosenumber_pasa()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pasa()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pasa()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Emptying_pbs(self):
        self.find_element(*self.emptying_pbs).click()###点击清空按钮

    def Paintball_single_bf(self):##点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bf(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bfs(self, q):  ###随机点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bf_nus_X(self,x):##选择比分玩法X场赛事结果
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                if n>1:
                                    target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bf(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_zjq(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    if i > 0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(1, 9):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-4
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    c=c-4
                                    self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS_pbs(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus(self, q):  ###随机点击总进球玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if n == 1:
                                self.top_more()  ###鼠标拉到顶部
                                c = random.randint(1, 4)  ###随机取C的值
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus_X(self,x):###点击总进球玩法X场比赛
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            self.top_more()
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                self.know()
                                print("第%d场，成功点击知道了"%n)
                                q = q + 1
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    c = random.randint(1, 4)  ###随机取C的值
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q=q+1
                                    print(q)
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    c = random.randint(1, 4)
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqc(self):  ###点击半全场显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqcs(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bqc_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bqc(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def Dgp_tan(self):
        self.find_element(*self.dgp_tan()).click()####点击单关配选号页弹框

    def Paintball_single_dgp(self):###选择单关配玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    self.top_more()
                    self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 8):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-3
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                        target = self.find_element(*self.VS_dgp(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def VSS_dgp(self,a):
        list=[]
        q=self.find_elements(*self.VSS(a))
        for i in range(len(q)):
            z=q[i].get_attribute('data-match')
            list.append(z)
        print(list)
        return list

    def Dgp_vs(self):
        na = self.Event_time_pbs()
        i=random.sample(len(na),1)
        a=na[i]
        self.VSS_dgp(a)

    def Paintball_single_dgps(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                if z>0:
                    self.Know_dgp()
                    print('成功点击提示信息“单关配只能选择一场赛事”')
                else:
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            if n == 1:
                                self.top_more_pbs()  ###鼠标拉到顶部
                                print('第%d天第%d场赛事' %(i+1,n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.Session_2(i + 1)
                            else:
                                js = "var q=document.body.scrollTop=10000"
                                self.driver.execute_script(js)
                                #self.wait_element_located(self.driver, self.VS_dgp(a, n-1))
                                target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                print('第%d天第%d场赛事' % (i + 1, n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.top_more_pbs()
                                self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2

    def Paintball_single_dgpss(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            print('第%d天第%d场赛事' %(i+1,n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            print('第%d天第%d场赛事' % (i + 1, n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2


    def Know_dgp(self):
        self.find_element(*self.know_dgp).click()###点击我知道了

    def Paintball_single_dgp_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q < x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>0:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                            else:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                                time.sleep(1)
                                self.Session_2(i + 1)
                        else:
                            break
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def jzdg_play_instruct(self):##竞足单关点击玩法说明--mj20171215
        self.wait_element_located(self.driver,self.jzdg_play_instruct_loc)
        self.find_element(*self.jzdg_play_instruct_loc).click()

class SingleFootChooseNumber_leyou(PaintBallChooseNumber_leyou,SingleFootChooseNumber_leyou_loc,HaobcChooseNumber_leyou_loc):
    def Play_dgp(self):#点击单关配模式
        self.wait_element_located(self.driver,self.dgp_lottery_loc)
        self.find_element(*self.dgp_lottery_loc).click()

    def Play_dgp_text(self):#获取单关配页面的单关配的文字
        self.wait_element_located(self.driver,self.dgp_text_loc)
        text=self.find_element(*self.dgp_text_loc).text
        return text
#############竞足单关，胜平负玩法选号页面的元素操作#############
    def jzdg_spf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(1, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_spf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(1)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_spf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.spf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    def jzdg_spf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞彩足球点击编辑赛事，对应的选号方法
    def jzdg_spf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
##############竞足单关，让球胜平负玩法选号页面的元素操作
    def jzdg_rqspf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(2, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_rqspf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_rqspf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.rqspf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0

    def jzdg_rqspf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #竞彩足球点击所有编辑赛事，对应的选号方法
    def jzdg_rqspf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
####################竞足单关，2x1玩法选号页面元素操作###########################
    def jzdg_two_choose_one_choose_means(self, num, time, n, number=0):
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                event_list.append(i)
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def jzdg_two_choose_one_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in event_time:
                print("wo shi zui bang de ")
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.two_choose_one_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
    def jzdg_two_choose_one_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_edit_event(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Text_nu_pbs(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list

        # 获取有多少天赛事的list

    def Event_time_pbs(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def This_open_pbs(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def top_more_pbs(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Session_2(self, n):
        self.top_more_pbs()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def pull_down(self):
        target = self.find_element(*self.cdxf_icon(1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Confirm_more(self):
        self.find_element(*self.confirm_more_pbs).click()  #####点击展开更多页面的确定

    def Confirm_more_sfc(self):
        self.find_element(*self.confirm_more_sfc).click()  #####点击展开更多页面的确定

    def choosenumber_pas(self):  ####竞足单关展开更多页面显示赛事结果
        list = []
        #self.wait_element_located(self.driver, self.more_pbs)
        nn = self.find_elements(*self.more_pbs)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '9002':
                    self.Cjqs_pbs()
                elif list[j] == '9003':
                    self.Cbf_pbs()
                elif list[j] == '9004':
                    self.Cbqc_pbs()
                elif list[j]=='9005':
                    self.Cspf_pbs()
                elif list[j]=='10003':
                    self.Csfc_jzdg()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def choosenumber_pasa(self):  ####竞足单关展开更多页面显示赛事结果
        list = []
        #self.wait_element_located(self.driver, self.more_pbs)
        nn = self.find_elements(*self.more_pbs)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in random.sample(range(len(list)),1):
                if list[j] == '9002':
                    self.Cjqs_pbsx()
                elif list[j] == '9003':
                    self.Cbf_pbsx()
                elif list[j] == '9004':
                    self.Cbqc_pbsx()
                elif list[j]=='9005':
                    self.Cspf_pbsx()
                elif list[j]=='10003':
                    self.Csfc_jzdgx()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Cspf_pbs(self):
        list5=['1','0','3']
        for n in list5:
            target = self.find_element(*self.cspf_pbs_icon(1))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            self.find_element(*self.cspf_pbs_icon(n)).click()###点击胜平负

    def Cspf_pbsx(self):
        list5=['1','0','3']
        for n in random.sample(list5,1):
            target = self.find_element(*self.cspf_pbs_icon(1))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            self.find_element(*self.cspf_pbs_icon(n)).click()###点击胜平负

    def Cjqs_pbs(self):
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7']
        for n in list1:
            self.find_element(*self.cjqs_pbs_icon(n)).click()  # 点击胜平负/

    def Cjqs_pbsx(self):
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7']
        for n in random.sample(list1,1):
            self.find_element(*self.cjqs_pbs_icon(n)).click()  # 点击胜平负/

    def Cbf_pbs(self):
        list2 = ['10', '20', '21', '30', '31', '32', '40', '41', '42', '50', '51', '52', '90', '00', '11', '22',
                 '33',
                 '99', '01', '02', '12', '03', '13', '23', '04', '14', '24', '05', '15', '25', '09']
        for n in list2:
            self.find_element(*self.cbf_pbs_icon(n)).click()  ##点击比分

    def Cbf_pbsx(self):
        list2 = ['10', '20', '21', '30', '31', '32', '40', '41', '42', '50', '51', '52', '90', '00', '11', '22',
                 '33',
                 '99', '01', '02', '12', '03', '13', '23', '04', '14', '24', '05', '15', '25', '09']
        for n in random.sample(list2,1):
            self.find_element(*self.cbf_pbs_icon(n)).click()  ##点击比分

    def Cbqc_pbs(self):
        list3 = ['30', '31', '33', '13', '11', '10', '03', '01', '00']
        for n in list3:
            self.find_element(*self.cbqc_pbs_icon(n)).click()  ##点击猜半全场

    def Cbqc_pbsx(self):
        list3 = ['30', '31', '33', '13', '11', '10', '03', '01', '00']
        for n in random.sample(list3,1):
            self.find_element(*self.cbqc_pbs_icon(n)).click()  ##点击猜半全场

    def Csfc_jzdg(self):
        list4=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list4:
            self.find_elements(*self.csfc_jczq_icon(n)).clcik()##点胜分差

    def Csfc_jzdgx(self):
        list4=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in random.sample(list4,1):
            self.find_elements(*self.csfc_jczq_icon(n)).clcik()##点胜分差

    def Paintball_single_mix(self):  ###点击混合玩法显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_mix(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_mixs(self, q):  ###随机点击混合玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        print("第%d天，第%d场赛事" %((i+1),n))
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2


    def Paintball_single_mix_nus_X(self,x):##点击混合玩法X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_mix(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_mix_nus_a(self,x):##点击混合玩法X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_mix(a, n)).click()
                                self.choosenumber_pasa()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pasa()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pasa()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Emptying_pbs(self):
        self.find_element(*self.emptying_pbs).click()###点击清空按钮

    def Paintball_single_bf(self):##点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bf(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bfs(self, q):  ###随机点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bf_nus_X(self,x):##选择比分玩法X场赛事结果
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                if n>1:
                                    target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bf(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % q)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_zjq(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    if i > 0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(1, 9):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-4
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    c=c-4
                                    self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS_pbs(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus(self, q):  ###随机点击总进球玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if n == 1:
                                self.top_more()  ###鼠标拉到顶部
                                c = random.randint(1, 4)  ###随机取C的值
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus_X(self,x):###点击总进球玩法X场比赛
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            self.top_more()
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                self.know()
                                print("第%d场，成功点击知道了"%n)
                                q = q + 1
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    c = random.randint(1, 4)  ###随机取C的值
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q=q+1
                                    print(q)
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    c = random.randint(1, 4)
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqc(self):  ###点击半全场显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqcs(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bqc_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                if n >1:
                                    target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bqc(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def Dgp_tan(self):
        self.find_element(*self.dgp_tan()).click()####点击单关配选号页弹框

    def Paintball_single_dgp(self):###选择单关配玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    self.top_more()
                    self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 8):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-3
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                        target = self.find_element(*self.VS_dgp(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def VSS_dgp(self,a):
        list=[]
        q=self.find_elements(*self.VSS(a))
        for i in range(len(q)):
            z=q[i].get_attribute('data-match')
            list.append(z)
        print(list)
        return list

    def Dgp_vs(self):
        na = self.Event_time_pbs()
        i=random.sample(len(na),1)
        a=na[i]
        self.VSS_dgp(a)

    def Paintball_single_dgps(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                if z>0:
                    self.Know_dgp()
                    print('成功点击提示信息“单关配只能选择一场赛事”')
                else:
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            if n == 1:
                                self.top_more_pbs()  ###鼠标拉到顶部
                                print('第%d天第%d场赛事' %(i+1,n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.Session_2(i + 1)
                            else:
                                js = "var q=document.body.scrollTop=10000"
                                self.driver.execute_script(js)
                                #self.wait_element_located(self.driver, self.VS_dgp(a, n-1))
                                target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                print('第%d天第%d场赛事' % (i + 1, n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.top_more_pbs()
                                self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2

    def Paintball_single_dgpss(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            print('第%d天第%d场赛事' %(i+1,n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            print('第%d天第%d场赛事' % (i + 1, n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2


    def Know_dgp(self):
        self.find_element(*self.know_dgp).click()###点击我知道了

    def Paintball_single_dgp_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q < x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>0:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                            else:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                                time.sleep(1)
                                self.Session_2(i + 1)
                        else:
                            break
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def jzdg_play_instruct(self):##竞足单关点击玩法说明--mj20171215
        self.wait_element_located(self.driver,self.jzdg_play_instruct_loc)
        self.find_element(*self.jzdg_play_instruct_loc).click()

class SingleFootChooseNumber_lelun(PaintBallChooseNumber_lelun,SingleFootChooseNumber_lelun_loc,HaobcChooseNumber_lelun_loc):
    def Play_dgp(self):#点击单关配模式
        self.wait_element_located(self.driver,self.dgp_lottery_loc)
        self.find_element(*self.dgp_lottery_loc).click()

    def Play_dgp_text(self):#获取单关配页面的单关配的文字
        self.wait_element_located(self.driver,self.dgp_text_loc)
        text=self.find_element(*self.dgp_text_loc).text
        return text
#############竞足单关，胜平负玩法选号页面的元素操作#############
    def jzdg_spf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(1, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_spf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_spf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_spf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.spf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    def jzdg_spf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞彩足球点击编辑赛事，对应的选号方法
    def jzdg_spf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_spf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
##############竞足单关，让球胜平负玩法选号页面的元素操作
    def jzdg_rqspf_choose_means(self ,num ,time ,n ,number = 0):#竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in random.sample(range(2, 4),1):
                    self.wait_element_located(self.driver ,self.event_one_loc(time ,k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9  :##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+ 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #竞足单关，胜平负玩法选号的方法
    def jzdg_rqspf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):

                if 'fold' in open_or_not[j]:
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)),1):
                time = event_time[i]
                event_list.append(i)
                print(event_list)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_rqspf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
    #竞足单关，点击所有赛事的方法
    def jzdg_rqspf_click_all(self):#点击页面所有的赛事
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.rqspf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:# 没有赛事的时候自动跳转至单关配页面
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0

    def jzdg_rqspf_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(2, 4):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(2, 4):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(2, 4), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #竞彩足球点击所有编辑赛事，对应的选号方法
    def jzdg_rqspf_edit_event(self,n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空等待进入单关配
        if event_time:
            for j in open_or_not:
                if 'fold' in j:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(open_or_not.index(j) + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_rqspf_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候等待跳转至单关配
            sleep(3)
            print("暂无赛事，前往单关配")
            return 0
####################竞足单关，2x1玩法选号页面元素操作###########################
    def jzdg_two_choose_one_choose_means(self, num, time, n, number=0):
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                event_list.append(i)
                print(num)
                if num == 1 and len(event_time)==1:  #所有场次为一场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)
                    return 3
                else:#场次为多场
                    self.Session(i + 1)  # 展开
                    self.jzdg_two_choose_one_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def jzdg_two_choose_one_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in event_time:
                print("wo shi zui bang de ")
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.two_choose_one_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
    def jzdg_two_choose_one_edit_choose_means(self, num, time, n, number=0):  # 竞足单关选号的方法
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, j))
                    self.find_element(*self.event_one_loc(time, j)).click()
                    self.find_element(*self.event_one_loc(time, j)).click()
            else:
                for k in range(1, 3):
                    self.wait_element_located(self.driver, self.event_one_loc(time, k))
                    self.find_element(*self.event_one_loc(time, k)).click()
        if num >= 2 and num < 9:  ##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num:
                for i in range(1, n + 1):
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num + 1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n + 1):  ##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3), 1):
                        lies = j
                        self.wait_element_located(self.driver, self.event_list_loc(time, number, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.wait_element_located(self.driver, self.vs_list_loc(time, number))
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def jzdg_two_choose_one_edit_event(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        # 如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            for i in random.sample(event_time, 1):
                time = i
                print(time)
                m = event_time.index(time)
                num = text_num[m]
                print(num)
                if num ==1:#场次等于1场的时候，在一场比赛中选择两场赛事
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                if num > 1:#场次大于1场时，选择另外1场比赛
                    self.Session(m + 1)  # 展开
                    self.jzdg_two_choose_one_edit_choose_means(num, time, n,number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Text_nu_pbs(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1])
            list.append(nnu)
        print(list)
        return list

        # 获取有多少天赛事的list

    def Event_time_pbs(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def This_open_pbs(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def top_more_pbs(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)  ###鼠标拉到顶部

    def Session_2(self, n):
        self.top_more_pbs()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def pull_down(self):
        target = self.find_element(*self.cdxf_icon(1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Confirm_more(self):
        self.find_element(*self.confirm_more_pbs).click()  #####点击展开更多页面的确定

    def Confirm_more_sfc(self):
        self.find_element(*self.confirm_more_sfc).click()  #####点击展开更多页面的确定

    def choosenumber_pas(self):  ####竞足单关展开更多页面显示赛事结果
        list = []
        #self.wait_element_located(self.driver, self.more_pbs)
        nn = self.find_elements(*self.more_pbs)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '9002':
                    self.Cjqs_pbs()
                elif list[j] == '9003':
                    self.Cbf_pbs()
                elif list[j] == '9004':
                    self.Cbqc_pbs()
                elif list[j]=='9005':
                    self.Cspf_pbs()
                elif list[j]=='10003':
                    self.Csfc_jzdg()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Cspf_pbs(self):
        list5=['1','0','3']
        for n in list5:
            target = self.find_element(*self.cspf_pbs_icon(1))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            self.find_element(*self.cspf_pbs_icon(n)).click()###点击胜平负

    def Cjqs_pbs(self):
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7']
        for n in list1:
            self.find_element(*self.cjqs_pbs_icon(n)).click()  # 点击胜平负/

    def Cbf_pbs(self):
        list2 = ['10', '20', '21', '30', '31', '32', '40', '41', '42', '50', '51', '52', '90', '00', '11', '22',
                 '33',
                 '99', '01', '02', '12', '03', '13', '23', '04', '14', '24', '05', '15', '25', '09']
        for n in list2:
            self.find_element(*self.cbf_pbs_icon(n)).click()  ##点击比分

    def Cbqc_pbs(self):
        list3 = ['30', '31', '33', '13', '11', '10', '03', '01', '00']
        for n in list3:
            self.find_element(*self.cbqc_pbs_icon(n)).click()  ##点击猜半全场

    def Csfc_jzdg(self):
        list4=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list4:
            self.find_elements(*self.csfc_jczq_icon(n)).clcik()##点胜分差

    def Paintball_single_mix(self):  ###点击混合玩法显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_mix(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_mixs(self, q):  ###随机点击混合玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        print("第%d天，第%d场赛事" %((i+1),n))
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_mix(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_mix_nus_X(self,x):##点击混合玩法X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_mix(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_mix(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Emptying_pbs(self):
        self.find_element(*self.emptying_pbs).click()###点击清空按钮

    def Paintball_single_bf(self):##点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bf(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bfs(self, q):  ###随机点击比分玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bf(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bf_nus_X(self,x):##选择比分玩法X场赛事结果
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                if n>1:
                                    target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bf(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bf(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_zjq(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    if i > 0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(1, 9):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-4
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    c=c-4
                                    self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS_pbs(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus(self, q):  ###随机点击总进球玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if n == 1:
                                self.top_more()  ###鼠标拉到顶部
                                c = random.randint(1, 4)  ###随机取C的值
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                self.top_more()
                                self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_zjq_nus_X(self,x):###点击总进球玩法X场比赛
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            self.top_more()
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 4)
                                self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                self.know()
                                print("第%d场，成功点击知道了"%n)
                                q = q + 1
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    c = random.randint(1, 4)  ###随机取C的值
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()  ###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q=q+1
                                    print(q)
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    c = random.randint(1, 4)
                                    self.find_element(*self.paintball_single_zjq(a, n, b, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, c))
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqc(self):  ###点击半全场显示的赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()  ###
        if na:
            for i in range(len(na)):
                print("点击%d天赛事" % (i + 1))
                a = na[i]
                nn = ns[i] + 1
                if i > 0:
                    self.top_more_pbs()
                    self.Session_2(i)
                    self.Session_2(i + 1)
                for n in range(1, nn):
                    print('第%d场赛事' % n)
                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                    self.choosenumber_pas()
                    self.choosenumber_pas()
                    self.Confirm_more()
                    target = self.find_element(*self.VS_pbs(a, n))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Paintball_single_bqcs(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            self.find_element(*self.paintball_single_bqc(a, n)).click()
                            self.choosenumber_pas()
                            self.Confirm_more()
                            self.top_more_pbs()
                            self.Session_2(i + 1)
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Paintball_single_bqc_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.paintball_single_bqc(a, n)).click()
                                self.choosenumber_pas()
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                                else:
                                    if n==1:
                                        self.top_more()
                                        #target = self.find_element(*self.VS(a, n))  ####定位到n-1场赛事的VS
                                        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    else:
                                        target = self.find_element(*self.VS_pbs(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.paintball_single_bqc(a, n)).click()
                                    self.choosenumber_pas()
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def Dgp_tan(self):
        self.find_element(*self.dgp_tan()).click()####点击单关配选号页弹框

    def Paintball_single_dgp(self):###选择单关配玩法赛事结果
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):
                    print("点击%d天赛事" % (i + 1))
                    a = na[i]
                    nn = ns[i] + 1
                    self.top_more()
                    self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 8):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                            else:
                                try:
                                    b = 2
                                    c=c-3
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                        target = self.find_element(*self.VS_dgp(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def VSS_dgp(self,a):
        list=[]
        q=self.find_elements(*self.VSS(a))
        for i in range(len(q)):
            z=q[i].get_attribute('data-match')
            list.append(z)
        print(list)
        return list

    def Dgp_vs(self):
        na = self.Event_time_pbs()
        i=random.sample(len(na),1)
        a=na[i]
        self.VSS_dgp(a)

    def Paintball_single_dgps(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                if z>0:
                    self.Know_dgp()
                    print('成功点击提示信息“单关配只能选择一场赛事”')
                else:
                    for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                            a = na[i]
                            self.Session_2(i + 1)  ##点击i+1天的赛事
                            if n == 1:
                                self.top_more_pbs()  ###鼠标拉到顶部
                                print('第%d天第%d场赛事' %(i+1,n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.Session_2(i + 1)
                            else:
                                js = "var q=document.body.scrollTop=10000"
                                self.driver.execute_script(js)
                                #self.wait_element_located(self.driver, self.VS_dgp(a, n-1))
                                target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                print('第%d天第%d场赛事' % (i + 1, n))
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                self.top_more_pbs()
                                self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2

    def Paintball_single_dgpss(self, q):  ###随机点击半全场玩法赛事结果
        ns = self.Text_nu_pbs()
        na = self.Event_time_pbs()
        nc = self.This_open_pbs()
        if na:
            for j in range(len(nc)):
                cla = nc[j]
                print(cla)
                if 'fold' in cla:
                    print("没有展开赛事")
                else:
                    self.Session_2(j + 1)
                    print("收起赛事展示")
            for z in range(q):  ##控制循环q次
                for i in random.sample(range(len(na)), 1):  ###随机1个取列表na的坐标
                    for n in random.sample(range(1, ns[i] + 1), 1):  ###随机取1个a对应的场次
                        a = na[i]
                        self.Session_2(i + 1)  ##点击i+1天的赛事
                        if n == 1:
                            self.top_more_pbs()  ###鼠标拉到顶部
                            print('第%d天第%d场赛事' %(i+1,n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.Session_2(i + 1)
                        else:
                            target = self.find_element(*self.VS_dgp(a, n-1))  ####定位到n-1场赛事的VS
                            self.driver.execute_script("arguments[0].scrollIntoView();", target)
                            print('第%d天第%d场赛事' % (i + 1, n))
                            for c in range(2, 8):
                                if c < 5:
                                    try:
                                        b = 1
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                else:
                                    try:
                                        b = 2
                                        c = c - 3
                                        self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                    except NoSuchElementException:
                                        print('没有第二行')
                            self.top_more_pbs()
                            self.Session_2(i + 1)
                return 1
            else:
                print('没有赛事展示')
                self.find_element(*self.return_link_loc).click()
                return 2


    def Know_dgp(self):
        self.find_element(*self.know_dgp).click()###点击我知道了

    def Paintball_single_dgp_nus_X(self,x):##选择半全场X场赛事
        q=0
        ns = self.Text_nu()
        na = self.Event_time()
        nc = self.This_open()
        if na:
                for j in range(len(nc)):
                    cla = nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j + 1)
                        print("收起赛事展示")
                for i in range(len(na)):  ###随机1个取列表na的坐标
                    for n in range(1, ns[i] + 1):  ###随机取1个a对应的场次
                        if q < x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>0:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                            break
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                            self.know()
                                            print("第%d场，成功点击知道了" % n)
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                            else:
                                for c in range(2, 8):
                                    if c < 5:
                                        try:
                                            b = 1
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            self.find_element(*self.paintball_single_dgpo(a, n, c)).click()
                                    else:
                                        try:
                                            b = 2
                                            c = c - 3
                                            self.find_element(*self.paintball_single_dgp(a, n, b, c)).click()
                                        except NoSuchElementException:
                                            print('没有第二行')
                                q = q + 1
                                time.sleep(1)
                                self.Session_2(i + 1)
                        else:
                            break
                return q
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def jzdg_play_instruct(self):##竞足单关点击玩法说明--mj20171215
        self.wait_element_located(self.driver,self.jzdg_play_instruct_loc)
        self.find_element(*self.jzdg_play_instruct_loc).click()