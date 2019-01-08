from time import sleep
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lexiu
from element_operate.homepage import HomePage_lexiu
from test_case.Base.mytest import MyTest
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
from element_operate.login import Login_lexiu
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm_lexiu
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lexiu
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lexiu
from element_operate.UnionLotto.order_details import OrderDetails_lexiu
####竞彩足球让球胜平负玩法测试用例---mj20171114
class PaintBall_rqspf_Case(MyTest):

    """竞足让球胜平负玩法流程测试"""
    def test_paintball_rqspf_2_case(self):
        '''选择两场比赛流程测试'''
        ###点击进入双色球选号页面###
        hp=HomePage_lexiu(self.driver)
        pbcn=PaintBallChooseNumber_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        l=Login_lexiu(self.driver)
        hp.open()
        hp.paintball_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_rqspf()#选择让球胜平负
        aa=pbcn.rqspf_choose(2)#选择比赛
        if aa==2:
            pbcn.confirm_match()#确认所选场次
            cl.submit_order_to_station_owner_button()#提交订单给站主
            l.login_lexiu()#点击登录
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
            cl.confirm_and_pay_button()#确认支付

    def test_paintball_rqspf_8_case(self):
        '''选择8场比赛，流程测试'''
        ###点击进入双色球选号页面###
        hp=HomePage_lexiu(self.driver)
        pbcn=PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        hp.open()
        hp.paintball_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_rqspf()#选择让球胜平负
        aa=pbcn.rqspf_choose(8)#选择比赛
        if aa==2:
            pbcn.confirm_match()#确认所选场次
            cl.submit_order_to_station_owner_button()#提交订单给站主


    def test_paintball_rqspf_9_case(self):
        '''选择九场比赛，获取“最大场次限制8场”提示，测试流程'''
        ###点击进入双色球选号页面###
        hp=HomePage_lexiu(self.driver)
        pbcn=PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        hp.open()
        hp.paintball_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_rqspf()#选择让球胜平负
        aa=pbcn.rqspf_choose(9)  # 选择比赛
        if aa == 2:
            try:
                pbcn.know()
            except ElementNotVisibleException:
                print("当前场次小于8场")
            pbcn.confirm_match()  # 确认所选场次
        else:
            print("我返回了")

    def test_paintball_rqrqspf_10_case(self):
        '''选择一天中所有比赛场次流程测试'''
        ###点击进入双色球选号页面###
        hp=HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        hp.open()
        hp.paintball_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_rqspf()#选择让球胜平负
        pbcn.rqspf_choose(10)#选择比赛

    def test_paintball_rqspf_click_all(self):
        '''点击页面展示所有比赛，测试流程'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        hp.open()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        pbcn.rqspf_click_all()  # 选择比赛
    def test_choose_num_clear_button_case(self):
        '''选号页面清除所选比赛流程测试'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择比赛
        if aa==2:
            pbcn.clear_button()#点击清除按钮
            pbcn.rqspf_choose(3)#选择3场比赛
            pbcn.confirm_match()#确认所选场次
            text=pbc.Pf_pass_text()#获取过关方式文本
            self.assertIn("3串1",text)


    def test_throw50_case(self):
        '''选择投50倍流程测试'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Times_input_click()  # 点击投注倍数
            pbc.throw_times(50)  # 点击投注50倍
            text = cl.throw_time_text()
            self.assertIn('50', text)

    def test_throw_add_btn_case(self):
        '''点击投注倍数的+按钮流程测试'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Btn_add()#点击+按钮
            text=cl.throw_time_text()
            self.assertIn('6',text)
    def test_throw_sub_btn_case(self):
        '''点击投注倍数的-按钮流程测试'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Btn_less()#点击-按钮
            text=cl.throw_time_text()
            self.assertIn('4',text)
    def test_input_throw_times_case(self):
        '''输入投注3倍测试流程'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Times_input_click()#点击投注倍数输入框
            pbc.Times_input(3)#输入投注3倍
            text = cl.throw_time_text()
            self.assertIn('3',text)
    def test_throw_way_case(self):
        '''改变默认投注过关方式流程测试'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(8)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Pf_pass()#点击过关方式
            mul = pbc.Pf_pass_nu()  ###读取点击的过关方式
            a = pbc.Pf_pass_text()  ###读取展示的过关方式
            self.assertEqual(a, mul)
    def test_patintball_rqspf_change_throw_way(self):##20171214
        '''选号页面，任意选择三场对阵，进入投注确认页，选择串关为3串1、2串1组合，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(3)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Pf_pass()  # 点击过关方式
            pbc.choose_all_pass_nu()  ###选中所有的过关方式
            a = pbc.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1',a)
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_paintball_rqspf_chage_throw_all_way(self):
        '''选号页面，任意选择六场对阵，进入投注确认页，选择串关为6串1、5串1、4串1，3串1，2串1组合，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(6)  # 选择6场比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Pf_pass()  # 点击过关方式
            pbc.choose_all_pass_nu()  ###选中所有的过关方式
            a = pbc.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1,4串1,5串1,6串1', a)
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_test_paintball_rqspf_option7chage_throw_all_way(self):
        '''选号页面，任意选择七场对阵，选择串关为6串1、5串1、2串1组合，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(7)  # 选择7场比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Pf_pass()  # 点击过关方式
            pbc.choose_all_pass_nu()  ###选中所有的过关方式
            a = pbc.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1,4串1,5串1,6串1,7串1', a)
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_patintball_rqspf_input10000times_case(self):##mj20171213
        '''选号页面，选择八场对阵，增加倍数为10000倍，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(8)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 确认所选场次
            pbc.Times_input_click()  # 点击投注倍数
            pbc.Times_input(10000)#输入投注10000倍
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_edit_event_case(self):
        '''验证投注确认页编辑赛事按钮测试流程'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_rqspf()  # 选择让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Add_event()#点击编辑赛事
            pbcn.edit_event(1)#选择1场比赛
            pbcn.confirm_match()  # 点击确认赛事
            text = pbc.Pf_pass_text()  # 获取过关方式文本
            self.assertIn("3串1", text)
    def test_delete_one_event_case(self):
        """验证单个删除赛事X按钮，流程测试"""
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(3)  ###随机点击3场比赛
        sleep(3)
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            a = pbc.Dxf_nn()  ###读取删除前有多少个X按钮
            pbc.DXF_del_n(1)  ##点击删除第一场赛事
            a1 =pbc.Dxf_nn()  ###读取删除后有多少个X按钮
            self.assertEqual(a - 1, a1)
    def test_delete_double_event_case(self):
        """选择两场赛事，验证单个删除多场赛事X按钮，流程测试"""
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  ###随机点击2场比赛
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.NN()  ###读取删除前有多少个X按钮
            pbc.N_del(1)  ##点击删除第一场赛事
            pbcn.rqspf_choose(2)  ###随机点击2场比赛
    def test_delete_all_event_case(self):
        """验证删除选择的全部赛事图标，流程测试"""
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        hl = Login_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  ###随机点击2场比赛
        if aa > 0:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_del_icon()#点击删除图标
            cl.confirm_delete_button()#点击确认删除按钮
            pbcn.rqspf_choose(4)#选择4场比赛
            pbcn.confirm_match()  ###点击确认赛事
            text = pbc.Pf_pass_text()  # 获取过关方式文本
            self.assertIn("4串1", text)
    def test_optimize_award_default_case(self):#mj20171214
        '''选择三场对阵，进入投注确认页面，选择串关为3串1、2串1，点击奖金优化，进入奖金优化页面，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()#点击我的彩票
        l.login_lexiu()#点击登录
        hp.homepage_link()#点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(3)  ###随机点击3场比赛
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_pass()  # 点击过关方式
            pbc.choose_all_pass_nu()  ###选中所有的过关方式
            a = pbc.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1', a)
            pbc.Pf_bouns()##点击奖金优化
            pbc.submit_order()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            text1 = sos.submit_order_success()#获取提交订单成功文本
            self.assertEqual('订单提交成功',text1)
    def test_optimize_award_add_lottery_sum_case(self):
        '''选择四场对阵，进入投注确认页面，选择串关为4串1、3串1、2串1，点击奖金优化，进入奖金优化页面，增加投注金额，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(4)  ###随机点击4场比赛
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_pass()  # 点击过关方式
            pbc.choose_all_pass_nu()  ###选中所有的过关方式
            a = pbc.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1,4串1', a)
            pbc.Pf_bouns()  ##点击奖金优化
            pbc.optimize_add_money_input(200)  # 修改奖金优化金额
            pbc.submit_order()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            hp.Moveable_float_close()
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_optimize_award_add_lottery_sum_restore_case(self):
        '''选择五场对阵，点击奖金优化，进入奖金优化页面，增加投注金额，然后点击还原选项，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(5)  ###随机点击5场比赛
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_pass()  # 点击过关方式
            pbc.choose_all_pass_nu()  ###选中所有的过关方式
            a = pbc.Pf_pass_text()  ###读取选中的过关方式
            self.assertIn('2串1,3串1,4串1', a)
            pbc.Pf_bouns()  ##点击奖金优化
            mix_text1 = pbc.maximum_text()
            pbc.optimize_add_money_input(200)  # 修改奖金优化金额
            pbc.restroe_button()#点击还原选项按钮
            mix_text3 = pbc.maximum_text()
            print('third%s'%mix_text3)
            self.assertEqual(mix_text1,mix_text3)
            pbc.submit_order()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            hp.Moveable_float_close()
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_play_instruction_open_close_case(self):
        '''在投注选号页面，点击右上角玩法说明，可以打开和关闭'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        t = There_D_choosenumber_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        t.Instruct()#点击右上角的。。。
        pbcn.paintball_play_instruct()#点击玩法说明
        t.There_D_know()#点击我知道了

    def test_filter_button_case(self):
        '''在投注选号页面，点击筛选按钮，对所有的筛选项进行点击'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.filter_button()#点击筛选按钮
        pbcn.allccsel()#点击全选
        pbcn.noallccsel()#点击反选
        pbcn.fivecc()#点击五大联赛
        pbcn.findcc()#点击筛选banner的确定按钮
    def test_immediately_reture_homepage(self):
        '''在投注选号页面，点击右上角即时比分，可以打开并返回首页'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        t = There_D_choosenumber_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        t.Instruct()  # 点击右上角的。。。
        pbcn.immediately()  # 点击即时比分
        pbcn.immediately_page_return_homepage()#点击返回首页
    def test_immediately_sorce_lottery_case(self):
        '''在投注选号页面，点击右上角即时比分，打开赛事分析数据，点击页面下方的投注竞彩足球按钮，页面跳转到选号页，选择两场比赛，提交订单'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        t = There_D_choosenumber_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        t.Instruct()  # 点击右上角的。。。
        pbcn.immediately()#点击即时比分
        aa=pbcn.enter_analysis_page()#点击进入赛事分析
        if aa ==1:
            pbcn.lottery_jczq_button()#点击【投注竞彩足球】
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_rqspf()  ##点击让球胜平负
            aa = pbcn.rqspf_choose(5)  ###随机点击5场比赛
            if aa == 2:
                pbcn.confirm_match()  ###点击确认赛事
                cl.submit_order_to_station_owner_button()  #点击提交订单给站主
                cl.confirm_and_pay_button()  #点击确认支付
                hp.Moveable_float_close()
                text1 = sos.submit_order_success()  #获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)
    def test_lottery_success_page_continue_lottery_case(self):#####################-----------------mj20171215
        '''验证投注成功页【继续投注该彩种】按钮，点击页面跳转至竞彩足球选号页面'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        t = There_D_choosenumber_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)#选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            hp.Moveable_float_close()
            sos.Continue_buy()#点击【继续投注该彩种】
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_rqspf()  ##点击让球胜平负
            bb = pbcn.rqspf_choose(2)#选择2场赛事
            if bb==2:
                pbcn.confirm_match()#点击确认赛事
                cl.submit_order_to_station_owner_button()#点击提交订单给站主
                hp.Moveable_float_close()
                cl.confirm_and_pay_button()#点击确认支付
                text1 = sos.submit_order_success()  # 获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)
    def test_check_order_details_case(self):
        '''验证点击【查看订单详情】页面跳转至订单详情页'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        od = OrderDetails_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            hp.Moveable_float_close()
            sos.check_order_details()#点击查看详情
            text1 = od.scheme_details()#获取订单详情页文本
            self.assertEqual("方案详情",text1,'页面未跳转至订单详情页')
    def test_order_details_score_direct_broadcast_link_case(self):
        '''验证订单详情页【比分直播】链接，点击页面跳转至即时比分页面，选择两场比赛'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        od = OrderDetails_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            hp.Moveable_float_close()
            sos.check_order_details()#点击查看详情
            od.score_direct_broadcast_link()#点击比分直播
            bb = pbcn.enter_analysis_page()  # 点击进入赛事分析
            if bb == 1:
                pbcn.lottery_jczq_button()  # 点击【投注竞彩足球】
                pbcn.Play_f()  ###点击玩法
                pbcn.Play_rqspf()  ##点击让球胜平负
                aa = pbcn.rqspf_choose(2)  # 选择2场赛事
                if aa == 2:
                    pbcn.confirm_match()  ###点击确认赛事
                    cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
                    cl.confirm_and_pay_button()  # 点击确认支付
                    hp.Moveable_float_close()
                    text1 = sos.submit_order_success()  # 获取提交订单成功文本
                    self.assertEqual('订单提交成功', text1)
    def test_play_instruct_case(self):
        '''验证订单详情页【玩法说明】，能正常打开和关闭'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        od = OrderDetails_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            hp.Moveable_float_close()
            sos.check_order_details()#点击查看详情
            od.play_instruct()#点击玩法说明
            od.i_know()#点击【知道了】
    def test_function_instruct_case(self):
        '''验证订单详情页【功能说明】，能正常打开和关闭'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        od = OrderDetails_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择2场赛事
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            hp.Moveable_float_close()
            sos.check_order_details()  # 点击查看详情
            self.driver.execute_script("window.scroll(0,200)")#鼠标滑动200px
            od.function_instruct()#点击功能说明
            od.i_know()#点击【知道了】
    def test_oder_details_page_lottery_paintball_case(self):
        '''验证订单详情页【点击投注竞彩足球】按钮，点击页面跳转至，竞彩足球选号页面'''
        hp = HomePage_lexiu(self.driver)
        pbcn = PaintBallChooseNumber_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        pbc = PaintBallConfirm_lexiu(self.driver)
        l = Login_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        od = OrderDetails_lexiu(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.paintball_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_rqspf()  ##点击让球胜平负
        aa = pbcn.rqspf_choose(2)  # 选择2场赛事
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            hp.Moveable_float_close()
            sos.check_order_details()  # 点击查看详情
            od.continue_buy()#验证订单详情页【点击投注竞彩足球】按钮
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_rqspf()  ##点击让球胜平负
            aa = pbcn.rqspf_choose(2)  # 选择2场赛事
            if aa == 2:
                pbcn.confirm_match()  ###点击确认赛事
                cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
                hp.Moveable_float_close()
                cl.confirm_and_pay_button()  # 点击确认支付
                hp.Moveable_float_close()
                text1 = sos.submit_order_success()  # 获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)


