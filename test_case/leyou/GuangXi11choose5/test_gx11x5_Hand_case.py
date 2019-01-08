from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_leyou
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_leyou
from element_operate.EleChooseFive.EleChooseFive_confirm_lottery import EleChooseFiveConfirmLottery_leyou
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery_leyou
from element_operate.SSC.SSC_confirmlottery import CQSSCConfirmLottery_leyou
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber_leyou
from element_operate.homepage import HomePage_leyou
from element_operate.UnionLotto.submit_order_sucess import SubmitOrderSuccess_leyou
from element_operate.UnionLotto.order_details import OrderDetails_leyou
from element_operate.login import Login_leyou
from test_case.Base.mytest import MyTest
from time import sleep


#广西11选5手选玩法测试用例 --mj171101
class gxEleChooseFiveHandCase(MyTest):
    '''广西11选5手选测试流程'''
    def test_options2_hand_choose2_case(self):
        '''广西11选5，任选二玩法，手选两个号流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)#任选两个号
        efcn.confirm_number_button()#点击确认选号

    def test_options2_hand_choose3_case(self):
        '''广西11选5，任选二玩法，手选三个号流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(3)  # 任选三个号
        efcn.confirm_number_button()  # 点击确认选号
        ecfcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ecfcl.chase_ticket_input("3")  # 输入追3期
        ecfcl.throw_times_input("3")  # 输入投3倍
    def test_options2_hand_choose11_case(self):
        '''广西11选5，任选二玩法，手选11个号流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_delete_num_case(self):
        '''验证选号页的清除按钮，测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        label=efcn.hand_options(2)
        ulcn.clear_number()#点击清除选号按钮
        label2 = efcn.hand_options(2)
        if label != label2:
            print("清除选号成功")
        else:
            print("清除选号失败")
        efcn.confirm_number_button()  # 点击确认选号
    def test_double_cancel_case(self):
        '''验证点击两次号码取消选号，流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.spread_mode_button()##选择展开玩法
        efcn.mode_choose(24,1)#广西11选5任选二
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        lable1 = efcn.hand_options(11)
        total_buy_text = efcn.total_buy_text()
        self.assertIn("55注 ",total_buy_text)
        efcn.hand_options(11)
        total_buy_text = efcn.total_buy_text()
        self.assertIn("请至少选择",total_buy_text)
        lable2 = efcn.hand_options(2)#任选两个球
        if lable1 != lable2:
            print("双击取消选号成功")
        else:
            print("双击取消选号失败")
        efcn.confirm_number_button()#确认选号
    def test_options3_hand_choose3_case(self):
        '''广西11选5，任选三玩法，手选三个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 2)  # 广西11选5任选三
        efcn.hand_options(3)  # 任选3个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options3_hand_choose11_case(self):
        '''广西11选5，任选三玩法，手选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 2)  # 广西11选5任选三
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options4_hand_choose4_case(self):
        '''广西11选5，任选四玩法，手选4个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 3)  # 广西11选5任选四
        efcn.hand_options(4)  # 任选4个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options4_hand_choose11_case(self):
        '''广西11选5，任选四玩法，手选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 3)  # 广西11选5任选四
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options5_hand_choose5_case(self):
        '''广西11选5，任选五玩法，手选5个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 4)  # 广西11选5任选五
        efcn.hand_options(5)  # 任选5个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options5_hand_choose11_case(self):
        '''广西11选5，任选五玩法，手选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 4)  # 广西11选5任选五
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options6_hand_choose6_case(self):
        '''广西11选5，任选六玩法，手选6个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 5)  # 广西11选5任选六
        efcn.hand_options(6)  # 任选6个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options6_hand_choose11_case(self):
        '''广西11选5，任选六玩法，手选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 5)  # 广西11选5任选六
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options7_hand_choose7_case(self):
        '''广西11选5，任选七玩法，手选7个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 6)  # 广西11选5任选七
        efcn.hand_options(7)  # 任选7个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options7_hand_choose11_case(self):
        '''广西11选5，任选七玩法，手选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 6)  # 广西11选5任选七
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options8_hand_choose8_case(self):
        '''广西11选5，任选八玩法，手选8个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 7)  # 广西11选5任选八
        efcn.hand_options(8)  # 任选8个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options8_hand_choose11_case(self):
        '''广西11选5，任选八玩法，手选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 7)  # 广西11选5任选八
        efcn.hand_options(11)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options9_hand_choose1_case(self):
        '''广西11选5，前一玩法，手选1个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 8)  # 广西11选5前一
        efcn.hand_options(1)  # 任选11个号
        efcn.confirm_number_button()  # 点击确认选号
    def test_options10_hand_choose1_1_case(self):
        '''广西11选5，前二直选玩法，前两位各选1个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 9)  # 广西11选5前二直选
        efcn.hand_options(1)#第一位选取1个号码
        efcn.second_num_choose(1)#第二位选取1个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_options10_hand_choose11_11_case(self):
        '''广西11选5，前二直选玩法，前两位各选11个号码流程测试'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 9)  # 广西11选5前二直选
        efcn.hand_options(11)#第一位选取11个号码
        efcn.second_num_choose(11)#第二位选取11个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option11_hand_choose2_case(self):
        '''广西11选5，前二组选玩法，任选两个号码流程测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 10)  # 广西11选5前二直选
        efcn.hand_options(2)  # 任选2个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option12_hand_choose1_1_1_case(self):
        '''广西11选5，前三直选玩法，前三位各选一个号码测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 11)  # 广西11选5前三直选
        efcn.hand_options(1)  # 第一位选取1个号码
        efcn.second_num_choose(1)  # 第二位选取1个号码
        efcn.third_num_choose(1)#第三位选取1个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option12_hand_choose11_11_11_case(self):
        '''广西11选5，前三直选玩法，前三位各选11号码测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 11)  # 广西11选5前三直选
        efcn.hand_options(11)  # 第一位选取11个号码
        efcn.second_num_choose(11)  # 第二位选取11个号码
        efcn.third_num_choose(11)#第三位选取11个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option13_hand_choose3_case(self):
        '''广西11选5，前三组选玩法，任选3号码测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 12)  # 广西11选5前三组选
        efcn.hand_options(3)  #任意选取3个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option14_hand_choose1_1_1_case(self):
        '''广西11选5，乐选三玩法，前三位各选1个号码测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 13)  # 广西11选5乐选三
        efcn.different_three_num(1,1,1)#前三位各选一个号码
        efcn.confirm_number_button()#点击确认选号
    def test_option15_hand_choose3_case(self):
        '''广西11选5，乐选四玩法，任选4号码测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 14)  # 广西11选5乐选四
        efcn.hand_options(4)  #任意选取3个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option16_hand_choose3_case(self):
        '''广西11选5，乐选五玩法，任选5号码测试流程'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 15)  # 广西11选5乐选五
        efcn.hand_options(5)  #任意选取5个号码
        efcn.confirm_number_button()  # 点击确认选号
    def test_option2_many_lottery_case(self):#####--mj21071211
        '''手动选号，单式，多注一倍，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        l = Login_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选两个号
        efcn.confirm_number_button()  # 点击确认选号
        efcl.continue_choose_num()#点击继续选号
        efcn.hand_options(2)#任选两个号码
        efcn.confirm_number_button()#点击确认选号
        efcl.submit_order_button()#点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
    def test_play_instruction_case(self):
        '''在投注选号页面，点击右上角玩法说明，可以打开和关闭'''
        hp = HomePage_leyou(self.driver)
        tD = There_D_choosenumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        ulcn.There_clock()#点击选号页的。。。
        tD.Play_instruction()#点击玩法说明
        tD.There_D_know()#点击我知道了
        text1 = efcn.total_buy_text()
        self.assertIn("请至少选择",text1)
    def test_mix_lottery_case(self):
        '''多注（复式、单式组合）选号，提交订单'''
        hp = HomePage_leyou(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        l = Login_leyou(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选两个号
        efcn.confirm_number_button()  # 点击确认选号
        efcl.continue_choose_num()  # 点击继续选号
        efcn.hand_options(3)  # 任选两个号码
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        text1=efcl.lottery_chase_throw_text()#获取期数和投注倍数
        self.assertIn("4注1期1倍",text1)
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
    def test_recommendation_one_lottery_one_times_case(self):
        '''选号页面，点开历史开奖，使用推荐号码投注（一注一倍），提交订单'''
        hp = HomePage_leyou(self.driver)
        tD = There_D_choosenumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        od = OrderDetails_leyou(self.driver)
        l =Login_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()#展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        ulcn.There_clock()  # 点击选号页的。。。
        efcn.history_trend()#点击历史走势
        efcn.recommendation_choose_num(2)#选择两个号码
        efcn.use_recommendation()#点击使用推荐号码
        efcn.confirm_number_button()  # 点击确认选号
        num1 = efcl.Ele_five_select_number()#获取投注确认页的选号
        efcl.submit_order_button()  # 点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()#点击查看订单详情
        num2 = od.Ele_five_betting_nu()#获取订单详情页的号码
        self.assertEqual(num1,num2)
    def test_recommendation_case(self):
        '''选号页面，点击右上方隐藏的“历史走势”按钮，点击使用推荐号码，提交订单'''
        hp = HomePage_leyou(self.driver)
        tD = There_D_choosenumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        od = OrderDetails_leyou(self.driver)
        l =Login_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()#展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        ulcn.There_clock()  # 点击选号页的。。。
        efcn.history_trend()#点击历史走势
        efcn.use_recommendation()#点击使用推荐号码
        efcn.confirm_number_button()  # 点击确认选号
        num1 = efcl.Ele_five_select_number()#获取投注确认页的选号
        efcl.submit_order_button()  # 点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()#点击查看订单详情
        num2 = od.Ele_five_betting_nu()#获取订单详情页的号码
        self.assertEqual(num1,num2)
    def test_recommendation_many_lottery_many_times_case(self):
        '''选号页面，点开历史开奖，使用推荐号码投注（多注多倍），提交订单'''
        hp = HomePage_leyou(self.driver)
        tD = There_D_choosenumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        od = OrderDetails_leyou(self.driver)
        l =Login_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()#展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        ulcn.There_clock()  # 点击选号页的。。。
        efcn.history_trend()#点击历史走势
        efcn.recommendation_choose_num(4)#选择两个号码
        efcn.use_recommendation()#点击使用推荐号码
        efcn.confirm_number_button()  # 点击确认选号
        num1 = efcl.Ele_five_select_number()#获取投注确认页的选号
        efcl.submit_order_button()  # 点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()#点击查看订单详情
        num2 = od.Ele_five_betting_nu()#获取订单详情页的号码
        self.assertEqual(num1,num2)
    def test_User_agreement_case(self):
        '''投注确认页面，点击用户协议，能够打开和关闭'''
        hp = HomePage_leyou(self.driver)
        tD = There_D_choosenumber_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        od = OrderDetails_leyou(self.driver)
        l = Login_leyou(self.driver)
        sos = SubmitOrderSuccess_leyou(self.driver)
        cl = ConfirmLottery_leyou(self.driver)
        hp.open()
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()  # 展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选两个号
        sleep(2)
        efcn.confirm_number_button()  # 点击确认选号
        num1 = efcl.Ele_five_select_number()  # 获取投注确认页的选号
        cl.User_agreement()#点击《用户协议》
        cl.User_know()#点击【我知道了】
        efcl.submit_order_button()  # 点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()  # 点击查看订单详情
        num2 = od.Ele_five_betting_nu()  # 获取订单详情页的号码
        self.assertEqual(num1, num2)
    def test_Investment_risk_case(self):
        '''投注确认页面，点击购彩风险，能够打开和关闭'''
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
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()  # 展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选两个号
        sleep(2)
        efcn.confirm_number_button()  # 点击确认选号
        num1 = efcl.Ele_five_select_number()  # 获取投注确认页的选号
        cl.Risk()#点击《风险提示》
        cl.Risk_know()#点击《我知道了》
        efcl.submit_order_button()  # 点击提交订单给站主
        l.login_leyou()  # 点击登录
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()  # 点击查看订单详情
        num2 = od.Ele_five_betting_nu()  # 获取订单详情页的号码
        self.assertEqual(num1, num2)
    def test_success_page_continue_buy_case(self):
        '''订单提交成功页面，点击继续投注该彩种，能够跳转到彩种选号页面'''
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
        hp.My_lottery_ticket()#点击我的彩票
        l.login_leyou()#登录
        hp.homepage_link()#点击首页
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()  # 展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选两个号
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        sos.Continue_buy()#点击机选购买此彩种
        efcn.hand_options(3)  # 任选3个号
        efcn.confirm_number_button()  # 点击确认选号
        num1 = efcl.Ele_five_select_number()  # 获取投注确认页的选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()#点击查看订单详情
        num2 = od.Ele_five_betting_nu()  # 获取订单详情页的号码
        self.assertEqual(num1, num2)
    def test_orderdetails_page_continue_buy_case(self):
        '''订单详情页面，点击继续购买该方案，可以跳转到选号确认页面，提交订单'''
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
        hp.My_lottery_ticket()#点击我的彩票
        l.login_leyou()#登录
        hp.homepage_link()#点击首页
        hp.Moveable_float_close()
        hp.gx_11_5_link()  # 点击广西11选5链接
        efcn.spread_mode_button()  # 展开玩法
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选两个号
        efcn.confirm_number_button()  # 点击确认选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        sos.check_order_details()#点击查看订单详情
        od.continue_buy()#点击继续投注该彩种
        efcn.hand_options(3)  # 任选3个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("3注1期1倍", text1)
        num1 = efcl.Ele_five_select_number()  # 获取投注确认页的选号
        efcl.submit_order_button()  # 点击提交订单给站主
        cl.confirm_and_pay_button()  ##点击确认并支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)
        sos.check_order_details()#点击查看订单详情
        num2 = od.Ele_five_betting_nu()  # 获取订单详情页的号码
        self.assertEqual(num1, num2)

    def test_many_lottery_many_times_case(self):
        '''复式多注，进入智能追号页面，默认追期，提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(4)  # 任选4个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("6注1期1倍",text1)
        efcl.continue_choose_num()#点击继续选号
        efcn.hand_options(4)#点击任选4个号码
        efcn.confirm_number_button()  # 点击确认选号
        text2 = efcl.lottery_chase_throw_text()
        self.assertIn("12注1期1倍", text2)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.submit_button()  # 点击提交订单

    ###############20171213
    def test_intelligently_input_periods_case(self):
        '''进入智能追号页面，输入追11期，点击【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.znzh_issue_num_input(11)  # 输入追11期
        ssc_cl.totalIssue()  # 更新追号期数
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2 + 1), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_chase_add_confirm_revise_case(self):
        '''【修改方案】点击连续追+按钮，点击【确定】，【提交】，提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_add()  # 点击追号的+按钮
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2 + 1), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_chase_sub_confirm_revise_case(self):
        '''【修改方案】点击连续追-按钮，点击【确定】，【提交】，提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_sub()  # 点击追号的-按钮
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2 - 1), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_chase_input12_confirm_revise_case(self):
        '''【修改方案】输入连续追号12期，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(12)  # 追号的输入框输入12
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        self.assertIn('12', text, '追号期数修改失败')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_chase_input12_cancel_revise_case(self):
        '''【修改方案】输入连续追号12期，点击【取消】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text2 = ssc_cl.totalIssue_num()  # 获取追号期数文本
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(12)  # 追号的输入框输入12
        ssc_cl.revise_cancel()  # 点击取消修改
        text = ssc_cl.totalIssue_text()
        self.assertIn(str(text2), text)  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_times_input12_confirm_revise_case(self):
        '''【修改方案】起始倍数，输入3倍，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_input(3)  # 起始倍数的输入框输入3
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text, '倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_times_add_confirm_revise_case(self):
        '''【修改方案】起始倍数，点击+，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_add()  # 点击起始倍数的+
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text, '倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_times_sub_confirm_revise_case(self):
        '''【修改方案】起始倍数，点击-，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_input(3)
        ssc_cl.revise_confirm()  # 点击确认修改
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_times_sub()  # 点击起始倍数的-
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertNotEqual(text1, text, '倍数没有被修改')  # 检查是否修改追号期数
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)

    def test_intelligently_chase_ravise_chase_input12_times_input3_confirm_revise_case(self):
        '''【修改方案】输入连续追12期，起始倍数，输入3倍，点击【确定】，【提交】提交订单'''
        hp = HomePage_leyou(self.driver)
        ulcn = UnionLottoChooseNumber_leyou(self.driver)
        efcn = ElevenFiveChooseNumber_leyou(self.driver)
        efcl = EleChooseFiveConfirmLottery_leyou(self.driver)
        ssc_cl = CQSSCConfirmLottery_leyou(self.driver)
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
        efcn.mode_choose(24, 1)  # 广西11选5任选二
        efcn.hand_options(2)  # 任选2个号
        efcn.confirm_number_button()  # 点击确认选号
        text1 = efcl.lottery_chase_throw_text()
        self.assertIn("1注1期1倍", text1)
        ssc_cl.intelligently_chase_button()  # 点击智能追号
        text = ssc_cl.totalIssue_text()
        ssc_cl.revise_button()  # 点击修改方案
        ssc_cl.revise_chase_input(12)  # 追号的输入框输入12
        ssc_cl.revise_times_input(3)  # 起始倍数输入框输入3
        ssc_cl.revise_confirm()  # 点击确认修改
        text1 = ssc_cl.totalIssue_text()
        self.assertIn('12', text1, '追号期数修改失败')  # 检查是否修改追号期数
        self.assertNotEqual(text, text1)
        ssc_cl.submit_button()  # 点击提交按钮
        cl.confirm_and_pay_button()  # 点击确认支付
        hp.Moveable_float_close()  # 如果出现浮层弹框，关闭
        text2 = sos.submit_order_success()  # 获取页面“订单提交成功”文本
        self.assertEqual("订单提交成功", text2)
        trade_name = sos.trade_name_text()  # 获取页面商品名称文本
        self.assertIn("商品名称：乐仑炫彩-桂11选5", trade_name)