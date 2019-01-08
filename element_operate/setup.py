from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import Setup_loc
from element_operate.base import Page_lexiu
from element_position.lexiu import Setup_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import Setup_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import Setup_lelun_loc
#设置页面
class SetUp(Page,Setup_loc):
#################################元素操作###############################################
    #点击“退出当前账号”按钮
    def LogOut_button(self):
        self.wait_element_located(self.driver,self.LogOut_button_loc)
        self.find_element(*self.LogOut_button_loc).click()

#设置页面
class SetUp_lexiu(Page_lexiu,Setup_lexiu_loc):
#################################元素操作###############################################
    #点击“退出当前账号”按钮
    def LogOut_button(self):
        self.wait_element_located(self.driver,self.LogOut_button_loc)
        self.find_element(*self.LogOut_button_loc).click()

class SetUp_leyou(Page_leyou,Setup_leyou_loc):
#################################元素操作###############################################
    #点击“退出当前账号”按钮
    def LogOut_button(self):
        self.wait_element_located(self.driver,self.LogOut_button_loc)
        self.find_element(*self.LogOut_button_loc).click()

class SetUp_lelun(Page_lelun,Setup_lelun_loc):
#################################元素操作###############################################
    #点击“退出当前账号”按钮
    def LogOut_button(self):
        self.wait_element_located(self.driver,self.LogOut_button_loc)
        self.find_element(*self.LogOut_button_loc).click()