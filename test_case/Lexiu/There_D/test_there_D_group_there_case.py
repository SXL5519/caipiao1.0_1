from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber_lexiu
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_lexiu
from element_operate.Arrange_there.Arrang_there_choosenumber import Arrang_there_choosenumber_lexiu
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lexiu
from  element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.homepage import HomePage_lexiu
from element_operate.login import Login_lexiu
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lexiu

class there_D_group_there_case(MyTest):
    """There_D,组三"""
    def test_group_there_all_choosenumber_case(self):
        """验证选号页面数字球功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_there_d()
        hb.group_there_d()
        hb.group_theres_d(2, 2)
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(0)  ###点击筛选中 奇 按钮
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(1)  ###点击筛选中 偶 按钮
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(2)  ###点击筛选中 大 按钮
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(2)  ###点击筛选中 小 按钮
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(4)  ###点击筛选中 全 按钮
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(5)  ###点击筛选中 清 按钮
        hb.group_theres_d(1, 1)
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = Arrang_there_choosenumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.Screening_d(4)  ###点击筛选中 全 按钮
        hb2.Group_delet()
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
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
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
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

    def test_Direct_add_many_note_a_double_case(self):
        """手动选择多注1倍号码"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('1', mur)  ##断言
        nu = hd.Test_note_nu()
        self.assertEqual('12', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主


    def test_Direct_add_many_note_many_double_case(self):
        """手动选择多注多倍号码"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        nu = hd.Test_note_nu()
        self.assertEqual('12', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主


    def test_Direct_add_many_note_a_double_Coun_nu_case(self):
        """验证多注1倍号码，点击继续选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Coun_nu()#点击继续选号
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('24', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('1', mur)  ##断言
        hc.submit_order_to_station_owner_button()##点击提交给站主


    def test_Direct_add_many_note_many_double_Coun_nu_case(self):
        """验证多注多倍号码，点击继续选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Coun_nu()#点击继续选号
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('24', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()##点击提交给站主


    def test_Direct_add_a_note_many_double_Pause_five_case(self):
        """验证1注多倍号码，点击机选5注按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Pause_five()  # 点击机选5注
        mur = hd.Test_note_nu()
        self.assertEqual('17', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()  ##点击提交给站主



    '''def test_Direct_add_many_note_many_double_Pause_one_case(self):
        """验证多注多倍号码，点击机选1注按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Pause_one()  # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('13', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()  ##点击提交给站主'''


    def test_Direct_add_a_note_Del_none_case(self):
        """验证确认投注页面，点击X图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb.group_theres_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Del_none(1)  ######删除1注
        mur = hd.Test_note_nu()
        self.assertEqual('11', mur)  ####断言注数

    def test_Direct_add_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_Direct_add_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hb.Clear()
        self.assertEqual('清空',mur)

    def test_Direct_add_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1=PaintBallChooseNumber_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()  ####点击组三
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur=hc1.Play_fb()
        self.assertEqual('玩\n法',mur)