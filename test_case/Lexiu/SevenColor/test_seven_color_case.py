from time import sleep
from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber_lexiu
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery_lexiu
from element_operate.Seven_color.Seven_color_choosenumber import Seven_color_choosenumber_lexiu
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.homepage import HomePage_lexiu
from element_operate.login import Login_lexiu
from test_case.Base.mytest import MyTest
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lexiu
from element_operate.less_pay_sucess import LessPaySucess_lexiu


class Seven_color(MyTest):
    """七星彩，自动化测试用例"""
    def test_choosenumber_all_case(self):
        '''验证数字球点击功能,随机选号，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb=Seven_color_choosenumber_lexiu(self.driver)
        hb1=UnionLottoChooseNumber_lexiu(self.driver)
        hb2=ArrangeFiveChooseNumber_lexiu(self.driver)
        hc=ConfirmLottery_lexiu(self.driver)
        hl=Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()#点击七星彩
        hb.Seven_nuo()#点击第一位选号
        hb.Seven_nut()#点击第二位选号
        hb.Seven_nut()#点击第三位选号
        hb.Seven_nuf()#点击第四位选号
        hb.Seven_nufi()#点击第五位选号
        hb.Seven_nus()#点击第六位选号
        hb.Seven_nuse()#点击第七位选号
        hb.Seven_nuf()#取消第四位选号
        hb.Seven_nufi()#取消第五位选号
        hb.Seven_nus()#取消第六位选号
        hb.Seven_nuse()#取消第七位选号
        hb.Afive_top()
        hb.Seven_nuo()#取消第一位选号
        hb.Seven_nut()#取消第二位选号
        hb.Seven_nut()#取消第三位选号
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Afive_down()  # 鼠标下拉
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()####点击确认选号
        hc.submit_order_to_station_owner_button()#点击订单给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_choosenumber_clear_nu_case(self):
        '''验证清除选号按钮功能，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb=Seven_color_choosenumber_lexiu(self.driver)
        hb1=ArrangeFiveChooseNumber_lexiu(self.driver)
        hb2 = UnionLottoChooseNumber_lexiu(self.driver)
        hc=ConfirmLottery_lexiu(self.driver)
        hc1=ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl=Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()#点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Afive_down()  # 鼠标下拉
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb.Afive_top()##鼠标拉到顶端
        hb2.clear_number()  # 点击清除选号按钮
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  ####点击确认选号
        mur = hc1.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击订单给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_coun_nu_case(self):
        '''确认页点击继续选号，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  # 点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  ####点击确认选号
        hc1.Coun_nu()###点击继续选号
        hb1.machine_choose_button()  #####点击机选按钮
        hb1.machine_choose_one_button()  ####点击机选1注
        hb2.Confirm_nu()  # 点击确认选号按钮
        mur = hc1.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击订单给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_coun_five_case(self):
        '''确认页点击机选5注，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  # 点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  ####点击确认选号
        hc1.Pause_five()  ###点击继续选号
        mur = hc1.Test_note_nu()
        self.assertEqual('6', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击订单给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    """def test_coun_one_case(self):
        '''确认页点击机选1注，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  # 点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  ####点击确认选号
        hc1.Pause_one()  ###点击机选一注
        mur = hc1.Test_note_nu()
        self.assertEqual('2', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击订单给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付"""

    def test_Del_none_case(self):
        '''验证点击X按钮，删除N注所选号码，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  # 点击七星彩
        hb1.machine_choose_button()  #####点击机选按钮
        hb1.machine_choose_ten_button()  ####点击机选10注
        hc1.Del_none(2)  ######删除2注
        mur = hc1.Test_note_nu()
        self.assertEqual('8', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击订单给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Del_all_nu_case(self):
        '''验证点击清除所有选择号码按钮，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_ten_button()  ####点击机选10注
        hc.delete_all_num_button()
        hc.cancel_delete_button()
        hc.delete_all_num_button()
        hc.confirm_delete_button()
        hb1.machine_choose_button()  #####点击机选按钮
        hb1.machine_choose_one_button()  ####点击机选1注
        hb2.Confirm_nu()
        mur = hc1.Test_note_nu()
        self.assertEqual('1', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_alter_nu_case(self):
        '''验证点击选择号码进行修改，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_five_button()  ####点击机选5注
        hc1.Note_none(2)##选择2注进行修改
        mur = hc1.Test_note_nu()
        self.assertEqual('13', mur)  ####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_iagree_case(self):
        '''验证点击我已满18岁单选按钮，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc1.Iagree()#点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc1.Know()#点击我知道了
        hc1.Iagree()  # 点击我已满18岁单选按钮
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Multiple_input_case(self):
        '''验证倍数输入框功能，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_input(3)###点击倍数输入功能
        mur=hc1.Test_multiple_show()#读取倍数
        self.assertEqual('3',mur)##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Multiple_less_case(self):
        '''验证倍数 -号功能，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_input(3)###点击倍数输入功能
        hc1.Multiple_less()##点击倍数 —号
        mur=hc1.Test_multiple_show()#读取倍数
        self.assertEqual('2',mur)##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Multiple_add_case(self):
        '''验证倍数 +号功能，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_add()##点击倍数 +号
        mur=hc1.Test_multiple_show()#读取倍数
        self.assertEqual('2',mur)##断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_input_case(self):
        """"手动输入期数进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_input(3)##输入追期
        nu=hc1.Test_period_show()
        self.assertEqual('3',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_add_case(self):
        """"点击期数+，进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc1.A_period()##点击期数+
        nu=hc1.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_less_case(self):
        """"点击期数-，进行修改"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_input(3)  ##输入追期
        hc1.L_period()##点击期数-
        nu=hc1.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_too_case(self):
        """"点击追加2期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_two()##点击 2期
        nu=hc1.Test_period_show()
        self.assertEqual('2',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_five_case(self):
        """"点击追加5期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_five()##点击 5期
        nu=hc1.Test_period_show()
        self.assertEqual('5',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_ten_case(self):
        """"点击追加10期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_ten()##点击 5期
        nu=hc1.Test_period_show()
        self.assertEqual('10',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_twenty_case(self):
        """"点击追加20期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_twenty()##点击 20期
        nu=hc1.Test_period_show()
        self.assertEqual('20',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_chase_ticket_fifty_case(self):
        """"点击追加50期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(3)  # 在一位随机点击3个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(2)  # 在三位随机点击2个数字
        hb.Seven_nufs(3)  ##在四位随机点击3个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(3)  # 在六位随机点击3个数字
        hb.Seven_nuses(2)  # 在七位随机点击2个数字
        hb2.Confirm_nu()  # 点击确认选号按钮
        hc.chase_ticket_button()###点击追期
        hc.chase_ticket_button_fifty()##点击 50期
        nu=hc1.Test_period_show()
        self.assertEqual('50',nu)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_machine_choose_one_case(self):
        '''验证机选1注支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_one_button()####点击机选1注
        hb2.Confirm_nu()###点击确认选号
        mur=hc1.Test_note_nu()
        self.assertEqual('1',mur)####断言注数
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_machine_choose_five_case(self):
        '''验证机选5注支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_five_button()####点击机选5注
        mur = hc1.Test_note_nu()
        self.assertEqual('5', mur)#####断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_machine_choose_ten_case(self):
        '''验证机选10注支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb1.machine_choose_button()#####点击机选按钮
        hb1.machine_choose_ten_button()####点击机选10注
        mur = hc1.Test_note_nu()
        self.assertEqual('10', mur)#######断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Confirm_nu_case(self):
        '''验证点击2次确认选号按钮，支付流程'''
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hb1 = UnionLottoChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb2.Confirm_nu()
        hb2.Confirm_nu()  ######点击2次确认选号
        mur = hc1.Test_note_nu()
        self.assertEqual('1', mur)#######断言
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_instruction_case(self):
        """验证玩法说明"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb2.Instruct()##点击右上角...
        hb.Seven_color_instruct()##点击玩法说明
        mur = hb.Seven_color_play()
        self.assertEqual('七星彩玩法', mur)
        hb.Seven_color_know()

    def test_seven_color_history(self):
        """历史走势"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb2.Instruct()##点击右上角...
        hb.Seven_color_history()##点击历史走势
        hb.Afive_down()###鼠标下拉
        mur=hb.History_date()##随机取显示的数据
        if mur=='':
            self.assertEqual('a',mur)
        else:
            print("历史走势展示正常")

    def test_many_note_many_double_case(self):
        """多注多倍"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(2)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击1个数字
        hb.Seven_nuths(2)  # 在三位随机点击1个数字
        hb.Seven_nufs(2)  ##在四位随机点击1个数字
        hb.Seven_nufis(2)  # 在五位随机点击1个数字
        hb.Seven_nuss(2)  # 在六位随机点击1个数字
        hb.Seven_nuses(2)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('128', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_many_note_many_double_Continue_case(self):
        """多注多倍,继续选号"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('3', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_many_note_many_double_Continue_entry_case(self):
        """多注多倍,继续选号,复式"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('2', mur1)
        hc1.Multiple_input(5)  ###点击倍数输入功能
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5', mur)
        hc1.Coun_nu()###点击继续选号
        hb.Seven_nuos(2)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(2)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur = hc1.Test_multiple_show()  ##读取倍数
        self.assertEqual('5',mur)
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('6', mur1)
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        #hl.new_user_login_tab()  # 点击新登录
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    '''def test_many_note_many_double_pause_one_case(self):
        """多注多倍,机选一注"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
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
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)'''

    def test_many_note_many_double_pause_five_case(self):
        """多注多倍,机选五注"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
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
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    '''def test_many_note_many_double_pause_period_one_case(self):
        """多注多倍,机选一注,追期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
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
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)'''

    def test_many_note_many_double_pause_five_period_case(self):
        """多注多倍,机选五注,追期"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd=LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
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
        hl.login_lexiu()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付
        mur1 = hd.assect_pay()  ##读取支付状态文本
        self.assertEqual('订单提交成功', mur1)

    def test_a_note_del_case(self):
        """单注号码，点击X按钮"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc1.Del_none(1)  ######删除1注
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(1)  # 在二位随机点击1个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        mur1 = hc1.Test_note_nu()  ##读取注数
        self.assertEqual('1', mur1)
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
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.cancel_delete_button()  # 点击取消
        mur=hc.confirm_num_page_text()
        self.assertEqual('提交订单给站主',mur)

    def test_seven_color_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        mur=hb2.Clear()
        self.assertEqual('清空',mur)

    def test_seven_color_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_lexiu(self.driver)
        hb = Seven_color_choosenumber_lexiu(self.driver)
        hb2 = There_D_choosenumber_lexiu(self.driver)
        hb1 = ArrangeFiveChooseNumber_lexiu(self.driver)
        hc = ConfirmLottery_lexiu(self.driver)
        hc1 = ArrangeFiveConfirmLottery_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hd = LessPaySucess_lexiu(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.colorful_star_link()  ###点击七星彩
        hb.Seven_nuos(1)  # 在一位随机点击1个数字
        hb.Seven_nuts(2)  # 在二位随机点击2个数字
        hb.Seven_nuths(1)  # 在三位随机点击1个数字
        hb.Seven_nufs(1)  ##在四位随机点击1个数字
        hb.Seven_nufis(1)  # 在五位随机点击1个数字
        hb.Seven_nuss(1)  # 在六位随机点击1个数字
        hb.Seven_nuses(1)  # 在七位随机点击1个数字
        hb1.Confirm_nu()  # 点击确认选号按钮
        hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur=hb.Seven_color_lor()
        self.assertEqual('七星彩',mur)