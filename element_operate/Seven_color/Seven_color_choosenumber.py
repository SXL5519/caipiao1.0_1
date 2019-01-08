from element_position.lemi import seven_color_num
import random
from time import sleep
from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lexiu import seven_color_num_lexiu
from element_operate.base import Page_lexiu
from element_position.leyou import seven_color_num_leyou
from element_operate.base import Page_leyou
from element_position.lelun import seven_color_num_lelun
from element_operate.base import Page_lelun

class Seven_color_choosenumber(Page,seven_color_num,):
    ############点击第一位的0-9的数字
    def Seven_nuo(self):
        for i in range(1,3):
            for n in range(1,6):
                self.find_element(*self.nu_one(i, n)).click()#点击第一位的数字

    ##############随机点击第一位的i+j个数字
    def Seven_nuos(self,i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_one(2, a)).click()
            else:
                self.find_element(*self.nu_one(1, n)).click()
            a = n - 1
            print('点击第一位:%d' % a)
                ############点击第二位的0-9的数字
    def Seven_nut(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_too(i, n)).click()  # 点击第二位的数字

        ##############随机点击第二位的i+j个数字
    def Seven_nuts(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_too(2, a)).click()
            else:
                self.find_element(*self.nu_too(1, n)).click()
            a = n - 1
            print('点击第二位:%d' % a)

           ############点击第三位的0-9的数字
    def Seven_nuth(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_there(i, n)).click()  # 点击第三位的数字

        ##############随机点击第三位的i+j个数字
    def Seven_nuths(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_there(2, a)).click()
            else:
                self.find_element(*self.nu_there(1, n)).click()
            a = n - 1
            print('点击第三位:%d' % a)

       ############点击第四位的0-9的数字
    def Seven_nuf(self):
        target = self.find_element(*self.nu_there(2, 1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_four(i, n)).click()  # 点击第四位的数字

        ##############随机点击第四位的i+j个数字
    def Seven_nufs(self, i):
        target = self.find_element(*self.nu_there(2,1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_four(2, a)).click()
            else:
                self.find_element(*self.nu_four(1, n)).click()
            a = n - 1
            print('点击第四位:%d' % a)

  ############点击第五位的0-9的数字
    def Seven_nufi(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_five(i, n)).click()  # 点击第五位的数字

        ##############随机点击第五位的i+j个数字
    def Seven_nufis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_five(2, a)).click()
            else:
                self.find_element(*self.nu_five(1, n)).click()
            a = n - 1
            print('点击第五位:%d' % a)

############点击第六位的0-9的数字
    def Seven_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_six(i, n)).click()  # 点击第六位的数字

        ##############随机点击第六位的i+j个数字
    def Seven_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_six(2, a)).click()
            else:
                self.find_element(*self.nu_six(1, n)).click()
            a = n - 1
            print('点击第六位:%d' % a)

############点击第七位的0-9的数字
    def Seven_nuse(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_seven(i, n)).click()  # 点击第七位的数字

        ##############随机点击第七位的i+j个数字
    def Seven_nuses(self, i):
        self.Afive_down()
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                print(a)
                self.find_element(*self.nu_seven(2, a)).click()
            else:
                self.find_element(*self.nu_seven(1, n)).click()
            a = n - 1
            print('点击第七位:%d' % a)


####################鼠标下拉到底部
    def Afive_down(self):
        js = "window.scroll(0,5000)"
        self.driver.execute_script(js)

######鼠标上移到顶
    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)

    def Seven_color_instruct(self):
        self.find_element(*self.seven_color_instruct).click()##点击玩法说明

    def Seven_color_play(self):
        a=self.find_element(*self.seven_color_play).text###读取玩法说明中的，七星彩玩法
        return a

    def Seven_color_know(self):
        self.find_element(*self.seven_color_know).click()##点击玩法说明，知道了

    def Seven_color_history(self):
        self.find_element(*self.seven_color_history).click()##点击历史走势

    def History_date(self):
        a=self.find_elements(*self.history_date)##取历史数据显示号码list
        i=random.randint(0,len(a)-1)##随机产生i
        b=a[i].text###取i对应的显示号码
        return b

    def Seven_color_lor(self):
        a=self.find_element(*self.seven_color_lor).text###读取七星彩文本
        return a

class Seven_color_choosenumber_lexiu(Page_lexiu,seven_color_num_lexiu):
    ############点击第一位的0-9的数字
    def Seven_nuo(self):
        for i in range(1,3):
            for n in range(1,6):
                self.find_element(*self.nu_one(i, n)).click()#点击第一位的数字

    ##############随机点击第一位的i+j个数字
    def Seven_nuos(self,i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_one(2, a)).click()
            else:
                self.find_element(*self.nu_one(1, n)).click()
            a = n - 1
            print('点击第一位:%d' % a)
                ############点击第二位的0-9的数字
    def Seven_nut(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_too(i, n)).click()  # 点击第二位的数字

        ##############随机点击第二位的i+j个数字
    def Seven_nuts(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_too(2, a)).click()
            else:
                self.find_element(*self.nu_too(1, n)).click()
            a = n - 1
            print('点击第二位:%d' % a)

           ############点击第三位的0-9的数字
    def Seven_nuth(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_there(i, n)).click()  # 点击第三位的数字

        ##############随机点击第三位的i+j个数字
    def Seven_nuths(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_there(2, a)).click()
            else:
                self.find_element(*self.nu_there(1, n)).click()
            a = n - 1
            print('点击第三位:%d' % a)

       ############点击第四位的0-9的数字
    def Seven_nuf(self):
        target = self.find_element(*self.nu_there(2, 1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_four(i, n)).click()  # 点击第四位的数字

        ##############随机点击第四位的i+j个数字
    def Seven_nufs(self, i):
        target = self.find_element(*self.nu_there(2,1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_four(2, a)).click()
            else:
                self.find_element(*self.nu_four(1, n)).click()
            a = n - 1
            print('点击第四位:%d' % a)

  ############点击第五位的0-9的数字
    def Seven_nufi(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_five(i, n)).click()  # 点击第五位的数字

        ##############随机点击第五位的i+j个数字
    def Seven_nufis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_five(2, a)).click()
            else:
                self.find_element(*self.nu_five(1, n)).click()
            a = n - 1
            print('点击第五位:%d' % a)

############点击第六位的0-9的数字
    def Seven_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_six(i, n)).click()  # 点击第六位的数字

        ##############随机点击第六位的i+j个数字
    def Seven_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_six(2, a)).click()
            else:
                self.find_element(*self.nu_six(1, n)).click()
            a = n - 1
            print('点击第六位:%d' % a)

############点击第七位的0-9的数字
    def Seven_nuse(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_seven(i, n)).click()  # 点击第七位的数字

        ##############随机点击第七位的i+j个数字
    def Seven_nuses(self, i):
        self.Afive_down()
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                print(a)
                self.find_element(*self.nu_seven(2, a)).click()
            else:
                self.find_element(*self.nu_seven(1, n)).click()
            a = n - 1
            print('点击第七位:%d' % a)


####################鼠标下拉到底部
    def Afive_down(self):
        js = "window.scroll(0,5000)"
        self.driver.execute_script(js)

######鼠标上移到顶
    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)

    def Seven_color_instruct(self):
        self.find_element(*self.seven_color_instruct).click()##点击玩法说明

    def Seven_color_play(self):
        a=self.find_element(*self.seven_color_play).text###读取玩法说明中的，七星彩玩法
        return a

    def Seven_color_know(self):
        self.find_element(*self.seven_color_know).click()##点击玩法说明，知道了

    def Seven_color_history(self):
        self.find_element(*self.seven_color_history).click()##点击历史走势

    def History_date(self):
        a=self.find_elements(*self.history_date)##取历史数据显示号码list
        i=random.randint(0,len(a)-1)##随机产生i
        b=a[i].text###取i对应的显示号码
        return b

    def Seven_color_lor(self):
        a=self.find_element(*self.seven_color_lor).text###读取七星彩文本
        return a

class Seven_color_choosenumber_leyou(Page_leyou,seven_color_num_leyou):
    ############点击第一位的0-9的数字
    def Seven_nuo(self):
        for i in range(1,3):
            for n in range(1,6):
                self.find_element(*self.nu_one(i, n)).click()#点击第一位的数字

    ##############随机点击第一位的i+j个数字
    def Seven_nuos(self,i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_one(2, a)).click()
            else:
                self.find_element(*self.nu_one(1, n)).click()
            a = n - 1
            print('点击第一位:%d' % a)
                ############点击第二位的0-9的数字
    def Seven_nut(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_too(i, n)).click()  # 点击第二位的数字

        ##############随机点击第二位的i+j个数字
    def Seven_nuts(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_too(2, a)).click()
            else:
                self.find_element(*self.nu_too(1, n)).click()
            a = n - 1
            print('点击第二位:%d' % a)

           ############点击第三位的0-9的数字
    def Seven_nuth(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_there(i, n)).click()  # 点击第三位的数字

        ##############随机点击第三位的i+j个数字
    def Seven_nuths(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_there(2, a)).click()
            else:
                self.find_element(*self.nu_there(1, n)).click()
            a = n - 1
            print('点击第三位:%d' % a)

       ############点击第四位的0-9的数字
    def Seven_nuf(self):
        target = self.find_element(*self.nu_there(2, 1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_four(i, n)).click()  # 点击第四位的数字

        ##############随机点击第四位的i+j个数字
    def Seven_nufs(self, i):
        target = self.find_element(*self.nu_there(2,1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_four(2, a)).click()
            else:
                self.find_element(*self.nu_four(1, n)).click()
            a = n - 1
            print('点击第四位:%d' % a)

  ############点击第五位的0-9的数字
    def Seven_nufi(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_five(i, n)).click()  # 点击第五位的数字

        ##############随机点击第五位的i+j个数字
    def Seven_nufis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_five(2, a)).click()
            else:
                self.find_element(*self.nu_five(1, n)).click()
            a = n - 1
            print('点击第五位:%d' % a)

############点击第六位的0-9的数字
    def Seven_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_six(i, n)).click()  # 点击第六位的数字

        ##############随机点击第六位的i+j个数字
    def Seven_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_six(2, a)).click()
            else:
                self.find_element(*self.nu_six(1, n)).click()
            a = n - 1
            print('点击第六位:%d' % a)

############点击第七位的0-9的数字
    def Seven_nuse(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_seven(i, n)).click()  # 点击第七位的数字

        ##############随机点击第七位的i+j个数字
    def Seven_nuses(self, i):
        self.Afive_down()
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                print(a)
                self.find_element(*self.nu_seven(2, a)).click()
            else:
                self.find_element(*self.nu_seven(1, n)).click()
            a = n - 1
            print('点击第七位:%d' % a)


####################鼠标下拉到底部
    def Afive_down(self):
        js = "window.scroll(0,5000)"
        self.driver.execute_script(js)

######鼠标上移到顶
    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)

    def Seven_color_instruct(self):
        self.find_element(*self.seven_color_instruct).click()##点击玩法说明

    def Seven_color_play(self):
        a=self.find_element(*self.seven_color_play).text###读取玩法说明中的，七星彩玩法
        return a

    def Seven_color_know(self):
        self.find_element(*self.seven_color_know).click()##点击玩法说明，知道了

    def Seven_color_history(self):
        self.find_element(*self.seven_color_history).click()##点击历史走势

    def History_date(self):
        a=self.find_elements(*self.history_date)##取历史数据显示号码list
        i=random.randint(0,len(a)-1)##随机产生i
        b=a[i].text###取i对应的显示号码
        return b

    def Seven_color_lor(self):
        a=self.find_element(*self.seven_color_lor).text###读取七星彩文本
        return a

class Seven_color_choosenumber_lelun(Page_lelun,seven_color_num_lelun):
    ############点击第一位的0-9的数字
    def Seven_nuo(self):
        for i in range(1,3):
            for n in range(1,6):
                self.find_element(*self.nu_one(i, n)).click()#点击第一位的数字

    ##############随机点击第一位的i+j个数字
    def Seven_nuos(self,i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_one(2, a)).click()
            else:
                self.find_element(*self.nu_one(1, n)).click()
            a = n - 1
            print('点击第一位:%d' % a)
                ############点击第二位的0-9的数字
    def Seven_nut(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_too(i, n)).click()  # 点击第二位的数字

        ##############随机点击第二位的i+j个数字
    def Seven_nuts(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_too(2, a)).click()
            else:
                self.find_element(*self.nu_too(1, n)).click()
            a = n - 1
            print('点击第二位:%d' % a)

           ############点击第三位的0-9的数字
    def Seven_nuth(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_there(i, n)).click()  # 点击第三位的数字

        ##############随机点击第三位的i+j个数字
    def Seven_nuths(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_there(2, a)).click()
            else:
                self.find_element(*self.nu_there(1, n)).click()
            a = n - 1
            print('点击第三位:%d' % a)

       ############点击第四位的0-9的数字
    def Seven_nuf(self):
        target = self.find_element(*self.nu_there(2, 1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_four(i, n)).click()  # 点击第四位的数字

        ##############随机点击第四位的i+j个数字
    def Seven_nufs(self, i):
        target = self.find_element(*self.nu_there(2,1))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_four(2, a)).click()
            else:
                self.find_element(*self.nu_four(1, n)).click()
            a = n - 1
            print('点击第四位:%d' % a)

  ############点击第五位的0-9的数字
    def Seven_nufi(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_five(i, n)).click()  # 点击第五位的数字

        ##############随机点击第五位的i+j个数字
    def Seven_nufis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_five(2, a)).click()
            else:
                self.find_element(*self.nu_five(1, n)).click()
            a = n - 1
            print('点击第五位:%d' % a)

############点击第六位的0-9的数字
    def Seven_nus(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_six(i, n)).click()  # 点击第六位的数字

        ##############随机点击第六位的i+j个数字
    def Seven_nuss(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_six(2, a)).click()
            else:
                self.find_element(*self.nu_six(1, n)).click()
            a = n - 1
            print('点击第六位:%d' % a)

############点击第七位的0-9的数字
    def Seven_nuse(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.find_element(*self.nu_seven(i, n)).click()  # 点击第七位的数字

        ##############随机点击第七位的i+j个数字
    def Seven_nuses(self, i):
        self.Afive_down()
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                print(a)
                self.find_element(*self.nu_seven(2, a)).click()
            else:
                self.find_element(*self.nu_seven(1, n)).click()
            a = n - 1
            print('点击第七位:%d' % a)


####################鼠标下拉到底部
    def Afive_down(self):
        js = "window.scroll(0,5000)"
        self.driver.execute_script(js)

######鼠标上移到顶
    def Afive_top(self):
        target = self.find_element(*self.down_top)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)

    def Seven_color_instruct(self):
        self.find_element(*self.seven_color_instruct).click()##点击玩法说明

    def Seven_color_play(self):
        a=self.find_element(*self.seven_color_play).text###读取玩法说明中的，七星彩玩法
        return a

    def Seven_color_know(self):
        self.find_element(*self.seven_color_know).click()##点击玩法说明，知道了

    def Seven_color_history(self):
        self.find_element(*self.seven_color_history).click()##点击历史走势

    def History_date(self):
        a=self.find_elements(*self.history_date)##取历史数据显示号码list
        i=random.randint(0,len(a)-1)##随机产生i
        b=a[i].text###取i对应的显示号码
        return b

    def Seven_color_lor(self):
        a=self.find_element(*self.seven_color_lor).text###读取七星彩文本
        return a