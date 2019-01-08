from element_position.lemi import SingleFootLotteryConfirm_loc
from element_operate.base import Page
from element_position.lexiu import SingleFootLotteryConfirm_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import SingleFootLotteryConfirm_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import SingleFootLotteryConfirm_lelun_loc
from element_operate.base import Page_lelun

###竞足单关的投注确认页的元素操作----mj171120
class SingleFootConfirmLottery(Page,SingleFootLotteryConfirm_loc):

    # 获取投注倍数的文本
    def lottery_times_text(self):
        times_text = self.find_element(*self.lottery_times_text_loc).text
        return times_text

    def Times_display_pbs(self):
        a=self.find_element(*self.lottery_times_text_loc).text####读取投注显示的文本
        print(a)
        return a

    def Lottery_dgp(self):
        a=self.find_element(*self.lottery_dgp).text##读取投注金额
        return a

class SingleFootConfirmLottery_lexiu(Page_lexiu,SingleFootLotteryConfirm_lexiu_loc):

    # 获取投注倍数的文本
    def lottery_times_text(self):
        times_text = self.find_element(*self.lottery_times_text_loc).text
        return times_text

    def Times_display_pbs(self):
        a=self.find_element(*self.lottery_times_text_loc).text####读取投注显示的文本
        print(a)
        return a

    def Lottery_dgp(self):
        a=self.find_element(*self.lottery_dgp).text##读取投注金额
        return a

class SingleFootConfirmLottery_leyou(Page_leyou,SingleFootLotteryConfirm_leyou_loc):

    # 获取投注倍数的文本
    def lottery_times_text(self):
        times_text = self.find_element(*self.lottery_times_text_loc).text
        return times_text

    def Times_display_pbs(self):
        a=self.find_element(*self.lottery_times_text_loc).text####读取投注显示的文本
        print(a)
        return a

    def Lottery_dgp(self):
        a=self.find_element(*self.lottery_dgp).text##读取投注金额
        return a

class SingleFootConfirmLottery_lelun(Page_lelun,SingleFootLotteryConfirm_lelun_loc):

    # 获取投注倍数的文本
    def lottery_times_text(self):
        times_text = self.find_element(*self.lottery_times_text_loc).text
        return times_text

    def Times_display_pbs(self):
        a=self.find_element(*self.lottery_times_text_loc).text####读取投注显示的文本
        print(a)
        return a

    def Lottery_dgp(self):
        a=self.find_element(*self.lottery_dgp).text##读取投注金额
        return a