from element_operate.BigLottery.BigLottery_choosenumber import BigLotteryChooseNum_lexiu
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.BigLottery.BigLottery_confirm_lottery import BigLotteryConfirmLottery_lexiu
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lexiu
from element_operate.homepage import HomePage_lexiu
from element_operate.login import Login_lexiu
from test_case.Base.mytest import MyTest
from time import sleep

class Lottery_DanTuo_case(MyTest):
    '''大乐透胆拖模式测试'''
    def test_Lottery_Dantuo_1_5_1_2_case(self):
        '''胆拖模式前区选择1个胆码，5个拖码，后区选择1个胆码，2个拖码测试流程'''
        ###点击进入大乐透选号页面###
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        blcn.l_red_one_five()  # 红球选取1个胆码5个拖码
        blcn.l_bule_one_two()  # 后区选择1个胆码2个拖码
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lexiu(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lexiu(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lexiu()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")

    def test_Lottery_Dantuo_4_2_1_11_case(self):
        '''胆拖模式前区选择4个胆码，2个拖码，后区选择1个胆码，11个拖码测试流程'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        blcn.l_red_four_two()  # 红球选取4个胆码2个拖码
        blcn.l_bule_one_eleven()  # 后区选择1个胆码11个拖码
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lexiu(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lexiu(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lexiu()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Dantuo_1_18_1_2_case(self):
        '''胆拖模式前区选择1个胆码，18个拖码，后区选择1个胆码，2个拖码测试流程'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        blcn.l_red_one_eighteen()  # 红球选取1个胆码18个拖码
        blcn.l_bule_one_two()  # 后区选择1个胆码2个拖码
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lexiu(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lexiu(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lexiu()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_DanTuo_4_18_1_11_case(self):
        '''胆拖模式前区选择4个胆码，18个拖码，后区选择1个胆码，11个拖码测试流程'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        blcn.l_red_four_eighteen()  # 红球选取4个胆码18个拖码
        blcn.l_bule_one_eleven()  # 后区选择1个胆码11个拖码
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lexiu(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lexiu(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lexiu()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Dantuo_5_19_2_2_case(self):
        '''胆拖模式前区选择5个胆码，19个拖码，后区选择2个胆码，2个拖码,弹出提示信息测试流程'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        blcn.l_red_five_nineteen()  # 红球选取5个胆码19个拖码
        blcn.l_bule_two_two()  # 后区选择2个胆码2个拖码
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lexiu(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lexiu(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lexiu()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Dantuo_1_5_1_2_chase_throws_case(self):
        '''胆拖投注，在投注确认页面增加倍数和期数，提交订单'''
        ###点击进入大乐透选号页面###
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        blcl = BigLotteryConfirmLottery_lexiu(self.driver)
        cl =ConfirmLottery_lexiu(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        blcn.l_red_one_five()  # 红球选取1个胆码5个拖码
        blcn.l_bule_one_two()  # 后区选择1个胆码2个拖码
        ulcn.Confirm_button()  # 点击确认选号
        cl.chase_ticket_button()#点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_two()  # 点击追加2期单选按钮
        cl.throw_times_input(2)  # 输入投注倍数
        cl.submit_order_to_station_owner_button()#点击提交订单给站主
        l = Login_lexiu(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lexiu()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")