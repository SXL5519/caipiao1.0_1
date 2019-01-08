from element_operate.base import Page
from element_position.lemi import JXKS_Confirm_loc
from element_operate.base import Page_lexiu
from element_position.lexiu import JXKS_Confirm_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import JXKS_Confirm_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import JXKS_Confirm_lelun_loc
class JXKS_Confirm(Page,JXKS_Confirm_loc):

    def Cont(self):
        self.find_element(*self.cont).click()  ###点击继续选号

    def Button_add(self):
        self.find_element(*self.button_add).click()##点击倍数+号

    def Button_less(self):
        self.find_element(*self.button_less).click()##点击倍数-号

class JXKS_Confirm_lexiu(Page_lexiu,JXKS_Confirm_lexiu_loc):

    def Cont(self):
        self.find_element(*self.cont).click()  ###点击继续选号

    def Button_add(self):
        self.find_element(*self.button_add).click()##点击倍数+号

    def Button_less(self):
        self.find_element(*self.button_less).click()##点击倍数-号

class JXKS_Confirm_leyou(Page_leyou,JXKS_Confirm_leyou_loc):

    def Cont(self):
        self.find_element(*self.cont).click()  ###点击继续选号

    def Button_add(self):
        self.find_element(*self.button_add).click()##点击倍数+号

    def Button_less(self):
        self.find_element(*self.button_less).click()##点击倍数-号

class JXKS_Confirm_lelun(Page_lelun,JXKS_Confirm_lelun_loc):

    def Cont(self):
        self.find_element(*self.cont).click()  ###点击继续选号

    def Button_add(self):
        self.find_element(*self.button_add).click()##点击倍数+号

    def Button_less(self):
        self.find_element(*self.button_less).click()##点击倍数-号