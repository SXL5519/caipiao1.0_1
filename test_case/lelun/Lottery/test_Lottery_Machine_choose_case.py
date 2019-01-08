from element_operate.BigLottery.BigLottery_confirm_lottery import BigLotteryConfirmLottery_lelun
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.BigLottery.BigLottery_choosenumber import BigLotteryChooseNum_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from test_case.Base.mytest import MyTest


class LotteryMachineChoose(MyTest):
    '''大乐透机选测试'''
#验证机选一注，追2期，输入投XX倍
    def test_Lottery_Machine_Choose_One_case(self):
        '''机选一注追加2期测试'''

        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()#关闭悬浮窗口
        hp.Lottery_link()#点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()#点击机选按钮
        ulcn.machine_choose_one_button()#点击机选一注
        ulcn.Confirm_button()#点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()#点击追xx期
        blcl.additional_radio_button()#点击追加单选按钮
        cl.chase_ticket_button_two()#点击追加2期单选按钮
        cl.throw_times_input(2)#输入投注倍数
        cl.submit_order_to_station_owner_button()#点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        # 返回首页
        sos.return_home()
##验证 机选5注，追5期，增加投注倍数按钮“+”，
    def test_Lottery_Machine_Choose_five_case(self):
        '''大乐透机选5注，追加5期测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_five_button()  # 点击机选5注
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_five()  # 点击追加5期单选按钮
        blcl.l_throw_times_button_add()  # 点击增加投注倍数
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        # 返回首页
        sos.return_home()

###验证机选10注，追10期，投注倍数“-”按钮
    def test_Lottery_Machine_Choose_ten_case(self):
        '''大乐透机选10注，追加10期测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_ten_button()  # 点击机选5注
        cl = ConfirmLottery_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_ten()  # 点击追加10期单选按钮
        blcl.l_throw_times_button_sub(3) #输入投注倍数，点击“-”按钮
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        # 返回首页
        sos.return_home()

# 验证机选一注，追20期，输入投XX倍
    def test_Lottery_Machine_Choose_chase20_case(self):
        '''机选一注追加20期测试'''

        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_twenty()  # 点击追加20期单选按钮
        cl.throw_times_input(2)  # 输入投注倍数
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        hp.Moveable_float_close()  # 关闭悬浮窗口
        # 返回首页
        sos.return_home()
# 验证机选一注，追50期，输入投XX倍
    def test_Lottery_Machine_Choose_chase50_case(self):
        '''机选一注追加50期测试'''

        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_fifty()  # 点击追加50期单选按钮
        cl.throw_times_input(2)  # 输入投注倍数
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        hp.Moveable_float_close()  # 关闭悬浮窗口
        # 返回首页
        sos.return_home()
#机选一注，继续选票，机选一注，确认选票（验证提交订单页的继续选票按钮）
    def test_Lottery_Machine_continue_choose_button_case(self):
        '''提交订单页继续选票按钮测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.continue_choose_num_button()#点击继续选号
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()#点击机选一注
        ulcn.Confirm_button()#点击确认选号
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Machine_continue_choose_double_button_case(self):
        '''提交订单页继续选票，复式选号流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        blcn = BigLotteryChooseNum_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.continue_choose_num_button()#点击继续选号
        blcn.l_red_label18()  # 任意选择18个红球
        blcn.l_bule_label2()  # 任意选择2个蓝球
        ulcn.Confirm_button()#点击确认选号
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
#验证提交订单页的机选一注按钮
    """def test_Lottery_Machine_choose_one_button_case(self):
        '''提交订单页机选一注测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.machine_choose_one_button()#点击机选一注
        cl.submit_order_to_station_owner_button()#提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")"""
    def test_Lottery_Machine_choose_one_button_delete_case(self):
        '''单式单注，验证删除流程'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_all_num_button()#点击删除所有按钮
        cl.confirm_delete_button()#确认删除
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl.submit_order_to_station_owner_button()#提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Machine_choose_one_button_double_delete_case(self):
        '''复式，验证删除流程'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        blcn = BigLotteryChooseNum_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_all_num_button()#点击删除所有按钮
        cl.confirm_delete_button()#确认删除
        blcn.l_red_label18()  # 任意选择18个红球
        blcn.l_bule_label2()  # 任意选择2个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl.submit_order_to_station_owner_button()#提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
#验证提交订单页"机选5注"按钮
    def test_Lottery_Machine_choose_five_button_case(self):
        '''提交订单页"机选5注"测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.machine_choose_five_button()  # 点击机选五注
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
#验证提交订单页“删除所有选号”按钮并确认删除
    def test_Lottery_Machine_delete_all_num(self):
        '''测试提交订单页"删除所有选号"按钮，确认删除'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_five_button()  # 点击机选5注
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_all_num_button()#点击删除所有选号按钮
        cl.confirm_delete_button()#点击确认删除按钮
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()#点击机选1注
        ulcn.Confirm_button()#确认选号
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
##验证提交订单页“删除所有选号”按钮并取消删除，删除不成功
    def test_Lottery_Machine_delete_all_num_cancel(self):
        '''测试提交订单页删除所有选号按钮，取消删除'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_five_button()  # 点击机选5注
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_all_num_button()  # 点击删除所有选号按钮
        cl.cancel_delete_button()# 点击取消删除按钮
        '''断言验证取消删除成功'''
        confirm_catchectic_text = cl.confirm_num_page_text()
        self.assertEqual("提交订单给站主", confirm_catchectic_text)
        print("我已放弃删除，回到了"+confirm_catchectic_text+"页")
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")

#验证提交订单页，确认并支付弹框的x按钮
    def test_Lottery_Machine_cancel_pay(self):
        '''测试提交订单页确认支付弹窗的x按钮'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()  # 关闭悬浮窗口
        hp.Lottery_link()  # 点击大乐透链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()#提交订单给站主
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.cancel_pay_button()#确认支付页点击x按钮
        '''断言验证取消支付成功'''
        text = cl.confirm_num_page_text()
        self.assertEqual("提交订单给站主", text)
        print("我已放弃删除，回到了" + text + "页")







