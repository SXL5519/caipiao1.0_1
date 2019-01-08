from time import sleep

from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.login import Login
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm
from element_operate.SingleFoot.single_foot_confim import SingleFootConfirmLottery
from element_operate.SingleFoot.single_foot_choose_number import SingleFootChooseNumber
class Singlefoot_dgp_case(MyTest):
    """竞足单关，单关配玩法"""
    def test_Play_dgp_choosnumber(self):
        """验证单关配玩法赛事结果功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1=SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()##点击弹框
        aa = hb1.Paintball_single_dgp() # 点击展开投注
        if aa == 1:
            hb1.Paintball_single_dgp_nus_X(1)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hb1.Know_dgp()##点击我知道了
            hc2.Times_input_click()  #####点击倍数输入框
            hc2.Times_number(10)  ####点击10倍
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_choosnumber_too(self):
        """验证单关配玩法选择2场赛事，弹出提示框，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1=SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(2) # 点击展开投注
        if aa >0:
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hb1.Know_dgp()##点击我知道了
            hc2.Times_input_click()  #####点击倍数输入框
            hc2.Times_number(10)  ####点击10倍
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_emptying(self):
        """验证选号页面清空按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)###随机点击1场比赛
        if aa>0:
            hb1.Emptying_pbs()###点击清空
            hb.confirm_match()  ###点击已选N场比赛
            hb1.Paintball_single_dgp_nus_X(1)  ###随机点击1场比赛
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hb1.Know_dgp()  ##点击我知道了
            hc2.Times_input_click()  #####点击倍数输入框
            hc2.Times_number(10)  ####点击10倍
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_Add_event(self):
        """验证添加/编辑赛事按钮，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)  ###随机点击1场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.Add_event_rqspf()  ###点击编辑/添加赛事
            mul = hb.Play_fb()  ###读取文本
            self.assertEqual('玩\n法', mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hb1.Know_dgp()  ##点击我知道了
            hc2.Times_input_click()  #####点击倍数输入框
            hc2.Times_number(10)  ####点击10倍
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_Pf_del_icon(self):
        """验证删除选择的全部赛事图标，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)  ###随机点击1场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.down_bf()
            hc2.Pf_del_icon()##点击删除图标
            hc.confirm_delete_button()
            hb.top_more()
            hb1.Paintball_single_dgp_nus_X(1)
            mul = hb.Text_confirm_loc()
            self.assertEqual('已选%d场比赛' % aa, mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hb1.Know_dgp()  ##点击我知道了
            hc2.Times_input_click()  #####点击倍数输入框
            hc2.Times_number(10)  ####点击10倍
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_Times_input(self):
        """验证修改倍数输入框功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.Times_input(33)  #####修改倍数为3
            mul = hc1.Lottery_dgp()  ###获取倍数
            self.assertEqual('共396元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc2.Times_input(10)  #####修改倍数为10
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_Btn_less(self):
        """验证修改倍数 - 功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.Times_input(34)  #####修改倍数为3
            hc2.Btn_less()  ####点击倍数-
            mul = hc1.Lottery_dgp()  ###获取倍数
            self.assertEqual('共396元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc2.Times_input(10)  #####修改倍数为10
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_dgp_Btn_add(self):
        """验证修改倍数 +功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)  ###随机点击2场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            #hc2.Times_input(32)  #####修改倍数为3
            hc2.Btn_add()  ####点击倍数+
            mul = hc1.Lottery_dgp()  ###获取倍数
            self.assertEqual('共132元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc2.Times_input(10)  #####修改倍数为3
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付


    def test_Play_dgp_Btn_eighty(self):
        """验证80倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = SingleFootChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = SingleFootConfirmLottery(self.driver)
        hc2 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_foot_link()  ###点击竞足单关
        hb.Play_f()  ####点击玩法
        hb1.Play_dgp()  ###点击单关配
        sleep(1)
        hb1.Dgp_tan()  ##点击弹框
        aa = hb1.Paintball_single_dgp_nus_X(1)  ###随机点击2场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.Times_input_click()  #####点击倍数输入框
            hc2.Times_number(80)  ####点击80倍
            mul = hc1.Lottery_dgp()  ###获取倍数
            self.assertEqual('共960元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc2.Times_input(10)  #####修改倍数为3
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

