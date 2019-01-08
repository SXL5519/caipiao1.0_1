from element_operate.JXKS.JXKS_choosenumber import GXKS_ChooseNumber_lelun
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lelun
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_lelun
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_lelun
from element_operate.JXKS.JXKS_confirm import JXKS_Confirm_lelun
from element_operate.less_pay_sucess import LessPaySucess_lelun
from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery_lelun
from time import sleep
class gxks_and_value_case(MyTest):
    """广西快三和值玩法"""
    def test_gxks_play_case(self):
        """验证玩法"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.All_play(7)##遍历所有的玩法
        mur=hb.All_play(1)##随机选择1个玩法
        mur1=hb.mode_choose_button_text()
        self.assertEqual(mur,mur1)

    def test_gxks_history_case(self):
        """历史走势"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1=UnionLottoChooseNumber_lelun(self.driver)
        hc1 = PaintBallChooseNumber_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb1.There_clock()##点击。。。
        hb.History_movements()##点击历史走势
        mur=hb.Date_nu()##读取最后一条数据
        if mur=='':
            self.assertEqual('a',mur)
        else:
            print('数据显示正常')
        hb.Ret()##点击返回按钮
        mur1 = hc1.Play_fb()
        self.assertEqual('玩\n法', mur1)

    def test_gxks_a_note_case(self):
        """1注1倍号码"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期1倍共2元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_gxks_a_note_many_double_case(self):
        """1注多倍号码"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期13倍共26元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_case(self):
        """多注1倍号码"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击5注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('5注1期1倍共10元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_case(self):
        """多注多倍号码"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('5注1期13倍共130元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_Continue_case(self):
        """继续选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_many_double_Continue_case(self):
        """1注多倍,继续选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc.Button_less()###点击倍数-号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期12倍共48元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_Continue_case(self):
        """多注1倍,继续选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('6注1期1倍共12元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_Continue_case(self):
        """多注多倍,继续选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Button_add()  #点击倍数+号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('6注1期2倍共24元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_pause_case(self):
        """1注1倍,机选"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_gxks_a_note_many_double_pause_case(self):
        """1注多倍号码,机选"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_pause_case(self):
        """多注1倍号码,机选"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('6注1期1倍共12元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_pause_case(self):
        """多注多倍号码,机选"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('6注1期13倍共156元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_znzh_case(self):
        """1注1倍,智能选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期1倍共2元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_gxks_a_note_many_double_znzh_case(self):
        """1注多倍号码,智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期13倍共26元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_znzh_case(self):
        """多注1倍号码,智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn('84', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_znzh_case(self):
        """多注多倍号码,智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击2注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_Continue_znzh_case(self):
        """继续选号,智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(12)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn('12', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_many_double_Continue_znzh_case(self):
        """1注多倍,继续选号，智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc.Button_less()###点击倍数-号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期12倍共48元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(12)  # 追号的输入框输入12
        ssc_cl.revise_cancel()  # 点击取消修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_Continue_znzh_case(self):
        """多注1倍,继续选号,智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击2注
        hb1.confirm_number_button()###点击确认选号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('3注1期1倍共6元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_input(3)  # 起始倍数的输入框输入3
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text, '倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_Continue_znzh_case(self):
        """多注多倍,继续选号，智能追号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Button_add()  #点击倍数+号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('3注1期2倍共12元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_add()  # 点击起始倍数的+
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text, '倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_znzh_tj_case(self):
        """1注1倍,智能选号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期1倍共2元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_gxks_a_note_many_double_znzh_yj_case(self):
        """1注多倍号码,智能追号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期13倍共26元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_znzh_tj_case(self):
        """多注1倍号码,智能追号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击5注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_znzh_tj_case(self):
        """多注多倍号码,智能追号，提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_Continue_znzh_tj_case(self):
        """继续选号,智能追号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_many_double_Continue_znzh_tj_case(self):
        """1注多倍,继续选号，智能追号，提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc.Button_less()###点击倍数-号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期12倍共48元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_a_double_Continue_znzh_tj_case(self):
        """多注1倍,继续选号,智能追号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击2注
        hb1.confirm_number_button()###点击确认选号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('3注1期1倍共6元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_many_note_many_double_Continue_znzh_tj_case(self):
        """多注多倍,继续选号，智能追号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = JXKS_Confirm_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hc2 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc.Button_add()  #点击倍数+号
        hc.Cont()###点击继续选号
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('3注1期2倍共12元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_gxks_a_note_pause_znxh_tj_case(self):
        """1注1倍,机选,智能选号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_jxks_a_note_many_double_pause_znxh_tj_case(self):
        """1注多倍号码,机选,智能选号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_a_double_pause_znxh_tj_case(self):
        """多注1倍号码,机选,智能选号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('6注1期1倍共12元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_pause_znxh_tj_case(self):
        """多注多倍号码,机选,智能选号,提交"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(5)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('6注1期13倍共156元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_pause_znxh_case(self):
        """1注1倍,机选,智能选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期1倍共4元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_jxks_a_note_many_double_pause_znxh_case(self):
        """1注多倍号码,机选,智能选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_a_double_pause_znxh_case(self):
        """多注1倍号码,机选,智能选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击2注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('3注1期1倍共6元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_pause_znxh_case(self):
        """多注多倍号码,机选,智能选号"""
        ha = HomePage_lelun(self.driver)
        hb=GXKS_ChooseNumber_lelun(self.driver)
        hb1 = ElevenFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ssc_cl = CQSSCConfirmLottery_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()#点击广西快三
        hb.play_jxks_add()##点击和值
        hb.Add_choosenumber(2)##点击5注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('3注1期13倍共78元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lelun()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)