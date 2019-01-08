from element_operate.base import Page
from element_position.lemi import HaobcChooseNumber_loc
from element_position.lemi import PaintBallChooseNumber_loc
from element_position.lemi import UChooseNum_loc
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from selenium.webdriver.common.by import By
from time import sleep
import time
import random
from element_operate.base import Page_lexiu
from element_position.lexiu import HaobcChooseNumber_lexiu_loc
from element_position.lexiu import PaintBallChooseNumber_lexiu_loc
from element_position.lexiu import UChooseNum_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import HaobcChooseNumber_leyou_loc
from element_position.leyou import PaintBallChooseNumber_leyou_loc
from element_position.leyou import UChooseNum_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import HaobcChooseNumber_lelun_loc
from element_position.lelun import PaintBallChooseNumber_lelun_loc
from element_position.lelun import UChooseNum_lelun_loc


##########################竞彩足球，混合投注页面点击赛事结果####################

class HaobcChooseNumber(Page,HaobcChooseNumber_loc,PaintBallChooseNumber_loc,UChooseNum_loc):
    def Play_f(self):
        self.wait_element_located(self.driver,self.choose_mode_loc)
        self.find_element(*self.choose_mode_loc).click()###点击玩法

    def Play_mix(self):
        #self.wait_element_located(self.driver,self.mix_mode_loc)
        self.find_element(*self.mix_mode_loc).click()####点击混合投注

    def Play_sf(self):
        self.wait_element_located(self.driver,self.sf_mode_loc)
        self.find_element(*self.sf_mode_loc).click()##点击胜负

    def Play_rfsf(self):
        self.wait_element_located(self.driver,self.rfsf_mode_loc)
        self.find_element(*self.rfsf_mode_loc).click()##让分胜负

    def Play_sfc(self):
        self.wait_element_located(self.driver,self.sfc_mode_loc)
        self.find_element(*self.sfc_mode_loc).click()####点击胜负差

    def Play_dxf(self):
        self.wait_element_located(self.driver,self.dxf_mode_loc)
        self.find_element(*self.dxf_mode_loc).click()###点击大小分
    ##获取所选场次大于8场时的提示信息--mj20171109
    def toast(self):
        self.wait_element_located(self.driver, self.nu_8)
        toast = self.find_element(*self.nu_8).text
        return toast

    #获取所选场次大于8场时点击我知道了--mj20171109
    def know(self):
        #self.wait_element_located(self.driver,self.know_loc)
        self.find_element(*self.know_loc).click()
    #点击，确认所选比赛场次---mj20171103
    def confirm_match(self):
        self.wait_element_located(self.driver,self.confirm_loc)
        self.find_element(*self.confirm_loc).click()
    ##点击清空所选比赛场次按钮  ---mj20171109
    def clear_button(self):
        self.wait_element_located(self.driver,self.delete_button_loc)
        self.find_element(*self.delete_button_loc).click()
    '''
    #展开竞足赛事详情----mj20171106
    def spread_event_details(self):
        nul = self.find_element(*self.nul_loc).text  ##获取今日比赛场次
        num = int(nul[:-1])  # 将获取的场次转换为整数
        number=0
        for i in range(1,num+1):
            number= number + 1
            self.find_element(*self.spread_event_details_loc(time,number)).click()
    '''
    #点击当天赛事场次控制展开/关闭
    def Session(self, n):
        # self.wait_element_located(self.driver,self.session(n))
        # target = self.find_element(*self.session(n))
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)#使用这种方法，今天的div会遮挡明天的div导致can not clickable
        self.driver.execute_script("window.scroll(0,0)")
        sleep(2)
        self.wait_element_located(self.driver,self.session(n))
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次
        print("我已经展开了")
    #获取当天的赛事场次，并放入列表中
    def Text_nu(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            print(id)
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list
    #获取有多少天赛事的list
    def Event_time(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list
    #当前操作天的赛事展开与否的前端js
    def This_open(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list


    def Football_mix_nu(self):####点击混合玩法显示的赛事结果
        ns=self.Text_nu()
        na=self.Event_time()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 6):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 5):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 5):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Text_ba(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list


    # 获取有多少天赛事的list
    def Event_time_ba(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def top_more(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)###鼠标拉到顶部

    def Session_ba(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次


    # 当前操作天的赛事展开与否的前端js
    def This_open_ba(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def Basketball_mix_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 5):
                            if c < 4:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 4):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 4):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Basketball_rfsf_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        list=[1,2]
                        for c in list:
                            self.Rfsf_ic(a,n,c)
                            self.Rfsf_ic(a, n, c)
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Confirm_more(self):
        self.find_element(*self.confirm_more).click()###点击展开更多页面确定按钮

    def Rfsf_ic(self,a,n,c):
        self.find_element(*self.rfsf_ic(a,n,c)).click()###点击让分胜负赛事结果


    def Basketball_mix_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 3)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_rfsf_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                c=random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Session_2(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def Football_bf(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        self.find_element(*self.football_bf(a,n)).click()
                        self.Cbf_icon()
                        self.Cbf_icon()
                        self.Confirm_more()
                        target = self.find_element(*self.VS_bf(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2


    def Football_mix_nus(self,q):
        ns = self.Text_nu()
        na = self.Event_time()
        nc=self.This_open()
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
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 4)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_bfs(self,q):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)),1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1,ns[i]+1),1):  ###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if n==1:
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                            else:
                                target = self.find_element(*self.VS_bf(a, n-1))
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 4)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        print(q)
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def More_paid_choosenumber(self):  ####竞彩篮球展开更多页面显示赛事结果
        list = []
        self.wait_element_located(self.driver, self.more_paid)
        nn = self.find_elements(*self.more_paid)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '10002':
                    self.Rfsf_icon()
                elif list[j] == '10004':
                    self.Cdxf_icon()
                elif list[j] == '10003':
                    self.Csfc_icon()
                elif list[j]=='10001':
                    self.Sf_icon()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Rfsf_icon(self):
        list=['1','2']
        for n in list:
            self.find_element(*self.rfsf_icon(n)).click()##点击让分胜负

    def Cdxf_icon(self):
        list1=['1','2']
        for n in list1:
            self.find_element(*self.cdxf_icon(n)).click()###点击猜大小分

    def Csfc_icon(self):
        list2=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list2:
            self.find_element(*self.csfc_icon(n)).click()###点击猜胜分差

    def Sf_icon(self):
        list3=['1','2']
        for n in list3:
            self.find_element(*self.sf_icon(n)).click()###点击胜负



    def More_choosenumber(self):
        ns = self.Text_nu()###读取当页展示的所有赛事场数
        na = self.Event_time()###读取当页展示的赛事天数
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    nc = self.This_open()##读取当页展示赛事天数的class值
                    '''for j in range(len(nc)):'''
                    cla = nc[i]###读取i+1天的class的值
                    print(cla)
                    if 'fold' in cla:###判断i+1天赛事是否展开
                        print("没有展开")
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事展开更多'%n)
                        self.More(a,n)###点击展开更多
                        self.More_paid_choosenumber()
                        self.More_paid_choosenumber()
                        self.Confirm_more()###点击确认
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def More_choosenumbers(self,q):
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
                            print('点击第%d天第%d场赛事展开更多' %((i+1),n))
                            if n==1:
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                            else:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                        self.top_more()
                        self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2



    def More(self,i,n):
        self.find_element(*self.more(i,n)).click()####点击展开更多

    def Cspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            self.find_element(*self.cspf_icon(n)).click()####点击猜胜平负赛事结果


    def Crqspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            sleep(5)
            self.find_element(*self.crqspf_icon(n)).click()####点击猜胜平负的第一个赛事结果

    def Cjqs_icon(self):
        list=['0','1','2','3','4','5','6','7']
        for n in list:
            self.find_element(*self.cjqs_icon(n)).click()###点击猜进球数结果

    def Cbf_icon(self):
        list=['10','20','21','30','31','32','40','41','42','50','51','52','90','00','11','22','33',
              '99','01','02','12','03','13','23','04','14','24','05','15','25','09']
        for n in list:
            self.find_element(*self.cbf_icon(n)).click()###点击猜比分结果

    def Cbqc_icon(self):
        list=['33','31','30','13','11','10','03','01','00']
        for n in list:
            self.find_element(*self.cbqc_icon(n)).click()###点击猜半全场结果

    def pull_down(self):
        target = self.find_element(*self.cjqs_icon(4))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Text_confirm_loc(self):
        nu=self.find_element(*self.confirm_loc).text#####读取混合玩法确认选号文字
        print(nu)
        return nu

    def Play_fb(self):
        aa=self.find_element(*self.play_fb).text###读取玩法文本
        print(aa)
        return aa

    def Emptying(self):
        self.find_element(*self.emptying).click()####点击清空按钮


    def sf_choose_means(self,num,time,n,number = 0):
        #number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+1):
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()#从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num+1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n+1):##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                        sleep(2)
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_choose(self, n):
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
                event_list.append(i)
                print(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:
                    self.Session(i + 1)  # 展开
                    self.find_element(*self.go_haobc_single_button_loc).click()  # 点击前往竞篮单关按钮
                    print("只有一场比赛，去往竞篮单关")
                    return 3
                elif num == 1 and len(event_time)!=1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0
    def sf_click_all_means(self,num,time):
        number = 0
        if num==1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                self.find_element(*self.event_one_loc(time,lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1,3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j+ 1)
                    print("关闭")
                    sleep(2)
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.sf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver,self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")

    def sf_edit_event(self,n):
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
                if num ==1 and event_time==1:#比赛场次只有一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择要投注1场次
                    print("比赛场次为1场")
                    return 3
                elif num == 1 and event_time != 1:#某一天的场次为一场，但所有场次不为一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:#场次为多于一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n,number=2)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Basketball_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 3)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Basketball_sfc_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                    self.Session_2(2)
                    a=na[1]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()###点击玩法说明

    def Race_basketball(self):
        self.find_element(*self.race_basketball).click()###点击投注竞彩蓝球

    def Event_analysis_data(self):
        na = self.Event_time()
        if na:
            b=na[0]
            self.find_element(*self.event_analysis_data(b,1)).click()
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Event_analysis_data_click(self):
        sleep(1)
        #self.wait_element_located(self.driver, self.event_analysis_data_click)
        self.find_element(*self.event_analysis_data_click).click()##点击数据分析

class HaobcChooseNumber_lexiu(Page_lexiu,HaobcChooseNumber_lexiu_loc,PaintBallChooseNumber_lexiu_loc,UChooseNum_lexiu_loc):
    def Play_f(self):
        self.wait_element_located(self.driver,self.choose_mode_loc)
        self.find_element(*self.choose_mode_loc).click()###点击玩法

    def Play_mix(self):
        #self.wait_element_located(self.driver,self.mix_mode_loc)
        self.find_element(*self.mix_mode_loc).click()####点击混合投注

    def Play_sf(self):
        self.wait_element_located(self.driver,self.sf_mode_loc)
        self.find_element(*self.sf_mode_loc).click()##点击胜负

    def Play_rfsf(self):
        self.wait_element_located(self.driver,self.rfsf_mode_loc)
        self.find_element(*self.rfsf_mode_loc).click()##让分胜负

    def Play_sfc(self):
        self.wait_element_located(self.driver,self.sfc_mode_loc)
        self.find_element(*self.sfc_mode_loc).click()####点击胜负差

    def Play_dxf(self):
        self.wait_element_located(self.driver,self.dxf_mode_loc)
        self.find_element(*self.dxf_mode_loc).click()###点击大小分
    ##获取所选场次大于8场时的提示信息--mj20171109
    def toast(self):
        self.wait_element_located(self.driver, self.nu_8)
        toast = self.find_element(*self.nu_8).text
        return toast

    #获取所选场次大于8场时点击我知道了--mj20171109
    def know(self):
        #self.wait_element_located(self.driver,self.know_loc)
        self.find_element(*self.know_loc).click()
    #点击，确认所选比赛场次---mj20171103
    def confirm_match(self):
        self.wait_element_located(self.driver,self.confirm_loc)
        self.find_element(*self.confirm_loc).click()
    ##点击清空所选比赛场次按钮  ---mj20171109
    def clear_button(self):
        self.wait_element_located(self.driver,self.delete_button_loc)
        self.find_element(*self.delete_button_loc).click()
    '''
    #展开竞足赛事详情----mj20171106
    def spread_event_details(self):
        nul = self.find_element(*self.nul_loc).text  ##获取今日比赛场次
        num = int(nul[:-1])  # 将获取的场次转换为整数
        number=0
        for i in range(1,num+1):
            number= number + 1
            self.find_element(*self.spread_event_details_loc(time,number)).click()
    '''
    #点击当天赛事场次控制展开/关闭
    def Session(self, n):
        # self.wait_element_located(self.driver,self.session(n))
        # target = self.find_element(*self.session(n))
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)#使用这种方法，今天的div会遮挡明天的div导致can not clickable
        self.driver.execute_script("window.scroll(0,0)")
        sleep(2)
        self.wait_element_located(self.driver,self.session(n))
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次
        print("我已经展开了")
    #获取当天的赛事场次，并放入列表中
    def Text_nu(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            print(id)
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list
    #获取有多少天赛事的list
    def Event_time(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list
    #当前操作天的赛事展开与否的前端js
    def This_open(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list


    def Football_mix_nu(self):####点击混合玩法显示的赛事结果
        ns=self.Text_nu()
        na=self.Event_time()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 6):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 5):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 5):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Text_ba(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list


    # 获取有多少天赛事的list
    def Event_time_ba(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def top_more(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)###鼠标拉到顶部

    def Session_ba(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次


    # 当前操作天的赛事展开与否的前端js
    def This_open_ba(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def Basketball_mix_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 5):
                            if c < 4:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 4):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 4):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Basketball_rfsf_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        list=[1,2]
                        for c in list:
                            self.Rfsf_ic(a,n,c)
                            self.Rfsf_ic(a, n, c)
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Confirm_more(self):
        self.find_element(*self.confirm_more).click()###点击展开更多页面确定按钮

    def Rfsf_ic(self,a,n,c):
        self.find_element(*self.rfsf_ic(a,n,c)).click()###点击让分胜负赛事结果


    def Basketball_mix_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 3)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_rfsf_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                c=random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Session_2(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def Football_bf(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        self.find_element(*self.football_bf(a,n)).click()
                        self.Cbf_icon()
                        self.Cbf_icon()
                        self.Confirm_more()
                        target = self.find_element(*self.VS_bf(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2


    def Football_mix_nus(self,q):
        ns = self.Text_nu()
        na = self.Event_time()
        nc=self.This_open()
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
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 4)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_bfs(self,q):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)),1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1,ns[i]+1),1):  ###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if n==1:
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                            else:
                                target = self.find_element(*self.VS_bf(a, n-1))
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 4)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        print(q)
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def More_paid_choosenumber(self):  ####竞彩篮球展开更多页面显示赛事结果
        list = []
        self.wait_element_located(self.driver, self.more_paid)
        nn = self.find_elements(*self.more_paid)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '10002':
                    self.Rfsf_icon()
                elif list[j] == '10004':
                    self.Cdxf_icon()
                elif list[j] == '10003':
                    self.Csfc_icon()
                elif list[j]=='10001':
                    self.Sf_icon()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Rfsf_icon(self):
        list=['1','2']
        for n in list:
            self.find_element(*self.rfsf_icon(n)).click()##点击让分胜负

    def Cdxf_icon(self):
        list1=['1','2']
        for n in list1:
            self.find_element(*self.cdxf_icon(n)).click()###点击猜大小分

    def Csfc_icon(self):
        list2=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list2:
            self.find_element(*self.csfc_icon(n)).click()###点击猜胜分差

    def Sf_icon(self):
        list3=['1','2']
        for n in list3:
            self.find_element(*self.sf_icon(n)).click()###点击胜负



    def More_choosenumber(self):
        ns = self.Text_nu()###读取当页展示的所有赛事场数
        na = self.Event_time()###读取当页展示的赛事天数
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    nc = self.This_open()##读取当页展示赛事天数的class值
                    '''for j in range(len(nc)):'''
                    cla = nc[i]###读取i+1天的class的值
                    print(cla)
                    if 'fold' in cla:###判断i+1天赛事是否展开
                        print("没有展开")
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事展开更多'%n)
                        self.More(a,n)###点击展开更多
                        self.More_paid_choosenumber()
                        self.More_paid_choosenumber()
                        self.Confirm_more()###点击确认
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def More_choosenumbers(self,q):
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
                            print('点击第%d天第%d场赛事展开更多' %((i+1),n))
                            if n==1:
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                            else:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                        self.top_more()
                        self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2



    def More(self,i,n):
        self.find_element(*self.more(i,n)).click()####点击展开更多

    def Cspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            self.find_element(*self.cspf_icon(n)).click()####点击猜胜平负赛事结果


    def Crqspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            sleep(5)
            self.find_element(*self.crqspf_icon(n)).click()####点击猜胜平负的第一个赛事结果

    def Cjqs_icon(self):
        list=['0','1','2','3','4','5','6','7']
        for n in list:
            self.find_element(*self.cjqs_icon(n)).click()###点击猜进球数结果

    def Cbf_icon(self):
        list=['10','20','21','30','31','32','40','41','42','50','51','52','90','00','11','22','33',
              '99','01','02','12','03','13','23','04','14','24','05','15','25','09']
        for n in list:
            self.find_element(*self.cbf_icon(n)).click()###点击猜比分结果

    def Cbqc_icon(self):
        list=['33','31','30','13','11','10','03','01','00']
        for n in list:
            self.find_element(*self.cbqc_icon(n)).click()###点击猜半全场结果

    def pull_down(self):
        target = self.find_element(*self.cjqs_icon(4))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Text_confirm_loc(self):
        nu=self.find_element(*self.confirm_loc).text#####读取混合玩法确认选号文字
        print(nu)
        return nu

    def Play_fb(self):
        aa=self.find_element(*self.play_fb).text###读取玩法文本
        print(aa)
        return aa

    def Emptying(self):
        self.find_element(*self.emptying).click()####点击清空按钮


    def sf_choose_means(self,num,time,n,number = 0):
        #number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+1):
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()#从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num+1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n+1):##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                        sleep(2)
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_choose(self, n):
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
                event_list.append(i)
                print(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:
                    self.Session(i + 1)  # 展开
                    self.find_element(*self.go_haobc_single_button_loc).click()  # 点击前往竞篮单关按钮
                    print("只有一场比赛，去往竞篮单关")
                    return 3
                elif num == 1 and len(event_time)!=1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0
    def sf_click_all_means(self,num,time):
        number = 0
        if num==1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                self.find_element(*self.event_one_loc(time,lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1,3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j+ 1)
                    print("关闭")
                    sleep(2)
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.sf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver,self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")

    def sf_edit_event(self,n):
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
                if num ==1 and event_time==1:#比赛场次只有一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择要投注1场次
                    print("比赛场次为1场")
                    return 3
                elif num == 1 and event_time != 1:#某一天的场次为一场，但所有场次不为一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:#场次为多于一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n,number=2)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Basketball_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 3)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Basketball_sfc_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                    self.Session_2(2)
                    a=na[1]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()###点击玩法说明

    def Race_basketball(self):
        self.wait_element_located(self.driver,self.race_basketball)
        self.find_element(*self.race_basketball).click()###点击投注竞彩蓝球

    def Event_analysis_data(self):
        na = self.Event_time()
        if na:
            b=na[0]
            self.find_element(*self.event_analysis_data(b,1)).click()
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Event_analysis_data_click(self):
        sleep(1)
        #self.wait_element_located(self.driver, self.event_analysis_data_click)
        self.find_element(*self.event_analysis_data_click).click()##点击数据分析

class HaobcChooseNumber_leyou(Page_leyou,HaobcChooseNumber_leyou_loc,PaintBallChooseNumber_leyou_loc,UChooseNum_leyou_loc):
    def Play_f(self):
        self.wait_element_located(self.driver,self.choose_mode_loc)
        self.find_element(*self.choose_mode_loc).click()###点击玩法

    def Play_mix(self):
        #self.wait_element_located(self.driver,self.mix_mode_loc)
        self.find_element(*self.mix_mode_loc).click()####点击混合投注

    def Play_sf(self):
        self.wait_element_located(self.driver,self.sf_mode_loc)
        self.find_element(*self.sf_mode_loc).click()##点击胜负

    def Play_rfsf(self):
        self.wait_element_located(self.driver,self.rfsf_mode_loc)
        self.find_element(*self.rfsf_mode_loc).click()##让分胜负

    def Play_sfc(self):
        self.wait_element_located(self.driver,self.sfc_mode_loc)
        self.find_element(*self.sfc_mode_loc).click()####点击胜负差

    def Play_dxf(self):
        self.wait_element_located(self.driver,self.dxf_mode_loc)
        self.find_element(*self.dxf_mode_loc).click()###点击大小分
    ##获取所选场次大于8场时的提示信息--mj20171109
    def toast(self):
        self.wait_element_located(self.driver, self.nu_8)
        toast = self.find_element(*self.nu_8).text
        return toast

    #获取所选场次大于8场时点击我知道了--mj20171109
    def know(self):
        #self.wait_element_located(self.driver,self.know_loc)
        self.find_element(*self.know_loc).click()
    #点击，确认所选比赛场次---mj20171103
    def confirm_match(self):
        self.wait_element_located(self.driver,self.confirm_loc)
        self.find_element(*self.confirm_loc).click()
    ##点击清空所选比赛场次按钮  ---mj20171109
    def clear_button(self):
        self.wait_element_located(self.driver,self.delete_button_loc)
        self.find_element(*self.delete_button_loc).click()
    '''
    #展开竞足赛事详情----mj20171106
    def spread_event_details(self):
        nul = self.find_element(*self.nul_loc).text  ##获取今日比赛场次
        num = int(nul[:-1])  # 将获取的场次转换为整数
        number=0
        for i in range(1,num+1):
            number= number + 1
            self.find_element(*self.spread_event_details_loc(time,number)).click()
    '''
    #点击当天赛事场次控制展开/关闭
    def Session(self, n):
        # self.wait_element_located(self.driver,self.session(n))
        # target = self.find_element(*self.session(n))
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)#使用这种方法，今天的div会遮挡明天的div导致can not clickable
        self.driver.execute_script("window.scroll(0,0)")
        sleep(2)
        self.wait_element_located(self.driver,self.session(n))
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次
        print("我已经展开了")
    #获取当天的赛事场次，并放入列表中
    def Text_nu(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            print(id)
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list
    #获取有多少天赛事的list
    def Event_time(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list
    #当前操作天的赛事展开与否的前端js
    def This_open(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list


    def Football_mix_nu(self):####点击混合玩法显示的赛事结果
        ns=self.Text_nu()
        na=self.Event_time()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 6):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 5):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 5):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Text_ba(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list


    # 获取有多少天赛事的list
    def Event_time_ba(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def top_more(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)###鼠标拉到顶部

    def Session_ba(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次


    # 当前操作天的赛事展开与否的前端js
    def This_open_ba(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def Basketball_mix_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 5):
                            if c < 4:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 4):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 4):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Basketball_rfsf_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        list=[1,2]
                        for c in list:
                            self.Rfsf_ic(a,n,c)
                            self.Rfsf_ic(a, n, c)
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        nc = self.This_open_ba()
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    self.top_more()
                    self.Session_ba(i+1)
                    for n in range(1, nn):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_ba(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Confirm_more(self):
        self.find_element(*self.confirm_more).click()###点击展开更多页面确定按钮

    def Rfsf_ic(self,a,n,c):
        self.find_element(*self.rfsf_ic(a,n,c)).click()###点击让分胜负赛事结果


    def Basketball_mix_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 3)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_rfsf_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                c=random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Session_2(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def Football_bf(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        self.find_element(*self.football_bf(a,n)).click()
                        self.Cbf_icon()
                        self.Cbf_icon()
                        self.Confirm_more()
                        target = self.find_element(*self.VS_bf(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2


    def Football_mix_nus(self,q):
        ns = self.Text_nu()
        na = self.Event_time()
        nc=self.This_open()
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
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 4)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_bfs(self,q):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)),1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1,ns[i]+1),1):  ###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if n==1:
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                            else:
                                target = self.find_element(*self.VS_bf(a, n-1))
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 4)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        print(q)
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def More_paid_choosenumber(self):  ####竞彩篮球展开更多页面显示赛事结果
        list = []
        self.wait_element_located(self.driver, self.more_paid)
        nn = self.find_elements(*self.more_paid)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '10002':
                    self.Rfsf_icon()
                elif list[j] == '10004':
                    self.Cdxf_icon()
                elif list[j] == '10003':
                    self.Csfc_icon()
                elif list[j]=='10001':
                    self.Sf_icon()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Rfsf_icon(self):
        list=['1','2']
        for n in list:
            self.find_element(*self.rfsf_icon(n)).click()##点击让分胜负

    def Cdxf_icon(self):
        list1=['1','2']
        for n in list1:
            self.find_element(*self.cdxf_icon(n)).click()###点击猜大小分

    def Csfc_icon(self):
        list2=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list2:
            self.find_element(*self.csfc_icon(n)).click()###点击猜胜分差

    def Sf_icon(self):
        list3=['1','2']
        for n in list3:
            self.find_element(*self.sf_icon(n)).click()###点击胜负



    def More_choosenumber(self):
        ns = self.Text_nu()###读取当页展示的所有赛事场数
        na = self.Event_time()###读取当页展示的赛事天数
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    nc = self.This_open()##读取当页展示赛事天数的class值
                    '''for j in range(len(nc)):'''
                    cla = nc[i]###读取i+1天的class的值
                    print(cla)
                    if 'fold' in cla:###判断i+1天赛事是否展开
                        print("没有展开")
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事展开更多'%n)
                        self.More(a,n)###点击展开更多
                        self.More_paid_choosenumber()
                        self.More_paid_choosenumber()
                        self.Confirm_more()###点击确认
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def More_choosenumbers(self,q):
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
                            print('点击第%d天第%d场赛事展开更多' %((i+1),n))
                            if n==1:
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                            else:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                        self.top_more()
                        self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2



    def More(self,i,n):
        self.find_element(*self.more(i,n)).click()####点击展开更多

    def Cspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            self.find_element(*self.cspf_icon(n)).click()####点击猜胜平负赛事结果


    def Crqspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            sleep(5)
            self.find_element(*self.crqspf_icon(n)).click()####点击猜胜平负的第一个赛事结果

    def Cjqs_icon(self):
        list=['0','1','2','3','4','5','6','7']
        for n in list:
            self.find_element(*self.cjqs_icon(n)).click()###点击猜进球数结果

    def Cbf_icon(self):
        list=['10','20','21','30','31','32','40','41','42','50','51','52','90','00','11','22','33',
              '99','01','02','12','03','13','23','04','14','24','05','15','25','09']
        for n in list:
            self.find_element(*self.cbf_icon(n)).click()###点击猜比分结果

    def Cbqc_icon(self):
        list=['33','31','30','13','11','10','03','01','00']
        for n in list:
            self.find_element(*self.cbqc_icon(n)).click()###点击猜半全场结果

    def pull_down(self):
        target = self.find_element(*self.cjqs_icon(4))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Text_confirm_loc(self):
        nu=self.find_element(*self.confirm_loc).text#####读取混合玩法确认选号文字
        print(nu)
        return nu

    def Play_fb(self):
        aa=self.find_element(*self.play_fb).text###读取玩法文本
        print(aa)
        return aa

    def Emptying(self):
        self.find_element(*self.emptying).click()####点击清空按钮


    def sf_choose_means(self,num,time,n,number = 0):
        #number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+1):
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()#从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num+1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n+1):##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                        sleep(2)
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_choose(self, n):
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
                event_list.append(i)
                print(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:
                    self.Session(i + 1)  # 展开
                    self.find_element(*self.go_haobc_single_button_loc).click()  # 点击前往竞篮单关按钮
                    print("只有一场比赛，去往竞篮单关")
                    return 3
                elif num == 1 and len(event_time)!=1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0
    def sf_click_all_means(self,num,time):
        number = 0
        if num==1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                self.find_element(*self.event_one_loc(time,lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1,3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j+ 1)
                    print("关闭")
                    sleep(2)
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.sf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver,self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")

    def sf_edit_event(self,n):
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
                if num ==1 and event_time==1:#比赛场次只有一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择要投注1场次
                    print("比赛场次为1场")
                    return 3
                elif num == 1 and event_time != 1:#某一天的场次为一场，但所有场次不为一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:#场次为多于一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n,number=2)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Basketball_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_mix_nus_X(self,x):
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
                    for n in range(1, ns[i]+1):  ###随机取1个a对应的场次
                        if q<x:
                            a = na[i]
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 3)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Basketball_sfc_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                    self.Session_2(2)
                    a=na[1]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()###点击玩法说明

    def Race_basketball(self):
        self.wait_element_located(self.driver,self.race_basketball)
        self.find_element(*self.race_basketball).click()###点击投注竞彩蓝球

    def Event_analysis_data(self):
        na = self.Event_time()
        if na:
            b=na[0]
            self.find_element(*self.event_analysis_data(b,1)).click()
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Event_analysis_data_click(self):
        sleep(1)
        #self.wait_element_located(self.driver, self.event_analysis_data_click)
        self.find_element(*self.event_analysis_data_click).click()##点击数据分析

class HaobcChooseNumber_lelun(Page_lelun,HaobcChooseNumber_lelun_loc,PaintBallChooseNumber_lelun_loc,UChooseNum_lelun_loc):
    def Play_f(self):
        self.wait_element_located(self.driver,self.choose_mode_loc)
        self.find_element(*self.choose_mode_loc).click()###点击玩法

    def Play_mix(self):
        #self.wait_element_located(self.driver,self.mix_mode_loc)
        self.find_element(*self.mix_mode_loc).click()####点击混合投注

    def Play_sf(self):
        self.wait_element_located(self.driver,self.sf_mode_loc)
        self.find_element(*self.sf_mode_loc).click()##点击胜负

    def Play_rfsf(self):
        self.wait_element_located(self.driver,self.rfsf_mode_loc)
        self.find_element(*self.rfsf_mode_loc).click()##让分胜负

    def Play_sfc(self):
        self.wait_element_located(self.driver,self.sfc_mode_loc)
        self.find_element(*self.sfc_mode_loc).click()####点击胜负差

    def Play_dxf(self):
        self.wait_element_located(self.driver,self.dxf_mode_loc)
        self.find_element(*self.dxf_mode_loc).click()###点击大小分
    ##获取所选场次大于8场时的提示信息--mj20171109
    def toast(self):
        self.wait_element_located(self.driver, self.nu_8)
        toast = self.find_element(*self.nu_8).text
        return toast

    #获取所选场次大于8场时点击我知道了--mj20171109
    def know(self):
        #self.wait_element_located(self.driver,self.know_loc)
        self.find_element(*self.know_loc).click()
    #点击，确认所选比赛场次---mj20171103
    def confirm_match(self):
        self.wait_element_located(self.driver,self.confirm_loc)
        self.find_element(*self.confirm_loc).click()
    ##点击清空所选比赛场次按钮  ---mj20171109
    def clear_button(self):
        self.wait_element_located(self.driver,self.delete_button_loc)
        self.find_element(*self.delete_button_loc).click()
    '''
    #展开竞足赛事详情----mj20171106
    def spread_event_details(self):
        nul = self.find_element(*self.nul_loc).text  ##获取今日比赛场次
        num = int(nul[:-1])  # 将获取的场次转换为整数
        number=0
        for i in range(1,num+1):
            number= number + 1
            self.find_element(*self.spread_event_details_loc(time,number)).click()
    '''
    #点击当天赛事场次控制展开/关闭
    def Session(self, n):
        # self.wait_element_located(self.driver,self.session(n))
        # target = self.find_element(*self.session(n))
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)#使用这种方法，今天的div会遮挡明天的div导致can not clickable
        self.driver.execute_script("window.scroll(0,0)")
        sleep(2)
        self.wait_element_located(self.driver,self.session(n))
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次
        print("我已经展开了")
    #获取当天的赛事场次，并放入列表中
    def Text_nu(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            print(id)
            nnu = int(id[1])
            list.append(nnu)
        print(list)
        return list
    #获取有多少天赛事的list
    def Event_time(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list
    #当前操作天的赛事展开与否的前端js
    def This_open(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list


    def Football_mix_nu(self):####点击混合玩法显示的赛事结果
        ns=self.Text_nu()
        na=self.Event_time()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 6):
                            if c < 5:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 5):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 5):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Text_ba(self):
        list = []
        nu = self.find_elements(*self.session_nu)  ######读取当天赛事场数
        for i in range(len(nu)):
            id = nu[i].text
            nnu = int(id[1:-3])
            list.append(nnu)
        print(list)
        return list


    # 获取有多少天赛事的list
    def Event_time_ba(self):
        list = []
        nn = self.find_elements(*self.event_time)
        for i in range(len(nn)):
            id = nn[i].get_attribute('id')
            list.append(id)
        print(list)
        return list

    def top_more(self):
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)###鼠标拉到顶部

    def Session_ba(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次


    # 当前操作天的赛事展开与否的前端js
    def This_open_ba(self):
        list = []
        nn = self.find_elements(*self.this_open)
        for i in range(len(nn)):
            cl = nn[i].get_attribute('class')
            list.append(cl)
        print(list)
        return list

    def Basketball_mix_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        for c in range(2, 5):
                            if c < 4:
                                try:
                                    b = 1
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    self.find_element(*self.football_ido(a,n,c)).click()
                            else:
                                try:
                                    b = 2
                                    for c in range(2, 4):
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                except NoSuchElementException:
                                    print('没有第二行')
                                    for c in range(2, 4):
                                        self.find_element(*self.football_ido(a, n, c)).click()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Basketball_rfsf_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        list=[1,2]
                        for c in list:
                            self.Rfsf_ic(a,n,c)
                            self.Rfsf_ic(a, n, c)
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_ba(self):####点击混合玩法显示的赛事结果
        ns=self.Text_ba()
        na=self.Event_time_ba()###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_ba(i)
                        self.Session_ba(i + 1)
                    for n in range(1, nn):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def Confirm_more(self):
        self.find_element(*self.confirm_more).click()###点击展开更多页面确定按钮

    def Rfsf_ic(self,a,n,c):
        self.find_element(*self.rfsf_ic(a,n,c)).click()###点击让分胜负赛事结果


    def Basketball_mix_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 3)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_rfsf_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                c=random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                c = random.randint(1, 2)
                                self.Rfsf_ic(a, n, c)
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_bas(self,q):###随机点击混合玩法赛事结果
        ns = self.Text_ba()
        na = self.Event_time_ba()
        nc=self.This_open_ba()
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
                        self.Session_ba(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_ba(i + 1)##点击i+1天的赛事
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.top_more()
                                self.Session_ba(i + 1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Session_2(self, n):
        self.top_more()
        sleep(1)
        self.find_element(*self.session(n)).click()  ###点击当天赛事场次

    def Football_bf(self):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击第%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    if i>0:
                        self.top_more()
                        self.Session_2(i)
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事' % n)
                        self.find_element(*self.football_bf(a,n)).click()
                        self.Cbf_icon()
                        self.Cbf_icon()
                        self.Confirm_more()
                        target = self.find_element(*self.VS_bf(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2


    def Football_mix_nus(self,q):
        ns = self.Text_nu()
        na = self.Event_time()
        nc=self.This_open()
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
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):##控制循环q次
                    for i in random.sample(range(len(na)),1):###随机1个取列表na的坐标
                        for n in random.sample(range(1, ns[i] + 1),1):###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i + 1)##点击i+1天的赛事
                            b = random.randint(1, 2)##随机取b的值
                            if n == 1:
                                self.top_more()###鼠标拉到顶部
                                try:
                                    c = random.randint(2, 4)###随机取C的值
                                    self.find_element(*self.football_id(a, n, b, c)).click()###点击对应的赛事结果
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" %((i+1),n,b,(c-1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d个结果" % ((i + 1), n, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                            else:
                                target = self.find_element(*self.VS(a, n-1))####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    time.sleep(2)
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                                except NoSuchElementException:
                                    print("没有第二行")
                                    b = 1
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                    self.top_more()
                                    self.Session_2(i + 1)
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_bfs(self,q):
        ns = self.Text_nu()
        na = self.Event_time()  ###
        nc = self.This_open()
        if na:
            if len(ns)==1 and ns[0]==1:
                print('只有1场比赛')
                return 0
            else:
                for j in range(len(nc)):
                    cla=nc[j]
                    print(cla)
                    if 'fold' in cla:
                        print("没有展开赛事")
                    else:
                        self.Session_2(j+1)
                        print("收起赛事展示")
                for z in range(q):  ##控制循环q次
                    for i in random.sample(range(len(na)),1):  ###随机1个取列表na的坐标
                        for n in random.sample(range(1,ns[i]+1),1):  ###随机取1个a对应的场次
                            a=na[i]
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if n==1:
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                            else:
                                target = self.find_element(*self.VS_bf(a, n-1))
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.football_bf(a,n)).click()
                                print("点击%d天赛事" % (i+1))
                                self.Cbf_icon()
                                self.Confirm_more()
                                self.top_more()
                                self.Session_2(i+1)
                return 1

        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 4)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 4)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Football_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 4)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 4)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        print(q)
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 4)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0



    def More_paid_choosenumber(self):  ####竞彩篮球展开更多页面显示赛事结果
        list = []
        self.wait_element_located(self.driver, self.more_paid)
        nn = self.find_elements(*self.more_paid)
        for i in range(len(nn)):
            paid = nn[i].get_attribute('paid')
            list.append(paid)
        print(list)
        if list:
            for j in range(len(list)):
                if list[j] == '10002':
                    self.Rfsf_icon()
                elif list[j] == '10004':
                    self.Cdxf_icon()
                elif list[j] == '10003':
                    self.Csfc_icon()
                elif list[j]=='10001':
                    self.Sf_icon()
                else:
                    print("无匹配赛事")
            return 1
        else:
            print('占无数据')
            return 0

    def Rfsf_icon(self):
        list=['1','2']
        for n in list:
            self.find_element(*self.rfsf_icon(n)).click()##点击让分胜负

    def Cdxf_icon(self):
        list1=['1','2']
        for n in list1:
            self.find_element(*self.cdxf_icon(n)).click()###点击猜大小分

    def Csfc_icon(self):
        list2=['11','12','13','14','15','16','01','02','03','04','05','06']
        for n in list2:
            self.find_element(*self.csfc_icon(n)).click()###点击猜胜分差

    def Sf_icon(self):
        list3=['1','2']
        for n in list3:
            self.find_element(*self.sf_icon(n)).click()###点击胜负



    def More_choosenumber(self):
        ns = self.Text_nu()###读取当页展示的所有赛事场数
        na = self.Event_time()###读取当页展示的赛事天数
        if na:
            if len(ns) == 1 and ns[0] == 1:
                print('只有1场比赛')
                return 0
            else:
                for i in range(len(na)):
                    print("点击%d天赛事"%(i+1))
                    a=na[i]
                    nn=ns[i]+1
                    nc = self.This_open()##读取当页展示赛事天数的class值
                    '''for j in range(len(nc)):'''
                    cla = nc[i]###读取i+1天的class的值
                    print(cla)
                    if 'fold' in cla:###判断i+1天赛事是否展开
                        print("没有展开")
                        self.Session_2(i + 1)
                    for n in range(1, nn):
                        print('第%d场赛事展开更多'%n)
                        self.More(a,n)###点击展开更多
                        self.More_paid_choosenumber()
                        self.More_paid_choosenumber()
                        self.Confirm_more()###点击确认
                        target = self.find_element(*self.VS(a, n))
                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.top_more()
                    self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 2

    def More_choosenumbers(self,q):
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
                            print('点击第%d天第%d场赛事展开更多' %((i+1),n))
                            if n==1:
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                            else:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.More(a, n)  ###点击展开更多
                                self.More_paid_choosenumber()
                                self.Confirm_more()  ###点击确认
                        self.top_more()
                        self.Session_2(i+1)
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2



    def More(self,i,n):
        self.find_element(*self.more(i,n)).click()####点击展开更多

    def Cspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            self.find_element(*self.cspf_icon(n)).click()####点击猜胜平负赛事结果


    def Crqspf_icon(self):
        list = ['0', '1', '3']
        for n in list:
            sleep(5)
            self.find_element(*self.crqspf_icon(n)).click()####点击猜胜平负的第一个赛事结果

    def Cjqs_icon(self):
        list=['0','1','2','3','4','5','6','7']
        for n in list:
            self.find_element(*self.cjqs_icon(n)).click()###点击猜进球数结果

    def Cbf_icon(self):
        list=['10','20','21','30','31','32','40','41','42','50','51','52','90','00','11','22','33',
              '99','01','02','12','03','13','23','04','14','24','05','15','25','09']
        for n in list:
            self.find_element(*self.cbf_icon(n)).click()###点击猜比分结果

    def Cbqc_icon(self):
        list=['33','31','30','13','11','10','03','01','00']
        for n in list:
            self.find_element(*self.cbqc_icon(n)).click()###点击猜半全场结果

    def pull_down(self):
        target = self.find_element(*self.cjqs_icon(4))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Text_confirm_loc(self):
        nu=self.find_element(*self.confirm_loc).text#####读取混合玩法确认选号文字
        print(nu)
        return nu

    def Play_fb(self):
        aa=self.find_element(*self.play_fb).text###读取玩法文本
        print(aa)
        return aa

    def Emptying(self):
        self.find_element(*self.emptying).click()####点击清空按钮


    def sf_choose_means(self,num,time,n,number = 0):
        #number = 0
        if num == 1:
            if n > 9:
                for j in range(1, 3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
                    self.find_element(*self.event_one_loc(time, lies)).click()
            else:
                for k in range(1,3):
                    lies = k
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_one_loc(time, lies)).click()
        if num >= 2 and num < 9:##比赛的场次大于2场小于9场的时候，任选n场比赛
            if n < 8 and n <= num :
                for i in range(1, n+1):
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()#从一场比赛中胜平负三种结果中任选一个
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
            if n >= 8:
                for i in range(1, num+1):
                    number = number + 1
                    print(number)
                    for j in range(1, 3):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
        if num >= 9:
            if n <= 9:
                for i in range(1, n+1):##场次大于等于9时，选择n场比赛
                    number = number + 1
                    for j in random.sample(range(1, 3),1):
                        lies = j
                        self.wait_element_located(self.driver,self.event_list_loc(time,number,lies))
                        self.find_element(*self.event_list_loc(time,number,lies)).click()
                        sleep(2)
                    self.wait_element_located(self.driver,self.vs_list_loc(time,number))
                    target = self.find_element(*self.vs_list_loc(time,number))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_choose(self, n):
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
                event_list.append(i)
                print(i)
                num = text_num[i]
                print(num)
                if num == 1 and len(event_time)==1:
                    self.Session(i + 1)  # 展开
                    self.find_element(*self.go_haobc_single_button_loc).click()  # 点击前往竞篮单关按钮
                    print("只有一场比赛，去往竞篮单关")
                    return 3
                elif num == 1 and len(event_time)!=1:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")
            return 0
    def sf_click_all_means(self,num,time):
        number = 0
        if num==1:
            for j in range(1, 3):
                lies = j
                self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                self.find_element(*self.event_one_loc(time,lies)).click()
                self.find_element(*self.event_one_loc(time, lies)).click()
        else:
            for i in range(1, num + 1):
                number = number + 1
                for j in range(1,3):
                    lies = j
                    self.wait_element_located(self.driver,self.event_one_loc(time,lies))
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                    self.find_element(*self.event_list_loc(time, number, lies)).click()
                target = self.find_element(*self.vs_list_loc(time, number))
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def sf_click_all(self):
        event_time = self.Event_time()  # 获取有多少天赛事的list
        text_num = self.Text_nu()  # 获取每天的场次数list
        open_or_not = self.This_open()  # 获取当前操作天的赛事展开与否的前端js
        if event_time:
            for j in range(len(open_or_not)):
                if 'fold' in open_or_not[j]:
                    print(j)
                    print("没有展开")
                else:
                    self.Session(j+ 1)
                    print("关闭")
                    sleep(2)
            for i in event_time:
                print(event_time)
                time = i
                m = event_time.index(time)
                num = text_num[m]
                self.Session(m + 1)  # 展开
                self.sf_click_all_means(num,time)  # 选择要投注的场次
                self.Session(m + 1)  # 关闭
        else:
            self.wait_element_located(self.driver,self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            print("暂无赛事，已返回")

    def sf_edit_event(self,n):
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
                if num ==1 and event_time==1:#比赛场次只有一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择要投注1场次
                    print("比赛场次为1场")
                    return 3
                elif num == 1 and event_time != 1:#某一天的场次为一场，但所有场次不为一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, 1)  # 选择场次为一场赛事点击
                    bb = [i for i in range(0, len(event_time)) if i not in event_list]
                    aa = random.sample(bb, 1)
                    self.Session(aa[0] + 1)  # 展开另外一场比赛的赛事
                    self.sf_choose_means(text_num[aa[0]], event_time[aa[0]], n - 1)  # 选择剩下的几场赛事
                    return 4
                else:#场次为多于一场
                    self.Session(i + 1)  # 展开
                    self.sf_choose_means(num, time, n,number=2)  # 选择要投注的场次
                    return 2
        else:  # 没有赛事的时候直接返回
            self.wait_element_located(self.driver, self.back_to_homepage_loc)
            self.find_element(*self.back_to_homepage_loc).click()
            return 0

    def Basketball_mix_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % ( b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    self.Session_2(2)
                    a=na[1]
                    b = random.randint(1, 2)  ##随机取b的值
                    try:
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_id(a, 1, b, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                    except NoSuchElementException:
                        print("没有第二行")
                        c = random.randint(2, 3)  ###随机取C的值
                        self.find_element(*self.football_ido(a, 1, c)).click()  ###点击对应的赛事结果
                        print("第1天第1场赛事的第%d排的第%d个结果" % (b, (c - 1)))
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        b = random.randint(1, 2)  ##随机取b的值
                        try:
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                        except NoSuchElementException:
                            print("没有第二行")
                            c = random.randint(2, 3)  ###随机取C的值
                            self.find_element(*self.football_ido(a, n, c)).click()  ###点击对应的赛事结果
                            print("第1天第%d场赛事的第%d排的第%d个结果" % (n,b, (c - 1)))
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_mix_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            b = random.randint(1, 2)  ##随机取b的值
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                try:
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_id(a, n, b, c)).click()
                                    self.know()
                                    print("第%d场，成功点击知道了"%n)
                                    q = q + 1
                                except NoSuchElementException:
                                    print("没有第二行")
                                    c = random.randint(2, 3)
                                    self.find_element(*self.football_ido(a, n, c)).click()
                                    self.know()
                                    q = q + 1
                                    print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    try:
                                        c = random.randint(2, 3)  ###随机取C的值
                                        self.find_element(*self.football_id(a, n, b, c)).click()  ###点击对应的赛事结果
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q=q+1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    try:
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_id(a, n, b, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                                    except NoSuchElementException:
                                        print("没有第二行")
                                        c = random.randint(2, 3)
                                        self.find_element(*self.football_ido(a, n, c)).click()
                                        print("第%d天第%d场赛事的第%d排的第%d个结果" % ((i + 1), n, b, (c - 1)))
                                        q = q + 1
                                        self.top_more()
                                        time.sleep(1)
                                        self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 0

    def Basketball_sfc_nus_too(self):
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
                if ns[0]==1:
                    self.Session_2(1)
                    a=na[0]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                    self.Session_2(2)
                    a=na[1]
                    self.find_element(*self.sfc_ic(a, 1)).click()
                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                    for j in list4:
                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                    self.Confirm_more()
                else:
                    self.Session_2(1)
                    a = na[0]
                    for n in (1,2):
                        self.find_element(*self.sfc_ic(a, n)).click()
                        list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                        for j in list4:
                            self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                        self.Confirm_more()
                return 1
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_loc).click()
            return 2

    def Basketball_sfc_nus_X(self,x):
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
                            sleep(1)
                            self.Session_2(i+1)  ##点击i+1天的赛事
                            if q>7:
                                target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                self.find_element(*self.sfc_ic(a, n)).click()
                                list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                for j in list4:
                                    self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                self.Confirm_more()
                                self.know()
                                q = q + 1
                                print("第%d场，成功点击知道了" % n)
                            else:
                                if q == 0:
                                    self.top_more()  ###鼠标拉到顶部
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
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
                                        target = self.find_element(*self.VS(a, n - 1))  ####定位到n-1场赛事的VS
                                        self.driver.execute_script("arguments[0].scrollIntoView();", target)
                                    self.find_element(*self.sfc_ic(a, n)).click()
                                    list4 = ['01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16']
                                    for j in list4:
                                        self.find_element(*self.csfc_icon(j)).click()  ##点击胜负差
                                    self.Confirm_more()
                                    q = q + 1
                                    self.top_more()
                                    time.sleep(1)
                                    self.Session_2(i + 1)
                return q
        else:
            print('，没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()###点击玩法说明

    def Race_basketball(self):
        self.find_element(*self.race_basketball).click()###点击投注竞彩蓝球

    def Event_analysis_data(self):
        na = self.Event_time()
        if na:
            b=na[0]
            self.find_element(*self.event_analysis_data(b,1)).click()
            return 1
        else:
            print('没有赛事展示')
            self.find_element(*self.return_link_jl_loc).click()
            return 0

    def Event_analysis_data_click(self):
        sleep(1)
        #self.wait_element_located(self.driver, self.event_analysis_data_click)
        self.find_element(*self.event_analysis_data_click).click()##点击数据分析

