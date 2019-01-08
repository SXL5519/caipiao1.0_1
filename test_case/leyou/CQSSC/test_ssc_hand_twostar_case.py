from element_operate.SSC.SSC_choosenumber import CQSSC_ChooseNumber_leyou
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_leyou
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_leyou
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_leyou
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.login import Login_leyou
from element_operate.homepage import HomePage_leyou
from test_case.Base.mytest import MyTest
##--mj20171205
class CQSSC_TwoStartCase(MyTest):
    '''重庆时时彩手选两星玩法测试用例'''
    def test_twostar_choose_one_case(self):
        '''两星直选玩法，个位十位各选一个号码并提交订单流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login_leyou()#点击登录
        hp.homepage_link()#点击首页
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.two_star()#选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
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
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_choose_all_case(self):
        '''二星直选玩法，个位选择9个号码十位选择9个号码'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login_leyou()#点击登录
        hp.homepage_link()#点击首页
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.two_star()#选择两星
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("100注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_choose_all_cancel_case(self):
        '''二星直选玩法，选择所有选号，再次点击取消流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login_leyou()#点击登录
        hp.homepage_link()#点击首页
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.two_star()#选择两星
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("100注 ", aa)
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", aa)
    def test_twostar_choose_one_clear_num(self):
        '''选择一个号码，点击【清除所有选号】，重新选择一个号码，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        aa = efcn.total_buy_text()
        self.assertIn("1注 ", aa)
        ulcn.clear_number()  # 清除所有选号
        cc = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", cc)
        ssc_cn.shiwei_random(2)
        ssc_cn.gewei_random(2)
        bb = efcn.total_buy_text()
        self.assertIn("4注 ", bb)
        efcn.confirm_number_button()  # 点击确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("4注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase2_case(self):
        '''投注确认页，点击追2期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_button()#点击追号期数
        cl.chase_ticket_button_two()#点击追2期
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注2期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase5_case(self):
        '''投注确认页，点击追5期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_button()#点击追号期数
        cl.chase_ticket_button_five()#点击追5期
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注5期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase10_case(self):
        '''投注确认页，点击追10期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_button()#点击追号期数
        cl.chase_ticket_button_ten()#点击追10期
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注10期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase20_case(self):
        '''投注确认页，点击追20期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_button()#点击追号期数
        cl.chase_ticket_button_twenty()#点击追20期
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注20期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase50_case(self):
        '''投注确认页，点击追50期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_button()#点击追号期数
        cl.chase_ticket_button_fifty()#点击追50期
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注50期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase3_case(self):
        '''投注确认页，输入追3期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_input(3)#输入追3期
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注3期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase_sub_case(self):
        '''投注确认页，点击追号-按钮，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_input(3)
        efcl.chase_sub_button()#点击追号-按钮
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注2期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_chase_add_case(self):
        '''投注确认页，点击追号+按钮，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_add_button()#点击追号+按钮
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注2期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_throw3_case(self):
        '''投注确认页，输入投3倍，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号、
        efcl.throw_times_input(3)#输入投注3倍
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期3倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_throw_sub_case(self):
        '''投注确认页，点击投-按钮倍，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.throw_times_input(3)#输入投注3倍
        efcl.throw_times_sub_button()#点击投注倍数的-按钮
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期2倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_throw_add_case(self):
        '''投注确认页，点击投+按钮倍，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.throw_times_add_button()#点击投注倍数的+按钮
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("1注1期2倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_twostar_throw_chase2throw2_case(self):
        '''投注确认页，输入追2期投2倍，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.two_star()  # 选择两星
        ssc_cn.shiwei_random(2)
        ssc_cn.gewei_random(2)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.chase_ticket_input(2)#输入追2期
        efcl.throw_times_input(2)#输入投注倍数2倍
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("4注2期2倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)

