from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber_leyou
from element_operate.homepage import HomePage_leyou
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.login import Login_leyou
from element_operate.Haobc.haobc_confirm import HaobcConfirm_leyou
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm_leyou
from element_operate.SingleFoot.single_foot_choose_number import SingleFootChooseNumber_leyou
from element_operate.SingleBasketball.single_basketball_choosenumber import SingleBasketballChooseNumber
from element_operate.SingleFoot.single_foot_confim import SingleFootConfirmLottery_leyou
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_leyou
from element_operate.UnionLotto.order_details import OrderDetails
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_leyou

class Single_basketball_mix(MyTest):
    """竞篮单关，混合投注玩法"""
    def test_Play_mix_choosenumber_case(self):
        """验证选号页面点击全部赛事结果，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞蓝单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击让分胜负玩法
        aa = hb.Basketball_sfc_ba()
        if aa == 1:
            hb.Basketball_sfc_bas(2)
            hb1.confirm_match()  ###点击已选择N场赛事
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_choosenumber_eight_case(self):
        """验证选号页面点击8场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击胜分差玩法
        aa=hb.Basketball_sfc_nus_X(8)####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_choosenumber_nine_case(self):
        """验证选号页面点击9场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(9) ####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_emptying(self):
        """验证选号页面清空按钮功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  #点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa>0:
            hb.Emptying()##点击清除
            hb.confirm_match()  ###点击已选N场比赛
            hb.Basketball_sfc_nus_X(5)  ###随机点击5场比赛
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Add_event(self):
        """验证添加/编辑赛事按钮，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = HaobcConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.edit_event()  ###点击编辑/添加赛事
            mul = hb.Play_fb()  ###读取文本
            self.assertEqual('玩\n法', mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_N_del(self):
        """验证删除赛事X按钮，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            a=hc1.NN()###读取删除前有多少个X按钮
            hc1.N_del(1)##点击第1场赛事的X按钮
            a1=hc1.NN()###读取删除后有多少个X按钮
            self.assertEqual(a-1,a1)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Pf_del_icon(self):
        """验证删除选择的全部赛事图标，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
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
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Times_input(self):
        """验证修改倍数输入框功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            mul=hc2.Lottery_dgp()###获取倍数
            self.assertEqual('共288元',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_less(self):
        """验证修改倍数 - 功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            hc1.Btn_less()####点击倍数-
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共192元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_add(self):
        """验证修改倍数 +功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            hc1.Btn_add()####点击倍数+
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共384元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_ten(self):
        """验证10倍按钮功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(10)####点击2倍
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共960元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_twenty(self):
        """验证20倍按钮功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(20)####点击20倍
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共1920元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_fifty(self):
        """验证50倍按钮功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(50)####点击50倍
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共4800元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_eighty(self):
        """验证80倍按钮功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(80)####点击80倍
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共7680元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_hundred(self):
        """验证100倍按钮功能，支付流程"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1 = PaintBallChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(100)####点击100倍
            mul = hc2.Lottery_dgp()  ###获取倍数
            self.assertEqual('共9600元', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_play_instruction_open_close_case(self):########mj20171215
        '''在投注选号页面，点击右上角玩法说明，可以打开和关闭'''
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1= PaintBallChooseNumber_leyou(self.driver)
        l = Login_leyou(self.driver)
        t = There_D_choosenumber_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.single_basketball_link()  ##点击竞篮单关
        hb1.three_clock()#点击右上角的。。。
        hb.Play_instruction()  # 点击玩法说明
        t.There_D_know()  # 点击我知道了

    def test_immediately_reture_homepage(self):
        '''在投注选号页面，点击右上角即时比分，可以打开并返回首页'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        l = Login_leyou(self.driver)
        t = There_D_choosenumber_leyou(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_basketball_link()  ##点击竞篮单关
        t.Instruct()  # 点击右上角的。。。
        pbcn.immediately()  # 点击即时比分
        pbcn.immediately_page_return_homepage()  # 点击返回首页

    def test_immediately_sorce_lottery_case(self):
        '''在投注选号页面，点击右上角即时比分，打开赛事分析数据，点击页面下方的投注竞彩足球按钮，页面跳转到选号页，选择两场比赛，提交订单'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        l = Login_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        t = There_D_choosenumber_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_basketball_link()  ##点击竞篮单关
        t.Instruct()  # 点击右上角的。。。
        pbcn.immediately()#点击即时比分
        aa=pbcn.enter_analysis_page()#点击进入赛事分析
        if aa ==1:
            hb.Race_basketball()#点击【投注竞彩蓝球】
            aa = hb.Basketball_mix_nus_X(2)  ###随机点击8场比赛
            if aa > 0:
                hb.confirm_match()  ###点击已选N场比赛
                hc.submit_order_to_station_owner_button()  ####点击提交给站主
                hc.confirm_and_pay_button()  # 点击确认支付
                text1 = sos.submit_order_success()  #获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)

    def test_Event_analysis_data_case(self):
        """竞蓝选号页，点击对阵左边下拉三角，展开赛事分析数据，点击页面下方的投注竞彩篮球按钮，页面跳转到选号页"""
        ha = HomePage_leyou(self.driver)
        hb=PaintBallChooseNumber_leyou(self.driver)
        hb1 = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd=SubmitOrderSuccess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login_leyou()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.single_basketball_link()  ##点击竞篮单关
        a=hb1.Event_analysis_data()##点击赛事向下箭头
        if a==1:
            hb1.Event_analysis_data_click()###点击数据分析
            hb1.Race_basketball()  # 点击【投注竞彩蓝球】
            hb1.Basketball_mix_nus_X(2)  ###随机点击8场比赛
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_jxks_play_case(self):
        """验证玩法"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hb1=SingleFootChooseNumber_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ###点击玩法
        hb.Play_mix()###点击混合投注
        a=hb1.Play_dgp_text()###读取显示的玩法文本
        self.assertEqual('混合投注',a)
        hb.Play_f()  ###点击玩法
        hb.Play_sf()  ###点击胜负
        b= hb1.Play_dgp_text()  ###读取显示的玩法文本
        self.assertEqual('胜负', b)
        hb.Play_f()  ###点击玩法
        hb.Play_rfsf()  ###点击让分胜负
        c= hb1.Play_dgp_text()  ###读取显示的玩法文本
        self.assertEqual('让分胜负', c)
        hb.Play_f()  ###点击玩法
        hb.Play_sfc()  ###点击让胜分差
        d= hb1.Play_dgp_text()  ###读取显示的玩法文本
        self.assertEqual('胜分差', d)
        hb.Play_f()  ###点击玩法
        hb.Play_dxf()  ###点击大小分
        e = hb1.Play_dgp_text()  ###读取显示的玩法文本
        self.assertEqual('大小分', e)

    def test_four_note_Times_input_one(self):
        """任选四场比赛，在投注确认页面，修改倍数为1倍"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(1)#####修改倍数为3
            mul=hc2.Lottery_dgp()###获取倍数
            self.assertEqual('共96元',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_eight_note_Times_input(self):
        """任选8场比赛，在投注确认页面，修改倍数为10000倍"""
        ha = HomePage_leyou(self.driver)
        hb = HaobcChooseNumber_leyou(self.driver)
        hc2 = SingleFootConfirmLottery_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(8)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(10000)#####修改倍数为3
            mul=hc2.Lottery_dgp()###获取倍数
            a=24*aa*10000
            self.assertEqual('共%d元'%a,mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_leyou()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_delete_one_event_case(self):###BUG修复中
        """验证单个删除赛事X按钮，流程测试"""
        ha = HomePage_leyou(self.driver)
        hb = PaintBallChooseNumber_leyou(self.driver)
        hb1 = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = SubmitOrderSuccess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login_leyou()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_sfc_nus_X(3)  ###随机点击4场比赛
        if aa == 3:
            hb.confirm_match()  ###点击已选N场比赛
            a = hc1.NN()  ###读取删除前有多少个X按钮
            hc1.N_del(1)  ##点击删除第一场赛事
            a1 =hc1.NN()  ###读取删除后有多少个X按钮
            self.assertEqual(a - 1, a1)
            hc.submit_order_to_station_owner_button()  # 提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_seven_color_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能,取消"""
        ha = HomePage_leyou(self.driver)
        hb = PaintBallChooseNumber_leyou(self.driver)
        hb1 = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_sfc_nus_X(3)  ###随机点击4场比赛
        if aa==3:
            hb.confirm_match()  ###点击已选N场比赛
            hc.delete_all_num_button()  ###点击清除所有选号
            hc.cancel_delete_button()  # 点击取消
            mur=hc.confirm_num_page_text()
            self.assertEqual('提交订单给站主',mur)

    def test_seven_color_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage_leyou(self.driver)
        hb = PaintBallChooseNumber_leyou(self.driver)
        hb1 = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_sfc_nus_X(3)  ###随机点击4场比赛
        if aa == 3:
            hb.confirm_match()  ###点击已选N场比赛
            hc.delete_all_num_button()  ###点击清除所有选号
            mur = hb2.Clear()
            self.assertEqual('清空', mur)

    def test_seven_color_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号，点击确定"""
        ha = HomePage_leyou(self.driver)
        hb = PaintBallChooseNumber_leyou(self.driver)
        hb1 = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hb2 = There_D_choosenumber_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_sfc_nus_X(3)  ###随机点击4场比赛
        if aa == 3:
            hb.confirm_match()  ###点击已选N场比赛
            hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur = hb.Play_fb()
        self.assertEqual('玩\n法', mur)

    def test_continue_toggle_play_case(self):
        """胜负玩法，点击编辑赛事，回到选号选号页面，切换玩法为混合投注"""
        ha = HomePage_leyou(self.driver)
        hb = PaintBallChooseNumber_leyou(self.driver)
        hb1 = HaobcChooseNumber_leyou(self.driver)
        hc = ConfirmLottery_leyou(self.driver)
        hc1 = PaintBallConfirm_leyou(self.driver)
        hc2 = HaobcConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hd = SubmitOrderSuccess_leyou(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login_leyou()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.single_basketball_link()  ##点击竞篮单关
        hb.Play_f()  # 选择玩法
        hb1.Play_sf()  # 选择胜负
        aa = hb1.sf_choose(2)  # 选择比赛
        if aa == 2:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.edit_event()  ###点击编辑/添加赛事
            hb.Play_f()  # 选择玩法
            hb.Play_mix()  ###点击混合投注
            aa = hb1.Basketball_sfc_nus_X(2)  ###随机点击4场比赛
            if aa == 2:
                hb.confirm_match()  ###点击已选N场比赛
                hc.submit_order_to_station_owner_button()  # 提交订单给站主
                hc.confirm_and_pay_button()  # 点击确认支付
                text1 = hd.submit_order_success()  # 获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)

