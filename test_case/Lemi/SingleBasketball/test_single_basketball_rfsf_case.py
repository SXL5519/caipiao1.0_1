from time import sleep
from element_operate.SingleBasketball.single_basketball_choosenumber import SingleBasketballChooseNumber
from element_operate.Haobc.haobc_choose_number import HaobcChooseNumber
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.login import Login
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm
from element_operate.Haobc.haobc_confirm import HaobcConfirm

#####竞篮单关让分胜负玩法测试用例###----mj20171123
class single_basketball_rfsf_Case(MyTest):
    '''竞篮单关让分胜负玩法流程测试'''
    def test_single_basketball_rfsf_1_case(self):
        '''选择一场比赛流程测试'''
        ###点击进入竞篮单关选号页面###
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hc = HaobcConfirm(self.driver)
        cl = ConfirmLottery(self.driver)
        l = Login(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分让分胜负
        aa = sbcn.jldg_sf_choose(1)  # 选择比赛
        if aa > 0:
            hcn.confirm_match()  # 确认所选场次
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
            l.login()  # 点击登录
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
            cl.confirm_and_pay_button()  # 确认支付
    def test_single_basketball_rfsf_2_case(self):
        '''选择两场比赛流程测试'''
        ###点击进入竞篮单关选号页面###
        hp=HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn=SingleBasketballChooseNumber(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hc = HaobcConfirm(self.driver)
        cl = ConfirmLottery(self.driver)
        l=Login(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()##点击竞篮单关
        hcn.Play_f()#选择玩法
        hcn.Play_rfsf()#选择让分胜负
        aa=sbcn.jldg_sf_choose(2)#选择比赛
        if aa > 0:
            hcn.confirm_match()#确认所选场次
            cl.submit_order_to_station_owner_button()#提交订单给站主
            l.login()#点击登录
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
            cl.confirm_and_pay_button()#确认支付

    def test_single_basketball_rfsf_8_case(self):
        '''选择8场比赛，流程测试'''
        ###点击进入双色球选号页面###
        hp=HomePage(self.driver)
        hcn=HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()##点击竞篮单关单关
        hcn.Play_f()#选择玩法
        hcn.Play_rfsf()#选择让分胜负
        aa=sbcn.jldg_sf_choose(8)#选择比赛
        if aa > 0:
            hcn.confirm_match()#确认所选场次
            cl.submit_order_to_station_owner_button()#提交订单给站主
    def test_single_basketball_rfsf_9_case(self):
        '''选择九场比赛，获取“最大场次限制8场”提示，测试流程'''
        ###点击进入双色球选号页面###
        hp=HomePage(self.driver)
        hcn=HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()##点击竞篮单关
        hcn.Play_f()#选择玩法
        hcn.Play_rfsf()#选择让分胜负
        aa=sbcn.jldg_sf_choose(9)  # 选择比赛
        if aa!=0 and aa!=3:
            try:
                hcn.know()
            except ElementNotVisibleException:
                print("当前场次小于8场")
            hcn.confirm_match()#确认赛事

    def test_single_basketball_rfsf_10_case(self):
        '''选择一天中所有比赛场次流程测试'''
        ###点击进入双色球选号页面###
        hp=HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()##点击竞篮单关
        hcn.Play_f()#选择玩法
        hcn.Play_rfsf()#选择让分胜负
        sbcn.jldg_sf_choose(10)#选择比赛

    def test_single_basketball_rfsf_click_all(self):
        '''点击页面展示所有比赛，测试流程'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        sbcn.jldg_click_all()  # 选择比赛
    def test_single_basketball_rfsf_choose_num_clear_button_case(self):
        '''选号页面清除所选比赛流程测试'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        pbc = PaintBallConfirm(self.driver)
        cl = ConfirmLottery(self.driver)
        l = Login(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(2)  # 选择比赛
        if aa > 0:
            hcn.clear_button()#点击清除按钮
            sbcn.jldg_sf_choose(3)#选择3场比赛
            hcn.confirm_match()#确认所选场次

    def test_single_basketball_rfsf_throw10_case(self):
        '''选择投10倍流程测试'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        l = Login(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(2)  # 选择比赛
        if aa==2:
            hcn.confirm_match()#点击确认赛事
            pbc.Times_input_click()#点击投注倍数
            pbc.throw_times(10)#点击投注10倍
            text = cl.throw_time_text()#获取投注倍数文本
            print(text)
            self.assertIn('10', text)

    def test_single_basketball_rfsf_throw_add_btn_case(self):
        '''点击投注倍数的+按钮流程测试'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        l = Login(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(2)  # 选择比赛
        if aa == 2:
            hcn.confirm_match()  # 点击确认赛事
            pbc.Btn_add()#点击+按钮
            text=cl.throw_time_text()
            self.assertIn('6',text)
    def test_single_basketball_rfsf_throw_sub_btn_case(self):
        '''点击投注倍数的-按钮流程测试'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        l = Login(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(2)  # 选择比赛
        if aa == 2:
            hcn.confirm_match()  # 点击确认赛事
            pbc.Btn_less()#点击-按钮
            text=cl.throw_time_text()
            self.assertIn('4',text)
    def test_single_basketball_rfsf_input_throw_times_case(self):
        '''输入投注3倍测试流程'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(2)  # 选择比赛
        if aa == 2:
            hcn.confirm_match()  # 点击确认赛事
            pbc.Times_input_click()#点击投注倍数输入框
            pbc.Times_input(3)#输入投注3倍
            text = cl.throw_time_text()
            self.assertIn('3',text)
    def test_single_basketball_rfsf_throw_way_case(self):
        '''改变默认投注过关方式流程测试'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hp.open()
        hp = HomePage(self.driver)
        hp.Moveable_float_close()
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(8)  # 选择比赛
        if aa == 2:
            hcn.confirm_match()  # 点击确认赛事
            pbc.Pf_pass()#点击过关方式
            mul = pbc.Pf_pass_nu()  ###读取点击的过关方式
            a = pbc.Pf_pass_text()  ###读取展示的过关方式
            self.assertEqual(a, mul)
    def test_single_basketball_rfsf_edit_event_case(self):
        '''验证投注确认页编辑赛事按钮测试流程'''
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        hc = HaobcConfirm(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        l = Login(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞篮单关
        hcn.Play_f()  # 选择玩法
        hcn.Play_rfsf()  # 选择让分胜负
        aa = sbcn.jldg_sf_choose(1)  # 选择比赛
        if aa == 2:
            hcn.confirm_match()  # 点击确认赛事
            hc.edit_event()#点击编辑赛事
            bb=sbcn.jldg_sf_edit_event(1)#选择1场比赛
            if bb == 1:
                print("暂无赛事，已返回")
                ###返回首页的检查点
            if bb == 2:
                hcn.confirm_match()  # 点击确认赛事
                #投注页获取注数的检查点，应该为2注1倍
            if bb == 0:#只有一场的时候
                print("我已进入竞足单关")
    def test_single_basketball_rfsf_delete_one_event_case(self):
        """验证单个删除赛事X按钮，流程测试"""
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞彩足球
        hcn.Play_f()  ###点击玩法
        hcn.Play_rfsf()  ##点击让分胜负
        aa = sbcn.jldg_sf_choose(3)  ###随机点击3场比赛
        sleep(3)
        if aa == 2:
            hcn.confirm_match()  ###点击确认赛事
            a = pbc.NN()  ###读取删除前有多少个X按钮
            pbc.N_del(1)  ##点击删除第一场赛事
            a1 =pbc.NN()  ###读取删除后有多少个X按钮
            self.assertEqual(a - 1, a1)
    def test_single_basketball_rfsf_delete_all_event_case(self):
        """验证删除选择的全部赛事图标，流程测试"""
        hp = HomePage(self.driver)
        hcn = HaobcChooseNumber(self.driver)
        sbcn = SingleBasketballChooseNumber(self.driver)
        cl = ConfirmLottery(self.driver)
        pbc = PaintBallConfirm(self.driver)
        hl = Login(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_basketball_link()  ##点击竞彩足球
        hcn.Play_f()  ###点击玩法
        hcn.Play_rfsf()  ##点击让分胜负
        aa = sbcn.jldg_sf_choose(2)  ###随机点击2场比赛
        if aa > 0:
            hcn.confirm_match()  ###点击确认赛事
            pbc.Pf_del_icon()#点击删除图标
            cl.confirm_delete_button()#点击确认删除按钮
            sbcn.jldg_sf_choose(4)#选择4场比赛
            hcn.confirm_match()  ###点击确认赛事
            text = pbc.Pf_pass_text()  # 获取过关方式文本
            self.assertIn("4串1", text)