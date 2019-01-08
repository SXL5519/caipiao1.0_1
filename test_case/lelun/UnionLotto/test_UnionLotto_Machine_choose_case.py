from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.UnionLotto.order_details import OrderDetails_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from element_operate.my_ticket import MyTicket_lelun
from element_operate.setup import SetUp_lelun
from test_case.Base.mytest import MyTest


class UnionLottoMachineChooseCase(MyTest):

    """双色球机选购买流程测试"""
##验证从登录到退出的主流程
    def test_UnionLotto_Machine_choose_one_case(self):
        '''机选一注测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()#点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()#点击机选
        ulcn.machine_choose_one_button()#机选一注
        ulcn.Confirm_button()#确认选号
        ######进入提交订单页面######
        cl = ConfirmLottery_lelun(self.driver)
        lottery_number_text = cl.lottery_number_text()
        self.assertIn("1",lottery_number_text)#检查投注注数为1注
        cl.submit_order_to_station_owner_button()#点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()#点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()#点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功",text)
        trade_text = sos.trade_name_text()#获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球",trade_text)#检查商品名称正确

#验证机选一注，确认支付取消流程
    def test_UnionLotton_Machine_cancel_pay(self):
        '''机选一注取消支付测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()# 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()# 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.cancel_pay_button()#点击取消支付x按钮
        '''断言验证取消支付成功'''
        text = cl.confirm_num_page_text()
        self.assertEqual("提交订单给站主", text)
        print("我已放弃删除，回到了" + text + "页")
#验证提交订单页，“继续选号”按钮
    def test_UnionLotto_Machine_continue_choose_button(self):
        '''机选一注“继续选号”按钮测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.continue_choose_num_button()#点击“继续选号”按钮
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        lottery_number_text = cl.lottery_number_text()
        self.assertIn("2",lottery_number_text)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()#确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()#关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()#查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check() #检查订单详情页
#验证提交订单页面“机选1注”按钮
    """def test_UnionLotto_Machine_choose_one_button_case(self):
        '''提交订单页“机选1注”按钮测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.machine_choose_one_button()#点击机选一注
        lottery_number_text = cl.lottery_number_text()
        self.assertIn("2",lottery_number_text)#检查投注的注数为2注
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()#关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页"""
#验证提交订单页“机选5注”按钮测试
    def test_UnionLotto_Machine_choose_five_button_case(self):
        '''提交订单页“机选5注”按钮测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.machine_choose_five_button() # 点击机选5注
        lottery_number_text = cl.lottery_number_text()#获取投注注数文本
        self.assertIn("6",lottery_number_text)#检查投注注数为6倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_chase_two_case(self):
        '''追2期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()#点击追xx期
        cl.chase_ticket_button_two()#点击追2期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1倍
        chase_time_text = cl.chase_time_text()#获取追号期数
        self.assertIn("2",chase_time_text)#检查追号期数为2期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页

    def test_UnionLotto_Machine_chase_five_case(self):
        '''追5期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        cl.chase_ticket_button_five()  # 点击追5期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("5", chase_time_text)  # 检查追号期数为5期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_chase_ten_case(self):
        '''追10期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        cl.chase_ticket_button_ten()  # 点击追10期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("10", chase_time_text)  # 检查追号期数为10期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_chase_twenty_case(self):
        '''追20期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        cl.chase_ticket_button_twenty()  # 点击追20期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("20", chase_time_text)  # 检查追号期数为20期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_chase_fifty_case(self):
        '''追50期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        cl.chase_ticket_button_fifty()  # 点击追50期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("50", chase_time_text)  # 检查追号期数为50期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_chase_three_case(self):
        '''输入追3期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_input("3")#输入追3期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("3", chase_time_text)  # 检查追号期数为3期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()
        hp.Moveable_float_close()  # 关闭弹窗
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页

    def test_UnionLotto_Machine_chase_four_sub_case(self):
        '''输入追4期点击-流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_input("4")#输入追4期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("4", chase_time_text)  # 检查追号期数为4期
        cl.u_chase_ticket_sub_button()#点击追期-
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("3", chase_time_text)  # 检查追号期数为3期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_chase_four_add_case(self):
        '''输入追4期点击+流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_input("4")#输入追4期
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("4", chase_time_text)  # 检查追号期数为4期
        cl.u_chase_ticket_add_button()#点击追期+
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = cl.chase_time_text()  # 获取追号期数
        self.assertIn("5", chase_time_text)  # 检查追号期数为5期
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_input_three_times_case(self):
        '''输入投3倍流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.throw_times_input("3")#输入投注倍数为3倍
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text() #获取投注倍数定位
        self.assertIn("3",throw_times)#检查投注倍数为3倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_input_three_times_sub_case(self):
        '''输入投3倍,再点击-流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.throw_times_input("3")#输入投注倍数为3倍
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text() #获取投注倍数定位
        self.assertIn("3",throw_times)#检查投注倍数为3倍
        cl.u_throw_times_button_sub()#点击-
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text()  # 获取投注倍数定位
        self.assertIn("2", throw_times)  # 检查投注倍数为2倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_input_three_times_add_case(self):
        '''输入投3倍,再点击+流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.throw_times_input("3")#输入投注倍数为3倍
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text() #获取投注倍数定位
        self.assertIn("3",throw_times)#检查投注倍数为3倍
        cl.u_throw_times_button_add()#点击+
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text()  # 获取投注倍数定位
        self.assertIn("4", throw_times)  # 检查投注倍数为4倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_times_sub_case(self):
        '''默认投注倍数为1倍时,再点击-流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text() #获取投注倍数定位
        self.assertIn("1",throw_times)#检查投注倍数为3倍
        cl.u_throw_times_button_sub()#点击-
        lottery_number_text = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number_text)  # 检查投注注数为1注
        throw_times = cl.throw_time_text()  # 获取投注倍数定位
        self.assertIn("1", throw_times)  # 检查投注倍数为1倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
#验证提交订单页，“删除所有选号”按钮测试并确认删除，删除成功
    """def test_UnionLotto_Machine_delete_all_num_case(self):
        '''提交订单页“删除所有选号”按钮并确认删除测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()#确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_all_num_button()#点击删除所有选号
        cl.confirm_delete_button()#点击确定删除按钮
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()#确认选号
        cl = ConfirmLottery_lelun(self.driver)
        lottery_number = cl.lottery_number_text()#获取投注注数文本
        self.assertIn("1",lottery_number)#检查投注注数
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页"""
#验证提交订单页面，“删除所有选号”按钮并取消，删除失败
    """def test_UnionLotto_Machine_delete_all_num_cancel_case(self):
        '''提交订单页“删除所有选号”按钮并取消测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.cancel_delete_button() # 点击取消删除按钮
        cl = ConfirmLottery_lelun(self.driver)
        lottery_number = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number)  # 检查投注注数
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页"""

    def test_UnionLotto_Machine_delete_one_num_cancel_case(self):
        '''提交订单页“单个删除选号”按钮测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.delete_one_num_button() # 点击单个删除选号
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        ulcn.Confirm_button()  # 确认选号
        lottery_number = cl.lottery_number_text()  # 获取投注注数文本
        self.assertIn("1", lottery_number)  # 检查投注注数
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
        #验证机选5注
    def test_UnionLotto_Machine_choose_five_case(self):
        '''机选五注流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ######进入提交订单页面######
        cl = ConfirmLottery_lelun(self.driver)
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()#获取投注注数
        self.assertEqual("5",lottery_num)#检查投注的注数为5注
        self.assertEqual("1", chase)  # 检查追号期数是否是所选期数
        self.assertEqual("1", times)  # 检查投注倍数是否是所投注倍数
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭弹窗
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
    def test_UnionLotto_Machine_choose_five_delete_all_case(self):
        '''机选五注全部删除并确定流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ######进入提交订单页面######
        cl = ConfirmLottery_lelun(self.driver)
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()#获取投注注数
        self.assertEqual("5",lottery_num)#检查投注的注数为5注
        self.assertEqual("1", chase)  # 检查追号期数1期
        self.assertEqual("1", times)  # 检查投注倍数1倍
        cl.delete_all_num_button()#点击删除所有选号
        cl.confirm_delete_button()#点击确认删除
        ulcn.machine_choose_button()#点击机选按钮
        ulcn.machine_choose_one_button()#点击机选1注
        ulcn.Confirm_button()#确认选号
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()  # 获取投注注数
        self.assertEqual("1", lottery_num)  # 检查投注的注数为1注
        self.assertEqual("1", chase)  # 检查追号期数1期
        self.assertEqual("1", times)  # 检查投注倍数1倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页
    '''def test_UnionLotto_Machine_choose_five_delete_all_cancel_case(self):
        """机选五注全部删除并取消删除流程测试"""
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ######进入提交订单页面######
        cl = ConfirmLottery_lelun(self.driver)
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()#获取投注注数
        self.assertEqual("5",lottery_num)#检查投注的注数为5注
        self.assertEqual("1", chase)  # 检查追号期数1期
        self.assertEqual("1", times)  # 检查投注倍数1倍
        cl.delete_all_num_button()#点击删除所有选号
        cl.cancel_delete_button()#点击取消删除
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()  # 获取投注注数
        self.assertEqual("5", lottery_num)  # 检查投注的注数为5注
        self.assertEqual("1", chase)  # 检查追号期数1期
        self.assertEqual("1", times)  # 检查投注倍数1倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        """断言验证提交订单成功"""
        sos = SubmitOrderSuccess_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页'''
    def test_UnionLotto_Machine_choose_five_delete_one_case(self):
        '''机选五注删除一注流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ######进入提交订单页面######
        cl = ConfirmLottery_lelun(self.driver)
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()#获取投注注数
        self.assertEqual("5",lottery_num)#检查投注的注数为5注
        self.assertEqual("1", chase)  # 检查追号期数1期
        self.assertEqual("1", times)  # 检查投注倍数1倍
        cl.delete_one_num_button()#点击删除一注
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()  # 获取投注注数
        self.assertEqual("4", lottery_num)  # 检查投注的注数为4注
        self.assertEqual("1", chase)  # 检查追号期数1期
        self.assertEqual("1", times)  # 检查投注倍数1倍
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页

    def test_UnionLotto_Machine_choose_ten__case(self):
        '''机选十注流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ####选择机选一注并确认选号####
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        ######进入提交订单页面######
        cl = ConfirmLottery_lelun(self.driver)
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取输入的投注倍数
        lottery_num = cl.lottery_number_text()  # 获取投注注数
        self.assertEqual("10", lottery_num)  # 检查投注的注数为10注
        self.assertEqual("1", chase)  # 检查追号期数是否是所选期数
        self.assertEqual("1", times)  # 检查投注倍数是否是所投注倍数
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        trade_text = sos.trade_name_text()  # 获取商品名称
        self.assertIn("商品名称：乐仑炫彩-双色球", trade_text)  # 检查商品名称正确
        sos.check_order_details()  # 查看订单详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_checks()  # 检查订单详情页

    def test_UnionLotto_machine_one_after(self):
        """机选一注之后，新增选号，变为复式"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.machine_choose_button()  # 点击机选
        hb.machine_choose_one_button()  # 机选一注
        hb.Confirm_button()  # 确认选号
        hc.re_selection_num()
        hb.Select_bule()###添加一个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('2', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_assemblage_after(self):
        """多注（复式、单式组合）选号"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.machine_choose_button()  # 点击机选
        hb.machine_choose_one_button()  # 机选一注
        hb.Confirm_button()  # 确认选号
        hc.continue_choose_num_button()##继续选号
        hb.u_red_label18()  # 任意选择18个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('18565', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_history_recommend(self):
        """使用推荐号码投注（一注一倍）"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=SubmitOrderSuccess_lelun(self.driver)
        he=OrderDetails_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.There_clock()##点击右上角。。。
        hb.History_movements()##点击历史走势
        mur=hb.Recommended_nu()#读取推荐号码
        hb.Recommended_number()#点击使用推荐号码
        hb.Confirm_button()  # 确认选号
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        hd.check_order_details()##点击查看订单详情
        mur1=he.Betting_number()##读取显示的投注号码
        self.assertEqual(mur,mur1)

    def test_UnionLotto_history_recommend_many(self):
        """使用推荐号码投注（多注注多倍）"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=SubmitOrderSuccess_lelun(self.driver)
        he=OrderDetails_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.There_clock()##点击右上角。。。
        hb.History_movements()##点击历史走势
        hb.Recommended_nu()#读取推荐号码
        hb.Recommended_number()#点击使用推荐号码
        hb.Select_bule()##点击一个蓝球
        hb.Confirm_button()  # 确认选号
        mur2=hc.Select_number()##读取投注号码
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('2', mur)  ##断言
        hc.throw_times_input(13)  ###点击倍数输入功能
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('13', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        hd.check_order_details()##点击查看订单详情
        mur1 = he.Betting_nu()  ##读取显示的投注号码
        self.assertEqual(mur2,mur1)

    def test_UnionLotto_Continue_pick(self):
        """继续选号添加复式选号"""
        ha = HomePage_lelun(self.driver)
        hb=UnionLottoChooseNumber_lelun(self.driver)
        hc=ConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.continue_choose_num_button()##继续选号
        hb.u_red_label18()  # 任意选择18个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('18565', mur)
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()##点击提交给站主


