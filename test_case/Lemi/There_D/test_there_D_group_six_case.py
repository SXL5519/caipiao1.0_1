from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery
from element_operate.Arrange_there.Arrang_there_choosenumber import Arrang_there_choosenumber
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber
from  element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.homepage import HomePage
from element_operate.login import Login
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber

class there_D_group_six_case(MyTest):
    """There_D,组六"""
    def test_group_six_all_choosenumber_case(self):
        """验证选号页面数字球功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.group_six_d()
        hb.group_six_d()
        hb.group_sixs_d(2, 2)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('4', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_Screening_ji_case(self):
        """验证选号页面筛选 奇按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.Screening_d(0)  ###点击筛选中 奇 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_Screening_ou_case(self):
        """验证选号页面筛选 偶 按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.Screening_d(1)  ###点击筛选中 偶 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_Screening_da_case(self):
        """验证选号页面筛选 大 按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
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
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_Screening_xi_case(self):
        """验证选号页面筛选 小 按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.Screening_d(2)  ###点击筛选中 小 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_Screening_qu_case(self):
        """验证选号页面筛选 全 按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.Screening_d(4)  ###点击筛选中 全 按钮
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('120', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_Screening_qing_case(self):
        """验证选号页面筛选 清 按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.Screening_d(5)  ###点击筛选中 清 按钮
        hb.group_theres_d(2, 1)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_pause_one_case(self):
        """验证选号页面，点击机选一注功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_one_button()  ##点击机选一注
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_pause_five_case(self):
        """验证选号页面，点击机选五注功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_five_button()  ##点击机选五注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_pause_ten_case(self):
        """验证选号页面，点击机选10注功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_click_too_confirm_case(self):
        """验证选号页面，点击2次确认选号按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_group_six_clear_number_case(self):
        """验证选号页面，点击清除选号按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.group_theres_d(2, 2)
        hb2.clear_number()  # 点击清除选号页面
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付


    def test_group_six_many_note_many_double_case(self):
        """手动选择多注多倍号码"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.group_theres_d(2, 3)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        nu = hd.Test_note_nu()
        self.assertEqual('10', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主


    def test_group_six_many_note_many_double_Coun_nu_case(self):
        """验证多注多倍号码，点击继续选号按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.group_theres_d(2, 3)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Coun_nu()#点击继续选号
        hb.group_theres_d(2, 1)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('11', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()##点击提交给站主


    '''def test_group_six_many_note_many_double_Pause_one_case(self):
        """验证多注多倍号码，点击机选1注按钮功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.group_theres_d(2, 3)
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Pause_one()  # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('11', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()  ##点击提交给站主'''


    def test_group_six_a_note_Del_none_case(self):
        """验证确认投注页面，点击X图标功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb.group_theres_d(2, 3)
        hb1.Confirm_nu()  # 点击确认选号
        hb.Del_x()  ######删除1注
        hb.group_theres_d(2, 3)
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数

    def test_group_six_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_group_six_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hb.Clear()
        self.assertEqual('清空',mur)

    def test_group_six_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        hc1 = PaintBallChooseNumber(self.driver)
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()  ####点击组六
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur=hc1.Play_fb()
        self.assertEqual('玩\n法',mur)