from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm_lelun
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_lelun
from element_operate.homepage import HomePage_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.login import Login_lelun
from element_operate.SingleFoot.single_foot_choose_number import SingleFootChooseNumber_lelun
from selenium.common.exceptions import NoSuchElementException,WebDriverException,ElementNotVisibleException
from element_operate.SingleFoot.single_foot_confim import SingleFootConfirmLottery_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_lelun
from element_operate.UnionLotto.order_details import OrderDetails_lelun
from time import sleep

#竞足单关，胜平负玩法，测试用例--mj20171120
class SingeFoot_spf_case(MyTest):
    '''竞足单关胜平负玩法流程测试'''
    def test_singlefoot_spf_1_case(self):
        '''选择一场比赛进行投注，流程测试'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()###点击进入竞足单关选号页面###
        pbcn.Play_f()#选择玩法
        pbcn.Play_spf()#选择胜平负模式
        aa=sfcn.jzdg_spf_choose(1)#选择一场比赛
        if aa > 0 :
            pbcn.confirm_match()#确认场次
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("1注5倍 ", text1)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_singlefoot_spf_2_case(self):
        '''选择两场比赛进行投注，流程测试'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ###点击进入竞足单关选号页面###
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负模式
        aa = sfcn.jzdg_spf_choose(2)  # 选择两场比赛
        if aa == 2:
            pbcn.confirm_match()  # 确认场次
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            sleep(10)
            self.assertIn("2注5倍 ", text1)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_singlefoot_spf_8_case(self):
        '''选择8场比赛，流程测试'''
        ###点击进入竞彩足球选号页面###
        hp=HomePage_lelun(self.driver)
        pbcn=PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_spf()#选择胜平负
        aa=sfcn.jzdg_spf_choose(8)#选择比赛
        if aa==2:
            pbcn.confirm_match()#确认所选场次
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            sleep(10)
            self.assertIn("8注5倍 ", text1)
            cl.submit_order_to_station_owner_button()#提交订单给站主
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_singlefoot_spf_input10000times_case(self):##mj20171215
        '''选号页面，选择八场对阵，增加倍数为10000倍，提交订单'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()#选择胜平负
        aa = sfcn.jzdg_spf_choose(8)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 确认所选场次
            pbc.Times_input_click()  # 点击投注倍数
            pbc.Times_input(10000)#输入投注10000倍
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
    def test_singlefoot_spf_9_case(self):
        '''选择九场比赛，获取“最大场次限制8场”提示，测试流程'''
        ###点击进入竞彩足球选号页面###
        hp=HomePage_lelun(self.driver)
        pbcn=PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_spf()#选择胜平负
        aa=sfcn.jzdg_spf_choose(9)  # 选择比赛
        if aa == 1 or aa==2:
            try:
                pbcn.know()
                pbcn.confirm_match()  # 确认所选场次
            except ElementNotVisibleException:
                print("当前赛事小于8场")
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)


    def test_singlefoot_spf_10_case(self):
        '''选择一天中所有比赛场次流程测试'''
        ###点击进入竞彩足球选号页面###
        hp=HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()##点击竞足
        pbcn.Play_f()#选择玩法
        pbcn.Play_spf()#选择胜平负
        aa = sfcn.jzdg_spf_choose(10)#选择比赛
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_singlefoot_spf_click_all(self):
        '''点击页面展示所有比赛，测试流程'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        sleep(10)
        aa=sfcn.jzdg_spf_click_all()  # 选择比赛
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_choose_num_clear_button_case(self):
        '''选号页面清除所选比赛流程测试'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.clear_button()#点击清除按钮
            sfcn.jzdg_spf_choose(1)#选择1场比赛
            pbcn.confirm_match()#确认所选场次
            sleep(2)
            text1=sfcl.lottery_times_text()#获取投注倍数文本
            self.assertIn("1注5倍 ",text1)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_throw10_case(self):
        '''选择投10倍流程测试'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(1)  # 选择比赛
        if aa>0:
            pbcn.confirm_match()#点击确认赛事
            pbc.Times_input_click()#点击投注倍数
            pbc.throw_times(10)#点击投注10倍
            text = sfcl.lottery_times_text()#获取投注倍数文本
            print(text)
            self.assertIn('1注10倍', text)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)

    def test_throw_add_btn_case(self):
        '''点击投注倍数的+按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Btn_add()#点击+按钮
            sleep(4)
            text=sfcl.lottery_times_text()#获取投注倍数文本
            self.assertIn('1注6倍',text)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_choose7_throw_add_btn_case(self):
        '''选号页面，任意选择七场对阵，增加倍数，提交订单'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(7)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            sleep(10)
            pbc.Btn_add()#点击+按钮
            text=sfcl.lottery_times_text()#获取投注倍数文本
            self.assertIn('1注6倍',text)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_throw_sub_btn_case(self):
        '''点击投注倍数的-按钮流程测试'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Btn_less()#点击-按钮
            text=sfcl.lottery_times_text()#获取投注倍数文本
            self.assertIn('1注4倍',text)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_input_throw_times_case(self):
        '''输入投注1倍测试流程'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(1)  # 选择比赛
        if aa > 0 :
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Times_input_click()#点击投注倍数输入框
            pbc.Times_input(1)#输入投注3倍
            text = sfcl.lottery_times_text()#获取投注倍数文本
            self.assertIn('1注1倍',text)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_edit_event_case(self):
        '''验证投注确认页编辑赛事按钮测试流程'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        l = Login_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法-
        pbcn.Play_spf()  # 选择胜平负
        aa = sfcn.jzdg_spf_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Add_event()#点击编辑赛事
            bb = sfcn.jzdg_spf_edit_event(1)  # 选择1场比赛
            if bb == 1:
                print("只有一场赛事")
                pbcn.confirm_match()  # 点击确认赛事
                text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
                self.assertIn("2注5倍 ", text1)
            if bb == 2:
                pbcn.confirm_match()  # 点击确认赛事
                text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
                self.assertIn("2注5倍 ", text1)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    # def test_delete_one_event_case(self):
    #     """验证单个删除赛事X按钮，流程测试"""
    #     hp = HomePage(self.driver)
    #     pbcn = PaintBallChooseNumber(self.driver)
    #     sfcn = SingleFootChooseNumber(self.driver)
    #     cl = ConfirmLottery(self.driver)
    #     pbc = PaintBallConfirm(self.driver)
    #     hl = Login(self.driver)
    #     hp.open()
    #     ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
    #     hp.Moveable_float_close()
    #     hp.single_foot_link()  ##点击竞彩足球
    #     pbcn.Play_f()  ###点击玩法
    #     pbcn.Play_spf()  ##点击胜平负
    #     aa = sfcn.jzdg_spf_choose(3)  ###随机点击3场比赛
    #     if aa == 2:
    #         pbcn.confirm_match()  ###点击确认赛事
    #         a = pbc.NN()  ###读取删除前有多少个X按钮
    #         pbc.N_del(1)  ##点击删除第一场赛事
    #         a1 =pbc.NN()  ###读取删除后有多少个X按钮
    #         self.assertEqual(a - 1, a1)
    #     if aa == 0 :
    #         text =sfcn.Play_dgp_text()
    #         self.assertIn("单关配",text)
    def test_delete_all_event_case(self):
        """验证删除选择的全部赛事图标，流程测试"""
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sfcl = SingleFootConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        hl = Login_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击胜平负
        aa = sfcn.jzdg_spf_choose(2)  ###随机点击2场比赛
        if aa > 0:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_del_icon()#点击删除图标
            cl.confirm_delete_button()#点击确认删除按钮
            sfcn.jzdg_spf_choose(1)#选择1场比赛
            pbcn.confirm_match()  ###点击确认赛事
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("1注5倍 ", text1)
        if aa == 0 :
            text =sfcn.Play_dgp_text()
            self.assertIn("单关配",text)
    def test_play_instruction_open_close_case(self):########mj20171215
        '''在投注选号页面，点击右上角玩法说明，可以打开和关闭'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        t = There_D_choosenumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.three_clock()#点击右上角的。。。
        sfcn.jzdg_play_instruct()#点击玩法说明
        t.There_D_know()#点击我知道了

    def test_filter_button_case(self):
        '''在投注选号页面，点击筛选按钮，对所有的筛选项进行点击'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.filter_button()#点击筛选按钮
        pbcn.allccsel()#点击全选
        pbcn.noallccsel()#点击反选
        pbcn.fivecc()#点击五大联赛
        pbcn.findcc()#点击筛选banner的确定按钮
    def test_immediately_reture_homepage(self):
        '''在投注选号页面，点击右上角即时比分，可以打开并返回首页'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        t = There_D_choosenumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.three_clock()  # 点击右上角的。。。
        pbcn.immediately()  # 点击即时比分
        pbcn.immediately_page_return_homepage()#点击返回首页
    def test_immediately_sorce_lottery_case(self):
        '''在投注选号页面，点击右上角即时比分，打开赛事分析数据，点击页面下方的投注竞彩足球按钮，页面跳转到选号页，选择两场比赛，提交订单'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        t = There_D_choosenumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.three_clock()  # 点击右上角的。。。
        pbcn.immediately()#点击即时比分
        aa=pbcn.enter_analysis_page()#点击进入赛事分析
        if aa ==1:
            pbcn.lottery_jczq_button()#点击【投注竞彩足球】
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_spf()  ##点击让球胜平负
            aa = sfcn.jzdg_spf_choose(2)  ###随机点击2场比赛
            if aa == 2:
                pbcn.confirm_match()  ###点击确认赛事
                cl.submit_order_to_station_owner_button()  #点击提交订单给站主
                cl.confirm_and_pay_button()  #点击确认支付
                hp.Moveable_float_close()
                text1 = sos.submit_order_success()  #获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)
    def test_lottery_success_page_continue_lottery_case(self):#####################-----------------mj20171215
        '''验证投注成功页【继续投注该彩种】按钮，点击页面跳转至竞彩足球选号页面'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        t = There_D_choosenumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击让球胜平负
        aa = sfcn.jzdg_spf_choose(2)#选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            sos.Continue_buy()#点击【继续投注该彩种】
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_spf()  ##点击让球胜平负
            bb = sfcn.jzdg_spf_choose(2)#选择2场赛事
            if bb==2:
                pbcn.confirm_match()#点击确认赛事
                cl.submit_order_to_station_owner_button()#点击提交订单给站主
                cl.confirm_and_pay_button()#点击确认支付
                text1 = sos.submit_order_success()  # 获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)
    def test_check_order_details_case(self):
        '''验证点击【查看订单详情】页面跳转至订单详情页'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击胜平负
        aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
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
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击让球胜平负
        aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            sos.check_order_details()#点击查看详情
            od.score_direct_broadcast_link()#点击比分直播
            bb = pbcn.enter_analysis_page()  # 点击进入赛事分析
            if bb == 1:
                pbcn.lottery_jczq_button()  # 点击【投注竞彩足球】
                pbcn.Play_f()  ###点击玩法
                pbcn.Play_spf()  ##点击让球胜平负
                aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
                if aa == 2:
                    pbcn.confirm_match()  ###点击确认赛事
                    cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
                    cl.confirm_and_pay_button()  # 点击确认支付
                    text1 = sos.submit_order_success()  # 获取提交订单成功文本
                    self.assertEqual('订单提交成功', text1)
    def test_play_instruct_case(self):
        '''验证订单详情页【玩法说明】，能正常打开和关闭'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击胜平负
        aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
        if aa ==2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()#点击提交订单给站主
            cl.confirm_and_pay_button()#点击确认支付
            sos.check_order_details()#点击查看详情
            od.play_instruct()#点击玩法说明
            od.i_know()#点击【知道了】
    def test_function_instruct_case(self):
        '''验证订单详情页【功能说明】，能正常打开和关闭'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击让球胜平负
        aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            sos.check_order_details()  # 点击查看详情
            self.driver.execute_script("window.scroll(0,200)")#鼠标滑动200px
            od.function_instruct()#点击功能说明
            od.i_know()#点击【知道了】
    def test_oder_details_page_lottery_paintball_case(self):
        '''验证订单详情页【点击投注竞彩足球】按钮，点击页面跳转至，竞彩足球选号页面'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击胜平负
        aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            sos.check_order_details()  # 点击查看详情
            od.continue_buy()#验证订单详情页【点击投注竞彩足球】按钮
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_spf()  ##点击让球胜平负
            aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
            if aa == 2:
                pbcn.confirm_match()  ###点击确认赛事
                cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
                cl.confirm_and_pay_button()  # 点击确认支付
                text1 = sos.submit_order_success()  # 获取提交订单成功文本
                self.assertEqual('订单提交成功', text1)
    def test_handover_paly_case(self):
        '''胜平负玩法，在投注确认页面，点击编辑赛事，回到选号选号页面，切换玩法为混合投注，任选两场赛事，提交订单，订单详情显示为混合投注'''
        hp = HomePage_lelun(self.driver)
        pbcn = PaintBallChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        pbc = PaintBallConfirm_lelun(self.driver)
        sfcn = SingleFootChooseNumber_lelun(self.driver)
        l = Login_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        od = OrderDetails_lelun(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.single_foot_link()  ##点击竞足单关
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_spf()  ##点击胜平负
        aa = sfcn.jzdg_spf_choose(2)  # 选择2场赛事
        if aa == 2:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Add_event()  # 点击编辑赛事
            pbcn.Play_f()  ###点击玩法
            pbcn.Play_mix()  ##点击混合玩法
            sfcn.Paintball_single_mixs(2)#选择两场赛事
            pbcn.confirm_match()  ###点击确认赛事
            cl.submit_order_to_station_owner_button()  # 点击提交订单给站主
            cl.confirm_and_pay_button()  # 点击确认支付
            sleep(5)
            text1 = sos.submit_order_success()  # 获取提交订单成功文本
            self.assertEqual('订单提交成功', text1)
