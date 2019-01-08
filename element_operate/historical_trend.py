from element_position.lemi import HistoricalTrend_loc
from element_operate.base import Page
from element_position.lexiu import HistoricalTrend_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import HistoricalTrend_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import HistoricalTrend_lelun_loc
from element_operate.base import Page_lelun


class HistoricalTrend(Page,HistoricalTrend_loc):

    ##点击使用推荐号码定位
    def use_recommend_num_button(self):
        self.wait_element_located(self.driver,self.use_recommend_num_button_loc)
        self.find_element(*self.use_recommend_num_button_loc).click()

class HistoricalTrend_lexiu(Page_lexiu,HistoricalTrend_lexiu_loc):

    ##点击使用推荐号码定位
    def use_recommend_num_button(self):
        self.wait_element_located(self.driver,self.use_recommend_num_button_loc)
        self.find_element(*self.use_recommend_num_button_loc).click()

class HistoricalTrend_leyou(Page_leyou,HistoricalTrend_leyou_loc):

    ##点击使用推荐号码定位
    def use_recommend_num_button(self):
        self.wait_element_located(self.driver,self.use_recommend_num_button_loc)
        self.find_element(*self.use_recommend_num_button_loc).click()

class HistoricalTrend_lelun(Page_lelun,HistoricalTrend_lelun_loc):

    ##点击使用推荐号码定位
    def use_recommend_num_button(self):
        self.wait_element_located(self.driver,self.use_recommend_num_button_loc)
        self.find_element(*self.use_recommend_num_button_loc).click()


