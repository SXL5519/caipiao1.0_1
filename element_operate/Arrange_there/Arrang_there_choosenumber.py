from element_position.lemi import arrang_there
from element_operate.base import Page
import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from element_position.lexiu import arrang_there_lexiu
from element_operate.base import Page_lexiu
from element_position.leyou import arrang_there_leyou
from element_operate.base import Page_leyou
from element_position.lelun import arrang_there_lelun
from element_operate.base import Page_lelun
#############排列三选号页面元素操作############
class Arrang_there_choosenumber(Page,arrang_there):
    def Play(self):
        self.wait_element_located(self.driver, self.play)
        self.find_element(*self.play).click()####点击玩法

    def Play_Direct(self):
        self.wait_element_located(self.driver, self.play_direct)
        self.find_element(*self.play_direct).click() ########点击直选

    def Play_Group_there(self):
        self.wait_element_located(self.driver,self.play_group_there)
        self.find_element(*self.play_group_there).click()######点击组三

    def Play_Group_six(self):
        self.wait_element_located(self.driver,self.play_group_six)
        self.find_element(*self.play_group_six).click()######点击组六

    def there_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai(i, n))
                self.find_element(*self.nu_bai(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_bais(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_bai(2, a)).click()
            else:
                self.find_element(*self.nu_bai(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)

    def there_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi(i, n))
                self.find_element(*self.nu_shi(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_shis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_shi(2, a)).click()
            else:
                self.find_element(*self.nu_shi(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)

    def there_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge(i, n))
                self.find_element(*self.nu_ge(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_ges(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_ge(2, a)).click()
            else:
                self.find_element(*self.nu_ge(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    #############组三  选号#############
    def group_there(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_there(i, n))
                self.find_element(*self.g_there(i, n)).click()#点击数字球

    def group_theres(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_there(2, a)).click()
            else:
                self.find_element(*self.g_there(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    ##################筛选
    def Screening(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening(list[i]))
            self.find_element(*self.screening(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    ##########组合选号读取
    def Group_display(self):
        n=random.randint(1,6)
        nu=self.find_element(*self.group_display(n)).text
        print(nu)
        return nu

    #######组合显示点击X按钮
    def Group_delet(self):
        n = random.randint(1, 6)
        self.find_element(*self.group_delet(n)).click()

###############组六选号
    def group_six(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six(i, n))
                self.find_element(*self.g_six(i, n)).click()#点击数字球

    def group_sixs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_six(2, a)).click()
            else:
                self.find_element(*self.g_six(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

##################筛选
    def Screening_s(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_s(list[i]))
            self.find_element(*self.screening_s(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    def Arrang_there_instruct(self):
        self.find_element(*self.arrang_there_instruct).click()###点击玩法说明

    def Arrany_there_play(self):
        a=self.find_element(*self.arrany_there_play).text##读取玩法说明，排列3玩法文本
        return a

    def Arrany_there_know(self):
        self.find_element(*self.arrany_there_know).click()##点击玩法说明中的我知道了

    def Arrang_there_history(self):
        self.find_element(*self.arrang_there_history).click()##点击历史走势

    def Arrany_there_date(self):
        a = self.find_elements(*self.arrany_there_date)  ##取历史数据显示号码list
        i = random.randint(0, len(a) - 1)  ##随机产生i
        b = a[i].text  ###取i对应的显示号码
        return b

    def Switch_play_ok(self):
        self.wait_element_located(self.driver, self.switch_play_ok)
        self.find_element(*self.switch_play_ok).click()##切换玩法，点击确定

class Arrang_there_choosenumber_lexiu(Page_lexiu,arrang_there_lexiu):
    def Play(self):
        self.wait_element_located(self.driver, self.play)
        self.find_element(*self.play).click()####点击玩法

    def Play_Direct(self):
        self.wait_element_located(self.driver, self.play_direct)
        self.find_element(*self.play_direct).click() ########点击直选

    def Play_Group_there(self):
        self.wait_element_located(self.driver,self.play_group_there)
        self.find_element(*self.play_group_there).click()######点击组三

    def Play_Group_six(self):
        self.wait_element_located(self.driver,self.play_group_six)
        self.find_element(*self.play_group_six).click()######点击组六

    def there_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai(i, n))
                self.find_element(*self.nu_bai(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_bais(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_bai(2, a)).click()
            else:
                self.find_element(*self.nu_bai(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)

    def there_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi(i, n))
                self.find_element(*self.nu_shi(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_shis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_shi(2, a)).click()
            else:
                self.find_element(*self.nu_shi(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)

    def there_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge(i, n))
                self.find_element(*self.nu_ge(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_ges(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_ge(2, a)).click()
            else:
                self.find_element(*self.nu_ge(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    #############组三  选号#############
    def group_there(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_there(i, n))
                self.find_element(*self.g_there(i, n)).click()#点击数字球

    def group_theres(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_there(2, a)).click()
            else:
                self.find_element(*self.g_there(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    ##################筛选
    def Screening(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening(list[i]))
            self.find_element(*self.screening(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    ##########组合选号读取
    def Group_display(self):
        n=random.randint(1,6)
        nu=self.find_element(*self.group_display(n)).text
        print(nu)
        return nu

    #######组合显示点击X按钮
    def Group_delet(self):
        n = random.randint(1, 6)
        self.find_element(*self.group_delet(n)).click()

###############组六选号
    def group_six(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six(i, n))
                self.find_element(*self.g_six(i, n)).click()#点击数字球

    def group_sixs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_six(2, a)).click()
            else:
                self.find_element(*self.g_six(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

##################筛选
    def Screening_s(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_s(list[i]))
            self.find_element(*self.screening_s(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    def Arrang_there_instruct(self):
        self.find_element(*self.arrang_there_instruct).click()###点击玩法说明

    def Arrany_there_play(self):
        a=self.find_element(*self.arrany_there_play).text##读取玩法说明，排列3玩法文本
        return a

    def Arrany_there_know(self):
        self.find_element(*self.arrany_there_know).click()##点击玩法说明中的我知道了

    def Arrang_there_history(self):
        self.find_element(*self.arrang_there_history).click()##点击历史走势

    def Arrany_there_date(self):
        a = self.find_elements(*self.arrany_there_date)  ##取历史数据显示号码list
        i = random.randint(0, len(a) - 1)  ##随机产生i
        b = a[i].text  ###取i对应的显示号码
        return b

    def Switch_play_ok(self):
        self.wait_element_located(self.driver, self.switch_play_ok)
        self.find_element(*self.switch_play_ok).click()##切换玩法，点击确定

class Arrang_there_choosenumber_leyou(Page_leyou,arrang_there_leyou):
    def Play(self):
        self.wait_element_located(self.driver, self.play)
        self.find_element(*self.play).click()####点击玩法

    def Play_Direct(self):
        self.wait_element_located(self.driver, self.play_direct)
        self.find_element(*self.play_direct).click() ########点击直选

    def Play_Group_there(self):
        self.wait_element_located(self.driver,self.play_group_there)
        self.find_element(*self.play_group_there).click()######点击组三

    def Play_Group_six(self):
        self.wait_element_located(self.driver,self.play_group_six)
        self.find_element(*self.play_group_six).click()######点击组六

    def there_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai(i, n))
                self.find_element(*self.nu_bai(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_bais(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_bai(2, a)).click()
            else:
                self.find_element(*self.nu_bai(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)

    def there_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi(i, n))
                self.find_element(*self.nu_shi(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_shis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_shi(2, a)).click()
            else:
                self.find_element(*self.nu_shi(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)

    def there_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge(i, n))
                self.find_element(*self.nu_ge(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_ges(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_ge(2, a)).click()
            else:
                self.find_element(*self.nu_ge(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    #############组三  选号#############
    def group_there(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_there(i, n))
                self.find_element(*self.g_there(i, n)).click()#点击数字球

    def group_theres(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_there(2, a)).click()
            else:
                self.find_element(*self.g_there(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    ##################筛选
    def Screening(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening(list[i]))
            self.find_element(*self.screening(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    ##########组合选号读取
    def Group_display(self):
        n=random.randint(1,6)
        nu=self.find_element(*self.group_display(n)).text
        print(nu)
        return nu

    #######组合显示点击X按钮
    def Group_delet(self):
        n = random.randint(1, 6)
        self.find_element(*self.group_delet(n)).click()

###############组六选号
    def group_six(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six(i, n))
                self.find_element(*self.g_six(i, n)).click()#点击数字球

    def group_sixs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_six(2, a)).click()
            else:
                self.find_element(*self.g_six(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

##################筛选
    def Screening_s(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_s(list[i]))
            self.find_element(*self.screening_s(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    def Arrang_there_instruct(self):
        self.find_element(*self.arrang_there_instruct).click()###点击玩法说明

    def Arrany_there_play(self):
        a=self.find_element(*self.arrany_there_play).text##读取玩法说明，排列3玩法文本
        return a

    def Arrany_there_know(self):
        self.find_element(*self.arrany_there_know).click()##点击玩法说明中的我知道了

    def Arrang_there_history(self):
        self.find_element(*self.arrang_there_history).click()##点击历史走势

    def Arrany_there_date(self):
        a = self.find_elements(*self.arrany_there_date)  ##取历史数据显示号码list
        i = random.randint(0, len(a) - 1)  ##随机产生i
        b = a[i].text  ###取i对应的显示号码
        return b

    def Switch_play_ok(self):
        self.wait_element_located(self.driver, self.switch_play_ok)
        self.find_element(*self.switch_play_ok).click()##切换玩法，点击确定

class Arrang_there_choosenumber_lelun(Page_lelun,arrang_there_lelun):
    def Play(self):
        self.wait_element_located(self.driver, self.play)
        self.find_element(*self.play).click()####点击玩法

    def Play_Direct(self):
        self.wait_element_located(self.driver, self.play_direct)
        self.find_element(*self.play_direct).click() ########点击直选

    def Play_Group_there(self):
        self.wait_element_located(self.driver,self.play_group_there)
        self.find_element(*self.play_group_there).click()######点击组三

    def Play_Group_six(self):
        self.wait_element_located(self.driver,self.play_group_six)
        self.find_element(*self.play_group_six).click()######点击组六

    def there_bai(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_bai(i, n))
                self.find_element(*self.nu_bai(i, n)).click()#点击百位的数字

##############随机点击百位的i+j个数字
    def there_bais(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_bai(2, a)).click()
            else:
                self.find_element(*self.nu_bai(1, n)).click()
            a = n - 1
            print('点击百位:%d' % a)

    def there_shi(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_shi(i, n))
                self.find_element(*self.nu_shi(i, n)).click()#点击十位的数字

##############随机点击十位的i+j个数字
    def there_shis(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_shi(2, a)).click()
            else:
                self.find_element(*self.nu_shi(1, n)).click()
            a = n - 1
            print('点击十位:%d' % a)

    def there_ge(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.nu_ge(i, n))
                self.find_element(*self.nu_ge(i, n)).click()#点击个位的数字

##############随机点击个位的i+j个数字
    def there_ges(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.nu_ge(2, a)).click()
            else:
                self.find_element(*self.nu_ge(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    #############组三  选号#############
    def group_there(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_there(i, n))
                self.find_element(*self.g_there(i, n)).click()#点击数字球

    def group_theres(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_there(2, a)).click()
            else:
                self.find_element(*self.g_there(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

    ##################筛选
    def Screening(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening(list[i]))
            self.find_element(*self.screening(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    ##########组合选号读取
    def Group_display(self):
        n=random.randint(1,6)
        nu=self.find_element(*self.group_display(n)).text
        print(nu)
        return nu

    #######组合显示点击X按钮
    def Group_delet(self):
        n = random.randint(1, 6)
        self.find_element(*self.group_delet(n)).click()

###############组六选号
    def group_six(self):
        for i in range(1,3):
            for n in range(1,6):
                self.wait_element_located(self.driver, self.g_six(i, n))
                self.find_element(*self.g_six(i, n)).click()#点击数字球

    def group_sixs(self, i):
        for n in random.sample(range(1, 11), i):
            if n>5:
                a=n-5
                self.find_element(*self.g_six(2, a)).click()
            else:
                self.find_element(*self.g_six(1, n)).click()
            a = n - 1
            print('点击个位:%d' % a)

##################筛选
    def Screening_s(self,i):
        list=['ji','ou','da','xi','qu','qing']
        try:
            self.wait_element_located(self.driver, self.screening_s(list[i]))
            self.find_element(*self.screening_s(list[i])).click()
        except NoSuchElementException:
            print('筛选按钮缺失')

    def Arrang_there_instruct(self):
        self.find_element(*self.arrang_there_instruct).click()###点击玩法说明

    def Arrany_there_play(self):
        a=self.find_element(*self.arrany_there_play).text##读取玩法说明，排列3玩法文本
        return a

    def Arrany_there_know(self):
        self.find_element(*self.arrany_there_know).click()##点击玩法说明中的我知道了

    def Arrang_there_history(self):
        self.find_element(*self.arrang_there_history).click()##点击历史走势

    def Arrany_there_date(self):
        a = self.find_elements(*self.arrany_there_date)  ##取历史数据显示号码list
        i = random.randint(0, len(a) - 1)  ##随机产生i
        b = a[i].text  ###取i对应的显示号码
        return b

    def Switch_play_ok(self):
        self.wait_element_located(self.driver, self.switch_play_ok)
        self.find_element(*self.switch_play_ok).click()##切换玩法，点击确定

