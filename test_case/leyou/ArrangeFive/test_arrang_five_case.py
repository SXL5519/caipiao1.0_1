from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber_leyou
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_leyou
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.homepage import HomePage_leyou
from element_operate.login import Login_leyou
from test_case.Base.mytest import MyTest
from element_operate.Seven_color.Seven_color_choosenumber import Seven_color_choosenumber_leyou
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_leyou
from element_operate.less_pay_sucess import LessPaySucess_leyou


class Arrang_Five(MyTest):
    ########排列5#########
    def test_choosenumber_all_case(self):
        '''验证数字球点击功能,随机选号，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()###点击排列5
        hb.Afive_nuw()#点击万位所有号码
        hb.Afive_nuq()#点击千位所有号码
        hb.Afive_nub()#点击百位所有号码
        hb.Afive_down()#鼠标向下拉动到底部
        hb.Afive_nus()#点击十位所有号码
        hb.Afive_nug()#点击个位所有号码
        hb.Afive_nus()#取消十位所有号码
        hb.Afive_nug()#取消个位所有号码
        hb.Afive_top()#鼠标向上拉动到顶部
        hb.Afive_nuw()#取消万位所有号码
        hb.Afive_nuq()#取消千位所有号码
        hb.Afive_nub()#取消百位所有号码
        hb.Afive_nuws(4)#随机选择4个万位号码
        hb.Afive_nuqs(4)#随机选择4个千位号码
        hb.Afive_nubs(4)#随机选择4个百位号码
        hb.Afive_down()#鼠标向下
        hb.Afive_nuss(5)#随机选择5个十位号码
        hb.Afive_nugs(7)#随机选择7个个位号码
        hb.Confirm_nu()#点击确认选号按钮
        hc.submit_order_to_station_owner_button()#点击提交给站主
        #hl.new_user_login_tab()#点击新登录
        hl.login_leyou()#输入账号，密码
        hc.submit_order_to_station_owner_button()#点击提交给站主
        hc.confirm_and_pay_button()#点击确认支付

    def test_Coun_nu_case(self):
        '''验证手选号码，点击继续选号，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 =UnionLottoChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hd.Coun_nu()  #点击继续选号
        hb1.machine_choose_button()  #####点击机选按钮
        hb1.machine_choose_one_button()  ####点击机选1注
        hb.Confirm_nu()  # 点击确认选号按钮
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Pause_five_case(self):
        '''验证手选号码，点击机选5注，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hd.Pause_five() # 点击机选5注
        mur = hd.Test_note_nu()
        self.assertEqual('6', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    """def test_Pause_one_case(self):
        '''验证手选号码，点击机选1注，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hd.Pause_one() # 点击机选1注
        mur = hd.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付"""

    def test_Del_none_case(self):
        '''验证点击X按钮，删除N注所选号码，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_ten_button()  ####点击机选10注
        hd.Del_none(2)  ######删除2注
        mur = hd.Test_note_nu()
        self.assertEqual('8', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Del_all_nu_case(self):
        '''验证点击清除选择号码按钮，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_ten_button()  ####点击机选10注
        hc.delete_all_num_button()###点击清除列表
        hc.cancel_delete_button()#点击取消
        hc.delete_all_num_button()
        hc.confirm_delete_button()#点击确定
        hb1.machine_choose_button()  #####点击机选按钮
        hb1.machine_choose_one_button()  ####点击机选1注
        hb.Confirm_nu()
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_alter_nu_case(self):
        '''验证点击选择号码进行修改，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_five_button()  ####点击机选5注
        hd.Note_none(2)
        mur = hd.Test_note_nu()
        self.assertEqual('13', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_iagree_case(self):
        '''验证点击我已满18岁单选按钮，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hd.Iagree()#点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hd.Know()#点击我知道了
        hd.Iagree()  # 点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Multiple_input_case(self):
        '''验证倍数输入框功能，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1=ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_input(3)###点击倍数输入功能
        mur=hd.Test_multiple_show()#读取倍数
        self.assertEqual('3',mur)##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Multiple_less_case(self):
        '''验证倍数 -号功能，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_input(3)###点击倍数输入功能
        hc1.Multiple_less()##点击倍数 —号
        mur=hc1.Test_multiple_show()#读取倍数
        self.assertEqual('2',mur)##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Multiple_add_case(self):
        '''验证倍数 +号功能，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_add()##点击倍数 +号
        mur=hc1.Test_multiple_show()#读取倍数
        self.assertEqual('2',mur)##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_input_case(self):
        """"手动输入期数进行修改"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_input(3)##输入追期
        nu=hc1.Test_period_show()
        self.assertEqual('3',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_add_case(self):
        """"点击期数+，进行修改"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc1.A_period()##点击期数+
        nu=hc1.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_less_case(self):
        """"点击期数-，进行修改"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_input(3)  ##输入追期
        hc1.L_period()##点击期数-
        nu=hc1.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_too_case(self):
        """"点击追加2期"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_two()##点击 2期
        nu=hc1.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_five_case(self):
        """"点击追加5期"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_five()##点击 5期
        nu=hc1.Test_period_show()
        self.assertEqual('5',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_ten_case(self):
        """"点击追加10期"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_ten()##点击 5期
        nu=hc1.Test_period_show()
        self.assertEqual('10',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_twenty_case(self):
        """"点击追加20期"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_twenty()##点击 20期
        nu=hc1.Test_period_show()
        self.assertEqual('20',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_fifty_case(self):
        """"点击追加50期"""
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Afive_nuws(1)  # 随机选择1个万位号码
        hb.Afive_nuqs(1)  # 随机选择1个千位号码
        hb.Afive_nubs(1)  # 随机选择1个百位号码
        hb.Afive_down()  # 鼠标向下
        hb.Afive_nuss(1)  # 随机选择1个十位号码
        hb.Afive_nugs(1)  # 随机选择1个个位号码
        hb.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_fifty()##点击 50期
        nu=hc1.Test_period_show()
        self.assertEqual('50',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_machine_choose_one_case(self):
        '''验证机选1注支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_one_button()####点击机选1注
        hb.Confirm_nu()###点击确认选号
        mur=hd.Test_note_nu()
        self.assertEqual('1',mur)####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_machine_choose_five_case(self):
        '''验证机选5注支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_five_button()####点击机选5注
        mur = hd.Test_note_nu()
        self.assertEqual('5', mur)#####断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_machine_choose_ten_case(self):
        '''验证机选10注支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_ten_button()####点击机选10注
        mur = hd.Test_note_nu()
        self.assertEqual('10', mur)#######断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Confirm_nu_case(self):
        '''验证点击2次确认选号按钮，支付流程'''
        ha = HomePage_leyou(self.driver)
        hb = ArrangeFiveChooseNumber_leyou(self.driver)
        hb1 = UnionLottoChooseNumber_leyou(self.driver)
        hd = ArrangeFiveConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb.Confirm_nu()
        hb.Confirm_nu()  ######点击2次确认选号
        mur = hd.Test_note_nu()
        self.assertEqual('1', mur)#######断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_instruction_case(self):
        """验证玩法说明"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb2.Instruct()##点击右上角...
        hb.Seven_color_instruct()##点击玩法说明
        mur = hb.Seven_color_play()
        self.assertEqual('排列5玩法', mur)
        hb.Seven_color_know()

    def test_seven_color_history(self):
        """历史走势"""
        ha = HomePage_leyou(self.driver)
        hb1=ArrangeFiveChooseNumber_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb2.Instruct()##点击右上角...
        hb.Seven_color_history()##点击历史走势
        hb.Afive_down()###鼠标下拉
        mur=hb1.history_arrange_five_date()##随机取显示的数据
        if mur=='':
            self.assertEqual('a',mur)
        else:
            print("历史走势展示正常")

    def test_many_note_many_double_case(self):
        """多注多倍"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(2)  # 随机选择1个千位号码
        hb1.Afive_nubs(2)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(2)  # 随机选择1个十位号码
        hb1.Afive_nugs(2)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('32', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_many_note_many_double_Continue_case(self):
        """多注多倍,继续选号"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('3', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_many_note_many_double_Continue_after_case(self):
        """多注多倍,继续选号,复式"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('4', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    '''def test_many_note_many_double_pause_one_case(self):
        """多注多倍,机选一注"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_one()  ###点击机选一注
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('3', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)'''

    def test_many_note_many_double_pause_five_case(self):
        """多注多倍,机选五注"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_five()  ###点击机选五注
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('7', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    '''def test_many_note_many_double_pause_period_one_case(self):
        """多注多倍,机选一注,追期"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(2)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_one()  ###点击机选一注
        hc.chase_ticket_input(3)  ##输入追期
        nu = hc1.Test_period_show()
        self.assertEqual('3', nu)
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('3', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)'''

    def test_many_note_many_double_pause_five_period_case(self):
        """多注多倍,机选五注,追期"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(2)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Pause_five()  ###点击机选五注
        hc.chase_ticket_input(3)  ##输入追期
        nu = hc1.Test_period_show()
        self.assertEqual('3', nu)
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('7', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)


    def test_a_note_del_case(self):
        """单注号码，点击X按钮"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc1.Del_none(1)  ######删除1注
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('1', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_leyou()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_seven_color_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_seven_color_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hb2.Clear()
        self.assertEqual('清空',mur)

    def test_seven_color_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_leyou(self.driver)
        hb = Seven_color_choosenumber_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        hb1 = ArrangeFiveChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = ArrangeFiveConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = LessPaySucess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.rank_five_link()  ###点击排列5
        hb1.Afive_nuws(1)  # 随机选择1个万位号码
        hb1.Afive_nuqs(1)  # 随机选择1个千位号码
        hb1.Afive_nubs(1)  # 随机选择1个百位号码
        hb1.Afive_down()  # 鼠标向下
        hb1.Afive_nuss(1)  # 随机选择1个十位号码
        hb1.Afive_nugs(1)  # 随机选择1个个位号码
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur=hb.Seven_color_lor()
        self.assertEqual('排列五',mur)