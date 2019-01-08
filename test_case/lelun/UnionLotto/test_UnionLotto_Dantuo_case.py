from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from test_case.Base.mytest import MyTest
from element_operate.UnionLotto.order_details import OrderDetails_lelun



class UnionLotto_DanTuo_case(MyTest):
    '''双色球胆拖玩法测试'''
    def test_UnionLotto_DanTuo_5_2_1_case(self):
        '''手选5个胆码2个拖码，1个蓝球的流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn= UnionLottoChooseNumber_lelun(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        ulcn.u_red_five_two() # 红球选取5个胆码2个拖码
        ulcn.u_bule_one()  # 选取一个蓝球
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()#关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_DanTuo_5_18_1_case(self):
        '''手选5个胆码18个拖码，1个蓝球的流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        ulcn.u_red_five_eighteen() # 红球选取5个胆码18个拖码
        ulcn.u_bule_one()  # 选取一个蓝球
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_DanTuo_5_18_16_case(self):
        '''手选5个胆码18个拖码，16个蓝球的流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        ulcn.u_red_five_eighteen() # 红球选取5个胆码18个拖码
        ulcn.u_bule_sixteen()  # 选取16个蓝球
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_DanTuo_6_19_1_case(self):
        '''手选6个胆码19个拖码，1个蓝球的流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.DanTuo_mode()  # 选择胆拖模式
        ulcn.u_red_six_nineteen()# 红球选取6个胆码19个拖码
        ulcn.u_bule_one()  # 选取1个蓝球
        ulcn.Confirm_button()  # 点击确认选号
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        l = Login_lelun(self.driver)
        l.login_lelun()  # 点击登录
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")

    def test_UnionLotto_DanTuo_5_2_16_case(self):
        """红球胆码5个 ，红球拖码 2个，蓝球16个"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = SubmitOrderSuccess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.DanTuo_mode() # 选择胆拖模式
        hb.u_red_five_two()#选择5个胆码2个拖码
        hb.u_bule_sixteen()##选择16个蓝球
        hb.Confirm_button()  # 确认选号
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('32', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_DanTuo_many_case(self):
        """增加倍数和期数"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = SubmitOrderSuccess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.DanTuo_mode()  # 选择胆拖模式
        hb.u_red_five_two()  # 红球选取5个胆码2个拖码
        hb.u_bule_one()  # 选取一个蓝球
        hb.Confirm_button()  # 确认选号
        hc.throw_times_input(13)
        hc.chase_ticket_button()  # 点击追xx期
        hc.chase_ticket_button_twenty()  # 点击追20期
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('2', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('13', nu)
        chase_time_text = hc.chase_time_text()  # 获取追号期数
        self.assertIn("20", chase_time_text)  # 检查追号期数为20期
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_DanTuo_Continue_buy_scheme_case(self):
        """继续购买该方案"""
        ha = HomePage_lelun(self.driver)
        hb = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = SubmitOrderSuccess_lelun(self.driver)
        he = OrderDetails_lelun(self.driver)
        hf = SubmitOrderSuccess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.DanTuo_mode()  # 选择胆拖模式
        hb.u_red_five_two()  # 红球选取5个胆码2个拖码
        hb.u_bule_one()  # 选取一个蓝球
        hb.Confirm_button()  # 确认选号
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('2', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        hd.check_order_details()  ##点击查看订单详情
        mur4 = he.order_status()
        self.assertEqual('待出票', mur4)
        he.Scheme()  # 点击继续购买该方案
        mur2 = hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主', mur2)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        ha.Moveable_float_close()
        text1 = hf.submit_order_success()  # 获取提交订单成功文本
        self.assertEqual('订单提交成功', text1)