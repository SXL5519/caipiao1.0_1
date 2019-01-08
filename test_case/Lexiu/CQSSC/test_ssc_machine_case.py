from element_operate.SSC.SSC_choosenumber import CQSSC_ChooseNumber_lexiu
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_lexiu
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_lexiu
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lexiu
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lexiu
# from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery
from element_operate.login import Login_lexiu
from element_operate.homepage import HomePage_lexiu
from test_case.Base.mytest import MyTest
from time import sleep
###重庆时时彩机选流程测试--mj20171206
class CQSSC_MachineChooseCase(MyTest):
    '''重庆时时彩机选流程测试'''
    def test_onestar_machine_choose_one_case(self):
        '''机选1注，确认选号提交订单，点击【查看订单详情】'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()#选择一星
        ulcn.machine_choose_button()#点击机选
        ulcn.machine_choose_one_button()#机选一注
        aa = efcn.total_buy_text()
        self.assertIn("1注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
        sos.check_order_details()#点击查看订单详情

    def test_onestar_machine_choose_one_confirm_delete_all_case(self):
        '''机选1注，投注确认页，点击【删除所有投注】图标【确认】删除，页面跳转至选号页，机选一注提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()#选择一星
        ulcn.machine_choose_button()#点击机选
        ulcn.machine_choose_one_button()#机选一注
        efcn.confirm_number_button()  # 点击确认选号
        cl.delete_all_num_button()#删除所有选号
        cl.confirm_delete_button()#确认删除
        cc = efcn.total_buy_text()
        self.assertIn("请至少选择1个号码", cc)
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 点击确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_onestar_machine_choose_one_cancel_delete_all_case(self):
        '''机选1注，投注确认页，点击【删除所有投注】图标【取消】删除，提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()#选择一星
        ulcn.machine_choose_button()#点击机选
        ulcn.machine_choose_one_button()#机选一注
        efcn.confirm_number_button()  # 点击确认选号
        cl.delete_all_num_button()#删除所有选号
        cl.cancel_delete_button()#取消删除
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_onestar_machine_choose_one_delete_one_case(self):
        '''机选1注，投注确认页，点击【单个删除投注】图标，页面跳转至选号页，机选1注，提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 点击确认选号
        cl.del_n(1)#选择删除一场投注
        ulcn.machine_choose_button()  # 点击机选 页面跳转至选号页
        ulcn.machine_choose_one_button()  # 机选一注
        efcn.confirm_number_button()  # 点击确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_onestar_machine_choose_five_case(self):
        '''机选5注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("5注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)

    def test_onestar_machine_choose_five_delete_one_case(self):
        '''机选5注，投注确认页，点击【单个删除投注】图标，投注注数减少一注，提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        num=cl.event_count()#获取总共有多少注
        cl.del_n(5)  # 选择删除第5场投注
        num1 = cl.event_count()#获取删除后的场数
        self.assertEqual(num-1,num1)
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("4注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_onestar_machine_choose_five_delete_all_case(self):
        '''机选5注，投注确认页，点击【单个删除投注】图标，删除所有注数，跳转至选号页，手选复式（2注），提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        num=cl.event_count()#获取总共有多少注
        print("删除前共有%d场"%num)
        for i in range(1,(num+1)):
            cl.del_n(i)  # 选择删除第5场投注
            sleep(1)
        ssc_cn.gewei_random(2)
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("2注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_onestar_machine_choose_ten_case(self):
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("10注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_twostar_machine_choose_one_case(self):
        '''二星玩法，机选1注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择二星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_twostar_machine_choose_five_case(self):
        '''二星玩法，机选5注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择二星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("5注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_twostar_machine_choose_ten_case(self):
        '''二星玩法，机选10注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择二星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("10注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_threestar_machine_choose_one_case(self):
        '''三星玩法，机选1注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.three_star()  # 选择三星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_threestar_machine_choose_five_case(self):
        '''三星玩法，机选5注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.three_star()  # 选择三星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("5注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_threestar_machine_choose_ten_case(self):
        '''三星玩法，机选10注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.three_star()  # 选择三星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("10注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_fivestar_machine_choose_one_case(self):
        '''五星直选玩法，机选1注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_fivestar_machine_choose_five_case(self):
        '''五星直选玩法，机选5注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("5注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_fivestar_machine_choose_ten_case(self):
        '''五星直选玩法，机选10注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("10注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_bigsmall_machine_choose_one_case(self):
        '''大小单双玩法，机选1注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_one_button()  # 机选1注
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_bigsmall_machine_choose_five_case(self):
        '''大小单双玩法，机选5注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_five_button()  # 机选5注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("5注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)
    def test_bigsmall_machine_choose_ten_case(self):
        '''大小单双玩法，机选10注，确认选号提交订单'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        l = Login_lexiu(self.driver)
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcl = EleChooseFiveConfirmLottery_lexiu(self.driver)
        cl = ConfirmLottery_lexiu(self.driver)
        sos = SubmitOrderSuccess_lexiu(self.driver)
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lexiu()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lexiu(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双玩法
        ulcn.machine_choose_button()  # 点击机选
        ulcn.machine_choose_ten_button()  # 机选10注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("10注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐秀赢球-重庆时时彩", trade_name)









