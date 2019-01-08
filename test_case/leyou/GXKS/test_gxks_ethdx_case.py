from element_operate.JXKS.JXKS_choosenumber import GXKS_ChooseNumber_leyou
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.homepage import HomePage_leyou
from element_operate.login import Login_leyou
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_leyou
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_leyou
from element_operate.JXKS.JXKS_confirm import JXKS_Confirm_leyou
from element_operate.less_pay_sucess import LessPaySucess_leyou
from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery_leyou
from time import sleep
class jxks_ethdx_case(MyTest):
    """二同号单选"""
    def test_jxks_choose_all_case(self):
        """验证选号页，选号功能"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()##点击二同号单选
        hb.Ethdx_all()##点击所有选号
        hb.Ethdx(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('1注1期1倍共2元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1=hd.assect_pay()##读取支付状态文本
        self.assertEqual('订单提交成功',mur1)

    def test_jxks_many_note_many_double_case(self):
        """多注多倍号码"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('9注1期13倍共234元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_Continue_case(self):
        """多注多倍,继续选号"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = JXKS_Confirm_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hc2 = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc.Button_add()  #点击倍数+号
        hc.Cont()###点击继续选号
        hb.Ethdx(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('10注1期2倍共40元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_pause_case(self):
        """多注多倍号码,机选"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('10注1期13倍共260元',mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_znzh_case(self):
        """多注多倍号码,智能追号"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('9注1期13倍共234元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_Continue_znzh_case(self):
        """多注多倍,继续选号，智能追号"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = JXKS_Confirm_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hc2 = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc.Button_add()  #点击倍数+号
        hc.Cont()###点击继续选号
        hb.Ethdx(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('10注1期2倍共40元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_add()  # 点击起始倍数的+
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text, '倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_znzh_tj_case(self):
        """多注多倍号码,智能追号，提交"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('9注1期13倍共234元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_Continue_znzh_tj_case(self):
        """多注多倍,继续选号，智能追号,提交"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = JXKS_Confirm_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hc2 = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc.Button_add()  #点击倍数+号
        hc.Cont()###点击继续选号
        hb.Ethdx(1)##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('10注1期2倍共40元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc2.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_pause_znxh_tj_case(self):
        """多注多倍号码,机选,智能选号,提交"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('10注1期13倍共260元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_many_double_pause_znxh_case(self):
        """多注多倍号码,机选,智能选号"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(3)  ##点击3注
        hb1.confirm_number_button()###点击确认选号
        hc1.throw_times_input(13)  ##输入倍数13倍
        hc1.machine_choose_one()##点击机选
        mur=hc1.lottery_chase_throw_text()#读取注数
        self.assertEqual('10注1期13倍共260元',mur)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(84)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertNotIn('10期', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_many_note_X_case(self):
        """多注号码，点击左边X按钮"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(1)  ##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.machine_choose_one()##点击机选
        hc1.machine_choose_one()  ##点击机选
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('3注1期1倍共6元', mur)
        hc.n_event_count()  ##点击第1场赛事的X按钮
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('2注1期1倍共4元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_a_note_X_case(self):
        """1注号码，点击左边X按钮"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(1)  ##点击1注
        hb1.confirm_number_button()###点击确认选号
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注1期1倍共2元', mur)
        hc.n_event_count()  ##点击1场赛事的X按钮
        hb.Ethdx(1)  ##点击1注
        hb1.confirm_number_button()  ###点击确认选号
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注1期1倍共2元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_too_term_case(self):
        """1注号码，2期按钮"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(1)  ##点击1注
        hb1.confirm_number_button()  ###点击确认选号
        hc1.chase_ticket_button()###展开期数按钮
        hc.chase_ticket_button_two()##点击2期
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注2期1倍共4元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_add_term_case(self):
        """1注号码，点击+按钮，添加期数"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(1)  ##点击1注
        hb1.confirm_number_button()###点击确认选号
        hc1.chase_add_button()###点击+按钮，期数
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注2期1倍共4元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_jxks_less_term_case(self):
        """1注号码，点击-按钮，添加期数"""
        ha = HomePage_leyou(self.driver)
        hb = GXKS_ChooseNumber_leyou(self.driver)
        hb1 = ElevenFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = EleChooseFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.guangxi_express_three_link()  # 点击广西快三
        hb.play_jxks_ethdx()  ##点击二同号单选
        hb.Ethdx(1)  ##点击1注
        hb1.confirm_number_button()  ###点击确认选号
        hc1.chase_ticket_button()  ###展开期数按钮
        hc.chase_ticket_button_twenty()  ##点击20期
        hc1.chase_sub_button()  ###点击-按钮，期数
        mur = hc1.lottery_chase_throw_text()  # 读取注数
        self.assertEqual('1注19期1倍共38元', mur)
        hc1.submit_order_button()  # 点击提交给站主
        hl.login_leyou()  # 输入账号，密码
        hc1.submit_order_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)