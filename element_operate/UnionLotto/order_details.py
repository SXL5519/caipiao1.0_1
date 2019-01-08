from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import OderDetails_loc
from selenium.common.exceptions import TimeoutException, NoSuchElementException,WebDriverException
import time
from element_operate.base import Page_lexiu
from element_position.lexiu import OderDetails_lexiu_loc
from element_operate.base import Page_leyou
from element_position.leyou import OderDetails_leyou_loc
from element_operate.base import Page_lelun
from element_position.lelun import OderDetails_lelun_loc


class OrderDetails(Page,OderDetails_loc):
    def order_amount_sum(self):
        try:
            self.wait_element_located(self.driver, self.amount_sum_loc)
            amount_sum_text = self.find_element(*self.amount_sum_loc).text
            if amount_sum_text:
                print("投注金额：" + amount_sum_text+"元")
                return amount_sum_text
        except WebDriverException:
            print("元素\“方案金额\”不存在")
            raise
    #获取"订单状态"文本
    def order_status(self):
        self.wait_element_located(self.driver,self.order_status_loc)
        status_text = self.find_element(*self.order_status_loc).text
        print("订单状态：" + status_text)
        return status_text
    #获取“方案内容”中"投注号码"
    def number_bet(self):
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")
            raise
    #获取5注以上“方案内容”中的投注号码
    def number_bets(self):
        try:
            self.find_element(*self.expand_more_link_loc).click()
        except NoSuchElementException:
            print("“展开更多”按钮缺失")
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")


    #获取“开奖时间”文本
    def official_open_time(self):
        self.wait_element_located(self.driver,self.official_open_time_loc)
        offical_open_time = self.find_element(*self.official_open_time_loc).text
        print("开奖时间：" + offical_open_time)
        return offical_open_time
    #获取“基本信息”中订单编号
    def order_number(self):
        self.wait_element_located(self.driver,self.order_number_loc)
        order_number_text = self.find_element(*self.order_number_loc).text
        print("订单编号：" + order_number_text)
        return order_number_text


    ##追号玩法订单详情页
    #获取玩法文本
    def union_top_text(self):
        self.wait_element_located(self.driver,self.union_top_text_loc)
        union_top_text = self.find_element(*self.union_top_text_loc).text
        return union_top_text
    #点击“停止追号”按钮
    def stop_chase_button(self):
        try:
            self.find_element(*self.stop_chase_button_loc)
            return True
        except NoSuchElementException:
            print("停止追号按钮缺失")
            return False
    #确认停止追号
    def confirm_stop_chase_button(self):
        self.wait_element_located(self.driver,self.confirm_stop_chase_loc)
        self.find_element(*self.confirm_stop_chase_loc).click()
    #取消停止追号
    def cancel_stop_chase_button(self):
        self.wait_element_located(self.driver,self.cancel_stop_chase_loc)
        self.find_element(*self.cancel_stop_chase_loc).click()
    #获取投注金额文本
    def amount_sum_text(self):
        try:
            amount_sum = self.find_element(*self.chase_amount_sum_loc).text
            if amount_sum != None:
                print("投注金额为：" + amount_sum)
                return amount_sum
        except NoSuchElementException:
            print("元素\“投注金额\”不存在")


    #获取投注号码定位
    def chase_number_bets(self):
        number = self.find_element(self.number_bets_loc).text#获取投注号码
        return number

    # 获取追号id
    def chase_id_text(self):
        try:
            chase_id = self.find_element(*self.chase_id_text_loc).text
            if chase_id != None:
                print("追号ID为：" + chase_id)
                return chase_id
        except NoSuchElementException:
            print("元素\“追号ID\”不存在")

    # 获取追号状态
    def chase_state_text(self):
        try:
            chase_state = self.find_element(*self.chase_state_text_loc).text
            if chase_state != None:
                print("追号状态为：" + chase_state)
                return chase_state
        except NoSuchElementException:
            print("元素\“追号状态\”不存在")
    #少于等于5注的详情页检查
    def order_details_check(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bet()
        self.official_open_time()
        self.order_number()

    #大于5注的详情页检查
    def order_details_checks(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bets()
        self.official_open_time()
        self.order_number()
    #追期玩法详情页面检查
    def chase_order_details_check(self):
        self.union_top_text()
        self.stop_chase_button()
        self.amount_sum_text()
        #self.chase_number_bets()
        self.chase_id_text()
        self.chase_state_text()

    def Betting_number(self):#读取详情页显示的投注号码，排序并以整型的形式输出
        list=[]
        a=self.find_elements(*self.betting_number)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            list.append(int(aa))
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Betting_nu(self):#读取详情页显示的投注号码，以字符串形式输出
        list=[]
        c=''
        a=self.find_elements(*self.betting_number)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            if i>0:
                c=c+' '+aa
            else:
                c=c+aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list

    def Pay_case(self):
        a=self.find_element(*self.pay_case).text##读取支付情况
        return a

    def Scheme(self):
        self.find_element(*self.scheme).click()###点击继续购买该方案

    def bet_number(self):##获取订单详情页，投注号码---mj20171207
        bet_num = self.find_element(*self.number_bet_loc).text
        return bet_num
    def continue_buy(self):#点击继续购买此彩种
        self.find_element(*self.continue_buy_loc).click()
    def Ele_five_betting_nu(self):#11选5读取订单详情页面的投注号码 ----mj20171211
        list = []
        c = ''
        a = self.find_elements(*self.betting_number)
        print("读取订单详情页的号码%s" % a)
        for i in range(len(a)):
            aa = self.find_element(*self.Ele_five_betting_loc(i + 1)).text
            if i > 0:
                c = c + ' ' + aa
            else:
                c = c + aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list
    def scheme_details(self):##获取订单详情页文本---mj20171215
        text =self.find_element(*self.scheme_details_loc).text
        return text
    def score_direct_broadcast_link(self):#点击比分直播链接
        self.wait_element_located(self.driver,self.score_direct_broadcast_link_loc)
        self.find_element(*self.score_direct_broadcast_link_loc).click()
    def play_instruct(self):#点击玩法说明链接
        self.wait_element_located(self.driver,self.play_instruct_loc)
        self.find_element(*self.play_instruct_loc).click()
    def function_instruct(self):##点击功能说明链接
        self.wait_element_located(self.driver,self.function_instruct_loc)
        self.find_element(*self.function_instruct_loc).click()
    def i_know(self):#点击【知道了】按钮
        self.wait_element_located(self.driver,self.i_know_loc)
        self.find_element(*self.i_know_loc).click()

    def Betting_after(self):
        list=[]
        a=self.find_element(*self.betting_after).text##读取号码
        b=a.replace('|',',')
        #b1=b[4:].strip(' ')
        b2=b.replace(',',' ')
        list.append(b2)
        print(list)
        return list

class OrderDetails_lexiu(Page_lexiu,OderDetails_lexiu_loc):
    def order_amount_sum(self):
        try:
            self.wait_element_located(self.driver, self.amount_sum_loc)
            amount_sum_text = self.find_element(*self.amount_sum_loc).text
            if amount_sum_text:
                print("投注金额：" + amount_sum_text+"元")
                return amount_sum_text
        except WebDriverException:
            print("元素\“方案金额\”不存在")
            raise
    #获取"订单状态"文本
    def order_status(self):
        self.wait_element_located(self.driver,self.order_status_loc)
        status_text = self.find_element(*self.order_status_loc).text
        print("订单状态：" + status_text)
        return status_text
    #获取“方案内容”中"投注号码"
    def number_bet(self):
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")
            raise
    #获取5注以上“方案内容”中的投注号码
    def number_bets(self):
        try:
            self.find_element(*self.expand_more_link_loc).click()
        except NoSuchElementException:
            print("“展开更多”按钮缺失")
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")


    #获取“开奖时间”文本
    def official_open_time(self):
        self.wait_element_located(self.driver,self.official_open_time_loc)
        offical_open_time = self.find_element(*self.official_open_time_loc).text
        print("开奖时间：" + offical_open_time)
        return offical_open_time
    #获取“基本信息”中订单编号
    def order_number(self):
        self.wait_element_located(self.driver,self.order_number_loc)
        order_number_text = self.find_element(*self.order_number_loc).text
        print("订单编号：" + order_number_text)
        return order_number_text


    ##追号玩法订单详情页
    #获取玩法文本
    def union_top_text(self):
        self.wait_element_located(self.driver,self.union_top_text_loc)
        union_top_text = self.find_element(*self.union_top_text_loc).text
        return union_top_text
    #点击“停止追号”按钮
    def stop_chase_button(self):
        try:
            self.find_element(*self.stop_chase_button_loc)
            return True
        except NoSuchElementException:
            print("停止追号按钮缺失")
            return False
    #确认停止追号
    def confirm_stop_chase_button(self):
        self.wait_element_located(self.driver,self.confirm_stop_chase_loc)
        self.find_element(*self.confirm_stop_chase_loc).click()
    #取消停止追号
    def cancel_stop_chase_button(self):
        self.wait_element_located(self.driver,self.cancel_stop_chase_loc)
        self.find_element(*self.cancel_stop_chase_loc).click()
    #获取投注金额文本
    def amount_sum_text(self):
        try:
            amount_sum = self.find_element(*self.chase_amount_sum_loc).text
            if amount_sum != None:
                print("投注金额为：" + amount_sum)
                return amount_sum
        except NoSuchElementException:
            print("元素\“投注金额\”不存在")


    #获取投注号码定位
    def chase_number_bets(self):
        number = self.find_element(self.number_bets_loc).text#获取投注号码
        return number

    # 获取追号id
    def chase_id_text(self):
        try:
            chase_id = self.find_element(*self.chase_id_text_loc).text
            if chase_id != None:
                print("追号ID为：" + chase_id)
                return chase_id
        except NoSuchElementException:
            print("元素\“追号ID\”不存在")

    # 获取追号状态
    def chase_state_text(self):
        try:
            chase_state = self.find_element(*self.chase_state_text_loc).text
            if chase_state != None:
                print("追号状态为：" + chase_state)
                return chase_state
        except NoSuchElementException:
            print("元素\“追号状态\”不存在")
    #少于等于5注的详情页检查
    def order_details_check(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bet()
        self.official_open_time()
        self.order_number()

    #大于5注的详情页检查
    def order_details_checks(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bets()
        self.official_open_time()
        self.order_number()
    #追期玩法详情页面检查
    def chase_order_details_check(self):
        self.union_top_text()
        self.stop_chase_button()
        self.amount_sum_text()
        #self.chase_number_bets()
        self.chase_id_text()
        self.chase_state_text()

    def Betting_number(self):#读取详情页显示的投注号码，排序并以整型的形式输出
        list=[]
        a=self.find_elements(*self.betting_number)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            list.append(int(aa))
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Betting_nu(self):#读取详情页显示的投注号码，以字符串形式输出
        list=[]
        c=''
        a=self.find_elements(*self.betting_number)
        print(a)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            if i>0:
                c=c+' '+aa
            else:
                c=c+aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list

    def Pay_case(self):
        a=self.find_element(*self.pay_case).text##读取支付情况
        return a

    def Scheme(self):
        self.find_element(*self.scheme).click()###点击继续购买该方案

    def bet_number(self):##获取订单详情页，投注号码---mj20171207
        bet_num = self.find_element(*self.number_bet_loc).text
        return bet_num
    def continue_buy(self):#点击继续购买此彩种
        self.find_element(*self.continue_buy_loc).click()
    def Ele_five_betting_nu(self):#11选5读取订单详情页面的投注号码 ----mj20171211
        list = []
        c = ''
        a = self.find_elements(*self.betting_number)
        print("读取订单详情页的号码%s" % a)
        for i in range(len(a)):
            aa = self.find_element(*self.Ele_five_betting_loc(i + 1)).text
            if i > 0:
                c = c + ' ' + aa
            else:
                c = c + aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list
    def scheme_details(self):##获取订单详情页文本---mj20171215
        text =self.find_element(*self.scheme_details_loc).text
        return text
    def score_direct_broadcast_link(self):#点击比分直播链接
        self.wait_element_located(self.driver,self.score_direct_broadcast_link_loc)
        self.find_element(*self.score_direct_broadcast_link_loc).click()
    def play_instruct(self):#点击玩法说明链接
        self.wait_element_located(self.driver,self.play_instruct_loc)
        self.find_element(*self.play_instruct_loc).click()
    def function_instruct(self):##点击功能说明链接
        self.wait_element_located(self.driver,self.function_instruct_loc)
        self.find_element(*self.function_instruct_loc).click()
    def i_know(self):#点击【知道了】按钮
        self.wait_element_located(self.driver,self.i_know_loc)
        self.find_element(*self.i_know_loc).click()

    def Betting_after(self):
        list=[]
        a=self.find_element(*self.betting_after).text##读取号码
        b=a.replace('|',',')
        #b1=b[4:].strip(' ')
        b2=b.replace(',',' ')
        list.append(b2)
        print(list)
        return list

class OrderDetails_leyou(Page_leyou,OderDetails_leyou_loc):
    def order_amount_sum(self):
        try:
            self.wait_element_located(self.driver, self.amount_sum_loc)
            amount_sum_text = self.find_element(*self.amount_sum_loc).text
            if amount_sum_text:
                print("投注金额：" + amount_sum_text+"元")
                return amount_sum_text
        except WebDriverException:
            print("元素\“方案金额\”不存在")
            raise
    #获取"订单状态"文本
    def order_status(self):
        self.wait_element_located(self.driver,self.order_status_loc)
        status_text = self.find_element(*self.order_status_loc).text
        print("订单状态：" + status_text)
        return status_text
    #获取“方案内容”中"投注号码"
    def number_bet(self):
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")
            raise
    #获取5注以上“方案内容”中的投注号码
    def number_bets(self):
        try:
            self.find_element(*self.expand_more_link_loc).click()
        except NoSuchElementException:
            print("“展开更多”按钮缺失")
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")


    #获取“开奖时间”文本
    def official_open_time(self):
        self.wait_element_located(self.driver,self.official_open_time_loc)
        offical_open_time = self.find_element(*self.official_open_time_loc).text
        print("开奖时间：" + offical_open_time)
        return offical_open_time
    #获取“基本信息”中订单编号
    def order_number(self):
        self.wait_element_located(self.driver,self.order_number_loc)
        order_number_text = self.find_element(*self.order_number_loc).text
        print("订单编号：" + order_number_text)
        return order_number_text


    ##追号玩法订单详情页
    #获取玩法文本
    def union_top_text(self):
        self.wait_element_located(self.driver,self.union_top_text_loc)
        union_top_text = self.find_element(*self.union_top_text_loc).text
        return union_top_text
    #点击“停止追号”按钮
    def stop_chase_button(self):
        try:
            self.find_element(*self.stop_chase_button_loc)
            return True
        except NoSuchElementException:
            print("停止追号按钮缺失")
            return False
    #确认停止追号
    def confirm_stop_chase_button(self):
        self.wait_element_located(self.driver,self.confirm_stop_chase_loc)
        self.find_element(*self.confirm_stop_chase_loc).click()
    #取消停止追号
    def cancel_stop_chase_button(self):
        self.wait_element_located(self.driver,self.cancel_stop_chase_loc)
        self.find_element(*self.cancel_stop_chase_loc).click()
    #获取投注金额文本
    def amount_sum_text(self):
        try:
            amount_sum = self.find_element(*self.chase_amount_sum_loc).text
            if amount_sum != None:
                print("投注金额为：" + amount_sum)
                return amount_sum
        except NoSuchElementException:
            print("元素\“投注金额\”不存在")


    #获取投注号码定位
    def chase_number_bets(self):
        number = self.find_element(self.number_bets_loc).text#获取投注号码
        return number

    # 获取追号id
    def chase_id_text(self):
        try:
            chase_id = self.find_element(*self.chase_id_text_loc).text
            if chase_id != None:
                print("追号ID为：" + chase_id)
                return chase_id
        except NoSuchElementException:
            print("元素\“追号ID\”不存在")

    # 获取追号状态
    def chase_state_text(self):
        try:
            chase_state = self.find_element(*self.chase_state_text_loc).text
            if chase_state != None:
                print("追号状态为：" + chase_state)
                return chase_state
        except NoSuchElementException:
            print("元素\“追号状态\”不存在")
    #少于等于5注的详情页检查
    def order_details_check(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bet()
        self.official_open_time()
        self.order_number()

    #大于5注的详情页检查
    def order_details_checks(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bets()
        self.official_open_time()
        self.order_number()
    #追期玩法详情页面检查
    def chase_order_details_check(self):
        self.union_top_text()
        self.stop_chase_button()
        self.amount_sum_text()
        #self.chase_number_bets()
        self.chase_id_text()
        self.chase_state_text()

    def Betting_number(self):#读取详情页显示的投注号码，排序并以整型的形式输出
        list=[]
        a=self.find_elements(*self.betting_number)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            list.append(int(aa))
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Betting_nu(self):#读取详情页显示的投注号码，以字符串形式输出
        list=[]
        c=''
        a=self.find_elements(*self.betting_number)
        print(a)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            if i>0:
                c=c+' '+aa
            else:
                c=c+aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list

    def Pay_case(self):
        a=self.find_element(*self.pay_case).text##读取支付情况
        return a

    def Scheme(self):
        self.find_element(*self.scheme).click()###点击继续购买该方案

    def bet_number(self):##获取订单详情页，投注号码---mj20171207
        bet_num = self.find_element(*self.number_bet_loc).text
        return bet_num
    def continue_buy(self):#点击继续购买此彩种
        self.find_element(*self.continue_buy_loc).click()
    def Ele_five_betting_nu(self):#11选5读取订单详情页面的投注号码 ----mj20171211
        list = []
        c = ''
        a = self.find_elements(*self.betting_number)
        print("读取订单详情页的号码%s" % a)
        for i in range(len(a)):
            aa = self.find_element(*self.Ele_five_betting_loc(i + 1)).text
            if i > 0:
                c = c + ' ' + aa
            else:
                c = c + aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list
    def scheme_details(self):##获取订单详情页文本---mj20171215
        text =self.find_element(*self.scheme_details_loc).text
        return text
    def score_direct_broadcast_link(self):#点击比分直播链接
        self.wait_element_located(self.driver,self.score_direct_broadcast_link_loc)
        self.find_element(*self.score_direct_broadcast_link_loc).click()
    def play_instruct(self):#点击玩法说明链接
        self.wait_element_located(self.driver,self.play_instruct_loc)
        self.find_element(*self.play_instruct_loc).click()
    def function_instruct(self):##点击功能说明链接
        self.wait_element_located(self.driver,self.function_instruct_loc)
        self.find_element(*self.function_instruct_loc).click()
    def i_know(self):#点击【知道了】按钮
        self.wait_element_located(self.driver,self.i_know_loc)
        self.find_element(*self.i_know_loc).click()

    def Betting_after(self):
        list=[]
        a=self.find_element(*self.betting_after).text##读取号码
        b=a.replace('|',',')
        b1=b.strip(' ')
        b2=b1.replace(',',' ')
        list.append(b2)
        print(list)
        return list

class OrderDetails_lelun(Page_lelun,OderDetails_lelun_loc):
    def order_amount_sum(self):
        try:
            self.wait_element_located(self.driver, self.amount_sum_loc)
            amount_sum_text = self.find_element(*self.amount_sum_loc).text
            if amount_sum_text:
                print("投注金额：" + amount_sum_text+"元")
                return amount_sum_text
        except WebDriverException:
            print("元素\“方案金额\”不存在")
            raise
    #获取"订单状态"文本
    def order_status(self):
        self.wait_element_located(self.driver,self.order_status_loc)
        status_text = self.find_element(*self.order_status_loc).text
        print("订单状态：" + status_text)
        return status_text
    #获取“方案内容”中"投注号码"
    def number_bet(self):
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")
            raise
    #获取5注以上“方案内容”中的投注号码
    def number_bets(self):
        try:
            self.find_element(*self.expand_more_link_loc).click()
        except NoSuchElementException:
            print("“展开更多”按钮缺失")
        try:
            self.wait_element_located(self.driver, self.number_bet_loc)
            number_bet_text = self.find_element( * self.number_bet_loc).text
            if number_bet_text != None:
                print("投注号码：" + number_bet_text)
                return number_bet_text
        except NoSuchElementException:
            print("元素\“投注号码\”不存在")


    #获取“开奖时间”文本
    def official_open_time(self):
        self.wait_element_located(self.driver,self.official_open_time_loc)
        offical_open_time = self.find_element(*self.official_open_time_loc).text
        print("开奖时间：" + offical_open_time)
        return offical_open_time
    #获取“基本信息”中订单编号
    def order_number(self):
        self.wait_element_located(self.driver,self.order_number_loc)
        order_number_text = self.find_element(*self.order_number_loc).text
        print("订单编号：" + order_number_text)
        return order_number_text


    ##追号玩法订单详情页
    #获取玩法文本
    def union_top_text(self):
        self.wait_element_located(self.driver,self.union_top_text_loc)
        union_top_text = self.find_element(*self.union_top_text_loc).text
        return union_top_text
    #点击“停止追号”按钮
    def stop_chase_button(self):
        try:
            self.find_element(*self.stop_chase_button_loc)
            return True
        except NoSuchElementException:
            print("停止追号按钮缺失")
            return False
    #确认停止追号
    def confirm_stop_chase_button(self):
        self.wait_element_located(self.driver,self.confirm_stop_chase_loc)
        self.find_element(*self.confirm_stop_chase_loc).click()
    #取消停止追号
    def cancel_stop_chase_button(self):
        self.wait_element_located(self.driver,self.cancel_stop_chase_loc)
        self.find_element(*self.cancel_stop_chase_loc).click()
    #获取投注金额文本
    def amount_sum_text(self):
        try:
            amount_sum = self.find_element(*self.chase_amount_sum_loc).text
            if amount_sum != None:
                print("投注金额为：" + amount_sum)
                return amount_sum
        except NoSuchElementException:
            print("元素\“投注金额\”不存在")


    #获取投注号码定位
    def chase_number_bets(self):
        number = self.find_element(self.number_bets_loc).text#获取投注号码
        return number

    # 获取追号id
    def chase_id_text(self):
        try:
            chase_id = self.find_element(*self.chase_id_text_loc).text
            if chase_id != None:
                print("追号ID为：" + chase_id)
                return chase_id
        except NoSuchElementException:
            print("元素\“追号ID\”不存在")

    # 获取追号状态
    def chase_state_text(self):
        try:
            chase_state = self.find_element(*self.chase_state_text_loc).text
            if chase_state != None:
                print("追号状态为：" + chase_state)
                return chase_state
        except NoSuchElementException:
            print("元素\“追号状态\”不存在")
    #少于等于5注的详情页检查
    def order_details_check(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bet()
        self.official_open_time()
        self.order_number()

    #大于5注的详情页检查
    def order_details_checks(self):
        self.order_amount_sum()
        self.order_status()
        self.number_bets()
        self.official_open_time()
        self.order_number()
    #追期玩法详情页面检查
    def chase_order_details_check(self):
        self.union_top_text()
        self.stop_chase_button()
        self.amount_sum_text()
        #self.chase_number_bets()
        self.chase_id_text()
        self.chase_state_text()

    def Betting_number(self):#读取详情页显示的投注号码，排序并以整型的形式输出
        list=[]
        a=self.find_elements(*self.betting_number)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            list.append(int(aa))
        for j in range(len(list)):
            for n in range(j+1,len(list)):
                if list[j]>list[n]:
                    b=list[j]
                    list[j]=list[n]
                    list[n]=b
        print(list)
        return list

    def Betting_nu(self):#读取详情页显示的投注号码，以字符串形式输出
        list=[]
        c=''
        a=self.find_elements(*self.betting_number)
        for i in range(len(a)):
            aa=self.find_element(*self.Betting_nus(i+1)).text
            if i>0:
                c=c+' '+aa
            else:
                c=c+aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list

    def Pay_case(self):
        a=self.find_element(*self.pay_case).text##读取支付情况
        return a

    def Scheme(self):
        self.find_element(*self.scheme).click()###点击继续购买该方案

    def bet_number(self):##获取订单详情页，投注号码---mj20171207
        bet_num = self.find_element(*self.number_bet_loc).text
        return bet_num
    def continue_buy(self):#点击继续购买此彩种
        self.find_element(*self.continue_buy_loc).click()
    def Ele_five_betting_nu(self):#11选5读取订单详情页面的投注号码 ----mj20171211
        list = []
        c = ''
        a = self.find_elements(*self.betting_number)
        print("读取订单详情页的号码%s" % a)
        for i in range(len(a)):
            aa = self.find_element(*self.Ele_five_betting_loc(i + 1)).text
            if i > 0:
                c = c + ' ' + aa
            else:
                c = c + aa
        c.strip(' ')
        list.append(c)
        print(list)
        return list
    def scheme_details(self):##获取订单详情页文本---mj20171215
        text =self.find_element(*self.scheme_details_loc).text
        return text
    def score_direct_broadcast_link(self):#点击比分直播链接
        self.wait_element_located(self.driver,self.score_direct_broadcast_link_loc)
        self.find_element(*self.score_direct_broadcast_link_loc).click()
    def play_instruct(self):#点击玩法说明链接
        self.wait_element_located(self.driver,self.play_instruct_loc)
        self.find_element(*self.play_instruct_loc).click()
    def function_instruct(self):##点击功能说明链接
        self.wait_element_located(self.driver,self.function_instruct_loc)
        self.find_element(*self.function_instruct_loc).click()
    def i_know(self):#点击【知道了】按钮
        self.wait_element_located(self.driver,self.i_know_loc)
        self.find_element(*self.i_know_loc).click()

    def Betting_after(self):
        list=[]
        a=self.find_element(*self.betting_after).text##读取号码
        b=a.replace('|',',')
        #b1=b[4:].strip(' ')
        b2=b.replace(',',' ')
        list.append(b2)
        print(list)
        return list