from element_operate.base import Page
from element_position.lemi import HomePage_loc
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException,TimeoutException
from time import sleep
from element_position.lexiu import HomePage_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import HomePage_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import HomePage_lelun_loc
from element_operate.base import Page_lelun

class HomePage(Page,HomePage_loc):
    ################################首页元素操作##############################################
    def header_text(self):##获取首页顶端文本
        self.wait_element_located(self.driver,self.header_text_loc)
        text=self.find_element(*self.header_text_loc).text
        return text

    ##判断是否出现浮层弹框，如果出现浮层点击X
    def Moveable_float_close(self):
        try:
            self.find_element(*self.Moveable_float_close_loc).click()
        except ElementNotVisibleException:
            print("没有弹窗")
        except NoSuchElementException:
            print("没有弹窗")
    #点击双色球链接
    def UnionLotto_link(self):
        try:
            self.find_element(*self.UnionLotto_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.UnionLotto_link_loc)
            self.find_element(*self.UnionLotto_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.UnionLotto_link_loc)
            self.find_element(*self.UnionLotto_link_loc).click()  # 对目标进行点击
    #点击大乐透链接
    def Lottery_link(self):
        try:
            self.find_element(*self.Lottery_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.Lottery_link_loc)
            self.find_element(*self.Lottery_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.Lottery_link_loc)
            self.find_element(*self.Lottery_link_loc).click()  # 对目标进行点击
    #点击广东11选5链接
    def gd_11_5_link(self):
        try:
            self.find_element(*self.gd_11_5_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.gd_11_5_link_loc)
            self.find_element(*self.gd_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gd_11_5_link_loc)
            self.find_element(*self.gd_11_5_link_loc).click()  # 对目标进行点击
    # 点击广西11选5链接
    def gx_11_5_link(self):
        try:
            self.find_element(*self.gx_11_5_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.gx_11_5_link_loc)
            self.find_element(*self.gx_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gx_11_5_link_loc)
            self.find_element(*self.gx_11_5_link_loc).click()  # 对目标进行点击
    #点击竞彩足球链接
    def paintball_link(self):
        try:
            self.find_element(*self.paintball_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.paintball_link_loc)
            self.find_element(*self.paintball_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.paintball_link_loc)
            self.find_element(*self.paintball_link_loc).click()  # 对目标进行点击
    #点击竞足单关链接
    def single_foot_link(self):
        try:
            self.find_element(*self.single_foot_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.single_foot_link_loc)
            self.find_element(*self.single_foot_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.single_foot_link_loc)
            self.find_element(*self.single_foot_link_loc).click()  # 对目标进行点击
    #点击竞彩篮球链接
    def haobc_link(self):
        try:
            self.find_element(*self.haobc_link_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()  # 对目标进行点击
    #点击竞篮单关
    def single_basketball_link(self):
        try:
            self.find_element(*self.single_basketball_loc).click()
        except NoSuchElementException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()  # 点击更多彩票
            self.wait_element_located(self.driver,self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()  # 对目标进行点击
    #点击福彩3D链接
    def fucai_3D_link(self):
        try:
            self.find_element(*self.fucai_3D_link_loc).click()
        except TimeoutException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.fucai_3D_link_loc)
            self.find_element(*self.fucai_3D_link_loc).click()  # 对目标进行点击
        except WebDriverException:
            self.more_lottery_link()  # 点击更多彩票
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.fucai_3D_link_loc)
            self.find_element(*self.fucai_3D_link_loc).click()

    #点击任选9场
    def optional_9_link(self):
        try:
            self.find_element(*self.optional_9_link_loc).click()
        except ElementNotVisibleException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.more_lottery_link()#点击更多彩票
            self.wait_element_located(self.driver,self.optional_9_link_loc)
            self.find_element(*self.optional_9_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.optional_9_link_loc)
            self.find_element(*self.optional_9_link_loc).click()#对目标进行点击

    # 点击重庆时时彩
    def cqssc_link(self):
        try:
            self.find_element(*self.cqssc_link_loc).click()
        except WebDriverException:
            self.more_lottery_link()  # 点击更多彩票
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.cqssc_link_loc)
            self.find_element(*self.cqssc_link_loc).click()
        except ElementNotVisibleException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.cqssc_link_loc)
            self.find_element(*self.cqssc_link_loc).click()  # 对目标进行点击

    #点击胜负14场
    def victory_defeat_14_link(self):
        try:
            self.find_element(*self.victory_or_defeat_link_loc).click()
        except ElementNotVisibleException:
            self.more_lottery_link()#点击更多彩票
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.victory_or_defeat_link_loc)
            self.find_element(*self.victory_or_defeat_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.victory_or_defeat_link_loc)
            self.find_element(*self.victory_or_defeat_link_loc).click()#点击胜负14场
    #点击江西快三
    def jiangxi_express_three_link(self):
        try:
            self.find_element(*self.jiangxi_express_three_link_loc).click()
        except WebDriverException:
            self.more_lottery_link()#点击更多彩票
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.jiangxi_express_three_link_loc)
            self.find_element(*self.jiangxi_express_three_link_loc).click()
        except ElementNotVisibleException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.jiangxi_express_three_link_loc)
            self.find_element(*self.jiangxi_express_three_link_loc).click()#对目标进行点击
    #点击排列5
    def rank_five_link(self):
        try:
            self.find_element(*self.rank_five_link_loc).click()
        except ElementNotVisibleException:
            self.more_lottery_link()  # 点击更多彩票
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_five_link_loc)
            self.find_element(*self.rank_five_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.rank_five_link_loc)
            self.find_element(*self.rank_five_link_loc).click()  # 对目标进行点击
    #点击排列三
    def rank_three_link(self):
        try:
            self.find_element(*self.rank_three_link_loc).click()
        except ElementNotVisibleException:
            self.more_lottery_link()  # 点击更多彩票
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_three_link_loc)
            self.find_element(*self.rank_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.rank_three_link_loc)
            self.find_element(*self.rank_three_link_loc).click()  # 对目标进行点击
    #点击七彩星
    def colorful_star_link(self):
        try:
            self.find_element(*self.colorful_star_link_loc).click()
        except WebDriverException:
            self.more_lottery_link()  # 点击更多彩票
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.colorful_star_link_loc)
            self.find_element(*self.colorful_star_link_loc).click()
        except ElementNotVisibleException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.colorful_star_link_loc)
            self.find_element(*self.colorful_star_link_loc).click()  # 对目标进行点击
    #点击山东十一选五
    def sd_11_5_link(self):
        try:
            self.find_element(*self.shandong_11x5_link_loc).click()
        except ElementNotVisibleException:
            self.more_lottery_link()  # 点击更多彩票
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.shandong_11x5_link_loc)
            self.find_element(*self.shandong_11x5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.shandong_11x5_link_loc)
            self.find_element(*self.shandong_11x5_link_loc).click()  # 对目标进行点击

    #点击更多彩种
    def more_lottery_link(self):
        self.wait_element_located(self.driver,self.more_lottery_link_loc)
        self.find_element(*self.more_lottery_link_loc).click()

    #点击我的彩票链接
    def MyTicket_link(self):
        self.wait_element_located(self.driver,self.MyTicket_link_loc)
        self.find_element(*self.MyTicket_link_loc).click()
    #点击下方tab首页链接
    def homepage_link(self):
        self.wait_element_located(self.driver,self.HomePage_link_loc)
        self.find_element(*self.HomePage_link_loc).click()

    def My_lottery_ticket(self):
        self.wait_element_located(self.driver, self.my_lottery_ticket)
        self.find_element(*self.my_lottery_ticket).click()##点击首页我的彩票

    def My_lottery_ticket_text(self):
        self.wait_element_located(self.driver, self.my_lottery_ticket)
        a=self.find_element(*self.my_lottery_ticket).text##点击首页我的彩票
        return a

    def Lemi(self):
        self.wait_element_located(self.driver, self.lemi)
        aa=self.find_element(*self.lemi).text##读取乐米彩票文本
        return aa

    def Home_page(self):
        self.find_element(*self.home_page).click()##点击首页

    def Lottery_information(self):
        self.find_element(*self.lottery_information).click()###点击开奖信息

    def Activity_zone(self):
        target = self.find_element(*self.activity_zone)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.lucky_pick).click()##点击幸运选号


#############乐秀
class HomePage_lexiu(Page_lexiu,HomePage_lexiu_loc):
    ################################首页元素操作##############################################
    def header_text(self):##获取首页顶端文本
        self.wait_element_located(self.driver,self.header_text_loc)
        text=self.find_element(*self.header_text_loc).text
        return text

    ##判断是否出现浮层弹框，如果出现浮层点击X
    def Moveable_float_close(self):
        try:
            self.find_element(*self.Moveable_float_close_loc).click()
        except ElementNotVisibleException:
            print("没有弹窗")
        except NoSuchElementException:
            print("没有弹窗")
    #点击双色球链接
    def UnionLotto_link(self):
        try:
            self.find_element(*self.UnionLotto_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.UnionLotto_link_loc)
            self.find_element(*self.UnionLotto_link_loc).click()
    #点击大乐透链接
    def Lottery_link(self):
        try:
            self.find_element(*self.Lottery_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.Lottery_link_loc)
            self.find_element(*self.Lottery_link_loc).click()

    #点击广东11选5链接
    def gd_11_5_link(self):
        try:
            self.find_element(*self.gd_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gd_11_5_link_loc)
            self.find_element(*self.gd_11_5_link_loc).click()

    # 点击广西11选5链接
    def gx_11_5_link(self):
        try:
            self.find_element(*self.gx_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gx_11_5_link_loc)
            self.find_element(*self.gx_11_5_link_loc).click()

    #点击竞彩足球链接
    def paintball_link(self):
        try:
            self.find_element(*self.paintball_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.paintball_link_loc)
            self.find_element(*self.paintball_link_loc).click()

    #点击竞足单关链接
    def single_foot_link(self):
        try:
            self.find_element(*self.single_foot_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.single_foot_link_loc)
            self.find_element(*self.single_foot_link_loc).click()

    #点击竞彩篮球链接
    def haobc_link(self):
        try:
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()

    #点击竞篮单关
    def single_basketball_link(self):
        try:
            self.wait_element_located(self.driver, self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()

    #点击福彩3D链接
    def fucai_3D_link(self):
        try:
            self.find_element(*self.fucai_3D_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,700)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.fucai_3D_link_loc)
            self.find_element(*self.fucai_3D_link_loc).click()

    #点击任选9场
    def optional_9_link(self):
        try:
            self.find_element(*self.optional_9_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.optional_9_link_loc)
            self.find_element(*self.optional_9_link_loc).click()


    # 点击重庆时时彩
    def cqssc_link(self):
        try:
            self.find_element(*self.cqssc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.cqssc_link_loc)
            self.find_element(*self.cqssc_link_loc).click()


    #点击胜负14场
    def victory_defeat_14_link(self):
        try:
            self.find_element(*self.victory_or_defeat_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.victory_or_defeat_link_loc)
            self.find_element(*self.victory_or_defeat_link_loc).click()

    #点击广西快三
    def guangxi_express_three_link(self):
        try:
            self.find_element(*self.guangxi_express_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.guangxi_express_three_link_loc)
            self.find_element(*self.guangxi_express_three_link_loc).click()

    # 点击江西快三
    def jiangxi_express_three_link(self):
        try:
            self.find_element(*self.jiangxi_express_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.jiangxi_express_three_link_loc)
            self.find_element(*self.jiangxi_express_three_link_loc).click()


    #点击排列5
    def rank_five_link(self):
        try:
            self.find_element(*self.rank_five_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_five_link_loc)
            self.find_element(*self.rank_five_link_loc).click()

    #点击排列三
    def rank_three_link(self):
        try:
            self.find_element(*self.rank_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,1000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_three_link_loc)
            self.find_element(*self.rank_three_link_loc).click()
    #点击七彩星
    def colorful_star_link(self):
        try:
            self.find_element(*self.colorful_star_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,10000)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.colorful_star_link_loc)
            self.find_element(*self.colorful_star_link_loc).click()

    #点击山东十一选五
    def sd_11_5_link(self):
        try:
            self.find_element(*self.shandong_11x5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.shandong_11x5_link_loc)
            self.find_element(*self.shandong_11x5_link_loc).click()

    '''#点击更多彩种
    def more_lottery_link(self):
        self.wait_element_located(self.driver,self.more_lottery_link_loc)
        self.find_element(*self.more_lottery_link_loc).click()'''

    #点击我的彩票链接
    def MyTicket_link(self):
        self.wait_element_located(self.driver,self.MyTicket_link_loc)
        self.find_element(*self.MyTicket_link_loc).click()
    #点击下方tab首页链接
    def homepage_link(self):
        self.wait_element_located(self.driver,self.HomePage_link_loc)
        self.find_element(*self.HomePage_link_loc).click()

    def My_lottery_ticket(self):
        self.wait_element_located(self.driver, self.my_lottery_ticket)
        self.find_element(*self.my_lottery_ticket).click()##点击首页我的彩票

    def Lemi(self):
        self.wait_element_located(self.driver, self.lemi)
        aa=self.find_element(*self.lemi).text##读取乐米彩票文本
        return aa

    def Home_page(self):
        self.find_element(*self.home_page).click()##点击首页

    def Lottery_information(self):
        self.find_element(*self.lottery_information).click()###点击开奖信息

    def Activity_zone(self):
        target = self.find_element(*self.activity_zone)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.lucky_pick).click()##点击幸运选号

class HomePage_leyou(Page_leyou,HomePage_leyou_loc):
    ################################首页元素操作##############################################
    def header_text(self):##获取首页顶端文本
        self.wait_element_located(self.driver,self.header_text_loc)
        text=self.find_element(*self.header_text_loc).text
        return text

    ##判断是否出现浮层弹框，如果出现浮层点击X
    def Moveable_float_close(self):
        try:
            self.find_element(*self.Moveable_float_close_loc).click()
        except ElementNotVisibleException:
            print("没有弹窗")
        except NoSuchElementException:
            print("没有弹窗")
    #点击双色球链接
    def UnionLotto_link(self):
        try:
            self.find_element(*self.UnionLotto_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.UnionLotto_link_loc)
            self.find_element(*self.UnionLotto_link_loc).click()
    #点击大乐透链接
    def Lottery_link(self):
        try:
            self.find_element(*self.Lottery_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.Lottery_link_loc)
            self.find_element(*self.Lottery_link_loc).click()

    #点击广东11选5链接
    def gd_11_5_link(self):
        try:
            self.find_element(*self.gd_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gd_11_5_link_loc)
            self.find_element(*self.gd_11_5_link_loc).click()

    # 点击广西11选5链接
    def gx_11_5_link(self):
        try:
            self.find_element(*self.gx_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gx_11_5_link_loc)
            self.find_element(*self.gx_11_5_link_loc).click()

    #点击竞彩足球链接
    def paintball_link(self):
        try:
            self.find_element(*self.paintball_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.paintball_link_loc)
            self.find_element(*self.paintball_link_loc).click()

    #点击竞足单关链接
    def single_foot_link(self):
        try:
            self.find_element(*self.single_foot_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.single_foot_link_loc)
            self.find_element(*self.single_foot_link_loc).click()

    #点击竞彩篮球链接
    def haobc_link(self):
        try:
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()

    #点击竞篮单关
    def single_basketball_link(self):
        try:
            self.wait_element_located(self.driver, self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()

    #点击福彩3D链接
    def fucai_3D_link(self):
        try:
            self.find_element(*self.fucai_3D_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.fucai_3D_link_loc)
            self.find_element(*self.fucai_3D_link_loc).click()

    #点击任选9场
    def optional_9_link(self):
        try:
            self.find_element(*self.optional_9_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,700)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.optional_9_link_loc)
            self.find_element(*self.optional_9_link_loc).click()


    # 点击重庆时时彩
    def cqssc_link(self):
        try:
            self.find_element(*self.cqssc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,700)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.cqssc_link_loc)
            self.find_element(*self.cqssc_link_loc).click()


    #点击胜负14场
    def victory_defeat_14_link(self):
        try:
            self.find_element(*self.victory_or_defeat_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.victory_or_defeat_link_loc)
            self.find_element(*self.victory_or_defeat_link_loc).click()

    #点击广西快三
    def guangxi_express_three_link(self):
        try:
            self.find_element(*self.guangxi_express_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.guangxi_express_three_link_loc)
            self.find_element(*self.guangxi_express_three_link_loc).click()

    # 点击江西快三
    def jiangxi_express_three_link(self):
        try:
            self.find_element(*self.jiangxi_express_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.jiangxi_express_three_link_loc)
            self.find_element(*self.jiangxi_express_three_link_loc).click()


    #点击排列5
    def rank_five_link(self):
        try:
            self.find_element(*self.rank_five_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_five_link_loc)
            self.find_element(*self.rank_five_link_loc).click()

    #点击排列三
    def rank_three_link(self):
        try:
            self.find_element(*self.rank_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_three_link_loc)
            self.find_element(*self.rank_three_link_loc).click()
    #点击七彩星
    def colorful_star_link(self):
        try:
            self.find_element(*self.colorful_star_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,700)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.colorful_star_link_loc)
            self.find_element(*self.colorful_star_link_loc).click()

    #点击山东十一选五
    def sd_11_5_link(self):
        try:
            self.find_element(*self.shandong_11x5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.shandong_11x5_link_loc)
            self.find_element(*self.shandong_11x5_link_loc).click()

    '''#点击更多彩种
    def more_lottery_link(self):
        self.wait_element_located(self.driver,self.more_lottery_link_loc)
        self.find_element(*self.more_lottery_link_loc).click()'''

    #点击我的彩票链接
    def MyTicket_link(self):
        self.wait_element_located(self.driver,self.MyTicket_link_loc)
        self.find_element(*self.MyTicket_link_loc).click()
    #点击下方tab首页链接
    def homepage_link(self):
        self.wait_element_located(self.driver,self.HomePage_link_loc)
        self.find_element(*self.HomePage_link_loc).click()

    def My_lottery_ticket(self):
        self.wait_element_located(self.driver, self.my_lottery_ticket)
        self.find_element(*self.my_lottery_ticket).click()##点击首页我的彩票

    def Lemi(self):
        self.wait_element_located(self.driver, self.lemi)
        aa=self.find_element(*self.lemi).text##读取乐米彩票文本
        return aa

    def Home_page(self):
        self.find_element(*self.home_page).click()##点击首页

    def Lottery_information(self):
        self.find_element(*self.lottery_information).click()###点击开奖信息

    def Activity_zone(self):
        target = self.find_element(*self.activity_zone)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.lucky_pick).click()##点击幸运选号

class HomePage_lelun(Page_lelun,HomePage_lelun_loc):
    ################################首页元素操作##############################################
    def header_text(self):##获取首页顶端文本
        self.wait_element_located(self.driver,self.header_text_loc)
        text=self.find_element(*self.header_text_loc).text
        return text

    ##判断是否出现浮层弹框，如果出现浮层点击X
    def Moveable_float_close(self):
        try:
            self.find_element(*self.Moveable_float_close_loc).click()
        except ElementNotVisibleException:
            print("没有弹窗")
        except NoSuchElementException:
            print("没有弹窗")
    #点击双色球链接
    def UnionLotto_link(self):
        try:
            self.find_element(*self.UnionLotto_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.UnionLotto_link_loc)
            self.find_element(*self.UnionLotto_link_loc).click()
    #点击大乐透链接
    def Lottery_link(self):
        try:
            self.find_element(*self.Lottery_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.Lottery_link_loc)
            self.find_element(*self.Lottery_link_loc).click()

    #点击广东11选5链接
    def gd_11_5_link(self):
        try:
            self.find_element(*self.gd_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gd_11_5_link_loc)
            self.find_element(*self.gd_11_5_link_loc).click()

    # 点击广西11选5链接
    def gx_11_5_link(self):
        try:
            self.find_element(*self.gx_11_5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.gx_11_5_link_loc)
            self.find_element(*self.gx_11_5_link_loc).click()

    #点击竞彩足球链接
    def paintball_link(self):
        try:
            self.find_element(*self.paintball_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.paintball_link_loc)
            self.find_element(*self.paintball_link_loc).click()

    #点击竞足单关链接
    def single_foot_link(self):
        try:
            self.find_element(*self.single_foot_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.single_foot_link_loc)
            self.find_element(*self.single_foot_link_loc).click()

    #点击竞彩篮球链接
    def haobc_link(self):
        try:
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.haobc_link_loc)
            self.find_element(*self.haobc_link_loc).click()

    #点击竞篮单关
    def single_basketball_link(self):
        try:
            self.wait_element_located(self.driver, self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()
        except WebDriverException:
            js = "window.scroll(0,300)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.single_basketball_loc)
            self.find_element(*self.single_basketball_loc).click()

    #点击福彩3D链接
    def fucai_3D_link(self):
        try:
            self.find_element(*self.fucai_3D_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,700)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.fucai_3D_link_loc)
            self.find_element(*self.fucai_3D_link_loc).click()

    #点击任选9场
    def optional_9_link(self):
        try:
            self.find_element(*self.optional_9_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.optional_9_link_loc)
            self.find_element(*self.optional_9_link_loc).click()


    # 点击重庆时时彩
    def cqssc_link(self):
        try:
            self.find_element(*self.cqssc_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.cqssc_link_loc)
            self.find_element(*self.cqssc_link_loc).click()


    #点击胜负14场
    def victory_defeat_14_link(self):
        try:
            self.find_element(*self.victory_or_defeat_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.victory_or_defeat_link_loc)
            self.find_element(*self.victory_or_defeat_link_loc).click()

    #点击广西快三
    def guangxi_express_three_link(self):
        try:
            self.find_element(*self.guangxi_express_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.guangxi_express_three_link_loc)
            self.find_element(*self.guangxi_express_three_link_loc).click()

    # 点击江西快三
    def jiangxi_express_three_link(self):
        try:
            self.find_element(*self.jiangxi_express_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.jiangxi_express_three_link_loc)
            self.find_element(*self.jiangxi_express_three_link_loc).click()


    #点击排列5
    def rank_five_link(self):
        try:
            self.find_element(*self.rank_five_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_five_link_loc)
            self.find_element(*self.rank_five_link_loc).click()

    #点击排列三
    def rank_three_link(self):
        try:
            self.find_element(*self.rank_three_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver,self.rank_three_link_loc)
            self.find_element(*self.rank_three_link_loc).click()
    #点击七彩星
    def colorful_star_link(self):
        try:
            self.find_element(*self.colorful_star_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.colorful_star_link_loc)
            self.find_element(*self.colorful_star_link_loc).click()

    #点击山东十一选五
    def sd_11_5_link(self):
        try:
            self.find_element(*self.shandong_11x5_link_loc).click()
        except WebDriverException:
            js = "window.scroll(0,500)"
            self.driver.execute_script(js)
            self.wait_element_located(self.driver, self.shandong_11x5_link_loc)
            self.find_element(*self.shandong_11x5_link_loc).click()

    '''#点击更多彩种
    def more_lottery_link(self):
        self.wait_element_located(self.driver,self.more_lottery_link_loc)
        self.find_element(*self.more_lottery_link_loc).click()'''

    #点击我的彩票链接
    def MyTicket_link(self):
        self.wait_element_located(self.driver,self.MyTicket_link_loc)
        self.find_element(*self.MyTicket_link_loc).click()
    #点击下方tab首页链接
    def homepage_link(self):
        self.wait_element_located(self.driver,self.HomePage_link_loc)
        self.find_element(*self.HomePage_link_loc).click()

    def My_lottery_ticket(self):
        self.wait_element_located(self.driver, self.my_lottery_ticket)
        self.find_element(*self.my_lottery_ticket).click()##点击首页我的彩票

    def Lemi(self):
        self.wait_element_located(self.driver, self.lemi)
        aa=self.find_element(*self.lemi).text##读取乐米彩票文本
        return aa

    def Home_page(self):
        self.find_element(*self.home_page).click()##点击首页

    def Lottery_information(self):
        self.find_element(*self.lottery_information).click()###点击开奖信息

    def Activity_zone(self):
        target = self.find_element(*self.activity_zone)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.find_element(*self.lucky_pick).click()##点击幸运选号