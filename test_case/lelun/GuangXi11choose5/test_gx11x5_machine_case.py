from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_lelun
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_lelun
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.UnionLotto.order_details import OrderDetails_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.historical_trend import HistoricalTrend_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from test_case.Base.mytest import MyTest


###广西11选5机选玩法测试---mj171101
class gxElevenChooseFiveCase(MyTest):
    '''广西11选5测试'''

    def test_use_recommand_num_case(self):
        '''使用推荐号码测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.current_period()  # 点击“正在开奖中”
        efcn.spread_historical_trend()  # 点击进入历史趋势页
        ht = HistoricalTrend_lelun(self.driver)
        ht.use_recommend_num_button()  # 点击使用推荐号码
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素
    def test_machine_choose_one_case(self):
        '''机选一注流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_button_case(self):
        '''投注确认页“机选一注”按钮测试流程'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.machine_choose_one()  # 点击“机选一注”按钮
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数
        self.assertIn("2注1期1倍", check)  ##验证投注注数、投注期号、投注倍数
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_five_button_case(self):
        '''投注确认页“机选五注”按钮测试流程'''
        hp = HomePage_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.machine_choose_five()  # 点击“机选5注”按钮
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数
        self.assertIn("6注1期1倍", check)  ##验证投注注数、投注期号、投注倍数
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_checks()  # 检查订单详情页页面元素

    def test_machine_choose_continue_button_case(self):
        '''投注确认页“继续选号”按钮测试流程'''
        hp = HomePage_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.continue_choose_num()  # 点击“继续选号”按钮
        efcn.hand_options(3)#任选三个号码（复式）
        efcn.confirm_number_button()  # 确认选号
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数
        self.assertIn("4注1期1倍", check)  ##验证投注注数、投注期号、投注倍数
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_chase2_case(self):
        '''机选一注追2期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_button()  # 点击追xxx期
        cl.chase_ticket_button_two()  # 点击追两期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注2期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_chase5_case(self):
        '''机选一注追5期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_button()  # 点击追xxx期
        cl.chase_ticket_button_five()  # 点击追5期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注5期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_chase10_case(self):
        '''机选一注追10期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_button()  # 点击追xxx期
        cl.chase_ticket_button_ten()  # 点击追10期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注10期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_chase20_case(self):
        '''机选一注追20期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_button()  # 点击追xxx期
        cl.chase_ticket_button_twenty()  # 点击追20期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注20期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_chase50_case(self):
        '''机选一注追50期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_button()  # 点击追xxx期
        cl.chase_ticket_button_fifty()  # 点击追50期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注50期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_input_chase3_case(self):
        '''机选一注输入追90期流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_input("90")  # 输入追90期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注90期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_input_chase3_sub_case(self):
        '''机选一注输入追3期，点击投注倍数的-按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_input("3")  # 输入追3期
        ecfcl.chase_sub_button()  # 点击投注倍数的-按钮
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注2期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_input_chase3_add_case(self):
        '''机选一注输入追3期，点击投注倍数的+按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.chase_ticket_input("3")  # 输入追3期
        ecfcl.chase_add_button()  # 点击投注倍数的+按钮
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注4期1倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.chase_order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_throw_input_case(self):
        '''机选一注输入投90倍流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.throw_times_input("90")  # 输入投90倍
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注1期90倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_throw_sub_case(self):
        '''机选一注输入投3倍,点击-流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.throw_times_input("3")  # 输入投3倍
        ecfcl.throw_times_sub_button()  # 点击投注倍数的-
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注1期2倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_throw_add_case(self):
        '''机选一注输入投3倍，点击投注倍数的+按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl = ConfirmLottery_lelun(self.driver)
        ecfcl.throw_times_input("3")  # 输入投3倍
        ecfcl.throw_times_add_button()  # 点击投注倍数的+按钮
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("1注1期4倍", check)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_delete_all_case(self):
        '''机选一注，投注确认页点击删除所有选号并确认按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", check)
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.confirm_delete_button()  # 点击确认删除所有选号
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_delete_all_cancel_case(self):
        '''机选一注，投注确认页点击删除所有选号按钮并取消删除流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.cancel_delete_button()  # 点击取消删除所有选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_one_delete_one_case(self):
        '''在投注确认页面，单注号码，点击左边X按钮，页面能跳转到选号页'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", check)
        ecfcl.delete_one_button()  # 点击删除单个选号
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 确认选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_five_case(self):
        '''机选5注流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_five_delete_one_case(self):
        '''机选5注，投注确认页点击单个删除选号按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("5注1期1倍", check)
        ecfcl.delete_one_button()  # 点击删除单个选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("4注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_five_delete_all_case(self):
        '''机选5注，投注确认页点击删除所有选号按钮并确认删除流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("5注1期1倍", check)
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.confirm_delete_button()  # 点击确认删除选号
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        efcn.confirm_number_button()  # 确认选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_five_delete_all_cancel_case(self):
        '''机选5注，投注确认页点击删除选号按钮并取消删除流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("5注1期1倍", check)
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.cancel_delete_button()  # 点击取消删除选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("5注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_ten_case(self):
        '''机选10注流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl = ConfirmLottery_lelun(self.driver)
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_checks()  # 检查订单详情页页面元素

    def test_machine_choose_ten_delete_one_case(self):
        '''机选10注，投注确认页点击单个删除选号按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("10注1期1倍", check)
        ecfcl.delete_one_button()  # 点击删除单个选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("9注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_ten_delete_all_case(self):
        '''机选10注，投注确认页点击删除所有选号按钮并确认删除流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("10注1期1倍", check)
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.confirm_delete_button()  # 点击确认删除选号
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选一注
        efcn.confirm_number_button()  # 确认选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_check()  # 检查订单详情页页面元素

    def test_machine_choose_ten_delete_all_cancel_case(self):
        '''机选10注，投注确认页点击删除选号按钮并取消删除流程测试'''
        hp = HomePage_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        ecfcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ecfcl.countdown_text()  # 检查倒计时文案
        check = ecfcl.lottery_chase_throw_text()
        self.assertIn("10注1期1倍", check)
        cl.delete_all_num_button()  # 点击删除所有选号
        cl.cancel_delete_button()  # 点击取消删除选号
        recheck = ecfcl.lottery_chase_throw_text()
        self.assertIn("10注1期1倍", recheck)
        ecfcl.submit_order_button()  # 提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 登录
        ecfcl.submit_order_button()  # 提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-广西11选5", trade_name)
        sos.check_order_details()  # 点击查看详情
        od = OrderDetails_lelun(self.driver)
        od.order_details_checks()  # 检查订单详情页页面元素













