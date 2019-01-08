from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.baofoo_payment import BaofooPayment_lexiu
from element_operate.choose_bank import ChooseBank_lexiu
from element_operate.confirm_pay import ConfirmPay_lexiu
from element_operate.homepage import HomePage_lexiu
from element_operate.less_pay_sucess import LessPaySucess_lexiu
from element_operate.login import Login_lexiu
from element_operate.my_ticket import MyTicket_lexiu
from element_operate.payment_mode import PaymetMode_lexiu
from test_case.Base.mytest import MyTest
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lexiu
from time import sleep
from element_operate.UnionLotto.order_details import OrderDetails_lexiu
from selenium.webdriver.common.action_chains import ActionChains


class LessPayment_case(MyTest):
    """=单线场景"""
    def test_less_payment_shortfall_case(self):
        '''验证差额支付流程'''
        ###点击进入双色球选号页面###
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l=Login_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.UnionLotto_link()#点击双色球链接
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ulcn.u_red_label6()  # 任意选择6个红球
        ulcn.u_bule_label1()  # 任意选择1个蓝球
        ulcn.Confirm_button()  # 点击确认选号按钮
        cl = ConfirmLottery_lexiu(self.driver)
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        l.login_nomoney_lexiu()#点击登录
        cl.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        cl.confirm_and_pay_button()  # 点击“确认并支付”按钮
        pm = PaymetMode_lexiu(self.driver)
        mur = pm.Top_up()  ##获取充值成功文本
        self.assertEqual('充值', mur)

    def test_recharge_case(self):
        """验证充值流程"""
        hp = HomePage_lexiu(self.driver)
        hb=MyTicket_lexiu(self.driver)
        hc=PaymetMode_lexiu(self.driver)
        hd=BaofooPayment_lexiu(self.driver)
        he=ChooseBank_lexiu(self.driver)
        hf=ConfirmPay_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()##点击我的彩票
        hl.login_lexiu()##登录
        hb.Recharge()#点击充值
        hb.Recharge_Money()##点击充值数字按钮
        hb.Next()##点击下一步
        mur = hc.Top_up()  ##获取充值成功文本
        self.assertEqual('充值', mur)

    def test_recharge_input_case(self):
        """验证手动输入金额充值流程"""
        hp = HomePage_lexiu(self.driver)
        hb = MyTicket_lexiu(self.driver)
        hc = PaymetMode_lexiu(self.driver)
        hd = BaofooPayment_lexiu(self.driver)
        he = ChooseBank_lexiu(self.driver)
        hf = ConfirmPay_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  ##点击我的彩票
        hl.login_lexiu()  ##登录
        hb.Recharge()  # 点击充值
        hb.Recharge_input(888)###输入888
        hb.Next()  ##点击下一步
        mur = hc.Top_up()  ##获取充值成功文本
        self.assertEqual('充值', mur)

    def test_Login_case(self):
        """验证登录流程"""
        hp = HomePage_lexiu(self.driver)
        hb = MyTicket_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  ##点击我的彩票
        hl.login_lexiu()  ##登录
        mur = hb.Account()
        self.assertEqual("17602882784", mur)

    def test_after_shortfall_case(self):
        '''验证差额支付,复式号码流程'''
        ###点击进入双色球选号页面###
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc= ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = ConfirmPay_lexiu(self.driver)
        hf2= LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()#点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1_too()  # 任意选择2个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hl.login_nomoney_lexiu()#点击登录
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hc.confirm_and_pay_button()  # 点击“确认并支付”按钮
        mur=hd.Top_up()##获取充值成功文本
        self.assertEqual('充值',mur)

    """def test_one_note_pause_one_shortfall_case(self):
        '''手选一注，确认页机选1注，差额支付流程'''
        ###点击进入双色球选号页面###
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc= ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = ConfirmPay_lexiu(self.driver)
        hf2= LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()#点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.machine_choose_one_button()#点击机选一注
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hl.login_nomoney_lexiu()#点击登录
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hc.confirm_and_pay_button()  # 点击“确认并支付”按钮
        mur = hd.Top_up()  ##获取充值成功文本
        self.assertEqual('充值', mur)"""

    def test_one_note_five_double_ten_period_shortfall_case(self):
        '''手选一注，1注单式号码，修改倍数5，修改期数10，差额支付流程'''
        ###点击进入双色球选号页面###
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc= ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = ConfirmPay_lexiu(self.driver)
        hf2= LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()#点击双色球链接
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.chase_ticket_input("10")#输入追10期
        hc.throw_times_input("5")#输入投注倍数为5倍
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hl.login_nomoney_lexiu()#点击登录
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hc.confirm_and_pay_button()  # 点击“确认并支付”按钮
        mur = hd.Top_up()  ##获取充值成功文本
        self.assertEqual('充值', mur)

    def test_after_Continue_buy(self):
        """打开追号订单详情，点击继续购买该方案"""
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd=MyTicket_lexiu(self.driver)
        he = OrderDetails_lexiu(self.driver)
        hf = SubmitOrderSuccess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login_lexiu()  # 点击登录
        hd.After_nu()##点击追号订单
        hd.After_nu_record()###点击追号记录的订单
        he.Scheme()#点击继续购买该方案
        mur = hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主', mur)
        hc.submit_order_to_station_owner_button()  # 点击提交订单给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        text1 = hf.submit_order_success()  # 获取提交订单成功文本
        self.assertEqual('订单提交成功', text1)

    def test_unionlotto_dantuo_continue_case(self):
        """胆拖选号页面，选择1注号码，在投注确认页面，继续选1注"""
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = ConfirmPay_lexiu(self.driver)
        hf2 = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.UnionLotto_link()  # 点击双色球链接
        hb.DanTuo_mode()  # 选择胆拖模式
        hb.u_red_five_two()  # 红球选取5个胆码2个拖码
        hb.u_bule_one()  # 选取一个蓝球
        hb.Confirm_button()  # 确认选号
        hc.continue_choose_num_button()  ##继续选号
        hb.u_red_five_two()  # 红球选取5个胆码2个拖码
        hb.u_bule_one()  # 选取一个蓝球
        hb.Confirm_button()  # 确认选号
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hl.login_nomoney_lexiu()  # 点击登录
        hc.submit_order_to_station_owner_button()  # 点击“提交订单给站主”按钮
        hc.confirm_and_pay_button()  # 点击“确认并支付”按钮
        mur = hd.Top_up()  ##获取充值成功文本
        self.assertEqual('充值', mur)

    def test_Lottery_information_buy_case(self):
        """进入开奖公告,点击投注双色球，进入双色球投注页面，选1注号码"""
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = SubmitOrderSuccess_lexiu(self.driver)
        hf2 = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.Lottery_information()##点击开奖信息
        hb.Lottery_information_unionlotto()##点击开奖信息中的双色球
        hc.Unionlotto_History_buy()###点击双色球最近的开奖信息
        hc.Buy_unionlotto()##点击投注双色球
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        text1 = hf1.submit_order_success()  # 获取提交订单成功文本
        self.assertEqual('订单提交成功', text1)

    '''def test_Lottery_information_buy_pause_one_case(self):
        """进入开奖公告，打开双色球开奖详情，点击投注双色球，进入双色球投注页面，选1注号码，在投注确认页，机选1注"""
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = SubmitOrderSuccess_lexiu(self.driver)
        hf2 = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.Lottery_information()##点击开奖信息
        hb.Lottery_information_unionlotto()##点击开奖信息中的双色球
        hc.Unionlotto_History_buy()###点击双色球最近的开奖信息
        hc.Buy_unionlotto()##点击投注双色球
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.machine_choose_one_button()##点击机选1注
        lottery_number_text = hc.lottery_number_text()  # 获取投注注数文本
        self.assertIn("2", lottery_number_text)  # 检查投注注数为1注
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        text1 = hf1.submit_order_success()  # 获取提交订单成功文本
        self.assertEqual('订单提交成功', text1)'''

    def test_Lottery_information_buy_pause_five_case(self):
        """进入开奖公告，打开双色球开奖详情，点击投注双色球，进入双色球投注页面，选1注号码，在投注确认页，机选5注，修改倍数，期数"""
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = SubmitOrderSuccess_lexiu(self.driver)
        hf2 = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.Lottery_information()##点击开奖信息
        hb.Lottery_information_unionlotto()##点击开奖信息中的双色球
        hc.Unionlotto_History_buy()###点击双色球最近的开奖信息
        hc.Buy_unionlotto()##点击投注双色球
        hb.u_red_label6()  # 任意选择6个红球
        hb.u_bule_label1()  # 任意选择1个蓝球
        hb.Confirm_button()  # 点击确认选号按钮
        hc.machine_choose_five_button()##点击机选5注
        hc.chase_ticket_input("4")  # 输入追4期
        hc.throw_times_input("3")#输入投注倍数为3倍
        lottery_number_text = hc.lottery_number_text()  # 获取投注注数文本
        self.assertIn("6", lottery_number_text)  # 检查投注注数为1注
        chase_time_text = hc.chase_time_text()  # 获取追号期数
        self.assertIn("4", chase_time_text)  # 检查追号期数为4期
        throw_times = hc.throw_time_text()  # 获取投注倍数定位
        self.assertIn("3", throw_times)  # 检查投注倍数为3倍
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        text1 = hf1.submit_order_success()  # 获取提交订单成功文本
        self.assertEqual('订单提交成功', text1)

    '''def test_aaa(self):
        """幸运选号"""
        ha = HomePage_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hb = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = PaymetMode_lexiu(self.driver)
        he = BaofooPayment_lexiu(self.driver)
        hf = ChooseBank_lexiu(self.driver)
        hf1 = SubmitOrderSuccess_lexiu(self.driver)
        hf2 = LessPaySucess_lexiu(self.driver)
        action = ActionChains(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.Activity_zone()###点击幸运选号
        hb.Lucky_number()##点击幸运选号
        hc.Choose_color()#点击选择彩种
        hc.Lucky_unionlotto(action)
        hc.Complete()##点击完成
        hc.Choose_note()#点击选择注数
        sleep(5)
        hc.Complete()##点击完成'''

