from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import SubmitOrderSuccess_loc
from element_operate.base import Page_lexiu
from element_position.lexiu import SubmitOrderSuccess_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import SubmitOrderSuccess_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import SubmitOrderSuccess_lelun_loc

###提交订单成功页
class SubmitOrderSuccess(Page,SubmitOrderSuccess_loc):

    #################################元素操作###############################################
    #获取“提交订单成功”文本
    def submit_order_success(self):
        self.wait_element_located(self.driver,self.submit_order_success_text_loc)
        success_text = self.find_element(*self.submit_order_success_text_loc).text
        return success_text
    #获取“商品名称”文本
    def trade_name_text(self):
        self.wait_element_located(self.driver,self.trade_name_text_loc)
        trade_name = self.find_element(*self.trade_name_text_loc).text
        return trade_name
    #返回首页操作
    def return_home(self):
        self.find_element(*self.return_home_loc).click()
    #点击查看订单详情操作
    def check_order_details(self):
        self.wait_element_located(self.driver,self.check_order_details_loc)
        self.find_element(*self.check_order_details_loc).click()

    def Continue_buy(self):
        self.wait_element_located(self.driver, self.continue_buy)
        self.find_element(*self.continue_buy).click()  ###点击继续购买该彩种

class SubmitOrderSuccess_lexiu(Page_lexiu,SubmitOrderSuccess_lexiu_loc):

    #################################元素操作###############################################
    #获取“提交订单成功”文本
    def submit_order_success(self):
        self.wait_element_located(self.driver,self.submit_order_success_text_loc)
        success_text = self.find_element(*self.submit_order_success_text_loc).text
        return success_text
    #获取“商品名称”文本
    def trade_name_text(self):
        self.wait_element_located(self.driver,self.trade_name_text_loc)
        trade_name = self.find_element(*self.trade_name_text_loc).text
        return trade_name
    #返回首页操作
    def return_home(self):
        self.find_element(*self.return_home_loc).click()
    #点击查看订单详情操作
    def check_order_details(self):
        self.wait_element_located(self.driver,self.check_order_details_loc)
        self.find_element(*self.check_order_details_loc).click()

    def Continue_buy(self):
        self.wait_element_located(self.driver, self.continue_buy)
        self.find_element(*self.continue_buy).click()  ###点击继续购买该彩种

class SubmitOrderSuccess_leyou(Page_leyou,SubmitOrderSuccess_leyou_loc):

    #################################元素操作###############################################
    #获取“提交订单成功”文本
    def submit_order_success(self):
        self.wait_element_located(self.driver,self.submit_order_success_text_loc)
        success_text = self.find_element(*self.submit_order_success_text_loc).text
        return success_text
    #获取“商品名称”文本
    def trade_name_text(self):
        self.wait_element_located(self.driver,self.trade_name_text_loc)
        trade_name = self.find_element(*self.trade_name_text_loc).text
        return trade_name
    #返回首页操作
    def return_home(self):
        self.find_element(*self.return_home_loc).click()
    #点击查看订单详情操作
    def check_order_details(self):
        self.wait_element_located(self.driver,self.check_order_details_loc)
        self.find_element(*self.check_order_details_loc).click()

    def Continue_buy(self):
        self.wait_element_located(self.driver, self.continue_buy)
        self.find_element(*self.continue_buy).click()  ###点击继续购买该彩种

class SubmitOrderSuccess_lelun(Page_lelun,SubmitOrderSuccess_lelun_loc):

    #################################元素操作###############################################
    #获取“提交订单成功”文本
    def submit_order_success(self):
        self.wait_element_located(self.driver,self.submit_order_success_text_loc)
        success_text = self.find_element(*self.submit_order_success_text_loc).text
        return success_text
    #获取“商品名称”文本
    def trade_name_text(self):
        self.wait_element_located(self.driver,self.trade_name_text_loc)
        trade_name = self.find_element(*self.trade_name_text_loc).text
        return trade_name
    #返回首页操作
    def return_home(self):
        self.find_element(*self.return_home_loc).click()
    #点击查看订单详情操作
    def check_order_details(self):
        self.wait_element_located(self.driver,self.check_order_details_loc)
        self.find_element(*self.check_order_details_loc).click()

    def Continue_buy(self):
        self.wait_element_located(self.driver, self.continue_buy)
        self.find_element(*self.continue_buy).click()  ###点击继续购买该彩种





