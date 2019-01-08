from time import sleep

from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.login import Login
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm
class PaintBall_bf_case(MyTest):
    """竞彩足球比分"""
    def test_Play_bf_choosnumber(self):
        """验证比分玩法赛事结果功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bf()  # 点击展开投注
        if aa == 1:
            hb.Football_bfs(8)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_choosenumber_too_case(self):
        """验证选号页面点击2场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bf_nus_too()  ####点击2场赛事
        if aa == 1:
            mul = hb.Text_confirm_loc()
            self.assertEqual('已选2场比赛', mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_choosenumber_eight_case(self):
        """验证选号页面点击8场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ###点击竞彩足球
        hb.Play_f()  ####点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(8)  ####点击8场赛事
        if aa > 1:
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_choosenumber_nine_case(self):
        """验证选号页面点击9场赛事，支付流程，若运行不成功，查看是否点击重复的场次"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ###点击竞彩足球
        hb.Play_f()  ####点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(9)  ####点击9场赛事
        if aa > 1:
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Add_event(self):
        """验证添加/编辑赛事按钮，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Add_event()  ###点击编辑/添加赛事
            mul = hb.Play_fb()  ###读取文本
            self.assertEqual('玩\n法', mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_N_del(self):
        """验证删除赛事X按钮，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            a = hc1.NN()  ###读取删除前有多少个X按钮
            hc1.Del_n(1)  ##点击第1场赛事的X按钮
            a1 = hc1.NN()  ###读取删除后有多少个X按钮
            self.assertEqual(a - 1, a1)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Pf_del_icon(self):
        """验证删除选择的全部赛事图标，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.down_bf()
            hc1.Pf_del_icon()
            hc.confirm_delete_button()
            hb.top_more()
            hb.Football_bfs_X(4)
            mul = hb.Text_confirm_loc()
            self.assertEqual('已选%d场比赛' % aa, mul)
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Times_input(self):
        """验证修改倍数输入框功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            mul = hc1.Times_display()  ###获取倍数
            self.assertEqual('3', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Btn_less(self):
        """验证修改倍数 - 功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            hc1.Btn_less()  ####点击倍数-
            mul = hc1.Times_display()  ###获取倍数
            self.assertEqual('2', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Btn_add(self):
        """验证修改倍数 +功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(2)  ###随机点击2场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input(3)  #####修改倍数为3
            hc1.Btn_add()  ####点击倍数+
            mul = hc1.Times_display()  ###获取倍数
            self.assertEqual('4', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Btn_ten(self):
        """验证10倍按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(2)  ###随机点击2场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Times_input_click()  #####点击倍数输入框
            hc1.Times_number(10)  ####点击10倍
            mul = hc1.Times_display()  ###获取倍数
            self.assertEqual('10', mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_Pf_bouns(self):
        """验证过关功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hc1 = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(8)  ###随机点击8场比赛
        if aa > 0:
            hb.confirm_match()  ###点击已选N场比赛
            hc1.Pf_pass()
            mul = hc1.Pf_pass_nu()  ###读取点击的过关方式
            a = hc1.Pf_pass_text()  ###读取展示的过关方式
            self.assertEqual(a, mul)
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def test_Play_bf_emptying(self):
        """验证选号页面清空按钮功能，支付流程"""
        ha = HomePage(self.driver)
        hb = PaintBallChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.paintball_link()  ##点击竞彩足球
        hb.Play_f()  ###点击玩法
        hb.Play_bf()  ##点击比分
        aa = hb.Football_bfs_X(4)  ###随机点击4场比赛
        if aa > 0:
            hb.Emptying()
            hb.confirm_match()  ###点击已选N场比赛
            hb.Football_bfs_X(4)  ###随机点击4场比赛
            hb.confirm_match()  ###点击已选N场比赛
            hc.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            hc.submit_order_to_station_owner_button()  # 点击提交给站主
            hc.confirm_and_pay_button()  # 点击确认支付

    def optimize_award_case(self):
        '''验证奖金优化流程测试'''
        hp = HomePage(self.driver)
        pbcn = PaintBallChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击胜平负
        aa = pbcn.spf_choose(4)  ###随机点击4场比赛
        if aa > 0:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_bouns()##点击奖金优化
            text=pbc.optimize_award()#获取奖金优化页上方文本
            self.assertIn("平均优化购买",text)
            cl.submit_order_to_station_owner_button()  ####点击提交给站主
            # hl.new_user_login_tab()  # 点击新登录
            hl.login()  # 输入账号，密码
            cl.submit_order_to_station_owner_button()  # 点击提交给站主
            cl.confirm_and_pay_button()  # 点击确认支付