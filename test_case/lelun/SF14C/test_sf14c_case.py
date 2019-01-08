from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from test_case.Base.mytest import MyTest
from  element_operate.RX9C.rx9c_choosenumber import RX9C_choosenumber_lelun
from time import sleep
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from  element_operate.RX9C.rx9c_confirmlottery import RX9C_ConfirmLottery_lelun
from element_operate.less_pay_sucess import LessPaySucess_lelun
from element_operate.Seven_color.Seven_color_choosenumber import Seven_color_choosenumber
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lelun
from element_operate.Arrange_there.Arrang_there_choosenumber import Arrang_there_choosenumber_lelun
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_lelun
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm_lelun
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lelun
class SF14C_case(MyTest):
    """胜负14场"""
    def test_choosenumber_case(self):
        """验证选号页赛事结果功能"""
        ha = HomePage_lelun(self.driver)
        hb=RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1=ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd=LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nu()###点击展示的全部赛事结果
        if a==1:
            hb.Games_nu()  ###取消展示的全部赛事结果
            hb.Games_nus(14,1)  ###点击14场展示的赛事结果
            hb.Confirm_pick()###点击确认选号
            hc.Submit_station()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_clear_case(self):
        """验证清楚按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Clear()###点击清除按钮
            hb.Games_nus(14,1)  ###点击9展示的赛事结果
            hb.Confirm_pick()###点击确认选号
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_Play_instruction_case(self):
        """验证玩法说明"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hb1=Arrang_there_choosenumber_lelun(self.driver)
        hb2 = There_D_choosenumber_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        hb2.Instruct()##点击右上角...
        hb1.Arrang_there_instruct()##点击玩法说明
        mur = hb.Rx9c_play()
        self.assertEqual('任选14场', mur)
        hb1.Arrany_there_know()

    def test_rx9c_term_case(self):
        """验证期数转换"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        hb.Term()#点击期数
        mur=hb.Term_next()##点击下一期，并读取文本
        if mur!=0:
            mur1=hb.Term_t()#读取显示的文本
            self.assertIn(mur1,mur)

    def test_nine_one_times_case(self):
        """9场对阵，默认倍数1倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('1', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_Continue_case(self):
        """添加/编辑赛事,默认倍数1倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hb.Cont_choose()##点击继续选号
            hb.Games_nus(14,1)  ###点击9展示的赛事结果
            hb.Confirm_pick()  ###点击确认选号
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('1', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('2', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_nine_too_times_case(self):
        """9场对阵,倍数2倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hc.Times_add()##点击倍数+
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('2', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_input_times_case(self):
        """输入10倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hc1.throw_times_input(10)  ##输入倍数99
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('10', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_times_less_case(self):
        """倍数-"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hc1.throw_times_input(10)  ##输入倍数10
            hc.Times_less()###点击倍数-
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('9', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_Continue_99_times_case(self):
        """添加/编辑赛事,倍数99倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hb.Cont_choose()##点击继续选号
            hb.Games_nus(14,1)  ###点击9展示的赛事结果
            hb.Confirm_pick()  ###点击确认选号
            hc1.throw_times_input(99)  ##输入倍数99
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('99', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('2', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_99_times_case(self):
        """选择9场,倍数99倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hc1.throw_times_input(99)  ##输入倍数99
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('99', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_14_games_case(self):
        """选择14场"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('1', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_9_games_all_case(self):
        """选择9场对阵的胜、平、负，默认倍数1倍"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14,2)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('1', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('16384', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_del_X_case(self):
        """多注号码，点击左边X按钮"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14, 1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hb.Cont_choose()##点击继续选号
            hb.Games_nus(14, 1)  ###点击9展示的赛事结果
            hb.Confirm_pick()  ###点击确认选号
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('2', mur2)
            hc.Del_x()##随机点击1个X按钮
            mur = hc1.throw_time_text()  ##读取倍数
            self.assertEqual('1', mur)
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_a_note_del_X_case(self):
        """单注号码，点击左边X按钮"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = RX9C_ConfirmLottery_lelun(self.driver)
        hc1 = ConfirmLottery_lelun(self.driver)
        hc2 = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hd = LessPaySucess_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14, 1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Del_x()  ##随机点击1个X按钮
            hb.Games_nus(14, 1)  ###点击9展示的赛事结果
            hb.Confirm_pick()  ###点击确认选号
            mur2 = hc1.lottery_number_text()  ##读取注数
            self.assertEqual('1', mur2)
            hc.Submit_station()  ####点击提交给站主
            hl.login_lelun()  # 输入账号，密码
            hc.Submit_station()  # 点击提交给站主
            hc1.confirm_and_pay_button()  # 点击确认支付()
            mur1 = hd.assect_pay()  ##读取支付状态文本
            self.assertEqual('订单提交成功', mur1)

    def test_seven_color_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号，点击确定"""
        ha = HomePage_lelun(self.driver)
        hb = RX9C_choosenumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hc2 = PaintBallChooseNumber_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.victory_defeat_14_link()  # 点击胜负14场
        a=hb.Games_nus(14, 1)  ###点击9展示的赛事结果
        if a==1:
            hb.Confirm_pick()  ###点击确认选号
            hc1.Pf_del_icon()  ###点击清除所有选号
            mur = hc2.Play_fb()
            self.assertEqual('期\n号', mur)