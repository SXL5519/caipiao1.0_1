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


class Arrang_there(MyTest):
    """排列3,直选"""
###########直选######################
    def test_Direct_all_choosenumber_case(self):
        """验证选号页面数字球功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb.there_bai()##点击百位全部数字
        hb.there_shi()##点击十位全部数字
        hb.there_ge()##点击个位全部数字
        hb.there_bai()##取消百位全部数字
        hb.there_shi()##取消十位全部数字
        hb.there_ge()##取消个位全部数字
        hb.there_bais(1)#随机选取百位1个数字
        hb.there_shis(1)#随机选取十位1个数字
        hb.there_ges(1)#随机选择个位1个数字
        hb1.Confirm_nu()#点击确认选号
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付


    def test_Direct_pause_one_case(self):
        """验证选号页面，点击机选一注功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb2.machine_choose_button()###点击机选
        hb2.machine_choose_one_button()##点击机选一注
        hb1.Confirm_nu()#点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_pause_five_case(self):
        """验证选号页面，点击机选五注功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb2.machine_choose_button()###点击机选
        hb2.machine_choose_five_button()##点击机选五注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_pause_ten_case(self):
        """验证选号页面，点击机选10注功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb2.machine_choose_button()###点击机选
        hb2.machine_choose_ten_button()##点击机选10注
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_click_too_confirm_case(self):
        """验证选号页面，点击2次确认选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付


    def test_Direct_clear_number_case(self):
        """验证选号页面，点击清除选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.clear_number()#点击清除选号页面
        hb1.Confirm_nu()  # 点击确认选号
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Coun_nu_case(self):
        """验证确认投注页面，点击继续选号按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb=Arrang_there_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()####点击排列3
        hb.Play()###点击玩法
        hb.Play_Direct()####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hb2.Coun_nu()#点击继续选号
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Pause_five_case(self):
        """验证确认投注页面，点击机选5注按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hb2.Pause_five()  # 点击机选5注
        mur = hd.Test_note_nu()
        self.assertEqual('6', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Pause_one_case(self):
        """验证确认投注页面，点击机选1注按钮功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb1.Confirm_nu()  # 点击确认选号
        hb2.Pause_one()  # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Del_none_case(self):
        """验证确认投注页面，点击X图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb1.machine_choose_button()  ###点击机选
        hb1.machine_choose_ten_button()  ##点击机选10注
        hd.Del_none(2)  ######删除2注
        mur = hd.Test_note_nu()
        self.assertEqual('8', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb1.machine_choose_button()  ###点击机选
        hb1.machine_choose_ten_button()  ##点击机选10注
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        hc.delete_all_num_button()
        hc.confirm_delete_button()  # 点击确定
        hb1.machine_choose_button()  ###点击机选
        hb1.machine_choose_one_button()  ##点击机选一注
        hb2.Confirm_nu()  # 点击确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_alter_nu_case(self):
        """验证确认投注页面，点击选择号码进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb1.machine_choose_button()  ###点击机选
        hb1.machine_choose_five_button()  ##点击机选5注
        hd.Note_none(2)
        mur = hd.Test_note_nu()
        self.assertEqual('13', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_iagree_case(self):
        """验证确认投注页面，'点击我已满18岁单选按钮"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hd.Iagree()  # 点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hd.Know()  # 点击我知道了
        hd.Iagree()  # 点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Multiple_input_case(self):
        """验证确认投注页面，'输入倍数"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(3)  ###点击倍数输入功能
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('3', mur)  ##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Multiple_less_case(self):
        """验证确认投注页面，点击倍数 -号"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hd.Multiple_input(3)  ###点击倍数输入功能
        hd.Multiple_less()  ##点击倍数 —号
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('2', mur)  ##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_Multiple_add_case(self):
        """验证确认投注页面，点击倍数+"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hd.Multiple_add()  ##点击倍数 +号
        mur = hd.Test_multiple_show()  # 读取倍数
        self.assertEqual('2', mur)  ##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_input_case(self):
        """"手动输入期数进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_input(3)##输入追期
        nu=hd.Test_period_show()
        self.assertEqual('3',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_add_case(self):
        """"点击期数+，进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hd.A_period()  ##点击期数+
        nu=hd.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_less_case(self):
        """"点击期数-，进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_input(3)  ##输入追期
        hd.L_period()  ##点击期数-
        nu=hd.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_too_case(self):
        """"点击追加2期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_two()  ##点击 2期
        nu=hd.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_five_case(self):
        """"点击追加5期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_five()  ##点击 5期
        nu=hd.Test_period_show()
        self.assertEqual('5',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_ten_case(self):
        """"点击追加10期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_ten()  ##点击 10期
        nu=hd.Test_period_show()
        self.assertEqual('10',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_twenty_case(self):
        """"点击追加20期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_twenty()  ##点击 20期
        nu=hd.Test_period_show()
        self.assertEqual('20',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Direct_chase_ticket_fifty_case(self):
        """"点击追加50期"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hd = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.chase_ticket_button()  ###点击追期
        hc.chase_ticket_button_fifty()  ##点击 50期
        nu=hd.Test_period_show()
        self.assertEqual('50',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_instruction_case(self):
        """验证玩法说明"""
        ha = HomePage_lexiu(self.driver)
        hb1=Arrang_there_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb2.Instruct()##点击右上角...
        hb1.Arrang_there_instruct()##点击玩法说明
        mur = hb1.Arrany_there_play()
        self.assertEqual('排列3玩法', mur)
        hb1.Arrany_there_know()

    def test_arrang_there_history(self):
        """历史走势"""
        ha = HomePage_lexiu(self.driver)
        hb1=Arrang_there_choosenumber_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb2.Instruct()##点击右上角...
        hb1.Arrang_there_history()##点击历史走势
        hb.Afive_down()###鼠标下拉
        mur=hb1.Arrany_there_date()##随机取显示的数据
        if mur=='':
            self.assertEqual('a',mur)
        else:
            print("历史走势展示正常")

    def test_arrany_there_play(self):
        """切换玩法"""
        ha = HomePage_lexiu(self.driver)
        hb = Arrang_there_choosenumber_lexiu(self.driver)
        hb1 = There_D_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_three_link()  ####点击排列3
        hb.Play()##点击玩法
        hb.Play_Direct()###点击直选
        mur1 = hb1.Show_play()
        self.assertEqual('排列三-直选', mur1)
        hb.Play()  ##点击玩法
        hb.Play_Group_there()  ###点击组三
        mur2 = hb1.Show_play()
        self.assertEqual('排列三-组三', mur2)
        hb.Play()  ##点击玩法
        hb.Play_Group_six()  ###点击组六
        mur3 = hb1.Show_play()
        self.assertEqual('排列三-组六', mur3)

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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(2)  # 随机选取十位1个数字
        hb.there_ges(2)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('8', mur1)
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(2)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb.there_bais(1)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
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
        mur4 = hd.assect_pay()  ##读取支付状态文本
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_five()  ###点击机选五注
        mur3 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur3)
        mur4 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('7', mur4)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur5 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur5)

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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        mur4 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur4)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur3 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur3)
        hc1.Pause_five()  ###点击机选五注
        hc.chase_ticket_input(3)  ##输入追期
        nu = hc1.Test_period_show()
        self.assertEqual('3', nu)
        mur2 = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur2)
        mur = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('7', mur)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)


    def test_a_note_del_case(self):
        """单注号码，点击X按钮"""
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        mur = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
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
        hb.Play_Direct()  ####点击直选
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
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
        hb.Play_Group_there()  ####点击组三
        hb.group_theres(4)###组三，选择4个号码
        hb2.Confirm_nu()  # 点击确认选号
        hc1.Coun_nu()###点击继续选号
        hb.Play()  ###点击玩法
        hb.Play_Direct()  ####点击直选
        hb.Switch_play_ok()##点击确定
        hb.there_bais(2)  # 随机选取百位去个数字
        hb.there_shis(1)  # 随机选取十位1个数字
        hb.there_ges(1)  # 随机选择个位1个数字
        hb2.Confirm_nu()  # 点击确认选号
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)