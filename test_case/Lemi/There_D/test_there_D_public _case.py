from element_operate.Arrange_five.Arrange_five_choosenumber import ArrangeFiveChooseNumber
from element_operate.Arrange_five.Arrange_five_confirm import ArrangeFiveConfirmLottery
from element_operate.Arrange_there.Arrang_there_choosenumber import Arrang_there_choosenumber
from element_operate.There_D.three_D_choosenumber import There_D_choosenumber
from  element_operate.UnionLotto.UnionLotto_choosenumber import UnionLottoChooseNumber
from element_operate.UnionLotto.confirm_lottery import ConfirmLottery
from element_operate.homepage import HomePage
from element_operate.login import Login
from test_case.Base.mytest import MyTest
class There_D_public_case(MyTest):
    """验证3D公有场景"""
    def test_there_D_play_case(self):
        """验证3D投注选号页面，切换玩法"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Play_d()  ###点击玩法
        hb.Play_direct_d()##点击直选
        mur=hb.Show_play()
        self.assertEqual('直选',mur)
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_d()#####点击组三
        mur = hb.Show_play()
        self.assertEqual('组三', mur)
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_d()####点击组六
        mur = hb.Show_play()
        self.assertEqual('组六', mur)
        hb.Play_d()  ###点击玩法
        hb.Play_group_direct_add_d()###点击直选和值
        mur = hb.Show_play()
        self.assertEqual('直选和值', mur)
        hb.Play_d()  ###点击玩法
        hb.Play_group_there_add_d()#####点击组三和值
        mur = hb.Show_play()
        self.assertEqual('组三和值', mur)
        hb.Play_d()  ###点击玩法
        hb.Play_group_six_add_d()##点击组六和值
        mur = hb.Show_play()
        self.assertEqual('组六和值', mur)

    def test_there_D_play_instruction(self):
        """验证玩法说明"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Instruct()##点击右上角...
        hb.Play_instruction()##点击玩法说明
        mur=hb.Group_there_add_play_instruction()
        self.assertEqual('组三和值',mur)
        hb.There_D_know()

    def test_there_D_history(self):
        """验证历史走势"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Instruct()  ##点击右上角...
        hb.History()###点击历史投注
        mur=hb.Charts()
        if mur=='':
            self.assertEqual('a',mur)
        else:
            print("历史走势展示正常")

    def test_there_D_history_recommend(self):
        """验证历史走势，使用推荐号码"""
        ha = HomePage(self.driver)
        hb = There_D_choosenumber(self.driver)
        hb1 = ArrangeFiveChooseNumber(self.driver)
        hb2 = UnionLottoChooseNumber(self.driver)
        hc = ConfirmLottery(self.driver)
        hd = ArrangeFiveConfirmLottery(self.driver)
        hl = Login(self.driver)
        ha.open()
        ######判断是否出现浮层弹框，如果出现浮层点击X，然后执行下一步操作
        ha.Moveable_float_close()
        ha.fucai_3D_link()  ###点击3D
        hb.Instruct()  ##点击右上角...
        hb.History()###点击历史投注
        mur=hb.Recommend()
        hb.Use_recommend()###点击使用推荐号码
        hb1.Confirm_nu()  # 点击确认选号
        mur1=hb.Number()
        self.assertIn(mur,mur1)
        hc.submit_order_to_station_owner_button()  ##点击提交给站主
        hl.new_user_login_tab()  # 点击新登录
        hl.login()  # 输入账号，密码
        hc.submit_order_to_station_owner_button()  # 点击提交给站主
        hc.confirm_and_pay_button()  # 点击确认支付

