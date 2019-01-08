from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber_lelun
from element_operate.homepage import HomePage_lelun
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.login import Login_lelun
from element_operate.Haobc.haobc_confirm import HaobcConfirm_lelun
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm_lelun
class BaskrtBall_sfc_case(MyTest):
    """竞篮，胜分差玩法"""
    def test_Play_sfc_choosnumber(self):
        """验证让分胜负玩法赛事结果功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击让分胜负玩法
        aa=hb.Basketball_sfc_ba()
        if aa==1:
            hb.Basketball_sfc_bas(6)
            hb1.confirm_match()  ###点击已选择N场赛事
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_choosenumber_too_case(self):
        """验证选号页面点击2场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击点击胜分差玩法
        aa=hb.Basketball_sfc_nus_too()####随机点击2场赛事
        if aa == 1:
            mul=hb.Text_confirm_loc()
            self.assertEqual('已选2场比赛',mul)
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_choosenumber_eight_case(self):
        """验证选号页面点击8场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击胜分差玩法
        aa=hb.Basketball_sfc_nus_X(8)####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_choosenumber_nine_case(self):
        """验证选号页面点击9场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  ##点击点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(9) ####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_emptying(self):
        """验证选号页面清空按钮功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
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
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Add_event(self):
        """验证添加/编辑赛事按钮，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = HaobcConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
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
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_N_del(self):
        """验证删除赛事X按钮，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            a=hc1.A_nn()###读取删除前有多少个X按钮
            hc1.Del_n(1)##点击第1场赛事的X按钮
            a1=hc1.A_nn()###读取删除后有多少个X按钮
            self.assertEqual(a-1,a1)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Pf_del_icon(self):
        """验证删除选择的全部赛事图标，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
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
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Times_input(self):
        """验证修改倍数输入框功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('3',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_less(self):
        """验证修改倍数 - 功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            hc1.Btn_less()####点击倍数-
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('2',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_add(self):
        """验证修改倍数 +功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            hc1.Btn_add()####点击倍数+
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('4',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_ten(self):
        """验证10倍按钮功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(10)####点击2倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('10',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_twenty(self):
        """验证20倍按钮功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(20)####点击20倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('20',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_fifty(self):
        """验证50倍按钮功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(50)####点击50倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('50',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_eighty(self):
        """验证80倍按钮功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(80)####点击80倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('80',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Btn_hundred(self):
        """验证100倍按钮功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(100)####点击100倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('100',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_sfc_Pf_bouns(self):
        """验证过关功能，支付流程"""
        ha = HomePage_lelun(self.driver)
        hb = HaobcChooseNumber_lelun(self.driver)
        hb1 = PaintBallChooseNumber_lelun(self.driver)
        hc = ConfirmLottery_lelun(self.driver)
        hc1 = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_sfc()  # 点击胜分差玩法
        aa = hb.Basketball_sfc_nus_X(4)  ###随机点击8场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Pf_pass()
            mul=hc1.Pf_pass_nu()###读取点击的过关方式
            a=hc1.Pf_pass_text()###读取展示的过关方式
            self.assertEqual(a,mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login_lelun()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

