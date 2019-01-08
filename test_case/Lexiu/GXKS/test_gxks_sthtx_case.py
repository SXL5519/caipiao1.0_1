from element_operate.JXKS.JXKS_choosenumber import GXKS_ChooseNumber_lexiu
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.homepage import HomePage_lexiu
from element_operate.login import Login_lexiu
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_lexiu
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_lexiu
from element_operate.JXKS.JXKS_confirm import JXKS_Confirm_lexiu
from element_operate.less_pay_sucess import LessPaySucess_lexiu
from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery_lexiu
class gxks_shtx_case(MyTest):
    """三同号通选"""

    def test_jxks_a_note_many_double_case(self):
        """1注多倍号码"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期13倍共26元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)


    def test_jxks_a_note_many_double_Continue_case(self):
        """1注多倍,继续选号"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = JXKS_Confirm_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hc2 = ConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc.Button_less()###点击倍数-号
        hc.Cont()###点击继续选号
        hb.sthtx_choosenumber()##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期12倍共48元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_pause_case(self):
        """1注多倍号码,机选"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_znzh_case(self):
        """1注多倍号码,智能追号"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期13倍共26元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn('84', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_Continue_znzh_case(self):
        """1注多倍,继续选号，智能追号"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = JXKS_Confirm_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hc2 = ConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc.Button_less()###点击倍数-号
        hc.Cont()###点击继续选号
        hb.sthtx_choosenumber()##点击1注
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
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_znzh_yj_case(self):
        """1注多倍号码,智能追号,提交"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期13倍共26元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_Continue_znzh_tj_case(self):
        """1注多倍,继续选号，智能追号，提交"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = JXKS_Confirm_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hc2 = ConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc.Button_less()###点击倍数-号
        hc.Cont()###点击继续选号
        hb.sthtx_choosenumber()##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期12倍共48元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_pause_znxh_tj_case(self):
        """1注多倍号码,机选,智能选号,提交"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('2注1期13倍共52元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_many_double_pause_znxh_case(self):
        """1注多倍号码,机选,智能选号"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
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
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_X_case(self):
        """1注号码，点击左边X按钮"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()###点击确认选号
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注1期1倍共2元', mur)
        hc.n_event_count()  ##点击1场赛事的X按钮
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()  ###点击确认选号
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注1期1倍共2元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_too_term_case(self):
        """1注号码，2期按钮"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()  ###点击确认选号
        hc1.chase_ticket_button()###展开期数按钮
        hc.chase_ticket_button_two()##点击2期
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注2期1倍共4元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_add_term_case(self):
        """1注号码，点击+按钮，添加期数"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()  ###点击确认选号
        hc1.chase_add_button()###点击+按钮，期数
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注2期1倍共4元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_less_term_case(self):
        """1注号码，点击-按钮，添加期数"""
        ha = HomePage_lexiu(self.driver)
        hb = GXKS_ChooseNumber_lexiu(self.driver)
        hb1 = ElevenFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = EleChooseFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ssc_cl = CQSSCConfirmLottery_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_sthtx()  ##点击三同号通选
        hb.sthtx_choosenumber()  ##点击选号
        hb1.confirm_number_button()  ###点击确认选号
        hc1.chase_ticket_button()  ###展开期数按钮
        hc.chase_ticket_button_twenty()  ##点击20期
        hc1.chase_sub_button()  ###点击-按钮，期数
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注19期1倍共38元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)