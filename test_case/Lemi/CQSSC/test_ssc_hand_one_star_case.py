from element_operate.SSC.SSC_choosenumber import CQSSC_ChooseNumber
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.login import Login
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from time import sleep
##--mj20171205
class CQSSC_OneStartCase(MyTest):
    '''重庆时时彩手选一星玩法测试用例'''
    def test_onestar_choose_one_case(self):
        '''一星玩法，选择一个号码并提交订单流程测试'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login()#点击登录
        hp.homepage_link()#点击首页
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.one_star()#选择一星
        ssc_cn.gewei_random(1)#选择一个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注 ",aa)
        efcn.confirm_number_button()#点击确认选号
        efcl.submit_order_button()#点击提交订单给站主
        cl.confirm_and_pay_button()#点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_onestar_choose_all_case(self):
        '''一星玩法，选择所有个号码，提交订单测试'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_all()  # 选择9个号码
        aa = efcn.total_buy_text()
        self.assertIn("10注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_onestar_choose_all_cancel_case(self):
        '''一星玩法，选择所有选号，并取消流程测试'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_all()  # 选择9个号码
        ssc_cn.gewei_all()#取消选中的9个号码
        aa = efcn.total_buy_text()
        self.assertIn("请至少选择1个号码", aa)
    def test_onestar_clear_num_case(self):
        '''一星玩法，选择5号码，并清除，流程测试'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        ulcn = UnionLottoChooseNumber(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_random(5)  #选择5个号码
        aa = efcn.total_buy_text()
        self.assertIn("5注", aa)
        ulcn.clear_number()#清除所有选号
        cc = efcn.total_buy_text()
        self.assertIn("请至少选择1个号码", cc)
        ssc_cn.gewei_random(2)#选择2个号码
        aa = efcn.total_buy_text()
        self.assertIn("2注", aa)
    def test_onestar_continue_choose(self):
        '''投注确认页，点击【继续选号】，页面跳转至选号页面，选择一个号码，提交订单'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        ulcn = UnionLottoChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_random(1)#选择1个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注",aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.continue_choose_num()#点击继续选号
        ssc_cn.gewei_random(1)  # 选择1个号码
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()#获取注数倍数
        self.assertIn("2注1期1倍",bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_onestar_continue_fushi_choose(self):
        '''投注确认页，点击【继续选号】，页面跳转至选号页面，选择多个号码，提交订单'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        ulcn = UnionLottoChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_random(1)#选择1个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注",aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.continue_choose_num()#点击继续选号
        ssc_cn.gewei_random(3)  # 选择1个号码
        efcn.confirm_number_button()#确认选号
        bb = efcl.lottery_chase_throw_text()#获取注数倍数
        self.assertIn("4注1期1倍",bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_onestar_machine_one_case(self):
        '''投注确认页，点击【机选1注】，提交订单'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        ulcn = UnionLottoChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_random(1)  # 选择1个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.machine_choose_one()#点击机选1注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("2注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_onestar_machine_five_case(self):
        '''投注确认页，点击【机选5注】，提交订单'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        ulcn = UnionLottoChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.one_star()  # 选择一星
        ssc_cn.gewei_random(1)  # 选择1个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.machine_choose_five()#点击机选5注
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("6注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    









