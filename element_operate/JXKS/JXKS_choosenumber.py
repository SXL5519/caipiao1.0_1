from element_operate.base import Page
from element_position.lemi import JXKS_ChooseNumber_loc,UChooseNum_loc
import random
from element_operate.base import Page_lexiu
from element_position.lexiu import JXKS_ChooseNumber_lexiu_loc,UChooseNum_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import JXKS_ChooseNumber_leyou_loc,UChooseNum_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import JXKS_ChooseNumber_lelun_loc,UChooseNum_lelun_loc
class JXKS_ChooseNumber(Page,JXKS_ChooseNumber_loc,UChooseNum_loc):
    def All_play(self,a):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        for i in random.sample(range(len(list)),a):
            n=list[i]
            self.find_element(*self.mode_choose_button_loc).click()##展开玩法
            self.Assert_play()
            self.wait_element_located(self.driver, self.all_play(n))
            self.find_element(*self.all_play(n)).click()##点击玩法
            self.Assert_play()
            if a==1:
                b=self.find_element(*self.all_play(n))
                data_text=b.get_attribute('data-text')
                return data_text

    def play_jxks_add(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[7]))
        self.find_element(*self.all_play(list[7])).click()  ##点击和值

    def play_jxks_sthdx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[5]))
        self.find_element(*self.all_play(list[5])).click()  ##点击三同号单选

    def play_jxks_sthtx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[6]))
        self.find_element(*self.all_play(list[6])).click()  ##点击三同号通选

    def play_jxks_ethdx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[1]))
        self.find_element(*self.all_play(list[1])).click()  ##点击二同号单选

    def play_jxks_ethfx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[2]))
        self.find_element(*self.all_play(list[2])).click()  ##点击二同号复选

    def play_jxks_sbth(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[4]))
        self.find_element(*self.all_play(list[4])).click()  ##点击三不同号

    def play_jxks_slhtx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[3]))
        self.find_element(*self.all_play(list[3])).click()  ##点击三连号通选

    def play_jxks_ebth(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[0]))
        self.find_element(*self.all_play(list[0])).click()  ##点击二不同号

    def Assert_play(self):
        a=self.find_element(*self.assert_play)##判断玩法展开或者打开
        style=a.get_attribute('style')
        if style=='display: none;':
            print('玩法关闭')
        else:
            print('玩法展开')

    def mode_choose_button_text(self):
        a=self.find_element(*self.mode_choose_button_loc).text##读取确定的玩法
        return a


    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Date_nu(self):
        a=self.find_elements(*self.date_nu)##读取页面展示的所有数据
        i=random.randint(1,len(a))
        b=self.find_element(*self.date_n(i)).text
        return b

    def Ret(self):
        self.wait_element_located(self.driver,self.ret)
        self.find_element(*self.ret).click()##点击返回按钮

    def Add_choosenumber(self,n):
        a=self.find_elements(*self.add_choosenumber)###和值玩法，随机选n个号码
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def ChooseNumber_da(self):
        self.find_element(*self.da).click()##点击 大

    def ChooseNumber_xiao(self):
        self.find_element(*self.xiao).click()##点击 小

    def ChooseNumber_dan(self):
        self.find_element(*self.dan).click()##点击 单

    def ChooseNumber_shuang(self):
        self.find_element(*self.shuang).click()#点击 双



    def sthdx_choosenumber_nu(self,n):##点击三同号单选选号
        a=self.find_elements(*self.sthdx_all)##读取三同号单选选号list
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sthtx_choosenumber(self):
        self.find_element(*self.sthtx).click()###点击三同号通选号码

    def Ethdx(self,n):###  二同号单选 选号，n <=3
        q=0
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in random.sample(range(len(a)),n):
            a[i].click()
        for j in random.sample(range(len(a)),6):
            if q>=n:
                break
            else:
                if b[j].get_attribute('class')!='b-flex off':
                    b[j].click()
                    q=q+1


    def Ethdx_all(self):###  二同号单选 选择全部号码
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in range(len(a)):
            a[i].click()
            a[i].click()
            b[i].click()
            b[i].click()

    def Ethfx_all(self):###  二同号复选选 选择全部号码
        a=self.find_elements(*self.ethfx_th)
        for i in range(len(a)):
            a[i].click()
            a[i].click()

    def Ethfx(self,n):###二同号复选，选择n个号码
        a = self.find_elements(*self.ethfx_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sbth(self,n):###三不同号，选择n个号码
        a = self.find_elements(*self.sbth_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def Slhtx_th(self):
        self.wait_element_located(self.driver,self.slhtx_th)
        self.find_element(*self.slhtx_th).click()###点击三连号通选 选号

    def Ebth(self,n):###选择二不同号N 个号码
        a = self.find_elements(*self.ebth)
        for i in random.sample(range(len(a)), n):
            a[i].click()

class GXKS_ChooseNumber_lexiu(Page_lexiu,JXKS_ChooseNumber_lexiu_loc,UChooseNum_lexiu_loc):
    def All_play(self,a):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        for i in random.sample(range(len(list)),a):
            n=list[i]
            self.find_element(*self.mode_choose_button_loc).click()##展开玩法
            self.Assert_play()
            self.wait_element_located(self.driver, self.all_play(n))
            self.find_element(*self.all_play(n)).click()##点击玩法
            self.Assert_play()
            if a==1:
                b=self.find_element(*self.all_play(n))
                data_text=b.get_attribute('data-text')
                return data_text

    def play_jxks_add(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[7]))
        self.find_element(*self.all_play(list[7])).click()  ##点击和值

    def play_jxks_sthdx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[5]))
        self.find_element(*self.all_play(list[5])).click()  ##点击三同号单选

    def play_jxks_sthtx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[6]))
        self.find_element(*self.all_play(list[6])).click()  ##点击三同号通选

    def play_jxks_ethdx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[1]))
        self.find_element(*self.all_play(list[1])).click()  ##点击二同号单选

    def play_jxks_ethfx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[2]))
        self.find_element(*self.all_play(list[2])).click()  ##点击二同号复选

    def play_jxks_sbth(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[4]))
        self.find_element(*self.all_play(list[4])).click()  ##点击三不同号

    def play_jxks_slhtx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[3]))
        self.find_element(*self.all_play(list[3])).click()  ##点击三连号通选

    def play_jxks_ebth(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[0]))
        self.find_element(*self.all_play(list[0])).click()  ##点击二不同号

    def Assert_play(self):
        a=self.find_element(*self.assert_play)##判断玩法展开或者打开
        style=a.get_attribute('style')
        if style=='display: none;':
            print('玩法关闭')
        else:
            print('玩法展开')

    def mode_choose_button_text(self):
        a=self.find_element(*self.mode_choose_button_loc).text##读取确定的玩法
        return a


    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Date_nu(self):
        a=self.find_elements(*self.date_nu)##读取页面展示的所有数据
        i=random.randint(1,len(a))
        b=self.find_element(*self.date_n(i)).text
        return b

    def Ret(self):
        self.wait_element_located(self.driver,self.ret)
        self.find_element(*self.ret).click()##点击返回按钮

    def Add_choosenumber(self,n):
        a=self.find_elements(*self.add_choosenumber)###和值玩法，随机选n个号码
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def ChooseNumber_da(self):
        self.find_element(*self.da).click()##点击 大

    def ChooseNumber_xiao(self):
        self.find_element(*self.xiao).click()##点击 小

    def ChooseNumber_dan(self):
        self.find_element(*self.dan).click()##点击 单

    def ChooseNumber_shuang(self):
        self.find_element(*self.shuang).click()#点击 双



    def sthdx_choosenumber_nu(self,n):##点击三同号单选选号
        a=self.find_elements(*self.sthdx_all)##读取三同号单选选号list
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sthtx_choosenumber(self):
        self.find_element(*self.sthtx).click()###点击三同号通选号码

    def Ethdx(self,n):###  二同号单选 选号，n <=3
        q=0
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in random.sample(range(len(a)),n):
            a[i].click()
        for j in random.sample(range(len(a)),6):
            if q>=n:
                break
            else:
                if b[j].get_attribute('class')!='b-flex off':
                    b[j].click()
                    q=q+1


    def Ethdx_all(self):###  二同号单选 选择全部号码
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in range(len(a)):
            a[i].click()
            a[i].click()
            b[i].click()
            b[i].click()

    def Ethfx_all(self):###  二同号复选选 选择全部号码
        a=self.find_elements(*self.ethfx_th)
        for i in range(len(a)):
            a[i].click()
            a[i].click()

    def Ethfx(self,n):###二同号复选，选择n个号码
        a = self.find_elements(*self.ethfx_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sbth(self,n):###三不同号，选择n个号码
        a = self.find_elements(*self.sbth_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def Slhtx_th(self):
        self.wait_element_located(self.driver,self.slhtx_th)
        self.find_element(*self.slhtx_th).click()###点击三连号通选 选号

    def Ebth(self,n):###选择二不同号N 个号码
        a = self.find_elements(*self.ebth)
        for i in random.sample(range(len(a)), n):
            a[i].click()

class JXKS_ChooseNumber_lexiu(Page_lexiu,JXKS_ChooseNumber_lexiu_loc,UChooseNum_lexiu_loc):
    def All_play(self,a):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        for i in random.sample(range(len(list)),a):
            n=list[i]
            self.find_element(*self.mode_choose_button_loc).click()##展开玩法
            self.Assert_play()
            self.wait_element_located(self.driver, self.all_play(n))
            self.find_element(*self.all_play(n)).click()##点击玩法
            self.Assert_play()
            if a==1:
                b=self.find_element(*self.all_play(n))
                data_text=b.get_attribute('data-text')
                return data_text

    def play_jxks_add(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[7]))
        self.find_element(*self.all_play(list[7])).click()  ##点击和值

    def play_jxks_sthdx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[5]))
        self.find_element(*self.all_play(list[5])).click()  ##点击三同号单选

    def play_jxks_sthtx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[6]))
        self.find_element(*self.all_play(list[6])).click()  ##点击三同号通选

    def play_jxks_ethdx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[1]))
        self.find_element(*self.all_play(list[1])).click()  ##点击二同号单选

    def play_jxks_ethfx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[2]))
        self.find_element(*self.all_play(list[2])).click()  ##点击二同号复选

    def play_jxks_sbth(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[4]))
        self.find_element(*self.all_play(list[4])).click()  ##点击三不同号

    def play_jxks_slhtx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[3]))
        self.find_element(*self.all_play(list[3])).click()  ##点击三连号通选

    def play_jxks_ebth(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[0]))
        self.find_element(*self.all_play(list[0])).click()  ##点击二不同号

    def Assert_play(self):
        a=self.find_element(*self.assert_play)##判断玩法展开或者打开
        style=a.get_attribute('style')
        if style=='display: none;':
            print('玩法关闭')
        else:
            print('玩法展开')

    def mode_choose_button_text(self):
        a=self.find_element(*self.mode_choose_button_loc).text##读取确定的玩法
        return a


    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Date_nu(self):
        a=self.find_elements(*self.date_nu)##读取页面展示的所有数据
        i=random.randint(1,len(a))
        b=self.find_element(*self.date_n(i)).text
        return b

    def Ret(self):
        self.wait_element_located(self.driver,self.ret)
        self.find_element(*self.ret).click()##点击返回按钮

    def Add_choosenumber(self,n):
        a=self.find_elements(*self.add_choosenumber)###和值玩法，随机选n个号码
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def ChooseNumber_da(self):
        self.find_element(*self.da).click()##点击 大

    def ChooseNumber_xiao(self):
        self.find_element(*self.xiao).click()##点击 小

    def ChooseNumber_dan(self):
        self.find_element(*self.dan).click()##点击 单

    def ChooseNumber_shuang(self):
        self.find_element(*self.shuang).click()#点击 双



    def sthdx_choosenumber_nu(self,n):##点击三同号单选选号
        a=self.find_elements(*self.sthdx_all)##读取三同号单选选号list
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sthtx_choosenumber(self):
        self.find_element(*self.sthtx).click()###点击三同号通选号码

    def Ethdx(self,n):###  二同号单选 选号，n <=3
        q=0
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in random.sample(range(len(a)),n):
            a[i].click()
        for j in random.sample(range(len(a)),6):
            if q>=n:
                break
            else:
                if b[j].get_attribute('class')!='b-flex off':
                    b[j].click()
                    q=q+1


    def Ethdx_all(self):###  二同号单选 选择全部号码
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in range(len(a)):
            a[i].click()
            a[i].click()
            b[i].click()
            b[i].click()

    def Ethfx_all(self):###  二同号复选选 选择全部号码
        a=self.find_elements(*self.ethfx_th)
        for i in range(len(a)):
            a[i].click()
            a[i].click()

    def Ethfx(self,n):###二同号复选，选择n个号码
        a = self.find_elements(*self.ethfx_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sbth(self,n):###三不同号，选择n个号码
        a = self.find_elements(*self.sbth_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def Slhtx_th(self):
        self.wait_element_located(self.driver,self.slhtx_th)
        self.find_element(*self.slhtx_th).click()###点击三连号通选 选号

    def Ebth(self,n):###选择二不同号N 个号码
        a = self.find_elements(*self.ebth)
        for i in random.sample(range(len(a)), n):
            a[i].click()

class GXKS_ChooseNumber_leyou(Page_lexiu,JXKS_ChooseNumber_lexiu_loc,UChooseNum_lexiu_loc):
    def All_play(self,a):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        for i in random.sample(range(len(list)),a):
            n=list[i]
            self.find_element(*self.mode_choose_button_loc).click()##展开玩法
            self.Assert_play()
            self.wait_element_located(self.driver, self.all_play(n))
            self.find_element(*self.all_play(n)).click()##点击玩法
            self.Assert_play()
            if a==1:
                b=self.find_element(*self.all_play(n))
                data_text=b.get_attribute('data-text')
                return data_text

    def play_jxks_add(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[7]))
        self.find_element(*self.all_play(list[7])).click()  ##点击和值

    def play_jxks_sthdx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[5]))
        self.find_element(*self.all_play(list[5])).click()  ##点击三同号单选

    def play_jxks_sthtx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[6]))
        self.find_element(*self.all_play(list[6])).click()  ##点击三同号通选

    def play_jxks_ethdx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[1]))
        self.find_element(*self.all_play(list[1])).click()  ##点击二同号单选

    def play_jxks_ethfx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[2]))
        self.find_element(*self.all_play(list[2])).click()  ##点击二同号复选

    def play_jxks_sbth(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[4]))
        self.find_element(*self.all_play(list[4])).click()  ##点击三不同号

    def play_jxks_slhtx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[3]))
        self.find_element(*self.all_play(list[3])).click()  ##点击三连号通选

    def play_jxks_ebth(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[0]))
        self.find_element(*self.all_play(list[0])).click()  ##点击二不同号

    def Assert_play(self):
        a=self.find_element(*self.assert_play)##判断玩法展开或者打开
        style=a.get_attribute('style')
        if style=='display: none;':
            print('玩法关闭')
        else:
            print('玩法展开')

    def mode_choose_button_text(self):
        a=self.find_element(*self.mode_choose_button_loc).text##读取确定的玩法
        return a


    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Date_nu(self):
        a=self.find_elements(*self.date_nu)##读取页面展示的所有数据
        i=random.randint(1,len(a))
        b=self.find_element(*self.date_n(i)).text
        return b

    def Ret(self):
        self.wait_element_located(self.driver,self.ret)
        self.find_element(*self.ret).click()##点击返回按钮

    def Add_choosenumber(self,n):
        a=self.find_elements(*self.add_choosenumber)###和值玩法，随机选n个号码
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def ChooseNumber_da(self):
        self.find_element(*self.da).click()##点击 大

    def ChooseNumber_xiao(self):
        self.find_element(*self.xiao).click()##点击 小

    def ChooseNumber_dan(self):
        self.find_element(*self.dan).click()##点击 单

    def ChooseNumber_shuang(self):
        self.find_element(*self.shuang).click()#点击 双



    def sthdx_choosenumber_nu(self,n):##点击三同号单选选号
        a=self.find_elements(*self.sthdx_all)##读取三同号单选选号list
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sthtx_choosenumber(self):
        self.find_element(*self.sthtx).click()###点击三同号通选号码

    def Ethdx(self,n):###  二同号单选 选号，n <=3
        q=0
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in random.sample(range(len(a)),n):
            a[i].click()
        for j in random.sample(range(len(a)),6):
            if q>=n:
                break
            else:
                if b[j].get_attribute('class')!='b-flex off':
                    b[j].click()
                    q=q+1


    def Ethdx_all(self):###  二同号单选 选择全部号码
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in range(len(a)):
            a[i].click()
            a[i].click()
            b[i].click()
            b[i].click()

    def Ethfx_all(self):###  二同号复选选 选择全部号码
        a=self.find_elements(*self.ethfx_th)
        for i in range(len(a)):
            a[i].click()
            a[i].click()

    def Ethfx(self,n):###二同号复选，选择n个号码
        a = self.find_elements(*self.ethfx_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sbth(self,n):###三不同号，选择n个号码
        a = self.find_elements(*self.sbth_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def Slhtx_th(self):
        self.wait_element_located(self.driver,self.slhtx_th)
        self.find_element(*self.slhtx_th).click()###点击三连号通选 选号

    def Ebth(self,n):###选择二不同号N 个号码
        a = self.find_elements(*self.ebth)
        for i in random.sample(range(len(a)), n):
            a[i].click()

class jXKS_ChooseNumber_leyou(Page_leyou,JXKS_ChooseNumber_leyou_loc,UChooseNum_leyou_loc):
    def All_play(self,a):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        for i in random.sample(range(len(list)),a):
            n=list[i]
            self.find_element(*self.mode_choose_button_loc).click()##展开玩法
            self.Assert_play()
            self.wait_element_located(self.driver, self.all_play(n))
            self.find_element(*self.all_play(n)).click()##点击玩法
            self.Assert_play()
            if a==1:
                b=self.find_element(*self.all_play(n))
                data_text=b.get_attribute('data-text')
                return data_text

    def play_jxks_add(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[7]))
        self.find_element(*self.all_play(list[7])).click()  ##点击和值

    def play_jxks_sthdx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[5]))
        self.find_element(*self.all_play(list[5])).click()  ##点击三同号单选

    def play_jxks_sthtx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[6]))
        self.find_element(*self.all_play(list[6])).click()  ##点击三同号通选

    def play_jxks_ethdx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[1]))
        self.find_element(*self.all_play(list[1])).click()  ##点击二同号单选

    def play_jxks_ethfx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[2]))
        self.find_element(*self.all_play(list[2])).click()  ##点击二同号复选

    def play_jxks_sbth(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[4]))
        self.find_element(*self.all_play(list[4])).click()  ##点击三不同号

    def play_jxks_slhtx(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[3]))
        self.find_element(*self.all_play(list[3])).click()  ##点击三连号通选

    def play_jxks_ebth(self):
        list=['52001','52002','52003','52004','52005','52006','52007','52008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[0]))
        self.find_element(*self.all_play(list[0])).click()  ##点击二不同号

    def Assert_play(self):
        a=self.find_element(*self.assert_play)##判断玩法展开或者打开
        style=a.get_attribute('style')
        if style=='display: none;':
            print('玩法关闭')
        else:
            print('玩法展开')

    def mode_choose_button_text(self):
        a=self.find_element(*self.mode_choose_button_loc).text##读取确定的玩法
        return a


    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Date_nu(self):
        a=self.find_elements(*self.date_nu)##读取页面展示的所有数据
        i=random.randint(1,len(a))
        b=self.find_element(*self.date_n(i)).text
        return b

    def Ret(self):
        self.wait_element_located(self.driver,self.ret)
        self.find_element(*self.ret).click()##点击返回按钮

    def Add_choosenumber(self,n):
        a=self.find_elements(*self.add_choosenumber)###和值玩法，随机选n个号码
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def ChooseNumber_da(self):
        self.find_element(*self.da).click()##点击 大

    def ChooseNumber_xiao(self):
        self.find_element(*self.xiao).click()##点击 小

    def ChooseNumber_dan(self):
        self.find_element(*self.dan).click()##点击 单

    def ChooseNumber_shuang(self):
        self.find_element(*self.shuang).click()#点击 双



    def sthdx_choosenumber_nu(self,n):##点击三同号单选选号
        a=self.find_elements(*self.sthdx_all)##读取三同号单选选号list
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sthtx_choosenumber(self):
        self.find_element(*self.sthtx).click()###点击三同号通选号码

    def Ethdx(self,n):###  二同号单选 选号，n <=3
        q=0
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in random.sample(range(len(a)),n):
            a[i].click()
        for j in random.sample(range(len(a)),6):
            if q>=n:
                break
            else:
                if b[j].get_attribute('class')!='b-flex off':
                    b[j].click()
                    q=q+1


    def Ethdx_all(self):###  二同号单选 选择全部号码
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in range(len(a)):
            a[i].click()
            a[i].click()
            b[i].click()
            b[i].click()

    def Ethfx_all(self):###  二同号复选选 选择全部号码
        a=self.find_elements(*self.ethfx_th)
        for i in range(len(a)):
            a[i].click()
            a[i].click()

    def Ethfx(self,n):###二同号复选，选择n个号码
        a = self.find_elements(*self.ethfx_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sbth(self,n):###三不同号，选择n个号码
        a = self.find_elements(*self.sbth_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def Slhtx_th(self):
        self.wait_element_located(self.driver,self.slhtx_th)
        self.find_element(*self.slhtx_th).click()###点击三连号通选 选号

    def Ebth(self,n):###选择二不同号N 个号码
        a = self.find_elements(*self.ebth)
        for i in random.sample(range(len(a)), n):
            a[i].click()

class GXKS_ChooseNumber_lelun(Page_lelun,JXKS_ChooseNumber_lelun_loc,UChooseNum_lelun_loc):
    def All_play(self,a):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        for i in random.sample(range(len(list)),a):
            n=list[i]
            self.find_element(*self.mode_choose_button_loc).click()##展开玩法
            self.Assert_play()
            self.wait_element_located(self.driver, self.all_play(n))
            self.find_element(*self.all_play(n)).click()##点击玩法
            self.Assert_play()
            if a==1:
                b=self.find_element(*self.all_play(n))
                data_text=b.get_attribute('data-text')
                return data_text

    def play_jxks_add(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[7]))
        self.find_element(*self.all_play(list[7])).click()  ##点击和值

    def play_jxks_sthdx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[5]))
        self.find_element(*self.all_play(list[5])).click()  ##点击三同号单选

    def play_jxks_sthtx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[6]))
        self.find_element(*self.all_play(list[6])).click()  ##点击三同号通选

    def play_jxks_ethdx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[1]))
        self.find_element(*self.all_play(list[1])).click()  ##点击二同号单选

    def play_jxks_ethfx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[2]))
        self.find_element(*self.all_play(list[2])).click()  ##点击二同号复选

    def play_jxks_sbth(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[4]))
        self.find_element(*self.all_play(list[4])).click()  ##点击三不同号

    def play_jxks_slhtx(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[3]))
        self.find_element(*self.all_play(list[3])).click()  ##点击三连号通选

    def play_jxks_ebth(self):
        list=['54001','54002','54003','54004','54005','54006','54007','54008']
        self.find_element(*self.mode_choose_button_loc).click()  ##展开玩法
        self.wait_element_located(self.driver, self.all_play(list[0]))
        self.find_element(*self.all_play(list[0])).click()  ##点击二不同号

    def Assert_play(self):
        a=self.find_element(*self.assert_play)##判断玩法展开或者打开
        style=a.get_attribute('style')
        if style=='display: none;':
            print('玩法关闭')
        else:
            print('玩法展开')

    def mode_choose_button_text(self):
        a=self.find_element(*self.mode_choose_button_loc).text##读取确定的玩法
        return a


    def History_movements(self):
        self.find_element(*self.history_movements).click()##点击历史走势

    def Date_nu(self):
        a=self.find_elements(*self.date_nu)##读取页面展示的所有数据
        i=random.randint(1,len(a))
        b=self.find_element(*self.date_n(i)).text
        return b

    def Ret(self):
        self.wait_element_located(self.driver,self.ret)
        self.find_element(*self.ret).click()##点击返回按钮

    def Add_choosenumber(self,n):
        a=self.find_elements(*self.add_choosenumber)###和值玩法，随机选n个号码
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def ChooseNumber_da(self):
        self.find_element(*self.da).click()##点击 大

    def ChooseNumber_xiao(self):
        self.find_element(*self.xiao).click()##点击 小

    def ChooseNumber_dan(self):
        self.find_element(*self.dan).click()##点击 单

    def ChooseNumber_shuang(self):
        self.find_element(*self.shuang).click()#点击 双



    def sthdx_choosenumber_nu(self,n):##点击三同号单选选号
        a=self.find_elements(*self.sthdx_all)##读取三同号单选选号list
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sthtx_choosenumber(self):
        self.find_element(*self.sthtx).click()###点击三同号通选号码

    def Ethdx(self,n):###  二同号单选 选号，n <=3
        q=0
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in random.sample(range(len(a)),n):
            a[i].click()
        for j in random.sample(range(len(a)),6):
            if q>=n:
                break
            else:
                if b[j].get_attribute('class')!='b-flex off':
                    b[j].click()
                    q=q+1


    def Ethdx_all(self):###  二同号单选 选择全部号码
        a=self.find_elements(*self.ethdx_th)
        b=self.find_elements(*self.ethdx_bth)
        for i in range(len(a)):
            a[i].click()
            a[i].click()
            b[i].click()
            b[i].click()

    def Ethfx_all(self):###  二同号复选选 选择全部号码
        a=self.find_elements(*self.ethfx_th)
        for i in range(len(a)):
            a[i].click()
            a[i].click()

    def Ethfx(self,n):###二同号复选，选择n个号码
        a = self.find_elements(*self.ethfx_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def sbth(self,n):###三不同号，选择n个号码
        a = self.find_elements(*self.sbth_th)
        for i in random.sample(range(len(a)),n):
            a[i].click()

    def Slhtx_th(self):
        self.wait_element_located(self.driver,self.slhtx_th)
        self.find_element(*self.slhtx_th).click()###点击三连号通选 选号

    def Ebth(self,n):###选择二不同号N 个号码
        a = self.find_elements(*self.ebth)
        for i in random.sample(range(len(a)), n):
            a[i].click()