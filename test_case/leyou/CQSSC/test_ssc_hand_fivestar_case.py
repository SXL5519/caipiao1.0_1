from element_operate.SSC.SSC_choosenumber import CQSSC_ChooseNumber_leyou
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_leyou
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_leyou
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_leyou
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery_leyou
from element_operate.login import Login_leyou
from element_operate.homepage import HomePage_leyou
from test_case.Base.mytest import MyTest
from time import sleep
##--mj20171205
class CQSSC_FiveStartCase(MyTest):
    '''重庆时时彩手选五星直选玩法测试用例'''

    def test_fivestar_choose_one_case(self):
        '''五星直选玩法，每位各选一个号码并提交订单流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
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
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
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
    def test_fivestar_choose_double_case(self):
        '''五星直选玩法，每位各选多个号码并提交订单流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
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
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(2)
        ssc_cn.qianwei_random(2)
        ssc_cn.baiwei_random(2)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(2)
        ssc_cn.gewei_random(2)
        aa = efcn.total_buy_text()
        self.assertIn("32注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_fivestar_choose_all_case(self):
        '''五星直选玩法，每位各选所有号码'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
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
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_all()
        ssc_cn.qianwei_all()
        ssc_cn.baiwei_all()
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("100000注 ", aa)
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        toast=cl.out_max_pay()
        self.assertEqual("投注金额不能大于100000元",toast)
    def test_fivestar_choose_all_cancel_case(self):
        '''五星直选玩法，选择所有选号，再次点击取消流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_all()
        ssc_cn.qianwei_all()
        ssc_cn.baiwei_all()
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("100000注 ", aa)
        self.driver.execute_script("window.scroll(0,0)")
        ssc_cn.wanwei_all()
        ssc_cn.qianwei_all()
        ssc_cn.baiwei_all()
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_all()
        ssc_cn.gewei_all()
        aa = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", aa)
    def test_fivestar_choose_one_clear_num(self):
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
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        aa = efcn.total_buy_text()
        self.assertIn("1注 ", aa)
        self.driver.execute_script("window.scroll(0,0)")
        ulcn.clear_number()  # 清除所有选号
        cc = efcn.total_buy_text()
        self.assertIn("请每位至少选择1个号码", cc)
        ssc_cn.wanwei_random(2)
        ssc_cn.qianwei_random(2)
        ssc_cn.baiwei_random(2)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(2)
        ssc_cn.gewei_random(2)
        bb = efcn.total_buy_text()
        self.assertIn("32注 ", bb)
        efcn.confirm_number_button()  # 点击确认选号
        bb = efcl.lottery_chase_throw_text()  # 获取注数倍数
        self.assertIn("32注1期1倍", bb)
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  # 点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
#############################智能追号验证#####################mj20171206
    def test_intelligently_chase_input11_case(self):
        '''输入追11期，点击【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()#确认选号
        ssc_cl.intelligently_chase_button()#点击智能追号
        text2 = ssc_cl.totalIssue_num()#获取追号期数文本
        ssc_cl.znzh_issue_num_input(11)#输入追11期
        ssc_cl.totalIssue()#更新追号期数
        text=ssc_cl.totalIssue_text()
        self.assertIn(str(text2+1),text)#检查是否修改追号期数
        ssc_cl.submit_button()#点击提交按钮
        cl.confirm_and_pay_button()#点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    #####mj20171207
    def test_intelligently_chase_ravise_chase_add_confirm_revise_case(self):
        '''【修改方案】点击连续追+按钮，点击【确定】，【提交】，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_chase_add()#点击追号的+按钮
        ssc_cl.revise_confirm()#点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2 + 1), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_chase_sub_confirm_revise_case(self):
        '''【修改方案】点击连续追-按钮，点击【确定】，【提交】，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_chase_sub()#点击追号的-按钮
        ssc_cl.revise_confirm()#点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2 - 1), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_chase_input12_confirm_revise_case(self):
        '''【修改方案】输入连续追号12期，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_chase_input(12)#追号的输入框输入12
        ssc_cl.revise_confirm()#点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn('12', text,'追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_chase_input12_cancel_revise_case(self):
        '''【修改方案】输入连续追号12期，点击【取消】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_chase_input(12)#追号的输入框输入12
        ssc_cl.revise_cancel()#点击取消修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_times_input12_confirm_revise_case(self):
        '''【修改方案】起始倍数，输入3倍，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_times_input(3)#起始倍数的输入框输入3
        ssc_cl.revise_confirm()#点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text,'倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_times_add_confirm_revise_case(self):
        '''【修改方案】起始倍数，点击+，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_times_add()#点击起始倍数的+
        ssc_cl.revise_confirm()#点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text,'倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_times_sub_confirm_revise_case(self):
        '''【修改方案】起始倍数，点击-，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_times_input(3)
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_sub()#点击起始倍数的-
        ssc_cl.revise_confirm()#点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text,'倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)
    def test_intelligently_chase_ravise_chase_input12_times_input3_confirm_revise_case(self):
        '''【修改方案】输入连续追12期，起始倍数，输入3倍，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        l = Login_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 点击登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()  # 点击关闭浮窗
        hp.cqssc_link()  # 点击重庆时时彩链接
        ssc_cn = CQSSC_ChooseNumber_leyou(self.driver)
        ssc_cn.play_mode()  # 选择模式
        ssc_cn.five_star()  # 选择五星
        ssc_cn.wanwei_random(1)
        ssc_cn.qianwei_random(1)
        ssc_cn.baiwei_random(1)
        self.driver.execute_script("window.scroll(0,300)")
        ssc_cn.shiwei_random(1)
        ssc_cn.gewei_random(1)
        efcn.confirm_number_button()  # 确认选号
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()#点击修改方案
        ssc_cl.revise_chase_input(12)#追号的输入框输入12
        ssc_cl.revise_times_input(3)#起始倍数输入框输入3
        ssc_cl.revise_confirm()#点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertIn('12', text1,'追号期数修改失败')  # 检查是否修改追号期数
        self.assertNotEqual(text,text1)
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-重庆时时彩", trade_name)




