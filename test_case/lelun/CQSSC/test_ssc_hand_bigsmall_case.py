from element_operate.SSC.SSC_choosenumber import CQSSC_ChooseNumber_lelun
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lelun
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_lelun
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_lelun
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_lelun
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_lelun
from element_operate.login import Login_lelun
from element_operate.homepage import HomePage_lelun
from test_case.Base.mytest import MyTest
##--mj20171205
class CQSSC_BigSmallSingleDoubleCase(MyTest):
    '''重庆时时彩手选大小单双玩法测试用例'''

    def test_bigsmall_choose_one_case(self):
        '''大小单双玩法，每位各选一个号码并提交订单流程测试'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        l = Login_lelun(self.driver)
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lelun(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双
        ssc_cn.ds_shiwei_random(1)#十位选择一个号码
        ssc_cn.ds_gewei_random(1)#个位选择一个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-重庆时时彩", trade_name)

    def test_bigsmall_choose_double_case(self):
        '''大小单双玩法，个位十位各选多个属性，确认选号，提交订单'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        l = Login_lelun(self.driver)
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lelun(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双
        ssc_cn.ds_shiwei_all()  # 十位选择所有号码
        ssc_cn.ds_gewei_all()  # 个位选择所有号码
        aa = efcn.total_buy_text()
        self.assertIn("16注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-重庆时时彩", trade_name)
    def test_bigsmall_choose_all_cancel_case(self):
        '''大小单双玩法，个位十位选择所有属性并取消'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        l = Login_lelun(self.driver)
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lelun(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双
        ssc_cn.ds_shiwei_all()  # 十位选择所有号码
        ssc_cn.ds_gewei_all()  # 个位选择所有号码
        aa = efcn.total_buy_text()
        self.assertIn("16注 ", aa)
        ssc_cn.ds_shiwei_all()  # 十位选择取消所有号码
        ssc_cn.ds_gewei_all()  # 个位选择取消所有号码
        aa = efcn.total_buy_text()
        self.assertIn("请至少每位选择1种属性", aa)
    def test_bigsmall_choose_one_clear_case(self):
        '''大小单双玩法，个位十位各选一个属性，点击【清除所有选号】图标，确认选号，提交订单'''
        hp = HomePage_lelun(self.driver)
        hp.open()
        l = Login_lelun(self.driver)
        efcn = ElevenFiveChooseNumber_lelun(self.driver)
        efcl = EleChooseFiveConfirmLottery_lelun(self.driver)
        ulcn = UnionLottoChooseNumber_lelun(self.driver)
        cl = ConfirmLottery_lelun(self.driver)
        sos = SubmitOrderSuccess_lelun(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_lelun()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_lelun(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.big_little()  # 选择大小单双
        ssc_cn.ds_shiwei_random(1)#十位选择一个号码
        ssc_cn.ds_gewei_random(1)#个位选择一个号码
        aa = efcn.total_buy_text()
        self.assertIn("1注 ", aa)
        ulcn.clear_number()  # 清除所有选号
        cc = efcn.total_buy_text()
        self.assertIn("请至少每位选择1种属性", cc)
        ssc_cn.ds_shiwei_random(2)  # 十位选择2个号码
        ssc_cn.ds_gewei_random(2)  # 个位选择2个号码
        cc = efcn.total_buy_text()
        self.assertIn("4注", cc)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-重庆时时彩", trade_name)





