from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.login import Login
from element_operate.Haobc.haobc_confirm import HaobcConfirm
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm
from element_operate.SingleFoot.single_foot_choose_number import SingleFootChooseNumber
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery


class BaskrtBall_mix_case(MyTest):
    """竞彩篮球，混合玩法"""
    def test_Play_mix_choosnumber(self):
        """验证混合玩法赛事结果功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1=PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()##点击混合玩法
        aa=hb.Basketball_mix_ba()###点击页面赛事结果
        if aa==1:
            hb.Basketball_mix_bas(6)##随机选择6场赛事结果
            hb1.confirm_match()###点击已选择N场赛事
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_choosenumber_too_case(self):
        """验证选号页面点击2场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa=hb.Basketball_mix_nus_too()####随机点击2场赛事
        if aa == 1:
            mul=hb.Text_confirm_loc()
            self.assertEqual('已选2场比赛',mul)
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_choosenumber_eight_case(self):
        """验证选号页面点击8场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa=hb.Basketball_mix_nus_X(8)####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付
    ##
    def test_Play_mix_choosenumber_nine_case(self):
        """验证选号页面点击9场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(9)  ####随机点击8场赛事
        if aa>0:
            hb.confirm_match()###点击已选N场比赛
            hc.submit_order_to_station_owner_button()####点击提交给站主
            #hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()# 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_More_case(self):
        """验证选号页面点击展开更多，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa=hb.More_choosenumber()###点击展开更多里的按钮
        if aa==1:
            hb.More_choosenumbers(4)  ####随机点击n场赛事展开更多
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_emptying(self):
        """验证选号页面清空按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa>0:
            hb.Emptying()##点击清除
            hb.confirm_match()  ###点击已选N场比赛
            hb.Basketball_mix_nus_X(5)  ###随机点击5场比赛
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Add_event(self):
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
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa=hb.Basketball_mix_nus_X(4)###随机点击4场比赛
        if aa>0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.edit_event()###点击编辑/添加赛事
            mul=hb.Play_fb()###读取文本
            self.assertEqual('玩\n法',mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_N_del(self):
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
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            a=hc1.A_nn()###读取删除前有多少个X按钮
            hc1.Del_n(1)##点击第1场赛事的X按钮
            a1=hc1.A_nn()###读取删除后有多少个X按钮
            self.assertEqual(a-1,a1)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Pf_del_icon(self):
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
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa>0:
            hb.confirm_match()  ###点击已选N场比赛
            #hc1.down_bf()
            hc1.Pf_del_icon()
            hc.confirm_delete_button()
            hb.Basketball_mix_nus_X(4)
            mul=hb.Text_confirm_loc()
            self.assertEqual('已选%d场比赛'%aa,mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Times_input(self):
        """验证修改倍数输入框功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('3',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_less(self):
        """验证修改倍数 - 功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)#####修改倍数为3
            hc1.Btn_less()####点击倍数-
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('2',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_add(self):
        """验证修改倍数 +功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            hc1.Btn_add()####点击倍数+
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('4',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_ten(self):
        """验证10倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(10)####点击2倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('10',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_twenty(self):
        """验证20倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(20)####点击20倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('20',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_fifty(self):
        """验证50倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(50)####点击50倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('50',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_eighty(self):
        """验证80倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(80)####点击80倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('80',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Btn_hundred(self):
        """验证100倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(2)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(100)####点击100倍
            mul=hc1.Times_display()###获取倍数
            self.assertEqual('100',mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_mix_Pf_bouns(self):
        """验证过关功能，支付流程"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1 = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  ##点击竞彩蓝球
        hb.Play_f()  ####点击玩法
        hb.Play_mix()  ##点击混合玩法
        aa = hb.Basketball_mix_nus_X(8)  ###随机点击8场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Pf_pass()
            mul=hc1.Pf_pass_nu()###读取点击的过关方式
            a=hc1.Pf_pass_text()###读取展示的过关方式
            self.assertEqual(a,mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付



    def test_jxks_play_case(self):
        """验证玩法"""
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hb1=SingleFootChooseNumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()#点击竞彩蓝球
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

    def test_play_instruction_open_close_case(self):
        '''在投注选号页面，点击右上角玩法说明，可以打开和关闭'''
        ha = HomePage(self.driver)
        hb = HaobcChooseNumber(self.driver)
        pbcn = PaintBallChooseNumber(self.driver)
        l = Login(self.driver)
        t = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()#点击竞彩蓝球
        t.Instruct()#点击右上角的。。。
        hb.Play_instruction()#点击玩法说明
        t.There_D_know()#点击我知道了

    def test_immediately_reture_homepage(self):
        '''在投注选号页面，点击右上角即时比分，可以打开并返回首页'''
        hp = HomePage(self.driver)
        pbcn = PaintBallChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        l = Login(self.driver)
        t = There_D_choosenumber(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.haobc_link()#点击竞彩蓝球
        t.Instruct()  # 点击右上角的。。。
        pbcn.immediately()  # 点击即时比分
        pbcn.immediately_page_return_homepage()#点击返回首页

    def test_immediately_sorce_lottery_case(self):
        '''在投注选号页面，点击右上角即时比分，打开赛事分析数据，点击页面下方的投注竞彩足球按钮，页面跳转到选号页，选择两场比赛，提交订单'''
        hp = HomePage(self.driver)
        pbcn = PaintBallChooseNumber(self.driver)
        l = Login(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        t = There_D_choosenumber(self.driver)
        hb = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.haobc_link()#点击竞彩蓝球
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
        ha = HomePage(self.driver)
        hb=PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hd=SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
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

    def test_patintball_rqspf_change_throw_way_case(self):
        '''选号页面，任意选择三场对阵，进入投注确认页，选择串关为3串1、2串1组合，提交订单'''
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()###点击混合投注
        aa = hb1.Basketball_mix_nus_X(3)  # 选择比赛
        if aa == 3:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Pf_pass()  # 点击过关方式
            hc1.choose_all_pass_nu()  ###选中所有的过关方式
            a = hc1.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1',a)
            hc.submit_order_to_station_owner_button()#点击提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_four_note_a_times_case(self):
        """四场比赛,修改倍数为1倍"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(4)  # 选择比赛
        if aa == 4:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            mur1 = hc2.Tnote_nu()  ##读取注数
            self.assertEqual('1', mur1)
            mur = hc2.Tmultiple_show()  ##读取倍数
            self.assertEqual('3', mur)

    def test_paintball_rqspf_chage_throw_all_way(self):
        '''选号页面，任意选择六场对阵，进入投注确认页，选择串关为6串1、5串1、4串1，3串1，2串1组合，提交订单'''
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(6)  # 选择比赛
        if aa == 6:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Pf_pass()  # 点击过关方式
            hc1.choose_all_pass_nu()  ###选中所有的过关方式
            a =hc1.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1,4串1,5串1,6串1', a)
            hc.submit_order_to_station_owner_button()  # 点击提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 =hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_test_paintball_rqspf_option7chage_throw_all_way(self):
        '''选号页面，任意选择七场对阵，选择串关为6串1、5串1、2串1组合，提交订单'''
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(7)  # 选择比赛
        if aa == 7:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Pf_pass()  # 点击过关方式
            hc1.choose_all_pass_nu()  ###选中所有的过关方式
            a = hc1.Pf_pass_text()  ###读取选中的过关方式
            a = hc1.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1,4串1,5串1,6串1,7串1', a)
            hc.submit_order_to_station_owner_button()  # 点击提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_patintball_rqspf_input10000times_case(self):##mj20171213
        '''选号页面，选择八场对阵，增加倍数为10000倍，提交订单'''
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(8)  # 选择比赛
        if aa == 8:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  # 点击投注倍数
            hc1.Times_input(10000)#输入投注10000倍
            hc.submit_order_to_station_owner_button()  # 提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_delete_one_event_case(self):
        """验证单个删除赛事X按钮，流程测试"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(3)  # 选择比赛
        if aa == 3:
            hb.confirm_match()  ###点击已选N场比赛
            a = hc1.A_nn()  ###读取删除前有多少个X按钮
            hc1.Del_n(1)  ##点击删除第一场赛事
            a1 =hc1.A_nn()  ###读取删除后有多少个X按钮
            self.assertEqual(a - 1, a1)
            hc.submit_order_to_station_owner_button()  # 提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_delete_double_event_case(self):
        """选择两场赛事，验证单个删除多场赛事X按钮，流程测试"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(2)  # 选择比赛
        if aa == 2:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.A_nn()  ###读取删除前有多少个X按钮
            hc1.Del_n(1)  ##点击删除第一场赛事
            hb1.Basketball_mix_nus_X(3)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  # 提交订单给站主
            hc.confirm_and_pay_button()  # 点击确认支付
            text1 = hd.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)

    def test_seven_color_Del_all_nu_cancel_case(self):
        """验证确认投注页面，点击删除选号图标功能,取消"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(2)  # 选择比赛
        if aa==2:
            hb.confirm_match()  ###点击已选N场比赛
            hc.delete_all_num_button()  ###点击清除所有选号
            hc.cancel_delete_button()  # 点击取消
            mur=hc.confirm_num_page_text()
            self.assertEqual('提交订单给站主',mur)

    def test_seven_color_Del_all_nu_case(self):
        """验证确认投注页面，点击删除选号图标功能"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hb2 = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(2)  # 选择比赛
        if aa == 2:
            hb.confirm_match()  ###点击已选N场比赛
            hc.delete_all_num_button()  ###点击清除所有选号
            mur = hb2.Clear()
            self.assertEqual('清空', mur)

    def test_seven_color_Del_all_nu_ok_case(self):
        """验证确认投注页面，点击删除选号，点击确定"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hb2 = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb.Play_mix()  ###点击混合投注
        aa = hb1.Basketball_mix_nus_X(2)  # 选择比赛
        if aa == 2:
            hb.confirm_match()  ###点击已选N场比赛
            hc.delete_all_num_button()  ###点击清除所有选号
        hc.confirm_delete_button()  # 点击确定
        mur = hb.Play_fb()
        self.assertEqual('玩\n法', mur)


    def test_continue_toggle_play_case(self):
        """胜负玩法，点击编辑赛事，回到选号选号页面，切换玩法为混合投注"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hb1 = HaobcChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hc2 = HaobcConfirm(self.driver)
        hl = Login(self.driver)
        hd = SubmitOrderSuccess(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.My_lottery_ticket()  # 点击我的彩票
        hl.login()  # 点击登录
        ha.homepage_link()  # 点击首页
        ha.haobc_link()  # 点击竞彩蓝球
        hb.Play_f()  # 选择玩法
        hb1.Play_sf()#选择胜负
        aa=hb1.sf_choose(2)#选择比赛
        if aa == 2:
            hb.confirm_match()  ###点击已选N场比赛
            hc2.edit_event()###点击编辑/添加赛事
            hb.Play_f()  # 选择玩法
            hb.Play_mix()  ###点击混合投注
            aa = hb1.Basketball_mix_nus_X(2)  # 选择比赛
            if aa == 2:
                hb.confirm_match()  ###点击已选N场比赛
                hc.submit_order_to_station_owner_button()  # 提交订单给站主
                hc.confirm_and_pay_button()  # 点击确认支付
                text1 = hd.submit_order_success()  # 获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)