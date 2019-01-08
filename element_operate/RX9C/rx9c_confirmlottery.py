from element_position.lemi import RX9C_ConfirmLottery_loc
from element_operate.base import Page
import random
from time import sleep
from element_position.lexiu import RX9C_ConfirmLottery_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import RX9C_ConfirmLottery_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import RX9C_ConfirmLottery_lelun_loc
from element_operate.base import Page_lelun
class RX9C_ConfirmLottery(Page,RX9C_ConfirmLottery_loc):
    def Submit_station(self):
        self.wait_element_located(self.driver,self.submit_station)
        self.find_element(*self.submit_station).click()##点击提交给站主

    def Times_add(self):
        self.find_element(*self.times_add).click()###点击倍数+

    def Times_less(self):
        self.find_element(*self.times_less).click()##点击倍数-

    def Del_x(self):
        a=self.find_elements(*self.del_X_nu)
        i=random.randint(1,len(a))
        a[i-1].click()

    def Submit_station_text(self):##读取提交订单给站主文本
        a=self.find_element(*self.submit_station).text
        return a

class RX9C_ConfirmLottery_lexiu(Page_lexiu,RX9C_ConfirmLottery_lexiu_loc):
    def Submit_station(self):
        self.wait_element_located(self.driver,self.submit_station)
        self.find_element(*self.submit_station).click()##点击提交给站主

    def Times_add(self):
        self.find_element(*self.times_add).click()###点击倍数+

    def Times_less(self):
        self.find_element(*self.times_less).click()##点击倍数-

    def Del_x(self):
        a=self.find_elements(*self.del_X_nu)
        i=random.randint(1,len(a))
        a[i-1].click()

    def Submit_station_text(self):##读取提交订单给站主文本
        a=self.find_element(*self.submit_station).text
        return a

class RX9C_ConfirmLottery_leyou(Page_leyou,RX9C_ConfirmLottery_leyou_loc):
    def Submit_station(self):
        self.wait_element_located(self.driver,self.submit_station)
        self.find_element(*self.submit_station).click()##点击提交给站主

    def Times_add(self):
        self.find_element(*self.times_add).click()###点击倍数+

    def Times_less(self):
        self.find_element(*self.times_less).click()##点击倍数-

    def Del_x(self):
        a=self.find_elements(*self.del_X_nu)
        i=random.randint(1,len(a))
        a[i-1].click()

    def Submit_station_text(self):##读取提交订单给站主文本
        a=self.find_element(*self.submit_station).text
        return a

class RX9C_ConfirmLottery_lelun(Page_lelun,RX9C_ConfirmLottery_lelun_loc):
    def Submit_station(self):
        self.wait_element_located(self.driver,self.submit_station)
        self.find_element(*self.submit_station).click()##点击提交给站主

    def Times_add(self):
        self.find_element(*self.times_add).click()###点击倍数+

    def Times_less(self):
        self.find_element(*self.times_less).click()##点击倍数-

    def Del_x(self):
        a=self.find_elements(*self.del_X_nu)
        i=random.randint(1,len(a))
        a[i-1].click()

    def Submit_station_text(self):##读取提交订单给站主文本
        a=self.find_element(*self.submit_station).text
        return a