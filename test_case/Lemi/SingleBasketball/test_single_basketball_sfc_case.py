from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.login import Login
from element_operate.Haobc.haobc_confirm import HaobcConfirm
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm
from element_operate.SingleFoot.single_foot_confim import SingleFootConfirmLottery
from element_operate.SingleBasketball.single_basketball_choosenumber import SingleBasketballChooseNumber
class Single_Basketball_sfc_case(MyTest):
    """竞篮单关，胜分差玩法"""
    def test_Play_sfc_choosenumber(self):
        """验证选号页面点击全部赛事结果，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞彩单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击让分胜负玩法
        aa = hb.Basketball_sfc_ba()
        if aa == 1:
            hb.Basketball_sfc_bas(6)
            hb1.confirm_match()  ###点击已选择N场赛事
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_choosenumber_eight_case(self):
        """验证选号页面点击8场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击胜分差玩法
        aa=hb.Basketball_sfc_nus_X(8)####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_choosenumber_nine_case(self):
        """验证选号页面点击9场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(9) ####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_emptying(self):
        """验证选号页面清空按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  #点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa>0:
            hb.Emptying()##点击清除
            hb.confirm_match()  ###点击已选N场比赛
            hb.Basketball_sfc_nus_X(5)  ###随机点击5场比赛
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Add_event(self):
        """验证添加/编辑赛事按钮，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = HaobcConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.edit_event()  ###点击编辑/添加赛事
            mul = hb.Play_fb()  ###读取文本
            self.assertEqual('玩\n法', mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_N_del(self):
        """验证删除赛事X按钮，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            a=hc1.NN()###读取删除前有多少个X按钮
            hc1.C_nn()##点击第1场赛事的X按钮
            a1=hc1.NN()###读取删除后有多少个X按钮
            self.assertEqual(a-1,a1)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Pf_del_icon(self):
        """验证删除选择的全部赛事图标，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa>0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.down_bf()
            hc1.Pf_del_icon()
            hc.confirm_delete_button()
            hb.Basketball_sfc_nus_X(4)
            mul=hb.Text_confirm_loc()
            self.assertEqual('已选%d场比赛'%aa,mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Times_input(self):
        """验证修改倍数输入框功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hc2 = SingleFootConfirmLottery(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            mul=hc2.Lottery_dgp()###获取倍数
            self.assertEqual('共288元',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_less(self):
        """验证修改倍数 - 功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = SingleFootConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            hc1.Btn_less()####点击倍数-
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共192元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_add(self):
        """验证修改倍数 +功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = SingleFootConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            hc1.Btn_add()####点击倍数+
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共384元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_eighty(self):
        """验证80倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = SingleFootConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(80)####点击80倍
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共7680元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def optimize_award_case(self):
        '''验证奖金优化流程测试'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  ###点击玩法
        hcn.Play_sfc()  ##点击胜负
        aa = hcn.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hcn.confirm_match()  ###点击确认赛事
            pbc.Pf_bouns()##点击奖金优化
            text=pbc.optimize_award()#获取奖金优化页上方文本
            self.assertIn("平均优化购买",text)
            cl.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            cl.submit_order_to_station_owner_button()  # 点击提交给站主
            cl.confirm_and_pay_button()  # 点击确认支付