from element_operate.base import Page
from element_position.lemi import PaintBallChooseNumber_loc
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber
import random
from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber_lexiu
from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber_leyou
from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber_lelun


##################竞篮单关-----mj20171122
class SingleBasketballChooseNumber(HaobcChooseNumber):


    #竞篮单关选号方法--mj20171123
    def jldg_sf_choose_means(self, num, time, n, number=0):
        # number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in random.sample(range(1,3),1):
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
    #竞篮单关选号操作--mj20171123
    def jldg_sf_choose(self, n):
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
            for i in random.sample(range(len(event_time)), 1):
                time = event_time[i]
                print(time)
                event_list.append(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time) == 1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num,time,1)  #投注
                    print("只有一场比赛")
                    return 3
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0
    ##竞篮单关编辑赛事，选号的方法---mj20171123
    def jldg_sf_edit_choose_means(self, num, time, n, number):  # 竞足单关选号的方法
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
    def jldg_sf_edit_event(self, n):
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
                if num == 1 and event_time==1:
                    self.Session(m + 1)  # 展开
                    self.jldg_sf_edit_choose_means(num, time, 1)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                else:
                    self.Session(m + 1)  # 展开
                    self.sf_choose_means(num, time, n, number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0
    ##挨个点击场次胜负方法--mj20171123
    def jldg_click_all_means(self, num, time):
        number = 0
        if num == 1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                self.find_element(*self.event_one_loc(time, lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
    # 竞篮单关，点击所有赛事的方法--mj20171123
    def jldg_click_all(self):  # 点击页面所有的赛事
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
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.jldg_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0

class SingleBasketballChooseNumber_lexiu(HaobcChooseNumber_lexiu):

        # 竞篮单关选号方法--mj20171123
    def jldg_sf_choose_means(self, num, time, n, number=0):
        # number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in random.sample(range(1, 3), 1):
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

        # 竞篮单关选号操作--mj20171123
    def jldg_sf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        #  如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)), 1):
                time = event_time[i]
                print(time)
                event_list.append(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time) == 1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 投注
                    print("只有一场比赛")
                    return 3
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0

        ##竞篮单关编辑赛事，选号的方法---mj20171123
    def jldg_sf_edit_choose_means(self, num, time, n, number):  # 竞足单关选号的方法
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

    def jldg_sf_edit_event(self, n):
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
                if num == 1 and event_time == 1:
                    self.Session(m + 1)  # 展开
                    self.jldg_sf_edit_choose_means(num, time, 1)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                else:
                    self.Session(m + 1)  # 展开
                    self.sf_choose_means(num, time, n, number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

        ##挨个点击场次胜负方法--mj20171123
    def jldg_click_all_means(self, num, time):
        number = 0
        if num == 1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                self.find_element(*self.event_one_loc(time, lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)

        # 竞篮单关，点击所有赛事的方法--mj20171123
    def jldg_click_all(self):  # 点击页面所有的赛事
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
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.jldg_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0

class SingleBasketballChooseNumber_leyou(HaobcChooseNumber_leyou):

        # 竞篮单关选号方法--mj20171123
        def jldg_sf_choose_means(self, num, time, n, number=0):
            # number = 0
            if num == 1:
                if n > 9:
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                        self.find_element(*self.event_one_loc(time, lies)).click()
                        self.find_element(*self.event_one_loc(time, lies)).click()
                else:
                    for k in random.sample(range(1, 3), 1):
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

                        # 竞篮单关选号操作--mj20171123

        def jldg_sf_choose(self, n):
            event_time = self.Event_time()  # 获取有多少天赛事的list
            text_num = self.Text_nu()  # 获取每天的场次数list
            open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
            #  如果赛事列表不为空，选择赛事，如果为空点击返回
            if event_time:
                for j in range(len(open_or_not)):
                    if 'fold' in open_or_not[j]:
                        print(j)
                        print("没有展开")
                    else:
                        self.Session(j + 1)
                        print("关闭")
                event_list = []
                for i in random.sample(range(len(event_time)), 1):
                    time = event_time[i]
                    print(time)
                    event_list.append(i)
                    num = text_num[i]
                    print(num)
                    if num == 1 and len(event_time) == 1:
                        self.Session(i + 1)  # 展开
                        self.sf_choose_means(num, time, 1)  # 投注
                        print("只有一场比赛")
                        return 3
                    else:
                        self.Session(i + 1)  # 展开
                        self.sf_choose_means(num, time, n)  # 选择要投注的场次
                        return 2
            else:  # 没有赛事的时候直接返回
                self.wait_element_located(self.driver, self.back_to_homepage_loc)
                self.find_element(*self.back_to_homepage_loc).click()
                print("暂无赛事，已返回")
                return 0

                ##竞篮单关编辑赛事，选号的方法---mj20171123

        def jldg_sf_edit_choose_means(self, num, time, n, number):  # 竞足单关选号的方法
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
                                self.find_element(
                                    *self.event_list_loc(time, number, lies)).click()  # 从一场比赛中胜平负三种结果中任选一个
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

        def jldg_sf_edit_event(self, n):
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
                    if num == 1 and event_time == 1:
                        self.Session(m + 1)  # 展开
                        self.jldg_sf_edit_choose_means(num, time, 1)  # 选择要投注的场次
                        print("只有一场比赛")
                        return 1
                    else:
                        self.Session(m + 1)  # 展开
                        self.sf_choose_means(num, time, n, number=1)  # 选择要投注的场次
                        return 2
            else:  # 没有赛事的时候直接返回
                self.wait_element_located(self.driver, self.back_to_homepage_loc)
                self.find_element(*self.back_to_homepage_loc).click()
                return 0

                ##挨个点击场次胜负方法--mj20171123

        def jldg_click_all_means(self, num, time):
            number = 0
            if num == 1:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for i in range(1, num + 1):
                    number = number + 1
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                        self.find_element(*self.event_list_loc(time, number, lies)).click()
                    target = self.find_element(*self.vs_list_loc(time, number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)

                    # 竞篮单关，点击所有赛事的方法--mj20171123

        def jldg_click_all(self):  # 点击页面所有的赛事
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
                    print(event_time)
                    time = i
                    m = event_time.index(time)
                    num = text_num[m]
                    self.Session(m + 1)  # 展开
                    self.jldg_click_all_means(num, time)  # 选择要投注的场次
                    self.Session(m + 1)  # 关闭
            else:  # 没有赛事的时候直接返回
                self.wait_element_located(self.driver, self.back_to_homepage_loc)
                self.find_element(*self.back_to_homepage_loc).click()
                print("暂无赛事，已返回")
                return 0


class SingleBasketballChooseNumber_lelun(HaobcChooseNumber_lelun):
    # 竞篮单关选号方法--mj20171123
    def jldg_sf_choose_means(self, num, time, n, number=0):
        # number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in random.sample(range(1, 3), 1):
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

                    # 竞篮单关选号操作--mj20171123

    def jldg_sf_choose(self, n):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操 作天的赛事展开与否的前端js
        #  如果赛事列表不为空，选择赛事，如果为空点击返回
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j + 1)
                    print("关闭")
            event_list = []
            for i in random.sample(range(len(event_time)), 1):
                time = event_time[i]
                print(time)
                event_list.append(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time) == 1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 投注
                    print("只有一场比赛")
                    return 3
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0

            ##竞篮单关编辑赛事，选号的方法---mj20171123

    def jldg_sf_edit_choose_means(self, num, time, n, number):  # 竞足单关选号的方法
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

    def jldg_sf_edit_event(self, n):
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
                if num == 1 and event_time == 1:
                    self.Session(m + 1)  # 展开
                    self.jldg_sf_edit_choose_means(num, time, 1)  # 选择要投注的场次
                    print("只有一场比赛")
                    return 1
                else:
                    self.Session(m + 1)  # 展开
                    self.sf_choose_means(num, time, n, number=1)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

            ##挨个点击场次胜负方法--mj20171123

    def jldg_click_all_means(self, num, time):
        number = 0
        if num == 1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                self.find_element(*self.event_one_loc(time, lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver, self.event_one_loc(time, lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)

                # 竞篮单关，点击所有赛事的方法--mj20171123

    def jldg_click_all(self):  # 点击页面所有的赛事
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
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.jldg_click_all_means(num, time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0