from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber_lexiu
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_lexiu
from element_operate.Arrange_there.Arrang_there_choosenumber import Arrang_there_choosenumber_lexiu
from  element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.homepage import HomePage_lexiu
from element_operate.login import Login_lexiu
from test_case.Base.mytest import MyTest
from element_operate.Seven_color.Seven_color_choosenumber import Seven_color_choosenumber_lexiu
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lexiu
from element_operate.less_pay_sucess import LessPaySucess_lexiu
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lexiu
from time import sleep

class Arrang_there_group_there(MyTest):
    """排列三，组三"""
    def test_group_there_all_choosenumber_case(self):
        """验证选号页面数字球功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_there()
        hb.group_there()
        hb.group_theres(4)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('12', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Screening_ji_case(self):
        """验证选号页面筛选 奇按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(0)  ###点击筛选中 奇 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('20', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Screening_ou_case(self):
        """验证选号页面筛选 偶 按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(1)  ###点击筛选中 偶 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('20', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Screening_da_case(self):
        """验证选号页面筛选 大 按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(2)  ###点击筛选中 大 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('20', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Screening_xi_case(self):
        """验证选号页面筛选 小 按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(2)  ###点击筛选中 小 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('20', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Screening_qu_case(self):
        """验证选号页面筛选 全 按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(4)  ###点击筛选中 全 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('90', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Screening_qing_case(self):
        """验证选号页面筛选 清 按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(5)  ###点击筛选中 清 按钮
        hb.group_theres(2)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_Group_delet_case(self):
        """验证选号页面组合显示X 按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Screening(4)  ###点击筛选中 全 按钮
        hb.Group_delet()
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('89', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_pause_one_case(self):
        """验证选号页面，点击机选一注功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_one_button()  ##点击机选一注
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_pause_five_case(self):
        """验证选号页面，点击机选五注功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_five_button()  ##点击机选五注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_pause_ten_case(self):
        """验证选号页面，点击机选10注功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_click_too_confirm_case(self):
        """验证选号页面，点击2次确认选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_there_clear_number_case(self):
        """验证选号页面，点击清除选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(4)
        hb2.clear_number()  # 点击清除选号页面
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付


    def test_many_note_many_double_case(self):
        """多注多倍"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur2 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur2)

    def test_many_note_many_double_Continue_case(self):
        """多注多倍,继续选号"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur3 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('4', mur3)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur4 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur4)

    def test_many_note_many_double_Continue_after_case(self):
        """多注多倍,继续选号,复式"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur3= hc1.Test_note_nu()  ##读取注数
        self.assertEqual('4', mur3)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur4= hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur4)

    '''def test_many_note_many_double_pause_one_case(self):
        """多注多倍,机选一注"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_one()  ###点击机选一注
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur3 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('3', mur3)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur4= hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur4)'''

    def test_many_note_many_double_pause_five_case(self):
        """多注多倍,机选五注"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_five()  ###点击机选五注
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur3 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('7', mur3)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur4 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur4)

    '''def test_many_note_many_double_pause_period_one_case(self):
        """多注多倍,机选一注,追期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_one()  ###点击机选一注
        hc.chase_ticket_input(3)  ##输入追期
        nu = hc1.Test_period_show()
        self.assertEqual('3', nu)
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur3 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('3', mur3)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur4 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur4)'''


    def test_many_note_many_double_pause_five_period_case(self):
        """多注多倍,机选五注,追期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(2)
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_five()  ###点击机选五注
        hc.chase_ticket_input(3)  ##输入追期
        nu = hc1.Test_period_show()
        self.assertEqual('3', nu)
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur3 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('7', mur3)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur4 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur4)

    def test_seven_color_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_six()  ####点击组六
        hb.group_sixs(3)
        hb2.Confirm_nu()  # 点击确认选号
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_seven_color_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = There_D_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_six()  ####点击组六
        hb.group_sixs(3)
        hb2.Confirm_nu()  # 点击确认选号
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hb1.Clear()
        self.assertEqual('清空',mur)

    def test_seven_color_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号，点击确定"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = PaintBallChooseNumber_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_six()  ####点击组六
        hb.group_sixs(3)
        hb2.Confirm_nu()  # 点击确认选号
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur = hc1.Play_fb()
        self.assertEqual('玩\n法', mur)

    def test_arrany_there_Continue_switch_play_case(self):
        """,组三，继续选号，切换玩法为直选"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Group_six()  ####点击组六
        hb.group_sixs(3)
        hb2.Confirm_nu()  # 点击确认选号
        hc1.Coun_nu()###点击继续选号
        hb.Play()  ###点击玩法
        hb.Play_Group_there()  ####点击组三
        hb.Switch_play_ok()##点击确定
        hb.group_theres(4)  ###组三，选择4个号码
        hb2.Confirm_nu()  # 点击确认选号
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)