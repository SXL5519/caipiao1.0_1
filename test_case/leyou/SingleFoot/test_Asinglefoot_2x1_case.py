from test_case.Base.mytest import MyTest
from element_operate.PaintBall.paintball_confirm import PaintBallConfirm_leyou
from element_operate.PaintBall.paintball_choosenumber import PaintBallChooseNumber_leyou
from element_operate.homepage import HomePage_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.login import Login_leyou
from element_operate.SingleFoot.single_foot_choose_number import SingleFootChooseNumber_leyou
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException
from time import sleep
from element_operate.SingleFoot.single_foot_confim import SingleFootConfirmLottery_leyou


##竞足单关2选1玩法测试用例---mj20171121
class SingeFoot_two_choose_one_case(MyTest):
    '''竞足单关让球2选1玩法流程测试'''

    def test_singlefoot_two_choose_one_1_case(self):
        '''选择一场比赛进行投注，流程测试'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ###点击进入竞足单关选号页面###
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1模式
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择一场比赛
        if aa > 0:
            pbcn.confirm_match()  # 确认场次
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("1注5倍 ", text1)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_singlefoot_two_choose_one_2_case(self):
        '''选择两场比赛进行投注，流程测试'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ###点击进入竞足单关选号页面###
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1模式
        aa = sfcn.jzdg_two_choose_one_choose(2)  # 选择两场比赛
        if aa == 2:
            pbcn.confirm_match()  # 确认场次
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("2注5倍 ", text1)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_singlefoot_two_choose_one_8_case(self):
        '''选择8场比赛，流程测试'''
        ###点击进入竞彩足球选号页面###
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(8)  # 选择比赛
        if aa == 2:
            pbcn.confirm_match()  # 确认所选场次
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("8注5倍 ", text1)
            cl.submit_order_to_station_owner_button()  # 提交订单给站主
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_singlefoot_two_choose_one_9_case(self):
        '''选择九场比赛，获取“最大场次限制8场”提示，测试流程'''
        ###点击进入竞彩足球选号页面###
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(9)  # 选择比赛
        if aa == 1 or aa == 2:
            try:
                pbcn.know()
                pbcn.confirm_match()  # 确认所选场次
            except ElementNotVisibleException:
                print("当前赛事小于8场")
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_singlefoot_two_choose_one_10_case(self):
        '''选择一天中所有比赛场次流程测试'''
        ###点击进入竞彩足球选号页面###
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(10)  # 选择比赛
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_singlefoot_two_choose_one_click_all(self):
        '''点击页面展示所有比赛，测试流程'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_click_all()  # 选择比赛
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_choose_num_clear_button_case(self):
        '''选号页面清除所选比赛流程测试'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.clear_button()  # 点击清除按钮
            sfcn.jzdg_two_choose_one_choose(1)  # 选择1场比赛
            pbcn.confirm_match()  # 确认所选场次
            sleep(2)
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("1注5倍 ", text1)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_throw10_case(self):
        '''选择投10倍流程测试'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Times_input_click()  # 点击投注倍数
            pbc.throw_times(10)  # 点击投注10倍
            text = sfcl.lottery_times_text()  # 获取投注倍数文本
            print(text)
            self.assertIn('1注10倍', text)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_throw_add_btn_case(self):
        '''点击投注倍数的+按钮流程测试'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Btn_add()  # 点击+按钮
            text = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn('1注6倍', text)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_throw_sub_btn_case(self):
        '''点击投注倍数的-按钮流程测试'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Btn_less()  # 点击-按钮
            text = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn('1注4倍', text)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_input_throw_times_case(self):
        '''输入投注3倍测试流程'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Times_input_click()  # 点击投注倍数输入框
            pbc.Times_input(3)  # 输入投注3倍
            text = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn('1注3倍', text)
        if aa ==0:
            texxt = hp.header_text()#获取首页顶端文本
            self.assertEqual("乐优炫彩",texxt)

    def test_edit_event_case(self):
        '''验证投注确认页编辑赛事按钮测试流程'''
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        l = Login_leyou(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞足
        pbcn.Play_f()  # 选择玩法-
        pbcn.Play_2x1()  # 选择2选1
        aa = sfcn.jzdg_two_choose_one_choose(1)  # 选择比赛
        if aa > 0:
            pbcn.confirm_match()  # 点击确认赛事
            pbc.Add_event()  # 点击编辑赛事
            bb = sfcn.jzdg_two_choose_one_edit_event(1)  # 选择1场比赛
            if bb == 1:
                print("只有一场赛事")
                pbcn.confirm_match()  # 点击确认赛事
                text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
                self.assertIn("2注5倍 ", text1)
            if bb == 2:
                pbcn.confirm_match()  # 点击确认赛事
                text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
                self.assertIn("2注5倍 ", text1)
        texxt = hp.header_text()  # 获取首页顶端文本
        self.assertEqual("乐优炫彩", texxt)

    def test_delete_all_event_case(self):
        """验证删除选择的全部赛事图标，流程测试"""
        hp = HomePage_leyou(self.driver)
        pbcn = PaintBallChooseNumber_leyou(self.driver)
        sfcn = SingleFootChooseNumber_leyou(self.driver)
        sfcl = SingleFootConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        pbc = PaintBallConfirm_leyou(self.driver)
        hl = Login_leyou(self.driver)
        hp.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.single_foot_link()  ##点击竞彩足球
        pbcn.Play_f()  ###点击玩法
        pbcn.Play_2x1()  ##点击2选1
        aa = sfcn.jzdg_two_choose_one_choose(2)  ###随机点击2场比赛
        if aa > 0:
            pbcn.confirm_match()  ###点击确认赛事
            pbc.Pf_del_icon()  # 点击删除图标
            cl.confirm_delete_button()  # 点击确认删除按钮
            sfcn.jzdg_two_choose_one_choose(1)  # 选择1场比赛
            pbcn.confirm_match()  ###点击确认赛事
            text1 = sfcl.lottery_times_text()  # 获取投注倍数文本
            self.assertIn("1注5倍 ", text1)
        texxt = hp.header_text()  # 获取首页顶端文本
        self.assertEqual("乐优炫彩", texxt)
