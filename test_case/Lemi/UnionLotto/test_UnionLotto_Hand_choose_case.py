from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.UnionLotto.order_details import OrderDetails
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.homepage import HomePage
from element_operate.login import Login
from element_operate.my_ticket import MyTicket
from element_operate.setup import SetUp
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from time import sleep
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber


class UnionLottoHandChooseCase(MyTest):
    '''双色球手选测试'''

    def test_UnionLotto_Hand_choose_case(self):
        """双色球手选6个红球1个蓝球购买流程测试"""
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()#点击双色球链接

        #选号
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_red_label6()#任意选择6个红球
        ulcn.u_bule_label1()#任意选择1个蓝球
        ulcn.Confirm_button()#点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login(self.driver)
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        '''hp.Moveable_float_close()
        # 返回首页
        sos.return_home()
        # 点击我的彩票，进入我的个人中心页面
        hp.MyTicket_link()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        # 点击个人中心页面右上角的设置，进入设置页面
        mt = MyTicket(self.driver)
        mt.setup_link()#点击设置按钮
        # 点击设置页面的“退出账户”按钮
        su = SetUp(self.driver)
        su.LogOut_button()'''

    def test_UnionLotto_Hand_r18b1_case(self):
        """双色球手选18个红球1个蓝球购买流程测试"""
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_red_label18()#选取18个红球
        ulcn.u_bule_label1()#选取1个蓝球
        ulcn.Confirm_button()#点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()#提交订单给站主
        l = Login(self.driver)#####用户登录######
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_Hand_r6b16_case(self):
        '''双色球手选6个红球16个蓝球购买流程测试'''
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_red_label6()  # 选取6个红球
        ulcn.u_bule_label16()  # 选取16个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login(self.driver)#####用户登录######
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_Hand_r19_case(self):
        '''双色球选取19个红球，第19个红球提示“红球不能超过18个”测试'''
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_red_label19()  # 选取19个红球
        text = ulcn.out_of_num()#获取超过18个红球时的toast提示信息
        self.assertIn("红球不能超过18个",text)
        ulcn.u_bule_label1()#选取1个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login(self.driver)  #####用户登录######
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_Hand_r18b16_case(self):
        '''双色球选取18个红球，16个蓝球提示“投注金额不能大于100000元”测试'''
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_red_label18()  # 选取18个红球
        ulcn.u_bule_label16()#选取16个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login(self.driver)  #####用户登录######
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()#点击确认并支付按钮
        text = cl.out_max_pay()#获取超额提示信息文本
        self.assertIn("投注金额不能大于100000元",text)
        cl.re_selection_num()#点击重新选号链接
        ulcn.u_bule_label16()#取消选中的16个蓝球
        ulcn.u_bule_label1()#选取1个蓝球
        ulcn.Confirm_button()#点击确认选号
        cl.submit_order_to_station_owner_button()#提交订单给站主
        cl.confirm_and_pay_button()#确认支付
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_Hand_re_r18b1_case(self):
        '''重复选号取消选中测试'''
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_rechoose_red_label18()#随机选中18个红球，再取消选中的红球
        ulcn.u_red_label18()#重新选取18个红球
        ulcn.u_bule_label1()#选取1个蓝球
        ulcn.Confirm_button()#点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()  # 提交订单给站主
        l = Login(self.driver)  #####用户登录######
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击确认并支付按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 关闭悬浮窗口
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
    def test_UnionLotto_CheckOrderDetails_case(self):
        '''查看订单详情页测试'''
        ###点击进入双色球选号页面###
        hp = HomePage(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()  # 点击双色球链接
        # 选号
        ulcn = UnionLottoChooseNumber(self.driver)
        ulcn.u_red_label6()  # 任意选择6个红球
        ulcn.u_bule_label1()  # 任意选择1个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        #####用户登录######
        l = Login(self.driver)
        l.login()
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        '''断言验证提交订单成功'''
        sos = SubmitOrderSuccess(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        text = sos.submit_order_success()
        self.assertEqual("订单提交成功", text, "提交订单失败")
        sos.check_order_details()#点击“查看订单详情”
        od = OrderDetails(self.driver)
        od.order_status()#获取订单状态
        od.number_bet()#获取投注号码
        od.official_open_time()#获取开奖时间
        od.order_number()#获取订单编号

    def test_UnionLotto_unitary_many_note(self):
        """单式，多注一倍"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.continue_choose_num_button()##继续选号
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('2', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_after_many_note(self):
        """复式，多注一倍"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label18()  # 任意选择18个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('18564', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_after_many_note_many_multiple(self):
        """复式，多注多倍"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label18()  # 任意选择18个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.throw_times_input(13)
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('18564', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('13', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_User_agreement(self):
        """验证用户协议"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.User_agreement()##点击用户协议
        hc.User_know()##点击用户协议我知道了
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_risk(self):
        """验证购彩风险"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.Risk()##点击用户协议
        hc.Risk_know()##点击用户协议我知道了
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_Continue_buy(self):
        """验证继续投注该彩种"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        hf = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        ha.Moveable_float_close()
        hd.Continue_buy()##点击继续购买该彩种
        mur1 = hc1.Play_fb()
        self.assertEqual('玩\n法', mur1)
        hb.machine_choose_button()  # 点击机选
        hb.machine_choose_one_button()  # 机选一注
        hb.Confirm_button()  # 确认选号
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        text1 = hf.submit_order_success()  # 获取提交订单成功文本
        self.assertEqual('订单提交成功', text1)

    def test_UnionLotto_Order_details(self):
        """验证订单详情页面"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        he=OrderDetails(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        mur2=hc.Select_number()##读取投注号码
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        ha.Moveable_float_close()
        hd.check_order_details()  ##点击查看订单详情
        mur1 = he.Betting_nu()  ##读取显示的投注号码
        self.assertEqual(mur2, mur1)
        #mur3=he.Pay_case()
        #self.assertEqual('资金已冻结',mur3)
        mur4=he.order_status()
        self.assertEqual('待出票',mur4)

    def test_UnionLotto_Continue_buy_scheme(self):
        """验证继续购买该方案"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        he=OrderDetails(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.Select_number()
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        ha.Moveable_float_close()
        hd.check_order_details()  ##点击查看订单详情
        mur4 = he.order_status()
        self.assertEqual('待出票', mur4)
        he.Scheme()#点击继续购买该方案
        mur2= hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur2)

    def test_UnionLotto_many_pause(self):
        """多期机选"""
        ha = HomePage(self.driver)
        hb = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        he = OrderDetails(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  ##点击我的彩票
        hl.login()  ##登录
        ha.Home_page()  ##点击首页
        ha.UnionLotto_link()  # 点击双色球链接
        hb.There_clock()  ##点击右上角。。。
        hb.Many_pause()#点击多期机选
        hb.Many_pause_nu()##点击期号
        hb.Many_pause_confirm()  ##点击提交
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_UnionLotto_history_recommend(self):
        """历史走势，手动选择6红1篮"""
        ha = HomePage(self.driver)
        hb = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd=SubmitOrderSuccess(self.driver)
        he=OrderDetails(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.There_clock()##点击右上角。。。
        hb.History_movements()##点击历史走势
        hb.Red_movements()##点击红球走势
        hb.History_red(6)##点击6个数字
        hb.Bule_movements()#点击蓝球走势
        hb.History_bule(2)###点击1个蓝球
        hb.Recommended_number()###点击使用已选号码
        hb.Confirm_button()  # 确认选号
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_history_recommend_many(self):
        """历史走势，手动选择，复式"""
        ha = HomePage(self.driver)
        hb = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd=SubmitOrderSuccess(self.driver)
        he=OrderDetails(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.There_clock()##点击右上角。。。
        hb.History_movements()##点击历史走势
        hb.Red_movements()##点击红球走势
        hb.History_red(7)##点击7个数字
        hb.Bule_movements()#点击蓝球走势
        hb.History_bule(2)###点击1个蓝球
        hb.Recommended_number()###点击使用已选号码
        hb.Confirm_button()  # 确认选号
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('7', mur)  ##断言
        nu = hc.throw_time_text()  ###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_unitary_many_note_del_X(self):
        """左边X按钮，能够删除所选号码"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        hd=PaintBallConfirm(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.continue_choose_num_button()##继续选号
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.Del_x()##点击左侧X按钮
        mur = hc.lottery_number_text()  # 读取注数
        self.assertEqual('1', mur)  ##断言
        nu = hc.throw_time_text()###倍数
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()

    def test_UnionLotto_unitary_del_X(self):
        """左边X按钮，能够删除所选号码"""
        ha = HomePage(self.driver)
        hb=UnionLottoChooseNumber(self.driver)
        hc=ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hd=PaintBallConfirm(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.Del_x()##点击左侧X按钮
        mur1 = hc1.Play_fb()
        self.assertEqual('玩\n法', mur1)

    def test_Direct_add_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage(self.driver)
        hb = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hd = PaintBallConfirm(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_Direct_add_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage(self.driver)
        hb = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hd = PaintBallConfirm(self.driver)
        hd1 = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hd1.Clear()
        self.assertEqual('清空',mur)

    def test_Direct_add_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage(self.driver)
        hb = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallChooseNumber(self.driver)
        hd = PaintBallConfirm(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur=hc1.Play_fb()
        self.assertEqual('玩\n法',mur)



