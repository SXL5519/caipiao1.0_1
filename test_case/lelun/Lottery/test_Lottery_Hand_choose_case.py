from time import sleep
from element_operate.BigLottery.BigLottery_choosenumber import BigLotteryChooseNum_lelun
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.BigLottery.BigLottery_confirm_lottery import BigLotteryConfirmLottery_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.UnionLotto.order_details import OrderDetails_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from element_operate.my_ticket import MyTicket_lelun
from element_operate.setup import SetUp_lelun
from test_case.Base.mytest import MyTest
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_lelun



class LotteryHandChooseCase(MyTest):
    '''大乐透手选测试'''
    def test_Lottery_Hand_choose_case(self):
        """大乐透手选5个红球2个蓝球购买流程测试"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcn.l_red_label5()#任意选择5个红球
        blcn.l_bule_label2()#任意选择2个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()#点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        '''hp.Moveable_float_close()
        # 返回首页
        sos.return_home()
        hp.Moveable_float_close()
        # 点击我的彩票，进入我的个人中心页面
        hp.MyTicket_link()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        # 点击个人中心页面右上角的设置，进入设置页面
        mt = MyTicket_lelun(self.driver)
        mt.setup_link()#点击设置按钮
        # 点击设置页面的“退出账户”按钮
        su = SetUp_lelun(self.driver)
        su.LogOut_button()'''

    def test_Lottery_Hand_r18b2_case(self):
        """大乐透手选18个红球2个蓝球购买流程测试"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcn.l_red_label18()  # 任意选择18个红球
        blcn.l_bule_label2()  # 任意选择2个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Hand_r5b12_case(self):
        """大乐透手选5个红球12个蓝球购买流程测试"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcn.l_red_label5()  # 任意选择5个红球
        blcn.l_bule_label12()  # 任意选择12个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Hand_r19_case(self):
        '''大乐透选取19个红球，第19个红球提示“红球不能超过18个”测试'''
        ###点击进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcn.l_red_label19()  # 选取19个红球
        text = blcn.out_of_num()#获取超过18个红球时的toast提示信息
        self.assertIn("红球不能超过18个",text)
        blcn.l_bule_label2()#选取2个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login_lelun(self.driver)  #####用户登录######
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Hand_r18b16_case(self):
        '''大乐透选取18个红球，12个蓝球提示“投注金额不能大于100000元”测试'''
        ###点击进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcn.l_red_label18()  # 选取18个红球
        blcn.l_bule_label12()#选取12个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login_lelun(self.driver)  #####用户登录######
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()#点击确认并支付按钮
        text = cl.out_max_pay()#获取超额提示信息文本
        self.assertIn("投注金额不能大于100000元",text)
        cl.re_selection_num()#点击重新选号链接
        blcn.l_bule_label12()#取消选中的12个蓝球
        blcn.l_bule_label2()#选取2个蓝球
        ulcn.Confirm_button()#点击确认选号
        sleep(2)#系统限制，操作订单不能过于频繁
        cl.submit_order_to_station_owner_button()#提交订单给站主
        cl.confirm_and_pay_button()#确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_re_r18b1_case(self):
        '''大乐透重复选号取消选中测试'''
        ###点击进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcn.l_rechoose_red_label18()#随机选中18个红球，再取消选中的红球
        blcn.l_red_label18()#重新选取18个红球
        blcn.l_bule_label2()#选取2个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()#点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login_lelun(self.driver)  #####用户登录######
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击确认并支付按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_Hand_choose_18_2_case(self):###################mj20171207
        """手选一注（复式），多注多倍，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        blcn.l_red_label18()  # 任意选择5个红球
        blcn.l_bule_label2()  # 任意选择2个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lelun(self.driver)
        cl.chase_ticket_button()  # 点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_two()  # 点击追加2期单选按钮
        cl.throw_times_input(3)  # 输入投注倍数
        num1 = cl.lottery_number_text()  # 获取注数
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取倍数
        self.assertEqual("856823", num1 + chase + times)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        '''hp.Moveable_float_close()
        # 返回首页
        sos.return_home()
        hp.Moveable_float_close()
        # 点击我的彩票，进入我的个人中心页面
        hp.MyTicket_link()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        # 点击个人中心页面右上角的设置，进入设置页面
        mt = MyTicket_lelun(self.driver)
        mt.setup_link()  # 点击设置按钮
        # 点击设置页面的“退出账户”按钮
        su = SetUp_lelun(self.driver)
        su.LogOut_button()'''
    def test_Lottery_Hand_choose_single_chase_throws_case(self):
        """手动选号，单式，多注多倍，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        blcn.l_red_label5()#任意选择5个红球
        blcn.l_bule_label2()#任意选择2个蓝球
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.Confirm_button()#点击确认选号按钮
        cl.chase_ticket_button()  # 点击追xx期
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_button_two()  # 点击追加2期单选按钮
        cl.throw_times_input(3)  # 输入投注倍数
        num1=cl.lottery_number_text()#获取注数
        chase = cl.chase_time_text()#获取追号期数
        times = cl.throw_time_text()#获取倍数
        self.assertEqual("123",num1+chase+times)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        '''hp.Moveable_float_close()
        # 返回首页
        sos.return_home()
        hp.Moveable_float_close()
        # 点击我的彩票，进入我的个人中心页面
        hp.MyTicket_link()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        # 点击个人中心页面右上角的设置，进入设置页面
        mt = MyTicket_lelun(self.driver)
        mt.setup_link()#点击设置按钮
        # 点击设置页面的“退出账户”按钮
        su = SetUp_lelun(self.driver)
        su.LogOut_button()'''
    def test_Lottery_Hand_history_Recommended_number_case(self):
        """选号页历史开奖，使用推荐号码，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn.History()#点击历史开奖
        ulcn.click_history()#点击展开了的历史开奖
        lottery1 = ulcn.Recommended_nu()  # 读取推荐号码
        ulcn.Recommended_number()#点击使用推荐号码
        ulcn.Confirm_button()  # 点击确认选号按钮
        num1 = cl.lottery_number_text()  # 获取注数
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取倍数
        self.assertEqual("111", num1 + chase + times)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        sos.check_order_details()  ##点击查看订单详情
        lottery2 = od.Betting_number()  ##读取显示的投注号码
        self.assertEqual(lottery1, lottery2)
    def test_Lottery_Hand_history_one_bet_one_times_case(self):
        """选号页面，右上方隐藏的历史走势历史走势，一注一倍，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.History_movements()#点击历史走势
        ulcn.Red_movements()#点击红球走势
        ulcn.History_red(5)#点击5个红球
        ulcn.Bule_movements()#点击蓝球走势
        blcn.bule_history_choose(2)#点击2个蓝球
        ulcn.Recommended_number()#点击【使用已选号码】
        ulcn.Confirm_button()  # 点击确认选号按钮
        num1 = cl.lottery_number_text()  # 获取注数
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取倍数
        self.assertEqual("111", num1 + chase + times)
        mul1 = cl.Select_number()#获取投注确认页投注的号码
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        sos.check_order_details()  ##点击查看订单详情
        lottery2 = od.Betting_nu()  ##读取显示的投注号码
        self.assertEqual(mul1, lottery2)
#################mj20171208
    def test_Lottery_Hand_history_double_bet_double_times_case(self):
        """选号页面，右上方隐藏的历史走势历史走势，多注多倍，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.History_movements()#点击历史走势
        ulcn.Red_movements()#点击红球走势
        ulcn.History_red(7)#点击7个红球
        ulcn.Bule_movements()#点击蓝球走势
        blcn.bule_history_choose(3)#点击3个蓝球
        ulcn.Recommended_number()#点击【使用已选号码】
        ulcn.Confirm_button()  # 点击确认选号按钮
        blcl.additional_radio_button()  # 点击追加单选按钮
        cl.chase_ticket_input(2)  # 输入追2期
        cl.throw_times_input(3)  # 输入投注倍数
        num1 = cl.lottery_number_text()  # 获取注数
        chase = cl.chase_time_text()  # 获取追号期数
        times = cl.throw_time_text()  # 获取倍数
        self.assertEqual("6323", num1 + chase + times)
        mul1 = cl.Select_number()#获取投注确认页投注的号码
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login_lelun(self.driver)
        #l.new_user_login_tab()  # 切换到新用户登录
        l.login_lelun()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        sos.check_order_details()  ##点击查看订单详情
        lottery2 = od.Betting_after()  ##读取显示的投注号码
        self.assertEqual(mul1, lottery2)
    def test_Lottery_multiphase_machine_choose5_case(self):
        """选号页面，右上方隐藏的多期机选，5期提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        ulcn.many_machine_choose(5)#点击5期
        text1=ulcn.many_machine_choose_text()
        self.assertIn("1注 5期 1倍",text1,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        #####用户登录######
        l = Login_lelun(self.driver)
        l.login_lelun()
        ulcn.There_clock()  # 点击。。。
        ulcn.Many_pause()  # 点击多期机选
        ulcn.many_machine_choose(5)  # 点击5期
        ulcn.Many_pause_confirm()  # 点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_multiphase_machine_choose10_case(self):
        """选号页面，右上方隐藏的多期机选，10期提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        ulcn.many_machine_choose(10)#点击10期
        text1=ulcn.many_machine_choose_text()
        self.assertIn("1注 10期 1倍",text1,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_multiphase_machine_choose20_case(self):
        """选号页面，右上方隐藏的多期机选，20期提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        ulcn.many_machine_choose(20)#点击20期
        text1=ulcn.many_machine_choose_text()
        self.assertIn("1注 20期 1倍",text1,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_multiphase_machine_choose50_case(self):
        """选号页面，右上方隐藏的多期机选，50期提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        ulcn.many_machine_choose(50)#点击50期
        text1=ulcn.many_machine_choose_text()
        self.assertIn("1注 50期 1倍",text1,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_multiphase_machine_input_case(self):
        """选号页面，右上方隐藏的多期机选，输入3，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        ulcn.many_choose_input(3)#输入追3期
        text1=ulcn.many_machine_choose_text()
        self.assertIn("1注 3期 1倍",text1,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")

    def test_Lottery_multiphase_machine_double_add_case(self):
        """选号页面，右上方隐藏的多期机选，双击+，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        text1 = ulcn.many_machine_choose_text()
        text2=int(text1[2:5])#切出点击+之前的期数
        ulcn.many_choose_add()#点击+按钮
        ulcn.many_choose_add()  # 点击+按钮
        text3=ulcn.many_machine_choose_text()
        self.assertIn(str(text2+2),text3,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_multiphase_machine_double_sub_case(self):
        """选号页面，右上方隐藏的多期机选，双击-，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        text1 = ulcn.many_machine_choose_text()
        text2=int(text1[2:5])#切出点击+之前的期数
        ulcn.many_choose_sub()#点击-按钮
        ulcn.many_choose_sub()  # 点击-按钮
        text3=ulcn.many_machine_choose_text()
        self.assertIn(str(text2-2),text3,'多期机选有误')
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_Lottery_multiphase_machine_single_radio_case(self):
        """选号页面，右上方隐藏的多期机选，点击追加单选按钮，提交订单"""
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()#点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn=UnionLottoChooseNumber_lelun(self.driver)
        ulcn.There_clock()#点击。。。
        ulcn.Many_pause()#点击多期机选
        ulcn.many_chase_radio()#点击多期机选的单选按钮
        text1=ulcn.many_machine_choose_text()
        ulcn.Many_pause_confirm()#点击多期机选页的【提交订单】
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_LotteryOderDetails_continue_case(self):
        '''提交订单成功页，点击【继续投注该彩种】，页面跳转至选号页验证'''
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        blcn.l_red_label5()#选择5个红球
        blcn.l_bule_label2()#选择2个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        mu1=cl.Select_number()#读取投注确认页所选号码
        cl.submit_order_to_station_owner_button()#提交订单给站主按钮
        cl.confirm_and_pay_button()#点击确认支付
        hp.Moveable_float_close()
        sos.check_order_details()#点击查看订单详情
        mu2=od.Betting_nu()#读取订单详情页号码
        self.assertEqual(mu1,mu2,'订单详情页显示有误')
        od.continue_buy()#点击继续投注该彩种
        blcn.l_red_label5()  # 选择5个红球
        blcn.l_bule_label2()  # 选择2个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
    def test_LotteryOderDetails_continue_buy_case(self):
        '''提交订单成功页，点击【继续购买该方案】，页面跳转至投注确认页'''
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        blcn.l_red_label5()#选择5个红球
        blcn.l_bule_label2()#选择2个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        mu1=cl.Select_number()#读取投注确认页所选号码
        cl.submit_order_to_station_owner_button()#提交订单给站主按钮
        cl.confirm_and_pay_button()#点击确认支付
        hp.Moveable_float_close()
        sos.check_order_details()#点击查看订单详情
        mu2=od.Betting_nu()#读取订单详情页号码
        self.assertEqual(mu1,mu2,'订单详情页显示有误')
        od.Scheme()#点击继续购买此方案
        mur = cl.confirm_num_page_text()
        self.assertEqual('提交订单给站主', mur)
    def test_SuccessPage_continue_buy_case(self):
        '''订单详情页，点击【点击投注大乐透】，页面跳转至选号页面，选择一注，提交订单'''
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        blcn.l_red_label5()  # 选择5个红球
        blcn.l_bule_label2()  # 选择2个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        mu1 = cl.Select_number()  # 读取投注确认页所选号码
        cl.submit_order_to_station_owner_button()  # 提交订单给站主按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()
        sos.Continue_buy()#点击继续购买此彩种
        blcn.l_red_label5()  # 选择5个红球
        blcn.l_bule_label2()  # 选择2个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
    def test_many_lottery_ckick_x_case(self):
        '''在投注确认页面，多注号码，点击左边X按钮，能够删除所选号码'''
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()#点击机选按钮
        ulcn.machine_choose_five_button()#点击机选5注
        num = cl.event_count()  # 获取总共有多少注
        print("删除前共有%d场" % num)
        for i in range(0, num):
            cl.Del_x() #点击单个删除x
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_one_button()  # 点击机选1注
        ulcn.Confirm_button()  # 确认选号
        num1 = cl.lottery_number_text()  # 获取注数
        self.assertIn("1", num1)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-大乐透", trade_name)
    def test_one_lottery_ckick_x_case(self):
        '''在投注确认页面，单注号码，点击左边X按钮，页面能跳转到选号页'''
        ###点击进入大乐透进入大乐透选号页面###
        hp = HomePage_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        l = Login_lelun(self.driver)
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.Lottery_link()  # 点击大乐透链接
        blcn = BigLotteryChooseNum_lelun(self.driver)
        blcl = BigLotteryConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        ulcn.machine_choose_button()#点击机选按钮
        ulcn.machine_choose_one_button()#点击机选1注
        ulcn.Confirm_button()  # 确认选号
        mur = cl.lottery_number_text()
        self.assertEqual('1', mur)
        cl.Del_x() #点击单个删除x
        ulcn.machine_choose_button()  # 点击机选按钮
        ulcn.machine_choose_five_button()  # 点击机选5注
        num1 = cl.lottery_number_text()  # 获取注数
        self.assertIn("5", num1)
        cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-大乐透", trade_name)



























