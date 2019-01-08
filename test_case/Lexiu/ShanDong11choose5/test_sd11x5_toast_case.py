from element_operate.EleChooseFive.EleChooseFive_choosenumber import ElevenFiveChooseNumber_lexiu
from element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber_lexiu
from element_operate.homepage import HomePage_lexiu
from test_case.Base.mytest import MyTest


##山东11选5 toast提示信息验证测试用例  ----mj20171102
class SD11x5ToastCase(MyTest):
    def test_dantuo_front3_choose_out_case(self):
        '''山东11选5胆拖玩法，前三组选玩法，3个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,23)  # 选择山东11选5胆拖模式前三组选玩法
        efcn.hand_options(3  )  # 选取3个胆码
        toast = ulcn.out_of_num(  )  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_front2_choose_out_case(self):
        '''山东11选5胆拖玩法，前二组选玩法，2个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,22)  # 选择山东11选5胆拖模式前二组选玩法
        efcn.hand_options(2  )  # 选取2个胆码
        toast = ulcn.out_of_num(  )  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_option7_choose_out_case(self):
        '''山东11选5胆拖玩法，任选七玩法，7个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,21)  # 选择山东11选5胆拖模式任选七玩法
        efcn.hand_options(7  )  # 选取7个胆码
        toast = ulcn.out_of_num(  )  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_option6_choose_out_case(self):
        '''山东11选5胆拖玩法，任选六玩法，6个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,20)  # 选择山东11选5胆拖模式任选六玩法
        efcn.hand_options(6)  # 选取6个胆码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_option5_choose_out_case(self):
        '''山东11选5胆拖玩法，任选五玩法，5个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,19)  # 选择山东11选5胆拖模式任选五玩法
        efcn.hand_options(5)  # 选取5个胆码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_option4_choose_out_case(self):
        '''山东11选5胆拖玩法，任选四玩法，4个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22 ,18  )  # 选择山东11选5胆拖模式任选四玩法
        efcn.hand_options(4  )  # 选取4个胆码
        toast = ulcn.out_of_num(  )  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_option3_choose_out_case(self):
        '''山东11选5胆拖玩法，任选三玩法，3个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,17)  # 选择山东11选5胆拖模式任选三玩法
        efcn.hand_options(3  )  # 选取3个胆码
        toast = ulcn.out_of_num(  )  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!" ,toast)
    def test_dantuo_option2_choose_out_case(self):
        '''山东11选5胆拖玩法，任选二玩法，2个胆码，提示“胆码个数超过限制”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,16)  # 选择山东11选5胆拖模式任选二玩法
        efcn.hand_options(2)  # 选取2个胆码
        toast = ulcn.out_of_num(  )  # 获取toast提示信息
        self.assertEqual("胆码个数超过限制!",toast)
    def test_option15_choose_out_case(self):
        '''山东11选5普通玩法，乐选五玩法，选取6个号码，提示“只支持单式投注”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,15)  # 选择山东11选5普通模式乐选五玩法
        efcn.hand_options(6)  # 选取6个号码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("只支持单注投注",toast)
    def test_option14_choose_out_case(self):
        '''山东11选5普通玩法，乐选四玩法，选取5个号码，提示“只支持单式投注”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,14)  # 选择山东11选5普通模式乐选四玩法
        efcn.hand_options(5)  # 选取5个号码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("只支持单注投注" ,toast)
    def test_option13_choose_out_case(self):
        '''山东11选5普通玩法，乐选三玩法，三位各选两个号码，提示“只支持单式投注”流程测试'''
        hp = HomePage_lexiu(self.driver)
        hp.open()
        ulcn = UnionLottoChooseNumber_lexiu(self.driver)
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        hp.Moveable_float_close()
        hp.sd_11_5_link()  # 点击山东11选5链接
        efcn = ElevenFiveChooseNumber_lexiu(self.driver)
        efcn.countdown_text()  # 检查“距离第xxx期截止：”文案是否存在
        efcn.spread_mode_button()  ##选择展开玩法
        efcn.mode_choose(22,13)  # 选择山东11选5普通模式乐选三玩法
        efcn.lexuan_choose(2,1)  # 第一位选取2个号码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("只支持单注投注" ,toast)
        efcn.lexuan_choose(2,2)  # 第二位选取2个号码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("只支持单注投注", toast)
        js = "window.scroll(0,300)"
        self.driver.execute_script(js)
        efcn.lexuan_choose(2,3)  # 第三位选取2个号码
        toast = ulcn.out_of_num()  # 获取toast提示信息
        self.assertEqual("只支持单注投注", toast)