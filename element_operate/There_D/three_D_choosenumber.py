from element_position.lemi import there_D_loc
from element_operate.base import Page
import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from element_position.lexiu import there_D_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import there_D_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import there_D_lelun_loc
from element_operate.base import Page_lelun
class There_D_choosenumber(Page,there_D_loc):
    def Play_d(self):
        self.find_element(*self.play_d).click()###点击玩法

    def Play_direct_d(self):
        self.find_element(*self.play_direct_d).click()###点击直选

    def Play_group_there_d(self):
        self.find_element(*self.play_group_there_d).click()###点击组三

    def Play_group_six_d(self):
        self.find_element(*self.play_group_six_d).click()###点击组六

    def Play_group_direct_add_d(self):
        self.find_element(*self.play_direct_add_d).click()###点击直选和值

    def Play_group_there_add_d(self):
        self.find_element(*self.play_group_there_add_d).click()###点击组三和值

    def Play_group_six_add_d(self):
        self.find_element(*self.play_group_six_add_d).click()###点击组六和值

#################选号
    def there_D_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai_d(i, n))
                self.find_element(*self.nu_bai_d(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_D_bais(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_bai_d(1, n))
                self.find_element(*self.nu_bai_d(1, n)).click()
                a = n - 1
                print('点击百位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_bai_d(2, n))
                self.find_element(*self.nu_bai_d(2, n)).click()
                a = n + 4
                print('点击百位:%d' % a)

    def there_D_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi_d(i, n))
                self.find_element(*self.nu_shi_d(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_D_shis(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_shi_d(1, n))
                self.find_element(*self.nu_shi_d(1, n)).click()
                a = n - 1
                print('点击十位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_shi_d(2, n))
                self.find_element(*self.nu_shi_d(2, n)).click()
                a = n + 4
                print('点击十位:%d' % a)

    def there_D_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge_d(i, n))
                self.find_element(*self.nu_ge_d(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_D_ges(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_ge_d(1, n))
                self.find_element(*self.nu_ge_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_ge_d(2, n))
                self.find_element(*self.nu_ge_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

                #############组三选号

    def group_there_d(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.wait_element_located(self.driver, self.g_there_d(i, n))
                self.find_element(*self.g_there_d(i, n)).click()  # 点击数字球

    def group_theres_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_there_d(1, n))
                self.find_element(*self.g_there_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_there_d(2, n))
                self.find_element(*self.g_there_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

    def Screening_d(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_d(list[i]))
            self.find_element(*self.screening_d(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

###############组六选号
    def group_six_d(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six_d(i, n))
                self.find_element(*self.g_six_d(i, n)).click()#点击数字球

    def group_sixs_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_six_d(1, n))
                self.find_element(*self.g_six_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_six_d(2, n))
                self.find_element(*self.g_six_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

###############直选和值
    def Direct_add(self,n):
        for i in random.sample(range(1,29),n):
            self.find_element(*self.direct_add(i)).click()##点击i-1
            a=i-1
            print('点击%d'%a)

    def Direct_add_one(self):
        i=1
        self.find_element(*self.direct_add(i)).click()##点击i-1
        a=i-1
        print('点击%d'%a)

    def Direct_addA(self):
        for i in random.sample(range(1, 29), 1):
            self.find_element(*self.direct_add(i)).click()
            c = i - 1
            print('点击1个数字%d' % c)
            if i > 14:
                n = i - 14
                i = i - (2 * n - 1)
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b
            else:
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b

##################组三和值
    def Group_there_add(self,n):
        for i in random.sample(range(1,27),n):
            self.find_element(*self.group_there_add(i)).click()##点击n个数字
            print('点击%d'%i)

    def Group_there_add_one(self):
        i=1
        self.find_element(*self.group_there_add(i)).click()##点击n个数字
        print('点击%d'%i)

    def Group_there_addA(self):
        for i in random.sample(range(1,27),1):
            self.find_element(*self.group_there_add(i)).click()######点击一个数字i
            print('点击1个数字%d' %i)
            if i>13:
                n=i-13
                i=i-(2*n-1)
            list=[1,3]
            list1=[4,5,6]
            list2=[7,9,12]
            list3=[8,10,11,13]
            if i in list:
                a=1
                b=str(a)
                return b
            if i==2:
                a=2
                b=str(a)
                return b
            if i in list1:
                a=3
                b=str(a)
                return b
            if i in list2:
                a=4
                b=str(a)
                return b
            if i in list3:
                a=5
                b=str(a)
                return b

##################组六和值
    def Group_six_add(self,n):
        for i in random.sample(range(1,23),n):
            self.find_element(*self.group_six_add(i)).click()##点击n个数字
            a=i+2
            print('点击%d'%a)

    def Group_six_add_one(self):
        i=1
        self.find_element(*self.group_six_add(i)).click()##点击n个数字
        print('点击%d'%(i+2))

    def Group_six_addA(self):
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        for i in random.sample(range(1, 23), 1):
            self.wait_element_located(self.driver, self.group_six_add(i))
            self.find_element(*self.group_six_add(i)).click()  ######点击一个数字i
            print('点击1个数字%d' % (i + 2))
            if i in list:
                b = str(i - 1)
                return b
            if i in list4:
                b = str(i)
                return b
            if i in list1:
                a = 10
                b = str(a)
                return b
            if i in list3:
                a = 1
                b = str(a)
                return b
            if i in list2:
                n = i - 11
                b = str(i - (2 * n))
                return b
            if i in list5:
                n = i - 11
                b = str(i - (2 * n - 1))
                return b

    def Show_play(self):
        a=self.find_element(*self.show_play).text###读取显示的玩法
        return a

    def Instruct(self):
        self.find_element(*self.instruct).click()##点击右上角....

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()##点击玩法说明

    def Group_there_add_play_instruction(self):
        a=self.find_element(*self.group_there_add_play_instruction).text###玩法说明页读取组三和值
        return a

    def There_D_know(self):
        self.find_element(*self.there_D_know).click()

    def History(self):
        self.find_element(*self.history).click()##点击历史走势

    def Charts(self):
        aa=self.find_elements(*self.charts_list)
        n=random.sample(range(len(aa)),1)
        a=self.find_element(*self.charts(n[0]+1)).text##读取历史走势里的数据
        return a

    def Recommend(self):
        a=self.find_element(*self.recommend).text###读取推荐的号码
        return a

    def Use_recommend(self):
        self.find_element(*self.use_recommend).click()###点击使用推荐号码

    def Number(self):
        a=self.find_element(*self.number).text
        return a

    def Clear(self):
        a=self.find_element(*self.clear).text##读取弹框，清楚文本
        return a

    def Del_x(self):
        self.find_element(*self.del_x).click()##点击X按钮

    def Coun_number(self):
        self.find_element(*self.coun_number).click()##点击继续选号

    def Pause_d(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)+1
        if i > 14:
            n = i - 14
            i = i - (2 * n - 1)
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b
        else:
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b

    def Pause_d_there(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)
        if i > 13:
            n = i - 13
            i = i - (2 * n - 1)
        list = [1, 3]
        list1 = [4, 5, 6]
        list2 = [7, 9, 12]
        list3 = [8, 10, 11, 13]
        if i in list:
            a = 1
            b = str(a)
            return b
        if i == 2:
            a = 2
            b = str(a)
            return b
        if i in list1:
            a = 3
            b = str(a)
            return b
        if i in list2:
            a = 4
            b = str(a)
            return b
        if i in list3:
            a = 5
            b = str(a)
            return b

    def Pause_d_six(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)-2
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        if i in list:
            b = str(i - 1)
            return b
        if i in list4:
            b = str(i)
            return b
        if i in list1:
            a = 10
            b = str(a)
            return b
        if i in list3:
            a = 1
            b = str(a)
            return b
        if i in list2:
            n = i - 11
            b = str(i - (2 * n))
            return b
        if i in list5:
            n = i - 11
            b = str(i - (2 * n - 1))
            return b

class There_D_choosenumber_lexiu(Page_lexiu,there_D_lexiu_loc):
    def Play_d(self):
        self.find_element(*self.play_d).click()###点击玩法

    def Play_direct_d(self):
        self.find_element(*self.play_direct_d).click()###点击直选

    def Play_group_there_d(self):
        self.find_element(*self.play_group_there_d).click()###点击组三

    def Play_group_six_d(self):
        self.find_element(*self.play_group_six_d).click()###点击组六

    def Play_group_direct_add_d(self):
        self.find_element(*self.play_direct_add_d).click()###点击直选和值

    def Play_group_there_add_d(self):
        self.find_element(*self.play_group_there_add_d).click()###点击组三和值

    def Play_group_six_add_d(self):
        self.find_element(*self.play_group_six_add_d).click()###点击组六和值

#################选号
    def there_D_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai_d(i, n))
                self.find_element(*self.nu_bai_d(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_D_bais(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_bai_d(1, n))
                self.find_element(*self.nu_bai_d(1, n)).click()
                a = n - 1
                print('点击百位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_bai_d(2, n))
                self.find_element(*self.nu_bai_d(2, n)).click()
                a = n + 4
                print('点击百位:%d' % a)

    def there_D_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi_d(i, n))
                self.find_element(*self.nu_shi_d(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_D_shis(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_shi_d(1, n))
                self.find_element(*self.nu_shi_d(1, n)).click()
                a = n - 1
                print('点击十位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_shi_d(2, n))
                self.find_element(*self.nu_shi_d(2, n)).click()
                a = n + 4
                print('点击十位:%d' % a)

    def there_D_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge_d(i, n))
                self.find_element(*self.nu_ge_d(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_D_ges(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_ge_d(1, n))
                self.find_element(*self.nu_ge_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_ge_d(2, n))
                self.find_element(*self.nu_ge_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

                #############组三选号

    def group_there_d(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.wait_element_located(self.driver, self.g_there_d(i, n))
                self.find_element(*self.g_there_d(i, n)).click()  # 点击数字球

    def group_theres_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_there_d(1, n))
                self.find_element(*self.g_there_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_there_d(2, n))
                self.find_element(*self.g_there_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

    def Screening_d(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_d(list[i]))
            self.find_element(*self.screening_d(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

###############组六选号
    def group_six_d(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six_d(i, n))
                self.find_element(*self.g_six_d(i, n)).click()#点击数字球

    def group_sixs_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_six_d(1, n))
                self.find_element(*self.g_six_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_six_d(2, n))
                self.find_element(*self.g_six_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

###############直选和值
    def Direct_add(self,n):
        for i in random.sample(range(1,29),n):
            self.find_element(*self.direct_add(i)).click()##点击i-1
            a=i-1
            print('点击%d'%a)

    def Direct_add_one(self):
        i=1
        self.find_element(*self.direct_add(i)).click()##点击i-1
        a=i-1
        print('点击%d'%a)

    def Direct_addA(self):
        for i in random.sample(range(1, 29), 1):
            self.find_element(*self.direct_add(i)).click()
            c = i - 1
            print('点击1个数字%d' % c)
            if i > 14:
                n = i - 14
                i = i - (2 * n - 1)
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b
            else:
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b

##################组三和值
    def Group_there_add(self,n):
        for i in random.sample(range(1,27),n):
            self.find_element(*self.group_there_add(i)).click()##点击n个数字
            print('点击%d'%i)

    def Group_there_add_one(self):
        i=1
        self.find_element(*self.group_there_add(i)).click()##点击n个数字
        print('点击%d'%i)

    def Group_there_addA(self):
        for i in random.sample(range(1,27),1):
            self.find_element(*self.group_there_add(i)).click()######点击一个数字i
            print('点击1个数字%d' %i)
            if i>13:
                n=i-13
                i=i-(2*n-1)
            list=[1,3]
            list1=[4,5,6]
            list2=[7,9,12]
            list3=[8,10,11,13]
            if i in list:
                a=1
                b=str(a)
                return b
            if i==2:
                a=2
                b=str(a)
                return b
            if i in list1:
                a=3
                b=str(a)
                return b
            if i in list2:
                a=4
                b=str(a)
                return b
            if i in list3:
                a=5
                b=str(a)
                return b

##################组六和值
    def Group_six_add(self,n):
        for i in random.sample(range(1,23),n):
            self.find_element(*self.group_six_add(i)).click()##点击n个数字
            a=i+2
            print('点击%d'%a)

    def Group_six_add_one(self):
        i=1
        self.find_element(*self.group_six_add(i)).click()##点击n个数字
        print('点击%d'%(i+2))

    def Group_six_addA(self):
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        for i in random.sample(range(1, 23), 1):
            self.wait_element_located(self.driver, self.group_six_add(i))
            self.find_element(*self.group_six_add(i)).click()  ######点击一个数字i
            print('点击1个数字%d' % (i + 2))
            if i in list:
                b = str(i - 1)
                return b
            if i in list4:
                b = str(i)
                return b
            if i in list1:
                a = 10
                b = str(a)
                return b
            if i in list3:
                a = 1
                b = str(a)
                return b
            if i in list2:
                n = i - 11
                b = str(i - (2 * n))
                return b
            if i in list5:
                n = i - 11
                b = str(i - (2 * n - 1))
                return b

    def Show_play(self):
        a=self.find_element(*self.show_play).text###读取显示的玩法
        return a

    def Instruct(self):
        self.find_element(*self.instruct).click()##点击右上角....

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()##点击玩法说明

    def Group_there_add_play_instruction(self):
        a=self.find_element(*self.group_there_add_play_instruction).text###玩法说明页读取组三和值
        return a

    def There_D_know(self):
        self.find_element(*self.there_D_know).click()

    def History(self):
        self.find_element(*self.history).click()##点击历史走势

    def Charts(self):
        aa=self.find_elements(*self.charts_list)
        n=random.sample(range(len(aa)),1)
        a=self.find_element(*self.charts(n[0]+1)).text##读取历史走势里的数据
        return a

    def Recommend(self):
        a=self.find_element(*self.recommend).text###读取推荐的号码
        return a

    def Use_recommend(self):
        self.find_element(*self.use_recommend).click()###点击使用推荐号码

    def Number(self):
        a=self.find_element(*self.number).text
        return a

    def Clear(self):
        a=self.find_element(*self.clear).text##读取弹框，清楚文本
        return a

    def Del_x(self):
        self.find_element(*self.del_x).click()##点击X按钮

    def Coun_number(self):
        self.find_element(*self.coun_number).click()##点击继续选号

    def Pause_d(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)+1
        if i > 14:
            n = i - 14
            i = i - (2 * n - 1)
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b
        else:
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b

    def Pause_d_there(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)
        if i > 13:
            n = i - 13
            i = i - (2 * n - 1)
        list = [1, 3]
        list1 = [4, 5, 6]
        list2 = [7, 9, 12]
        list3 = [8, 10, 11, 13]
        if i in list:
            a = 1
            b = str(a)
            return b
        if i == 2:
            a = 2
            b = str(a)
            return b
        if i in list1:
            a = 3
            b = str(a)
            return b
        if i in list2:
            a = 4
            b = str(a)
            return b
        if i in list3:
            a = 5
            b = str(a)
            return b

    def Pause_d_six(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)-2
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        if i in list:
            b = str(i - 1)
            return b
        if i in list4:
            b = str(i)
            return b
        if i in list1:
            a = 10
            b = str(a)
            return b
        if i in list3:
            a = 1
            b = str(a)
            return b
        if i in list2:
            n = i - 11
            b = str(i - (2 * n))
            return b
        if i in list5:
            n = i - 11
            b = str(i - (2 * n - 1))
            return b

class There_D_choosenumber_leyou(Page_leyou,there_D_leyou_loc):
    def Play_d(self):
        self.find_element(*self.play_d).click()###点击玩法

    def Play_direct_d(self):
        self.find_element(*self.play_direct_d).click()###点击直选

    def Play_group_there_d(self):
        self.find_element(*self.play_group_there_d).click()###点击组三

    def Play_group_six_d(self):
        self.find_element(*self.play_group_six_d).click()###点击组六

    def Play_group_direct_add_d(self):
        self.find_element(*self.play_direct_add_d).click()###点击直选和值

    def Play_group_there_add_d(self):
        self.find_element(*self.play_group_there_add_d).click()###点击组三和值

    def Play_group_six_add_d(self):
        self.find_element(*self.play_group_six_add_d).click()###点击组六和值

#################选号
    def there_D_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai_d(i, n))
                self.find_element(*self.nu_bai_d(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_D_bais(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_bai_d(1, n))
                self.find_element(*self.nu_bai_d(1, n)).click()
                a = n - 1
                print('点击百位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_bai_d(2, n))
                self.find_element(*self.nu_bai_d(2, n)).click()
                a = n + 4
                print('点击百位:%d' % a)

    def there_D_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi_d(i, n))
                self.find_element(*self.nu_shi_d(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_D_shis(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_shi_d(1, n))
                self.find_element(*self.nu_shi_d(1, n)).click()
                a = n - 1
                print('点击十位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_shi_d(2, n))
                self.find_element(*self.nu_shi_d(2, n)).click()
                a = n + 4
                print('点击十位:%d' % a)

    def there_D_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge_d(i, n))
                self.find_element(*self.nu_ge_d(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_D_ges(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_ge_d(1, n))
                self.find_element(*self.nu_ge_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_ge_d(2, n))
                self.find_element(*self.nu_ge_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

                #############组三选号

    def group_there_d(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.wait_element_located(self.driver, self.g_there_d(i, n))
                self.find_element(*self.g_there_d(i, n)).click()  # 点击数字球

    def group_theres_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_there_d(1, n))
                self.find_element(*self.g_there_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_there_d(2, n))
                self.find_element(*self.g_there_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

    def Screening_d(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_d(list[i]))
            self.find_element(*self.screening_d(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

###############组六选号
    def group_six_d(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six_d(i, n))
                self.find_element(*self.g_six_d(i, n)).click()#点击数字球

    def group_sixs_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_six_d(1, n))
                self.find_element(*self.g_six_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_six_d(2, n))
                self.find_element(*self.g_six_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

###############直选和值
    def Direct_add(self,n):
        for i in random.sample(range(1,29),n):
            self.find_element(*self.direct_add(i)).click()##点击i-1
            a=i-1
            print('点击%d'%a)

    def Direct_add_one(self):
        i=1
        self.find_element(*self.direct_add(i)).click()##点击i-1
        a=i-1
        print('点击%d'%a)

    def Direct_addA(self):
        for i in random.sample(range(1, 29), 1):
            self.find_element(*self.direct_add(i)).click()
            c = i - 1
            print('点击1个数字%d' % c)
            if i > 14:
                n = i - 14
                i = i - (2 * n - 1)
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b
            else:
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b

##################组三和值
    def Group_there_add(self,n):
        for i in random.sample(range(1,27),n):
            self.find_element(*self.group_there_add(i)).click()##点击n个数字
            print('点击%d'%i)

    def Group_there_add_one(self):
        i=1
        self.find_element(*self.group_there_add(i)).click()##点击n个数字
        print('点击%d'%i)

    def Group_there_addA(self):
        for i in random.sample(range(1,27),1):
            self.find_element(*self.group_there_add(i)).click()######点击一个数字i
            print('点击1个数字%d' %i)
            if i>13:
                n=i-13
                i=i-(2*n-1)
            list=[1,3]
            list1=[4,5,6]
            list2=[7,9,12]
            list3=[8,10,11,13]
            if i in list:
                a=1
                b=str(a)
                return b
            if i==2:
                a=2
                b=str(a)
                return b
            if i in list1:
                a=3
                b=str(a)
                return b
            if i in list2:
                a=4
                b=str(a)
                return b
            if i in list3:
                a=5
                b=str(a)
                return b

##################组六和值
    def Group_six_add(self,n):
        for i in random.sample(range(1,23),n):
            self.find_element(*self.group_six_add(i)).click()##点击n个数字
            a=i+2
            print('点击%d'%a)

    def Group_six_add_one(self):
        i=1
        self.find_element(*self.group_six_add(i)).click()##点击n个数字
        print('点击%d'%(i+2))

    def Group_six_addA(self):
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        for i in random.sample(range(1, 23), 1):
            self.wait_element_located(self.driver, self.group_six_add(i))
            self.find_element(*self.group_six_add(i)).click()  ######点击一个数字i
            print('点击1个数字%d' % (i + 2))
            if i in list:
                b = str(i - 1)
                return b
            if i in list4:
                b = str(i)
                return b
            if i in list1:
                a = 10
                b = str(a)
                return b
            if i in list3:
                a = 1
                b = str(a)
                return b
            if i in list2:
                n = i - 11
                b = str(i - (2 * n))
                return b
            if i in list5:
                n = i - 11
                b = str(i - (2 * n - 1))
                return b

    def Show_play(self):
        a=self.find_element(*self.show_play).text###读取显示的玩法
        return a

    def Instruct(self):
        self.find_element(*self.instruct).click()##点击右上角....

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()##点击玩法说明

    def Group_there_add_play_instruction(self):
        a=self.find_element(*self.group_there_add_play_instruction).text###玩法说明页读取组三和值
        return a

    def There_D_know(self):
        self.find_element(*self.there_D_know).click()

    def History(self):
        self.find_element(*self.history).click()##点击历史走势

    def Charts(self):
        aa=self.find_elements(*self.charts_list)
        n=random.sample(range(len(aa)),1)
        a=self.find_element(*self.charts(n[0]+1)).text##读取历史走势里的数据
        return a

    def Recommend(self):
        a=self.find_element(*self.recommend).text###读取推荐的号码
        return a

    def Use_recommend(self):
        self.find_element(*self.use_recommend).click()###点击使用推荐号码

    def Number(self):
        a=self.find_element(*self.number).text
        return a

    def Clear(self):
        a=self.find_element(*self.clear).text##读取弹框，清楚文本
        return a

    def Del_x(self):
        self.find_element(*self.del_x).click()##点击X按钮

    def Coun_number(self):
        self.find_element(*self.coun_number).click()##点击继续选号

    def Pause_d(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)+1
        if i > 14:
            n = i - 14
            i = i - (2 * n - 1)
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b
        else:
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b

    def Pause_d_there(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)
        if i > 13:
            n = i - 13
            i = i - (2 * n - 1)
        list = [1, 3]
        list1 = [4, 5, 6]
        list2 = [7, 9, 12]
        list3 = [8, 10, 11, 13]
        if i in list:
            a = 1
            b = str(a)
            return b
        if i == 2:
            a = 2
            b = str(a)
            return b
        if i in list1:
            a = 3
            b = str(a)
            return b
        if i in list2:
            a = 4
            b = str(a)
            return b
        if i in list3:
            a = 5
            b = str(a)
            return b

    def Pause_d_six(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)-2
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        if i in list:
            b = str(i - 1)
            return b
        if i in list4:
            b = str(i)
            return b
        if i in list1:
            a = 10
            b = str(a)
            return b
        if i in list3:
            a = 1
            b = str(a)
            return b
        if i in list2:
            n = i - 11
            b = str(i - (2 * n))
            return b
        if i in list5:
            n = i - 11
            b = str(i - (2 * n - 1))
            return b

class There_D_choosenumber_lelun(Page_lelun,there_D_lelun_loc):
    def Play_d(self):
        self.find_element(*self.play_d).click()###点击玩法

    def Play_direct_d(self):
        self.find_element(*self.play_direct_d).click()###点击直选

    def Play_group_there_d(self):
        self.find_element(*self.play_group_there_d).click()###点击组三

    def Play_group_six_d(self):
        self.find_element(*self.play_group_six_d).click()###点击组六

    def Play_group_direct_add_d(self):
        self.find_element(*self.play_direct_add_d).click()###点击直选和值

    def Play_group_there_add_d(self):
        self.find_element(*self.play_group_there_add_d).click()###点击组三和值

    def Play_group_six_add_d(self):
        self.find_element(*self.play_group_six_add_d).click()###点击组六和值

#################选号
    def there_D_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai_d(i, n))
                self.find_element(*self.nu_bai_d(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_D_bais(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_bai_d(1, n))
                self.find_element(*self.nu_bai_d(1, n)).click()
                a = n - 1
                print('点击百位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_bai_d(2, n))
                self.find_element(*self.nu_bai_d(2, n)).click()
                a = n + 4
                print('点击百位:%d' % a)

    def there_D_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi_d(i, n))
                self.find_element(*self.nu_shi_d(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_D_shis(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_shi_d(1, n))
                self.find_element(*self.nu_shi_d(1, n)).click()
                a = n - 1
                print('点击十位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_shi_d(2, n))
                self.find_element(*self.nu_shi_d(2, n)).click()
                a = n + 4
                print('点击十位:%d' % a)

    def there_D_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge_d(i, n))
                self.find_element(*self.nu_ge_d(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_D_ges(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.nu_ge_d(1, n))
                self.find_element(*self.nu_ge_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.nu_ge_d(2, n))
                self.find_element(*self.nu_ge_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

                #############组三选号

    def group_there_d(self):
        for i in range(1, 3):
            for n in range(1, 6):
                self.wait_element_located(self.driver, self.g_there_d(i, n))
                self.find_element(*self.g_there_d(i, n)).click()  # 点击数字球

    def group_theres_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_there_d(1, n))
                self.find_element(*self.g_there_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_there_d(2, n))
                self.find_element(*self.g_there_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

    def Screening_d(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_d(list[i]))
            self.find_element(*self.screening_d(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

###############组六选号
    def group_six_d(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six_d(i, n))
                self.find_element(*self.g_six_d(i, n)).click()#点击数字球

    def group_sixs_d(self, i, j):
        if i > 0:
            for n in random.sample(range(1, 6), i):
                self.wait_element_located(self.driver, self.g_six_d(1, n))
                self.find_element(*self.g_six_d(1, n)).click()
                a = n - 1
                print('点击个位:%d' % a)

        if j > 0:
            for n in random.sample(range(1, 6), j):
                self.wait_element_located(self.driver, self.g_six_d(2, n))
                self.find_element(*self.g_six_d(2, n)).click()
                a = n + 4
                print('点击个位:%d' % a)

###############直选和值
    def Direct_add(self,n):
        for i in random.sample(range(1,29),n):
            self.find_element(*self.direct_add(i)).click()##点击i-1
            a=i-1
            print('点击%d'%a)

    def Direct_add_one(self):
        i=1
        self.find_element(*self.direct_add(i)).click()##点击i-1
        a=i-1
        print('点击%d'%a)

    def Direct_addA(self):
        for i in random.sample(range(1, 29), 1):
            self.find_element(*self.direct_add(i)).click()
            c = i - 1
            print('点击1个数字%d' % c)
            if i > 14:
                n = i - 14
                i = i - (2 * n - 1)
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b
            else:
                if i == 11:
                    a = 63
                    b = str(a)
                    return b
                elif i == 12:
                    a = 69
                    b = str(a)
                    return b
                elif i == 13:
                    a = 73
                    b = str(a)
                    return b
                elif i == 14:
                    a = 75
                    b = str(a)
                    return b
                else:
                    a = int((i * i + i) / 2)
                    b = str(a)
                    return b

##################组三和值
    def Group_there_add(self,n):
        for i in random.sample(range(1,27),n):
            self.find_element(*self.group_there_add(i)).click()##点击n个数字
            print('点击%d'%i)

    def Group_there_add_one(self):
        i=1
        self.find_element(*self.group_there_add(i)).click()##点击n个数字
        print('点击%d'%i)

    def Group_there_addA(self):
        for i in random.sample(range(1,27),1):
            self.find_element(*self.group_there_add(i)).click()######点击一个数字i
            print('点击1个数字%d' %i)
            if i>13:
                n=i-13
                i=i-(2*n-1)
            list=[1,3]
            list1=[4,5,6]
            list2=[7,9,12]
            list3=[8,10,11,13]
            if i in list:
                a=1
                b=str(a)
                return b
            if i==2:
                a=2
                b=str(a)
                return b
            if i in list1:
                a=3
                b=str(a)
                return b
            if i in list2:
                a=4
                b=str(a)
                return b
            if i in list3:
                a=5
                b=str(a)
                return b

##################组六和值
    def Group_six_add(self,n):
        for i in random.sample(range(1,23),n):
            self.find_element(*self.group_six_add(i)).click()##点击n个数字
            a=i+2
            print('点击%d'%a)

    def Group_six_add_one(self):
        i=1
        self.find_element(*self.group_six_add(i)).click()##点击n个数字
        print('点击%d'%(i+2))

    def Group_six_addA(self):
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        for i in random.sample(range(1, 23), 1):
            self.wait_element_located(self.driver, self.group_six_add(i))
            self.find_element(*self.group_six_add(i)).click()  ######点击一个数字i
            print('点击1个数字%d' % (i + 2))
            if i in list:
                b = str(i - 1)
                return b
            if i in list4:
                b = str(i)
                return b
            if i in list1:
                a = 10
                b = str(a)
                return b
            if i in list3:
                a = 1
                b = str(a)
                return b
            if i in list2:
                n = i - 11
                b = str(i - (2 * n))
                return b
            if i in list5:
                n = i - 11
                b = str(i - (2 * n - 1))
                return b

    def Show_play(self):
        a=self.find_element(*self.show_play).text###读取显示的玩法
        return a

    def Instruct(self):
        self.find_element(*self.instruct).click()##点击右上角....

    def Play_instruction(self):
        self.find_element(*self.play_instruction).click()##点击玩法说明

    def Group_there_add_play_instruction(self):
        a=self.find_element(*self.group_there_add_play_instruction).text###玩法说明页读取组三和值
        return a

    def There_D_know(self):
        self.find_element(*self.there_D_know).click()

    def History(self):
        self.find_element(*self.history).click()##点击历史走势

    def Charts(self):
        aa=self.find_elements(*self.charts_list)
        n=random.sample(range(len(aa)),1)
        a=self.find_element(*self.charts(n[0]+1)).text##读取历史走势里的数据
        return a

    def Recommend(self):
        a=self.find_element(*self.recommend).text###读取推荐的号码
        return a

    def Use_recommend(self):
        self.find_element(*self.use_recommend).click()###点击使用推荐号码

    def Number(self):
        a=self.find_element(*self.number).text
        return a

    def Clear(self):
        a=self.find_element(*self.clear).text##读取弹框，清楚文本
        return a

    def Del_x(self):
        self.find_element(*self.del_x).click()##点击X按钮

    def Coun_number(self):
        self.find_element(*self.coun_number).click()##点击继续选号

    def Pause_d(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)+1
        if i > 14:
            n = i - 14
            i = i - (2 * n - 1)
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b
        else:
            if i == 11:
                a = 63
                b = str(a)
                return b
            elif i == 12:
                a = 69
                b = str(a)
                return b
            elif i == 13:
                a = 73
                b = str(a)
                return b
            elif i == 14:
                a = 75
                b = str(a)
                return b
            else:
                a = int((i * i + i) / 2)
                b = str(a)
                return b

    def Pause_d_there(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)
        if i > 13:
            n = i - 13
            i = i - (2 * n - 1)
        list = [1, 3]
        list1 = [4, 5, 6]
        list2 = [7, 9, 12]
        list3 = [8, 10, 11, 13]
        if i in list:
            a = 1
            b = str(a)
            return b
        if i == 2:
            a = 2
            b = str(a)
            return b
        if i in list1:
            a = 3
            b = str(a)
            return b
        if i in list2:
            a = 4
            b = str(a)
            return b
        if i in list3:
            a = 5
            b = str(a)
            return b

    def Pause_d_six(self):
        self.find_element(*self.pause_d).click()##点击机选
        a=self.find_element(*self.pause_nu).text###读取机选的值
        i=int(a)-2
        list = [2, 3, 4, 5, 6]
        list1 = [10, 11, 12, 13]
        list2 = [17, 18, 19, 20, 21]
        list3 = [1, 22]
        list4 = [7, 8, 9]
        list5 = [14, 15, 16]
        if i in list:
            b = str(i - 1)
            return b
        if i in list4:
            b = str(i)
            return b
        if i in list1:
            a = 10
            b = str(a)
            return b
        if i in list3:
            a = 1
            b = str(a)
            return b
        if i in list2:
            n = i - 11
            b = str(i - (2 * n))
            return b
        if i in list5:
            n = i - 11
            b = str(i - (2 * n - 1))
            return b