from element_operate.SSC.SSC_choosenumber import CQSSC_ChooseNumber
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.UnionLotto.order_details import OrderDetails
from element_operate.historical_trend import HistoricalTrend
from element_operate.login import Login
from element_operate.homepage import HomePage
from test_case.Base.mytest import MyTest
from time import sleep
##--mj20171205
class CQSSC_ThreeStartCase(MyTest):
    '''重庆时时彩手选三星玩法测试用例'''
    def test_threestar_choose_one_case(self):
        '''三星直选玩法，个位十位百位各选一个号码并提交订单流程测试'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        od =OrderDetails(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login()#点击登录
        hp.homepage_link()#点击首页
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.three_star()#选择三星
        num1=ssc_cn.three_star_select(1,1,1)#百十个位各选一个数字
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
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
        sos.check_order_details()#点击查看订单详情
        num2 = od.bet_number()#获取页面投注号码
        self.assertIn(num1,num2)
    def test_threestar_choose_all_case(self):
        '''二星直选玩法，个十百三位各选所有号码'''
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
        ssc_cn.three_star()#选择三星
        ssc_cn.baiwei_all()
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("1000注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_threestar_choose_all_cancel_case(self):
        '''三星直选玩法，选择所有选号，再次点击取消流程'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login()#点击登录
        hp.homepage_link()#点击首页
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.three_star()#选择三星
        ssc_cn.baiwei_all()
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("1000注 ", aa)
        ssc_cn.baiwei_all()
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", aa)
    def test_threestar_choose_one_clear_num(self):
        '''选择一个号码，点击【清除所有选号】，重新选择一个号码，提交订单'''
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
        ssc_cn.three_star()  # 选择三星
        ssc_cn.baiwei_random(1)
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        aa = efcn.total_buy_text()
        self.assertIn("1注 ", aa)
        ulcn.clear_number()  #清除所有选号
        cc = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", cc)
        ssc_cn.baiwei_random(2)
        ssc_cn.shiwei_random(2)
        ssc_cn.gewei_random(2)
        bb = efcn.total_buy_text()
        self.assertIn("8注 ", bb)
        efcn.confirm_number_button()  # 点击确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("8注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)
    def test_threestar_choose_one_continue_buy_case(self):
        '''验证订单详情页【继续购买该方案】页面跳转至投注确认页，流程'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        od =OrderDetails(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login()#点击登录
        hp.homepage_link()#点击首页
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.three_star()#选择三星
        ssc_cn.baiwei_random(1)
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        sos.check_order_details()  # 点击查看订单详情
        od.Scheme()#点击继续购买该方案
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        text = cl.lottery_confirm_num_page_text()
        self.assertEqual("投注确认",text,'页面未跳转至投注确认页')
    def test_threestar_choose_one_continue_choose_case(self):
        '''验证订单详情页【点击投注重庆时时彩】，页面跳转至选号页面'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        od =OrderDetails(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login()#点击登录
        hp.homepage_link()#点击首页
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.three_star()#选择三星
        num1=ssc_cn.three_star_select(1, 1, 1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        sos.check_order_details()  # 点击查看订单详情
        od.continue_buy()#点击继续购买此彩种
        cc = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", cc,'页面未跳转至选号页面')
    def test_threestar_choose_one_continue_buy_caizhong_case(self):
        '''验证购买成功页【点击继续投注该彩种】，页面跳转至选号页面'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        od =OrderDetails(self.driver)
        hp.Moveable_float_close()#点击关闭浮窗
        hp.My_lottery_ticket()#点击我的彩票
        l.login()#点击登录
        hp.homepage_link()#点击首页
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.cqssc_link()#点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ssc_cn.play_mode()#选择模式
        ssc_cn.three_star()#选择三星
        num1=ssc_cn.three_star_select(1, 1, 1)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        sos.Continue_buy()#点击继续投注该彩种
        cc = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", cc, '页面未跳转至选号页面')
    def test_choose_number_history_recommendation_num_case(self):
        '''选号页面，右上方隐藏的“历史走势”按钮，点击【使用推荐号码】，提交订单'''
        hp = HomePage(self.driver)
        hp.open()
        l = Login(self.driver)
        efcn = ElevenFiveChooseNumber(self.driver)
        ulcn =UnionLottoChooseNumber(self.driver)
        ssc_cn = CQSSC_ChooseNumber(self.driver)
        ht = HistoricalTrend(self.driver)
        efcl = EleChooseFiveConfirmLottery(self.driver)
        cl = ConfirmLottery(self.driver)
        sos = SubmitOrderSuccess(self.driver)
        od = OrderDetails(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.cqssc_link()  # 点击重庆时时彩链接
        ulcn.There_clock()#点击。。。
        ssc_cn.history_trend()#点击历史走势
        ht.use_recommend_num_button()#点击使用推荐号码
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐米彩票-重庆时时彩", trade_name)



