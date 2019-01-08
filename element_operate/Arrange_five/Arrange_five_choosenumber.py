from element_operate.base import Page
from element_position.lemi import Arrang_five_num
import random
from element_operate.base import Page_lexiu
from element_position.lexiu import Arrang_five_num_lexiu
from element_operate.base import Page_leyou
from element_position.leyou import Arrang_five_num_leyou
from element_operate.base import Page_lelun
from element_position.lelun import Arrang_five_num_lelun

class ArrangeFiveChooseNumber(Page,Arrang_five_num):
#############################################排列5选号###################################1018

    ####################点击万位0-9数字
    def Afive_nuw(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_w(i, n)).click()  # 点击万位0-9个数字


    ###################随机点击万位数字
    def Afive_nuws(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_w(2, a)).click()
            else:
                self.find_element(*self.nu_w(1, n)).click()
            a = n - 1
            print('点击万位:%d' % a)


    ################### 点击千位0-9个数字
    def Afive_nuq(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_q(i, n)).click()  # 点击千位0-9个数字


    ######################随机点击千位数字
    def Afive_nuqs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_q(2, a)).click()
            else:
                self.find_element(*self.nu_q(1, n)).click()
            a = n - 1
            print('点击千位:%d' % a)


    ####################### 点击百位0-9个数字
    def Afive_nub(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_b(i, n)).click()  # 点击百位0-9个数字


    #########################随机点击百位数字
    def Afive_nubs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_b(2, a)).click()
            else:
                self.find_element(*self.nu_b(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)


    ###################### 点击十位0-9个数字
    def Afive_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_s(i, n)).click()  # 点击十位0-9个数字


    ####################随机点击十位数字
    def Afive_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_s(2, a)).click()
            else:
                self.find_element(*self.nu_s(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)


    ###################### 点击个位0-9个数字
    def Afive_nug(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_g(i, n)).click()  # 点击个位0-9个数字


    #######################随机点击个位数字
    def Afive_nugs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_g(2, a)).click()
            else:
                self.find_element(*self.nu_g(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)


    ####################鼠标下拉到底部
    def Afive_down(self):
        target = self.find_element(*self.down_nu)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)


    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)


    ####################点击确认选号
    def Confirm_nu(self):
        self.wait_element_located(self.driver, self.confirm_nu)
        self.find_element(*self.confirm_nu).click()

    def history_arrange_five_date(self):
        a=self.find_elements(*self.history_date)
        i=random.randint(0,len(a)-1)
        b=a[i].text
        return b


class ArrangeFiveChooseNumber_lexiu(Page_lexiu,Arrang_five_num_lexiu):
#############################################排列5选号###################################1018

    ####################点击万位0-9数字
    def Afive_nuw(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_w(i, n)).click()  # 点击万位0-9个数字


    ###################随机点击万位数字
    def Afive_nuws(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_w(2, a)).click()
            else:
                self.find_element(*self.nu_w(1, n)).click()
            a = n - 1
            print('点击万位:%d' % a)


    ################### 点击千位0-9个数字
    def Afive_nuq(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_q(i, n)).click()  # 点击千位0-9个数字


    ######################随机点击千位数字
    def Afive_nuqs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_q(2, a)).click()
            else:
                self.find_element(*self.nu_q(1, n)).click()
            a = n - 1
            print('点击千位:%d' % a)


    ####################### 点击百位0-9个数字
    def Afive_nub(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_b(i, n)).click()  # 点击百位0-9个数字


    #########################随机点击百位数字
    def Afive_nubs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_b(2, a)).click()
            else:
                self.find_element(*self.nu_b(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)


    ###################### 点击十位0-9个数字
    def Afive_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_s(i, n)).click()  # 点击十位0-9个数字


    ####################随机点击十位数字
    def Afive_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_s(2, a)).click()
            else:
                self.find_element(*self.nu_s(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)


    ###################### 点击个位0-9个数字
    def Afive_nug(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_g(i, n)).click()  # 点击个位0-9个数字


    #######################随机点击个位数字
    def Afive_nugs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_g(2, a)).click()
            else:
                self.find_element(*self.nu_g(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)


    ####################鼠标下拉到底部
    def Afive_down(self):
        target = self.find_element(*self.down_nu)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)


    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)


    ####################点击确认选号
    def Confirm_nu(self):
        self.wait_element_located(self.driver, self.confirm_nu)
        self.find_element(*self.confirm_nu).click()

    def history_arrange_five_date(self):
        a=self.find_elements(*self.history_date)
        i=random.randint(0,len(a)-1)
        b=a[i].text
        return b

class ArrangeFiveChooseNumber_leyou(Page_leyou,Arrang_five_num_leyou):
#############################################排列5选号###################################1018

    ####################点击万位0-9数字
    def Afive_nuw(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_w(i, n)).click()  # 点击万位0-9个数字


    ###################随机点击万位数字
    def Afive_nuws(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_w(2, a)).click()
            else:
                self.find_element(*self.nu_w(1, n)).click()
            a = n - 1
            print('点击万位:%d' % a)


    ################### 点击千位0-9个数字
    def Afive_nuq(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_q(i, n)).click()  # 点击千位0-9个数字


    ######################随机点击千位数字
    def Afive_nuqs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_q(2, a)).click()
            else:
                self.find_element(*self.nu_q(1, n)).click()
            a = n - 1
            print('点击千位:%d' % a)


    ####################### 点击百位0-9个数字
    def Afive_nub(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_b(i, n)).click()  # 点击百位0-9个数字


    #########################随机点击百位数字
    def Afive_nubs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_b(2, a)).click()
            else:
                self.find_element(*self.nu_b(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)


    ###################### 点击十位0-9个数字
    def Afive_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_s(i, n)).click()  # 点击十位0-9个数字


    ####################随机点击十位数字
    def Afive_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_s(2, a)).click()
            else:
                self.find_element(*self.nu_s(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)


    ###################### 点击个位0-9个数字
    def Afive_nug(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_g(i, n)).click()  # 点击个位0-9个数字


    #######################随机点击个位数字
    def Afive_nugs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_g(2, a)).click()
            else:
                self.find_element(*self.nu_g(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)


    ####################鼠标下拉到底部
    def Afive_down(self):
        target = self.find_element(*self.down_nu)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)


    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)


    ####################点击确认选号
    def Confirm_nu(self):
        self.wait_element_located(self.driver, self.confirm_nu)
        self.find_element(*self.confirm_nu).click()

    def history_arrange_five_date(self):
        a=self.find_elements(*self.history_date)
        i=random.randint(0,len(a)-1)
        b=a[i].text
        return b

class ArrangeFiveChooseNumber_lelun(Page_lelun,Arrang_five_num_lelun):
#############################################排列5选号###################################1018

    ####################点击万位0-9数字
    def Afive_nuw(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_w(i, n)).click()  # 点击万位0-9个数字


    ###################随机点击万位数字
    def Afive_nuws(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_w(2, a)).click()
            else:
                self.find_element(*self.nu_w(1, n)).click()
            a = n - 1
            print('点击万位:%d' % a)


    ################### 点击千位0-9个数字
    def Afive_nuq(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_q(i, n)).click()  # 点击千位0-9个数字


    ######################随机点击千位数字
    def Afive_nuqs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_q(2, a)).click()
            else:
                self.find_element(*self.nu_q(1, n)).click()
            a = n - 1
            print('点击千位:%d' % a)


    ####################### 点击百位0-9个数字
    def Afive_nub(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_b(i, n)).click()  # 点击百位0-9个数字


    #########################随机点击百位数字
    def Afive_nubs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_b(2, a)).click()
            else:
                self.find_element(*self.nu_b(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)


    ###################### 点击十位0-9个数字
    def Afive_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_s(i, n)).click()  # 点击十位0-9个数字


    ####################随机点击十位数字
    def Afive_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_s(2, a)).click()
            else:
                self.find_element(*self.nu_s(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)


    ###################### 点击个位0-9个数字
    def Afive_nug(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_g(i, n)).click()  # 点击个位0-9个数字


    #######################随机点击个位数字
    def Afive_nugs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_g(2, a)).click()
            else:
                self.find_element(*self.nu_g(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)


    ####################鼠标下拉到底部
    def Afive_down(self):
        target = self.find_element(*self.down_nu)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)


    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)


    ####################点击确认选号
    def Confirm_nu(self):
        self.wait_element_located(self.driver, self.confirm_nu)
        self.find_element(*self.confirm_nu).click()

    def history_arrange_five_date(self):
        a=self.find_elements(*self.history_date)
        i=random.randint(0,len(a)-1)
        b=a[i].text
        return b

