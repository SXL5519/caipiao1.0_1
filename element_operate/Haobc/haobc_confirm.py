from element_operate.base import Page
from element_position.lemi import HaobcLotteryConfirm
from element_operate.base import Page_lexiu
from element_position.lexiu import HaobcLotteryConfirm_lexiu
from element_operate.base import Page_leyou
from element_position.leyou import HaobcLotteryConfirm_leyou
from element_operate.base import Page_lelun
from element_position.lelun import HaobcLotteryConfirm_lelun
##竞彩篮球投注确认页元素操作
class HaobcConfirm(Page,HaobcLotteryConfirm):

    def edit_event(self):
        self.wait_element_located(self.driver,self.edit_event_loc)
        self.find_element(*self.edit_event_loc).click()

class HaobcConfirm_lexiu(Page_lexiu,HaobcLotteryConfirm_lexiu):

    def edit_event(self):
        self.wait_element_located(self.driver,self.edit_event_loc)
        self.find_element(*self.edit_event_loc).click()

class HaobcConfirm_leyou(Page_leyou,HaobcLotteryConfirm_leyou):

    def edit_event(self):
        self.wait_element_located(self.driver,self.edit_event_loc)
        self.find_element(*self.edit_event_loc).click()

class HaobcConfirm_lelun(Page_lelun,HaobcLotteryConfirm_lelun):

    def edit_event(self):
        self.wait_element_located(self.driver,self.edit_event_loc)
        self.find_element(*self.edit_event_loc).click()