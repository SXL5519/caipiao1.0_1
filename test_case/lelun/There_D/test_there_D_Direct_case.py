from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber_lelun
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_lelun
from element_operate.Arrange_there.Arrang_there_choosenumber import Arrang_there_choosenumber
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lelun
from  element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.login import Login_lelun
from test_case.Base.mytest import MyTest
from time import sleep


class there_D_case(MyTest):
    """There_D,直选"""
    def test_Direct_all_choosenumber_case(self):
        """验证选号页面数字球功能"""
        ha = HomePage_lelun(self.driver)
        hb=There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()###点击3D
        hb.Play_d()###点击玩法
        hb.Play_direct_d()###点击直选
        hb.there_D_bai()##点击百位数字
        hb.there_D_shi()##点击十位数字
        hb.there_D_ge()##点击个位数字
        hb.there_D_bai()##取消百位数字
        hb.there_D_shi()##取消十位数字
        hb.there_D_ge()##取消个位数字
        hb.there_D_bais(1,0)##随机取百位1个数字
        hb.there_D_shis(0,1)##随机取十位1个数字
        hb.there_D_ges(0,1)##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    '''def test_Direct_pause_one_case(self):
        """验证选号页面，点击机选一注功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1=ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()###点击机选
        hb2.machine_choose_one_button()##点击机选一注
        hb1.Confirm_nu()#点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付'''

    def test_Direct_pause_five_case(self):
        """验证选号页面，点击机选五注功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()###点击机选
        hb2.machine_choose_five_button()##点击机选五注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_pause_ten_case(self):
        """验证选号页面，点击机选10注功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()###点击机选
        hb2.machine_choose_ten_button()##点击机选10注
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_click_too_confirm_case(self):
        """验证选号页面，点击2次确认选号按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付


    def test_Direct_clear_number_case(self):
        """验证选号页面，点击清除选号按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb2.clear_number()#点击清除选号页面
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Coun_nu_case(self):
        """验证确认投注页面，点击继续选号按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Coun_nu()#点击继续选号
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Pause_five_case(self):
        """验证确认投注页面，点击机选5注按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Pause_five()  # 点击机选5注
        mur = hd.Test_note_nu()
        self.assertEqual('6', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Pause_one_case(self):
        """验证确认投注页面，点击机选1注按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Pause_one()  # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Del_none_case(self):
        """验证确认投注页面，点击X图标功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hd.Del_none(2)  ######删除2注
        mur = hd.Test_note_nu()
        self.assertEqual('8', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_one_button()  ##点击机选一注
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_alter_nu_case(self):
        """验证确认投注页面，点击选择号码进行修改"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_five_button()  ##点击机选5注
        hd.Note_none(2)
        mur = hd.Test_note_nu()
        self.assertEqual('13', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_iagree_case(self):
        """验证确认投注页面，'点击我已满18岁单选按钮"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Iagree()  # 点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hd.Know()  # 点击我知道了
        hd.Iagree()  # 点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Multiple_input_case(self):
        """验证确认投注页面，'输入倍数"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(3)  ###点击倍数输入功能
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('3', mur)  ##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Multiple_less_case(self):
        """验证确认投注页面，点击倍数 -号"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(3)  ###点击倍数输入功能
        hd.Multiple_less()  ##点击倍数 —号
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('2', mur)  ##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Multiple_add_case(self):
        """验证确认投注页面，点击倍数+"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_add()  ##点击倍数 +号
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('2', mur)  ##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_input_case(self):
        """"手动输入期数进行修改"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_input(3)##输入追期
        nu=hd.Test_period_show()
        self.assertEqual('3',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_add_case(self):
        """"点击期数+，进行修改"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.A_period()  ##点击期数+
        nu=hd.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_less_case(self):
        """"点击期数-，进行修改"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_input(3)  ##输入追期
        hd.L_period()  ##点击期数-
        nu=hd.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_too_case(self):
        """"点击追加2期"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_two()  ##点击 2期
        nu=hd.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_five_case(self):
        """"点击追加5期"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_five()  ##点击 5期
        nu=hd.Test_period_show()
        self.assertEqual('5',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_ten_case(self):
        """"点击追加10期"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_ten()  ##点击 10期
        nu=hd.Test_period_show()
        self.assertEqual('10',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_twenty_case(self):
        """"点击追加20期"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_twenty()  ##点击 20期
        nu=hd.Test_period_show()
        self.assertEqual('20',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_fifty_case(self):
        """"点击追加50期"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位去个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_fifty()  ##点击 50期
        nu=hd.Test_period_show()
        self.assertEqual('50',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lelun()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_a_note_many_double_case(self):
        """手动选择1注多倍号码"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  # 随机选取百位1个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(0, 1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(13)  ###点击倍数输入功能
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('13', mur)  ##断言
        nu = hd.Test_note_nu()
        self.assertEqual('1', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主


    def test_Direct_many_note_a_double_case(self):
        """手动选择多注1倍号码"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 3)  # 随机选取百位4个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(1, 1)  # 随机选择个位2个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('1', mur)  ##断言
        nu = hd.Test_note_nu()
        self.assertEqual('8', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主


    def test_Direct_many_note_many_double_case(self):
        """手动选择多注多倍号码"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 3)  # 随机选取百位4个数字
        hb.there_D_shis(0, 1)  # 随机选取十位1个数字
        hb.there_D_ges(1, 1)  # 随机选择个位2个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        nu = hd.Test_note_nu()
        self.assertEqual('8', nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主


    def test_Direct_a_note_many_double_Coun_nu_case(self):
        """验证1注多倍号码，点击继续选号按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Coun_nu()#点击继续选号
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()##点击提交给站主


    def test_Direct_many_note_a_double_Coun_nu_case(self):
        """验证多注1倍号码，点击继续选号按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(3, 1)  ##随机取十位4个数字
        hb.there_D_ges(1, 1)  ##随机取个位2个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Coun_nu()#点击继续选号
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('9', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('1', mur)  ##断言
        hc.submit_order_to_station_owner_button()##点击提交给站主


    def test_Direct_many_note_many_double_Coun_nu_case(self):
        """验证多注多倍号码，点击继续选号按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(3, 1)  ##随机取十位4个数字
        hb.there_D_ges(1, 1)  ##随机取个位2个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Coun_nu()#点击继续选号
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('9', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()##点击提交给站主


    def test_Direct_a_note_many_double_Pause_five_case(self):
        """验证1注多倍号码，点击机选5注按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Pause_five()  # 点击机选5注
        mur = hd.Test_note_nu()
        self.assertEqual('6', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()  ##点击提交给站主


    '''def test_Direct_many_note_a_double_Pause_one_case(self):
        """验证多注1倍号码，点击机选1注按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(3, 1)  ##随机取十位4个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Pause_one()  # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('1', mur)  ##断言
        hc.submit_order_to_station_owner_button()  ##点击提交给站主'''


    '''def test_Direct_many_note_many_double_Pause_one_case(self):
        """验证多注多倍号码，点击机选1注按钮功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(3, 1)  ##随机取十位4个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(10)  ###点击倍数输入功能
        hd.Pause_one()  # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)  ####断言注数
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('10', mur)  ##断言
        hc.submit_order_to_station_owner_button()  ##点击提交给站主'''


    def test_Direct_a_note_Del_none_case(self):
        """验证确认投注页面，点击X图标功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hd.Del_none(1)  ######删除1注
        hb.there_D_bais(1, 0)  ##随机取百位1个数字
        hb.there_D_shis(0, 1)  ##随机取十位1个数字
        hb.there_D_ges(0, 1)  ##随机取个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数

    def test_Direct_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_Direct_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lelun(self.driver)
        hb = There_D_choosenumber_lelun(self.driver)
        hb1 = ArrangeFiveChooseNumber_lelun(self.driver)
        hb2 = UnionLottoChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hd = ArrangeFiveConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()  ###点击直选
        hb2.machine_choose_button()  ###点击机选
        hb2.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hb.Clear()
        self.assertEqual('清空',mur)