from time import sleep
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_leyou
from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_leyou
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_leyou
from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.login import Login_leyou
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_leyou
from element_operate.UnionLotto.order_details import OrderDetails_leyou
from element_operate.homepage import HomePage_leyou
from test_case.Base.mytest import MyTest


####广西11选5胆拖玩法测试用例 ----mj171101
class gx11X5DanTuoChooseCase(MyTest):
    '''广西11选5胆拖玩法测试流程'''
    def test_dantuo_option2_choose_1_2_case(self):
        '''广西11选5胆拖玩法，任选二玩法，1个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24,16)#选择广西11选5胆拖模式任选二玩法
        efcn.dantuo_choose_num(1,2)#选取1个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()#点击确认选号
    def test_danyuo_many_lottery_and_times_case(self):
        '''胆拖投注，在投注确认页面增加倍数和期数，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 16)  # 选择广西11选5胆拖模式任选二玩法
        efcn.dantuo_choose_num(1, 2)  # 选取1个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
        ecfcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ecfcl.chase_ticket_input(3)  # 输入追3期
        ecfcl.throw_times_input(3)  # 输入投3倍
    def test_danyuo_chase_90_case(self):
        '''胆拖投注，修改期数为90期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 16)  # 选择广西11选5胆拖模式任选二玩法
        efcn.dantuo_choose_num(1, 2)  # 选取1个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
        ecfcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ecfcl.chase_ticket_input("90")  # 输入追90期
        check = ecfcl.lottery_chase_throw_text()  # 获取投注注数、追号期数、投注倍数文本
        self.assertIn("2注90期1倍", check)
    def test_dantuo_option3_choose_1_3_case(self):
        '''广西11选5胆拖玩法，任选三玩法，1个胆码，3个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 17)  # 选择广西11选5胆拖模式任选三玩法
        efcn.dantuo_choose_num(1, 3)  # 选取1个胆码3个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("3", total)  # 检查3注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option3_choose_2_2_case(self):
        '''广西11选5胆拖玩法，任选三玩法，2个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 17)  # 选择广西11选5胆拖模式任选三玩法
        efcn.dantuo_choose_num(2, 2)  # 选取2个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option4_choose_1_4_case(self):
        '''广西11选5胆拖玩法，任选四玩法，1个胆码，4个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 18)  # 选择广西11选5胆拖模式任选四玩法
        efcn.dantuo_choose_num(1, 4)  # 选取1个胆码4个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("4", total)  # 检查4注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option4_choose_2_3_case(self):
        '''广西11选5胆拖玩法，任选四玩法，3个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 18)  # 选择广西11选5胆拖模式任选四玩法
        efcn.dantuo_choose_num(3, 2)  # 选取3个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option5_choose_1_5_case(self):
        '''广西11选5胆拖玩法，任选五玩法，1个胆码，5个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 19)  # 选择广西11选5胆拖模式任选五玩法
        efcn.dantuo_choose_num(1, 5)  # 选取1个胆码5个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("5", total)  # 检查5注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option5_choose_4_2_case(self):
        '''广西11选5胆拖玩法，任选五玩法，4个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 19)  # 选择广西11选5胆拖模式任选五玩法
        efcn.dantuo_choose_num(4, 2)  # 选取4个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option6_choose_1_6_case(self):
        '''广西11选5胆拖玩法，任选六玩法，1个胆码，6个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 20)  # 选择广西11选5胆拖模式任选六玩法
        efcn.dantuo_choose_num(1, 6)  # 选取1个胆码6个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("6", total)  # 检查6注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option6_choose_5_2_case(self):
        '''广西11选5胆拖玩法，任选六玩法，5个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 20)  # 选择广西11选5胆拖模式任选六玩法
        efcn.dantuo_choose_num(5, 2)  # 选取5个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option7_choose_1_7_case(self):
        '''广西11选5胆拖玩法，任选七玩法，1个胆码，7个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 21)  # 选择广西11选5胆拖模式任选七玩法
        efcn.dantuo_choose_num(1, 7)  # 选取1个胆码7个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("7", total)  # 检查7注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_option7_choose_6_2_case(self):
        '''广西11选5胆拖玩法，任选七玩法，6个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 21)  # 选择广西11选5胆拖模式任选七玩法
        efcn.dantuo_choose_num(6, 2)  # 选取6个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
    def test_dantuo_front2_choose_1_2_case(self):
        '''广西11选5胆拖玩法，前二组选玩法，选取1个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24,22)#选择广西11选5胆拖模式前二组选玩法
        efcn.dantuo_choose_num(1,2)#选取1个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()#点击确认选号
    def test_dantuo_front3_choose_1_3_case(self):
        '''广西11选5胆拖玩法，前三组选玩法，1个胆码，3个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24,23)#选择广西11选5胆拖模式前三组选玩法
        sleep(2)
        efcn.dantuo_choose_num(1,3)#选取1个胆码3个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("3", total)  # 检查3注
        efcn.confirm_number_button()#点击确认选号
    def test_dantuo_front3_choose_case(self):
        '''广西11选5胆拖玩法，前三组选玩法，2个胆码，2个拖码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24,23)#选择广西11选5胆拖模式前三组选玩法
        efcn.dantuo_choose_num(2,2)#选取2个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()#点击确认选号
    def test_dantuo_optiops2_intelligent_chase_case(self):###mj20171211
        '''胆拖投注，进入智能追号页面，默认追期，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
        uncl = ConfirmLottery_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        od = OrderDetails_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.My_lottery_ticket()#点击我的彩票
        l = Login_leyou(self.driver)
        l.login_leyou()  # 点击登录
        hp.Home_page()#点击首页
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 16)  # 选择广西11选5胆拖模式任选二玩法
        efcn.dantuo_choose_num(1, 2)  # 选取1个胆码2个拖码
        total = efcn.total_buy_text()  # 获取注数文本
        self.assertIn("2", total)  # 检查2注
        efcn.confirm_number_button()  # 点击确认选号
        ssc_cl.intelligently_chase_button()#点击智能选号
        ssc_cl.submit_button()#点击智能追号的提交按钮
        uncl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐优炫彩-桂11选5", trade_name)
    def test_orderdetails_continue_scheme_case(self):
        '''胆拖投注提交订单之后，查看订单详情，点击继续购买该方案，提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        od = OrderDetails_leyou(self.driver)
        l = Login_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.My_lottery_ticket()  # 点击我的彩票
        l.login_leyou()  # 登录
        hp.homepage_link()  # 点击首页
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()  # 展开玩法
        efcn.mode_choose(24, 16)  # 选择广西11选5胆拖模式任选二玩法
        efcn.dantuo_choose_num(1, 2)  # 选取1个胆码2个拖码
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        sos.check_order_details()  # 点击查看订单详情
        od.Scheme()#点击继续投注该方案
        num1 = efcl.Ele_five_select_number()  # 获取投注确认页的选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付