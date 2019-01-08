from selenium.webdriver.common.by import By
class Login_leyou_loc():
    ######新用户登录定位##########
    ##new_user_login_tab_loc = (By.ID,"login_tab_v2")无
    #####用户名输入框定位#####
    username_loc = (By.ID,"user_name")

    #####密码输入框定位#####
    password_loc = (By.ID,"pass_word")

    #####确认登录按钮定位######
    login_button_loc = (By.ID,"to_submit_v2")
###首页定位器###############################################
class HomePage_leyou_loc():
    header_text_loc = (By.CLASS_NAME,"headtitfix")##首页顶部文本定位
    ###活动浮层弹窗定位
    Moveable_float_close_loc = (By.CLASS_NAME, "mi_ldialog_close")
    ######################彩种定位############################################
    UnionLotto_link_loc = (By.CLASS_NAME, "logo-ssq")#双色球定位
    Lottery_link_loc = (By.CLASS_NAME, "logo-dlt")#大乐透定位
    gd_11_5_link_loc = (By.CSS_SELECTOR, "i[style*='img_key=8DD32F30F870483E89DA129D5861A50D']")#广东11选5定位
    paintball_link_loc = (By.CLASS_NAME,"logo-jczq")##竞彩足球定位
    single_foot_link_loc = (By.CLASS_NAME,"logo-jzdg")##竞足单关定位
    gx_11_5_link_loc = (By.CSS_SELECTOR,"i[style*='76AD386EEC174D199A98CF6FFA9779EA']")#广西11选5定位
    haobc_link_loc = (By.CLASS_NAME,"logo-jclq")#竞彩篮球定位
    single_basketball_loc = (By.CLASS_NAME,"logo-jldg")#竞篮单关定位
    fucai_3D_link_loc =(By.CLASS_NAME,"logo-3d")#福彩3D定位
    optional_9_link_loc = (By.CLASS_NAME,"logo-rxj")#任选9场定位
    cqssc_link_loc = (By.CSS_SELECTOR, "i[style*='3898CD38BB504982A53ED89470C5E8A9']")  ##重庆时时彩元素定位
    victory_or_defeat_link_loc = (By.CLASS_NAME,"logo-sfc")#胜负14场
    # 无 activities_loc = (By.CSS_SELECTOR,"section[id*='mi_act_1'] div[class*='ui-avc']")#活动专区定位
    # 无 more_lottery_link_loc = (By.CLASS_NAME,"logo-no")#更多彩种定位
    rank_three_link_loc = (By.CLASS_NAME,"logo-pls")#排列3定位
    rank_five_link_loc = (By.CLASS_NAME,"logo-plw")#排列5元素定位
    colorful_star_link_loc = (By.CLASS_NAME,"logo-qxc")#七彩星定位
    jiangxi_express_three_link_loc = (By.CSS_SELECTOR,'i[style*="12BF3B64C3EC4309AA254C1ECC38E840"]')#江西快三元素定位
    guangxi_express_three_link_loc = (By.CSS_SELECTOR,'div[ontap*="shopmicai/shoppage/gpc/gxks/index.html"]')  # 广西快三元素定位
    shandong_11x5_link_loc = (By.CLASS_NAME,"logo-11x5")#山东11选5元素定位
    ############我的彩票定位
    my_lottery_ticket = (By.CSS_SELECTOR,'li[ontap*="/android_asset/www/newmicai/user/user_center_index.html"]')  ###首页我的彩票
    lemi = (By.CSS_SELECTOR, 'div.backtitlefix >h3')  ##乐米彩票
    MyTicket_link_loc = (By.CSS_SELECTOR, "li[ontap*='newmicai/user/user_center_index.html']")
    HomePage_link_loc = (By.XPATH,'//*[@id="foottab"]/ul/li[1]')##购彩
    home_page = (By.XPATH,'//*[@id="foottab"]/ul/li[1]')##购彩
    lottery_information=(By.CSS_SELECTOR,'li[ontap*="newmicai/lotteryinfo/kjgg.html#?page=kjgg_index"]')###开奖信息
    activity_zone=(By.ID,'mi_act_1')#活动专区
    lucky_pick=(By.CSS_SELECTOR,'li[ontap*="activity/lucy-num/index.html"]')##幸运选号

###双色球选号页元素定位
class UChooseNum_leyou_loc():
    ######################选择模式定位##################
    mode_choose_button_loc = (By.ID,"g-nav")#选择模式定位
    ######################选择普通模式定位
    UnionLotto_type_Normal_loc = (By.XPATH, '//*[@id="switchPlay"]/li[1]/div')
    ######################选择胆拖模式定位
    UnionLotto_type_DanTuo_loc = (By.XPATH, "//*[@id='switchPlay']/li[2]/div")
    ###############历史开奖定位#############
    history = (By.ID,'showHistory')
    spread_run_lottery_loc = (
    By.CSS_SELECTOR, "section[id='zst_section_short'] div[class*='gray']")  # 展开历史走势定位--mj20171207
    ##清除选号图标按钮定位
    clear_number_icon_loc = (By.CSS_SELECTOR, "i[ontap='clearnumber()']")
    ######################手动选择投注号码定位################################################
    ###普通模式蓝球列表定位
    bule_loc = (By.ID, "blueq")
    ##红球胆码列表定位
    DanMa_loc = (By.ID, "danredq")
    ##红球拖码列表定位
    TuoMa_loc = (By.ID, "tuoredq")
    ##蓝球列表定位
    DT_bule_loc = (By.ID, "dtblueq")
    ##蓝球胆码列表定位
    DanTuo_Dan_bule_loc = (By.ID, "danblueq")
    # 蓝球拖码列表定位
    Dantuo_Tuo_bule_loc = (By.ID, "tuoblueq")
    ##选号列表的上线元素
    above_element_loc = (By.ID, "openshow")
    ##选号列表下线元素
    bottom_element_loc = (By.CSS_SELECTOR, "div[id='dtblueq'] i[vrq='16']")
    ####选择超过规定数量红球toast提示信息定位
    out_toast_loc = (By.ID, "v_open_message_content")
    know_loc = (By.ID, 'v_open_message_btn')  ####我知道了
    ###选择机选定位###########################
    # 机选按钮定位
    machine_choose_button_loc = (By.ID, "randbtn")
    # 机选一注定位
    machine_choose_one_button_loc = (By.CSS_SELECTOR, "li[data-zs='1']")
    # 机选五注定位
    machine_choose_five_button_loc = (By.CSS_SELECTOR, "li[data-zs='5']")
    # 机选十注定位
    machine_choose_ten_button_loc = (By.CSS_SELECTOR, "li[data-zs='10']")
    #####确定选号按钮定位###########################
    confirm_button_loc = (By.ID, "tobuy")
    select_bule=(By.CSS_SELECTOR,'div#blueq>label>i.checked')###选中蓝球定位
    there_clock=(By.CLASS_NAME,'i-head_more')###右上角。。。
    history_movements=(By.XPATH,'//*[@id="selhm"]/header/div/div[2]/i/ul/li[2]')###历史走势
    recommended_number=(By.ID,'zst_page_finish')###使用推荐号码
    recommended_nu=(By.CSS_SELECTOR,'em.on')##推荐号码
    many_pause=(By.XPATH,'//*[@id="selhm"]/header/div/div[2]/i/ul/li[3]')##多期机选
    def many_pause_nu(self,n):
        nu=(By.CSS_SELECTOR,'li[data-val="%d"]'%n)##多期机选 期号
        return nu

    many_text_loc = (By.ID, 'Mi_random_tips')  # 多期机选页倍数注数文本定位---mj20171208
    many_choose_input_loc = (By.ID, 'Mi_random_qs')  # 多期选号页的追号期数输入框定位
    many_choose_add_loc = (By.ID, 'Mi_random_add')  # 多期选号页的追号期数的+按钮定位
    many_choose_sub_loc = (By.ID, 'Mi_random_min')  # 多期选号页的追号期数的-按钮定位
    many_chase_radio_loc = (By.ID, 'Mi_random_addamt')  # 多期机选页面的追加单选按钮定位
    def Recommended_nus(self,n):
        recommended_nus=(By.CSS_SELECTOR,'div.ssqfont>em:nth-of-type(%d)'%n)##第n个推荐号码
        return recommended_nus

    many_pause_confirm=(By.ID,'Mi_random_confirm')##多期机选，提交订单

    def history_red(self,n):
        red=(By.XPATH,'//*[@id="select_balls_red_table"]/tbody/tr/td[%d]/i'%n)#历史走势红球定位
        return red

    def history_bule(self,n):
        bule=(By.XPATH,'//*[@id="select_balls_blue_table"]/tbody/tr/td[%d]/i'%n)
        return bule

    red_movements=(By.XPATH,'//*[@id="choose_tabs"]/li[3]')###红球走势
    bule_movements=(By.XPATH,'//*[@id="choose_tabs"]/li[4]')##蓝球走势

    lottery_information_unionlotto=(By.CSS_SELECTOR,'a[href*="#?page=kjgg_list&lot_code=50"]')###开奖信息，双色球
    lucky_number=(By.CSS_SELECTOR,'img[src*="activity/lucy-num/images/icon_home_a.png"]')###幸运选号
    birthday_pick=(By.CSS_SELECTOR,'img[src*="activity/lucy-num/images/icon_home_b.png"]')###生日选号
    phone_pick=(By.CSS_SELECTOR,'img[src*="activity/lucy-num/images/icon_home_c.png"]')##手机号选号
    qq_pick=(By.CSS_SELECTOR,'img[src*="activity/lucy-num/images/icon_home_c.png"]')##qq选号

##大乐透选号页元素定位
class LChooseNum_leyou_loc():
    ##大乐透胆拖玩法，选号列表的上线元素
    above_element_loc = (By.ID, "openshow")
    ###大乐透胆拖玩法，鼠标下移定位
    l_bottom_element_loc = (By.CSS_SELECTOR, "div[id='tuoblueq'] i[vbq='12'")
    def bule_history_choose_loc(self, n):  # 历史走势，蓝球号码定位
        bule_history_choose_loc = (By.XPATH, '//*[@id="select_balls_blue"]/div[%d]/em' % n)
        return bule_history_choose_loc

#############投注确认页元素定位##########
class ConfirmLottery_leyou_loc():
    confirm_num_page_text_loc = (By.PARTIAL_LINK_TEXT, "投注确认")  # 投注确认页，“投注确认”文本定位
    continue_choose_num_button_loc = (By.ID,'contisel')  # “继续选号”按钮定位II
    Machine_choose_five_button_loc = (By.CSS_SELECTOR, "div[data-zs='5']")  # “机选5注”定位
    Machine_choose_one_button_loc = (By.ID, "conrand")  # "机选1注"定位
    re_selection_num_loc = (By.ID, "addli")  # 重新选号定位
    delete_all_num_button_loc = (By.CSS_SELECTOR, 'div[ontap*="#del_all_body"]')  # 清除列表按钮
    delete_one_num_button_loc =(By.CSS_SELECTOR,"div[ontap='deli(0)']")#单条删除选号按钮
    ###################mj20171206
    event_field_loc = (By.CLASS_NAME, "i-cartdel")  # 投注笔数定位
    def del_n_loc(self, n):
        n = (By.XPATH, '//*[@id="%d"]/div/i' % (n - 1))  ####清除n场赛事X定位
        return n
    #########################mj20171206############################
    confirm_delete_button_loc = (By.PARTIAL_LINK_TEXT, "确定")  # 确认删除所有选号按钮定位
    cancel_delete_button_loc = (By.PARTIAL_LINK_TEXT, "取消")  # 取消删除所有选号按钮定位
    choose_station_loc = (By.ID, "tzzname")  # 选择投注站入口定位
    appoint_station_tab_loc = (By.ID, "appoint")  # 选择指定投注站标签定位
    chase_ticket_button_loc = (By.ID, "qs")  # 选择追xx期定位
    stop_chase_win_radio_loc = (By.ID, "Mi_hit_stop")  # 中奖停追单选按钮定位
    chase_ticket_button_two_loc = (By.CSS_SELECTOR, "li[val='2']")  # 选择追2期定位
    chase_ticket_button_five_loc = (By.CSS_SELECTOR, "li[val='5']")  # 选择追5期定位
    chase_ticket_button_ten_loc = (By.CSS_SELECTOR, "li[val='10']")  # 选择追10期定位
    chase_ticket_button_twenty_loc = (By.CSS_SELECTOR, "li[val='20']")  # 选择追20期定位
    chase_ticket_button_fifty_loc = (By.CSS_SELECTOR, "li[val='50']")  # 选择追50期定位
    chase_ticket_sub_button_loc = (By.XPATH,"//*[@id='buy']/section[2]/div/div[1]/div[1]/div/div/i[1]")#追期-按钮
    chase_ticket_add_button_loc = (By.XPATH,"//*[@id='buy']/section[2]/div/div[1]/div[1]/div/div/i[2]")#追期+按钮
    throw_times_input_loc = (By.ID, "bs")  # 输入投XX倍定位
    u_throw_times_button_add_loc = (
    By.XPATH, "//*[@id='buy']/section[2]/div/div[1]/div[2]/div/div/i[2]")  # 双色球投注XX倍，“+”定位
    u_throw_times_button_sub_loc = (
    By.XPATH, "//*[@id='buy']/section[2]/div/div[1]/div[2]/div/div/i[1]")  # 双色球投注XX倍，“-”定位
    throw_times_text_loc = (By.ID, "sbs")  # 投注倍数文本定位
    chase_times_text_loc = (By.ID, "sqs")  # 追号期数文本定位
    lottery_number_text_loc = (By.ID,"szs") #投注注数文本定位
    submit_order_to_station_owner_button_loc = (By.ID, "totouzhu")  # “提交订单给站主”按钮定位
    confirm_and_pay_button_loc = (By.ID, "consure")  # “确认并支付”按钮
    cancel_pay_button_loc = (By.ID, "concancel")  # "取消确认支付"按钮
    # 订单金额超过100000时，所投注期停售时，toast提示信息定位
    toast_loc = (By.ID, "v_open_message_content")
    i_know_loc = (By.ID,"ylz_switch_issue_reminder_i_know")#停止销售时，弹出“我知道了”定位
    user_agreement=(By.CSS_SELECTOR,'a[href="javascript:open_agreementDialog();"]')###用户协议
    user_know=(By.ID,'v_open_dialog_btn')##用户协议，我知道了
    risk=(By.ID,'g-explain')##购彩风险
    risk_know=(By.ID,'g-explain_b')###购彩风险，我知道了
    select_red=(By.CSS_SELECTOR,'var[ontap="edit(0)"]>span.red')##选择的红球
    select_blue=(By.CSS_SELECTOR,'var[ontap="edit(0)"]>span.blue')###选择蓝球
    del_X=(By.XPATH,'//*[@id="addli"]/li[1]/div/i')##左侧X按钮
    unionlotto_History_buy=(By.CSS_SELECTOR,'#openCodes > ul > a:nth-child(1)')##历史开奖，双色球展示的最近开奖信息
    buy_unionlotto=(By.ID,'mi_btn_buy')###投注双色球
    choose_color=(By.CSS_SELECTOR,'article.pagewra.fullscreen.m-xyxh.bg-xy.bg_a>section>div>.g-cz')##幸运选号，选择彩种定位
    choose_note = (By.CSS_SELECTOR, 'article.pagewra.fullscreen.m-xyxh.bg-xy.bg_a>section>div>.g-zs')  ##幸运选号，选择注数定位
    lucky_unionlotto=(By.CSS_SELECTOR,'p[value="50"]')##幸运选号，双色球定位
    lucky_lottery=(By.CSS_SELECTOR,'p[value="1"]')##幸运选号，大乐透
    complete=(By.ID,'Mi_wheels_sure')###幸运选号，完成
    submit_frequently=(By.ID,'v_open_message_btn')###提交频繁，点击知道了

###订单详情页元素定位
class OderDetails_leyou_loc():
    #方案金额定位
    amount_sum_loc = (By.ID,"project_total_amount")
    #获取订单状态定位
    order_status_loc = (By.ID,"order_status")
    #获取“方案内容”中“投注号码"的定位
    number_bet_loc = (By.ID,"bet_content")
    #获取“方案内容”中“开奖时间”定位
    official_open_time_loc = (By.ID,"official_open_time")
    #获取“基本信息”中的“订单编号”定位
    order_number_loc = (By.ID,"project_id")
    #“展开更多”链接元素定位
    expand_more_link_loc = (By.ID,"showmoretxt")
    #####追号玩法的订单详情页元素定位
    union_top_text_loc = (By.XPATH,"//*[@id='full_zhdetails_info']/section[1]/header/div")##玩法定位
    stop_chase_button_loc = (By.ID,"cancel_track")#停止追号按钮定位
    confirm_stop_chase_loc = (By.ID,"yes_cancel")#确定停止追号定位
    cancel_stop_chase_loc = (By.ID,"no_cancel")#取消停止追号定位
    chase_amount_sum_loc = (By.XPATH,"//*[@id='full_zhdetails_info']/section[1]/ul/li[1]/strong")##投注金额元素定位
    number_bets_loc = (By.XPATH,"//*[@id='full_zhdetails_info']/section[2]/div[1]/div[2]/li")##方案内容中的投注号码定位
    chase_id_text_loc = (By.XPATH,"//*[@id='full_zhdetails_info']/section[2]/div[2]/div[2]/li[1]/div[1]/span")#追号id元素定位
    chase_state_text_loc =(By.ID,"track_state")#追号状态元素定位
    betting_number=(By.CSS_SELECTOR,'#bet_content>p>i')###投注号码定位

    def Betting_nus(self,n):
        betting_nus=(By.CSS_SELECTOR,'div#bet_content>p>i:nth-of-type(%d)'%n)###第n个投注号码
        return betting_nus
    def Ele_five_betting_loc(self,n):######第n个投注号码--mj20171211
        Ele_five_betting_loc = (By.CSS_SELECTOR,'#bet_content > p > i:nth-child(%d)'%n)
        return Ele_five_betting_loc
    pay_case=(By.ID,'fukuanstatus')##是否支付
    scheme=(By.ID,'buy_project')##继续购买该方案
    continue_buy_loc = (By.ID,'mi_btn_buy')##继续投注此彩种定位
    scheme_details_loc = (By.CSS_SELECTOR,'div.ui-cvertical>h3')#方案详情文本元素定位 ----mj20171215
    score_direct_broadcast_link_loc = (By.PARTIAL_LINK_TEXT,'比分直播')#比分直播链接定位
    play_instruct_loc = (By.ID,"jzdg_guide")#玩法说明链接定位
    function_instruct_loc = (By.ID,'g-zrbtn')#功能说明链接定位
    i_know_loc = (By.PARTIAL_LINK_TEXT,'知道了')#知道了按钮定位
    betting_after=(By.CSS_SELECTOR,'.b-flex.c_9')###订单详情页，追期投注号码显示

###提交訂單成功頁元素定位###############################################
class SubmitOrderSuccess_leyou_loc():
    # 获取“提交订单成功”文本定位
    submit_order_success_text_loc = (By.CLASS_NAME,"suc-t")
    ##购买彩种的商品名称文本定位
    trade_name_text_loc = (By.CLASS_NAME,"mt_10")

    #“返回首页”链接定位
    return_home_loc = (By.PARTIAL_LINK_TEXT,"首页")
    ##"查看订单详情"定位
    check_order_details_loc = (By.CLASS_NAME,"ml_6")
    continue_buy=(By.CLASS_NAME,'btn_white')##继续购买该彩种

##11选5页选号页元素定位
class EleChooseFiveChooseNum_leyou_loc():
    # 当前期定位
    current_period_text_loc = (By.XPATH, "//*[@id='g-lskj']/div[1]/p[1]")
    # 显示倒计时定位
    countdown_text_loc = (By.ID ,"open_history")
    # 展开“正在开奖中”之后定位
    spread_run_lottery_loc = (By.CSS_SELECTOR, "section[id='zst_section_short'] div[class*='gray']")
    total_buy_text_loc = (By.ID,"zh_total_buy")
    #乐选
    l_first_num_loc = (By.ID,"codes_div_lx3_1")#第一位选号列表定位
    l_second_num_loc = (By.ID,"codes_div_lx3_2")#第二位选号列表定位
    l_third_num_loc = (By.ID,"codes_div_lx3_3")#第三位选号列表定位
    #直选
    first_num_loc = (By.ID, "codes_div")  # 第一位选号列表定位
    second_num_loc = (By.ID, "codes_div1")  # 第二位选号列表定位
    third_num_loc = (By.ID, "codes_div2")  # 第三位选号列表定位
    confirm_number_button_loc = (By.ID, "sub_commit_id")# 确认选号按钮定位
    def recommendation_choose_num_loc(self, n):  ##11选5推荐号码页面的号码定位--mj20171211
        recommendation_choose_num_loc = (By.XPATH, '//*[@id="all_recommended_div"]/div[%d]/em' % n)
        return recommendation_choose_num_loc


    use_recommendation_loc = (By.ID, 'all_zst_page_finish')  # 使用推荐号码按钮定位
    history_trend_loc = (By.CSS_SELECTOR, 'li[ontap*="open_history"]')  # 历史走势定位


###大乐透投注确认页元素定位
class BigLotteryConfirmLottery_leyou_loc():
    additional_radio_button_loc = (By.ID, "addamt")  # “追加”单选按钮定位
    l_throw_times_button_add_loc = (
        By.XPATH, "//*[@id='buy']/section[2]/div/div[3]/div[2]/div/div/i[2]")  # 大乐透投注XX倍，“+”定位
    l_throw_times_button_sub_loc = (
        By.XPATH, "//*[@id='buy']/section[2]/div/div[3]/div[2]/div/div/i[1]")  # 大乐透投注XX倍，“-”定位
    #单条删除选号按钮、清除所有选号按钮、追XX期、追2期、追5期、追10期、追20期、追50期、投XX倍、确认并支付按钮，
    # 取消确认并支付和双色球相同，定位在双色球投注确认页，类名为ConfirmLottery_loc
###11选5投注确认页元素定位
class EleChooseFiveConfirmLottery_leyou_loc():
    countdown_text_loc = (By.CSS_SELECTOR, "strong[name='current_child_issue']")# 倒计时文案定位
    machine_choose_one_loc = (By.ID, "random_code_id")# 机选一注定位
    machine_choose_five_loc = (By.CSS_SELECTOR, "div[data-zs='5']")# 机选五注定位
    continue_choose_num_loc = (By.CSS_SELECTOR,"div[ontap='contiueBuy(1);']")# 继续选号定位
    delete_one_button_loc = (By.XPATH,"//*[@id='0']/div")##单个删除选号定位
    chase_ticket_button_loc = (By.ID, "qs")  # 选择追xx期定位
    chase_sub_button_loc = (By.XPATH,"//*[@id='directly_pay_div']/div[1]/div[1]/div/div/i[1]")#追号-按钮定位
    chase_add_button_loc = (By.XPATH,"//*[@id='directly_pay_div']/div[1]/div[1]/div/div/i[2]")#追号+按钮定位
    throw_times_input_loc = (By.ID,"bs_num_id")#输入投注倍数定位
    throw_sub_button_loc = (By.XPATH,"//*[@id='directly_pay_div']/div[1]/div[2]/div/div/i[1]")#投注倍数-按钮定位
    throw_add_button_loc = (By.XPATH,"//*[@id='directly_pay_div']/div[1]/div[2]/div/div/i[2]")#投注倍数+按钮定位
    lottery_chase_throw_text_loc = (By.ID,"total_data") #获取投注注数，追号期数、投注倍数的文本
    submit_order_button_loc = (By.ID,"commit_data")#提交订单给站按钮元素定位
    ###11选5确认投注页的 追2期、追5期、追10期、追20期、追50期元素定位与双色球元素定位相同，定位class为Confirm_Lottery_loc##
    select_num_loc = (By.CSS_SELECTOR,"var[ontap *= 'edit'] > span.red")#投注确认页，投注号码定位

###我的彩票页定位器###############################################
class MyTicket_leyou_loc():
    recharge = (By.CSS_SELECTOR, '.btn_recharge')  ##充值按钮
    setup_link_loc = (By.CLASS_NAME,"i-acc_setup")###设置链接定位##
    available_cash_loc = (By.ID,"Mi_keyong_money")#可用余额定位
    after_nu=(By.CSS_SELECTOR,'a[href*="newmicai/user/lotterybuy/buy_record_zh.html"]')##追号订单
    after_nu_record=(By.CSS_SELECTOR,'#my_lot_buy>li')###追号所有订单list

###设置页元素定位
class Setup_leyou_loc():
    #“退出当前账号”按钮定位
    LogOut_button_loc = (By.PARTIAL_LINK_TEXT,"退出账号")
##历史走势页元素定位
class HistoricalTrend_leyou_loc():
    ##使用推荐号码按钮定位
    use_recommend_num_button_loc = (By.ID,"zhixuan_zst_finish")
##充值页元素定位
class Recharge_leyou_loc ():
    def Recharge_money(self,n):
        recharge_money=(By.CSS_SELECTOR,'li[data-money="%s"]'%n)##充值金额定位
        return recharge_money
    recharge_input=(By.ID,'mi_money_other')##输入充值金额
    next=(By.ID,'nextStep')###下一步
    more_payment=(By.CLASS_NAME,'j-morecharge')###更多支付方式
    account=(By.ID,'Mi_username')###显示的账户

##差额支付时确认支付页面元素定位
class ConfirmPay_leyou_loc():
    #“确认支付”按钮定位
    confirm_pay_loc = (By.CLASS_NAME,"input")
    pay_true=(By.CSS_SELECTOR,'section[style=" padding-top:45%;"]>h2')##支付成功文本
    shut_down=(By.CSS_SELECTOR,'span[ontap="goHome();"]')##关闭
################排列5选号定位###############1018
class Arrang_five_num_leyou():
    def nu_w(self,i,n):
        w_one=(By.XPATH,'//*[@id="plw_1"]/div[%d]/div[%d]/i' %(i,n)) #万位0-9
        return  w_one

    def nu_q(self,i,n):
        w_one=(By.XPATH,'//*[@id="plw_2"]/div[%d]/div[%d]/i' %(i,n)) #千位0-9
        return  w_one

    def nu_b(self,i,n):
        w_one=(By.XPATH,'//*[@id="plw_3"]/div[%d]/div[%d]/i' %(i,n)) #百位0-9
        return  w_one

    def nu_s(self,i,n):
        w_one=(By.XPATH,'//*[@id="plw_4"]/div[%d]/div[%d]/i' %(i,n)) #十位0-9
        return  w_one

    def nu_g(self,i,n):
        w_one=(By.XPATH,'//*[@id="plw_5"]/div[%d]/div[%d]/i' %(i,n)) #个位0-9
        return  w_one

    confirm_nu=(By.ID,'confirmBtn')#########排列5 确认选号
    down_nu=(By.ID,'plw_5')#个位
    down_top=(By.ID,'plw_1')#万位
    #########排列5 机选按钮，机选1注，机选5注，机选10注，清除选号图标 与双色球定位一致
    history_date=(By.CSS_SELECTOR,'#show_long_zst>li')###历史数据


#####################排列5投注确认页定位################1018
class Arrang_five_pick_leyou():
    coun_nu=(By.CSS_SELECTOR,"div[ontap*='contiueBuy()")#####继续选号按钮
    coun_five=(By.CSS_SELECTOR, "div[data-zs='5']")######机选5注
    coun_one=(By.CSS_SELECTOR,"div[ontap='randomNumber()']")###########机选1注

    ############### 清除图标，提交订单给站主，投注站，与 双色球一致
    note=(By.ID,'totalzs')##########投注页面显示注数

    ################选中号码左侧X按钮################
    def del_one(self,n):
        del_nu=(By.XPATH,'//*[@id="tobuynumber"]/li[%d]/div/i'%n)
        return del_nu

    #################选中号码定位##################
    def note_one(self,n):
        note_nu=(By.XPATH,'//*[@id="tobuynumber"]/li[%d]/var'%n)
        return note_nu

    ##############w我满18岁单选按钮###########
    iagree=(By.ID,'iagree')
    know=(By.ID,'v_open_message_btn')####我知道了

###############################################################################1020
    ################倍数 -号
    multiple_less=(By.XPATH,'//*[@id="buydiv"]/section[2]/div/div[1]/div[2]/div/div/i[1]')

    ################倍数 +号
    multiple_add=(By.XPATH,'//*[@id="buydiv"]/section[2]/div/div[1]/div[2]/div/div/i[2]')

    ###################倍数 输入
    multiple_input=(By.ID,'bs')

    multiple=(By.ID,'beishutext')###投注页倍数显示
    period=(By.ID,'qishutext')####投注页期数显示

    ################期数 +号
    a_period=(By.XPATH,'//*[@id="buydiv"]/section[2]/div/div[1]/div[1]/div/div/i[2]')

    ###########期数 -号
    l_period=(By.XPATH,'//*[@id="buydiv"]/section[2]/div/div[1]/div[1]/div/div/i[1]')

######################七星彩选号定位
class seven_color_num_leyou():
    def nu_one(self,i,n):
        num_one=(By.XPATH,'//*[@id="qxc_1"]/div[%d]/div[%d]/i'%(i,n))###第一位数字
        return num_one

    def nu_too(self,i,n):
        num_too=(By.XPATH,'//*[@id="qxc_2"]/div[%d]/div[%d]/i'%(i,n))###第二位数字
        return num_too

    def nu_there(self,i,n):
        num_there=(By.XPATH,'//*[@id="qxc_3"]/div[%d]/div[%d]/i'%(i,n))###第三位数字
        return num_there

    def nu_four(self,i,n):
        num_four=(By.XPATH,'//*[@id="qxc_4"]/div[%d]/div[%d]/i'%(i,n))###第四位数字
        return num_four

    def nu_five(self,i,n):
        num_five=(By.XPATH,'//*[@id="qxc_5"]/div[%d]/div[%d]/i'%(i,n))###第五位数字
        return num_five

    def nu_six(self,i,n):
        num_six=(By.XPATH,'//*[@id="qxc_6"]/div[%d]/div[%d]/i'%(i,n))###第六位数字
        return num_six

    def nu_seven(self,i,n):
        num_seven =(By.XPATH,'//*[@id="qxc_7"]/div[%d]/div[%d]/i'%(i,n))###第七位数字
        return num_seven

    down_nu=(By.ID,'qxc_7')#####第七位
    down_top=(By.ID,'qxc_1')#######第一位
    seven_color_instruct=(By.ID,'g-jj')##玩法说明
    seven_color_play=(By.CSS_SELECTOR,'article#g-jjbody>div>section>h3')###玩法说明，七星彩玩法定位
    seven_color_know=(By.ID,'g-jjbtn')###玩法说明，知道了
    seven_color_history=(By.CSS_SELECTOR,'#sel > header > div > div > i > ul > li:nth-child(2)')###历史走势
    history_date=(By.CSS_SELECTOR,'#show_long_zst>li.tr>div.td>i.red')###历史走势数据显示号码定位
    seven_color_lor=(By.CSS_SELECTOR,'#sel>header>div>h3')###选号页面，七星彩文本定位
############################排列三   选号页面定位############################1023
class arrang_there_leyou():
    play=(By.ID,'Mi_lot_title')###玩法
    play_direct=(By.ID,'g-tab_z')####直选
    play_group_there=(By.ID,'g-tab_zs')###组三
    play_group_six=(By.ID,'g-tab_zl')###组六

    #############选号定位
    def nu_bai(self,i,n):
        bai=(By.XPATH,'//*[@id="pls_1"]/div[%d]/div[%d]/i'%(i,n))####百位
        return bai

    def nu_shi(self,i,n):
        shi=(By.XPATH,'//*[@id="pls_2"]/div[%d]/div[%d]/i'%(i,n))####十位
        return shi

    def nu_ge(self,i,n):
        ge=(By.XPATH,'//*[@id="pls_3"]/div[%d]/div[%d]/i'%(i,n))####个位
        return ge

######组三玩法##########1030
    #####选号定位
    def g_there(self, i, n):
        nu = (By.XPATH, '//*[@id="pls_zs"]/div[%d]/div[%d]/i' % (i, n))  ####百位
        return nu

    ####筛选定位
    def screening(self,i):
        nu=(By.CSS_SELECTOR,"div[id='funct_zs'] li[value='%s']"%i)
        return nu

    ####组合显示号码定位
    def group_display(self,n):
        nu=(By.XPATH,'//*[@id="zsnumberlist"]/li[%d]/div/div[1]'%n)
        return nu

    ####组合显示X图标定位
    def group_delet(self,n):
        nu=(By.XPATH,'//*[@id="zsnumberlist"]/li[%d]/div/div[2]/i'%n)
        return nu


###########组六玩法#############
  ######选号定位
    def g_six(self, i, n):
        nu = (By.XPATH, '//*[@id="pls_zl"]/div[%d]/div[%d]/i' % (i, n))
        return nu

####筛选定位
    def screening_s(self,i):
        nu=(By.CSS_SELECTOR,"div[id='funct_zl'] li[value='%s']"%i)
        return nu
    arrang_there_instruct=(By.ID,'g-sm')###玩法说明

    arrany_there_play=(By.CSS_SELECTOR,'#g-smbody>div>section>h3')###玩法说明，排列3玩法定位
    arrany_there_know=(By.ID,'g-btn_sm')##玩法说明，我知道了
    arrang_there_history=(By.XPATH,'//*[@id="sel"]/header/div/div[2]/i/ul/li[2]')##历史走势
    arrany_there_date=(By.CSS_SELECTOR,'#show_long_zst>li')##历史走势数据

    switch_play_ok=(By.ID,'switchconfrim')###切换玩法知道了

    #################### 3D选号页面定位###############
class there_D_leyou_loc():
    play_d=(By.ID,'g-nav')###########玩法
    play_direct_d=(By.CSS_SELECTOR,"div[playid='51001']")###直选
    play_group_there_d=(By.CSS_SELECTOR,"div[playid='51002']")###组三
    play_group_six_d=(By.CSS_SELECTOR,"div[playid='51004']")###组六
    play_direct_add_d=(By.CSS_SELECTOR,"div[playid='51005']")###直选和值
    play_group_there_add_d=(By.CSS_SELECTOR,"div[playid='51006']")###组三和值
    play_group_six_add_d=(By.CSS_SELECTOR,"div[playid='51007']")##组六和值
    show_play=(By.ID,'Mi_lot_title')##显示玩法
    instruct=(By.CLASS_NAME,'i-head_more')###右上角。。。。
    play_instruction=(By.ID,'g-sm')###玩法说明
    group_there_add_play_instruction=(By.XPATH,'//*[@id="Mi_rule_box"]/div/section[1]/div/table/tbody/tr[6]/td[1]')#组三和值玩法说明
    there_D_know=(By.ID,'g-smbtn')##玩法说明页，我知道了
    history=(By.XPATH,'//*[@id="sel"]/header/div/div[2]/i/ul/li[2]')##历史走势
    def charts(self,i):
        n=(By.XPATH,'//*[@id="bai_zst_page"]/li[%d]/div[2]'%i)##历史走势数据
        return n
    charts_list=(By.CSS_SELECTOR,'#bai_zst_page>li')
    recommend=(By.CSS_SELECTOR,'div#bai_recommended_div>div>em.on')##推荐号码
    use_recommend=(By.ID,'zhixuan_zst_finish')##使用推荐号码
    number=(By.CSS_SELECTOR,'var[ontap="edit(0)"]>span')##投注确认页，投注号码
    clear=(By.CSS_SELECTOR,'h3.tit.c_ten.c_333.mt_10')##删除弹框，清楚文本
    del_x=(By.XPATH,'//*[@id="tobuynumber"]/li/div/i')###X按钮
    coun_number=(By.CSS_SELECTOR,'div#hzjxbtns>div[ontap="contiueBuy()"]')##继续选号
    pause_d=(By.ID,'jxbtn')##机选
    pause_nu=(By.XPATH,'//*[@id="tobuynumber"]/li[1]/var/span')##机选号码

    ########直选选号定位
    def nu_bai_d(self,i,n):
        bai=(By.XPATH,'//*[@id="baiwei"]/div[2]/div[%d]/div[%d]/i'%(i,n))####百位
        return bai

    def nu_shi_d(self,i,n):
        shi=(By.XPATH,'//*[@id="shiwei"]/div[2]/div[%d]/div[%d]/i'%(i,n))####十位
        return shi

    def nu_ge_d(self,i,n):
        ge=(By.XPATH,'//*[@id="gewei"]/div[2]/div[%d]/div[%d]/i'%(i,n))####个位
        return ge

#####组三选号定位
    def g_there_d(self, i, n):
        nu = (By.XPATH, '//*[@id="zszl"]/div[1]/div[2]/div[%d]/div[%d]/i' % (i, n))  ####百位
        return nu

    def screening_d(self,i):
        nu=(By.CSS_SELECTOR,"div[id='funct'] li[value='%s']"%i)
        return nu

###########组六玩法#############
  ######选号定位
    def g_six_d(self, i, n):
        nu = (By.XPATH, '//*[@id="zszl"]/div[1]/div[2]/div[%d]/div[%d]/i' % (i, n))
        return nu

#################直选和值
    ###选号定位
    def direct_add(self,i):
        nu=(By.XPATH,'//*[@id="zxhz"]/div/div[2]/label[%d]/i'%i)
        return nu

###############组三和值
    #####选号定位
    def group_there_add(self,i):
        nu=(By.XPATH,'//*[@id="zshz"]/div/div[2]/label[%d]/i'%i)
        return nu

################组六和值
    ########选号定位
    def group_six_add(self,i):
        nu=(By.XPATH,'//*[@id="zlhz"]/div/div[2]/label[%d]/i'%i)
        return nu

##############################################竞彩足球
####################混合投注 选号页面定位
class PaintBallChooseNumber_leyou_loc():
    filter_button_loc = (By.ID, 'handcc')  # 点击筛选按钮---mj20171214
    allccsel_loc = (By.ID, 'allccsel')  # 点击全选
    noallccsel_loc = (By.ID, 'noallccsel')  # 点击反选
    fivecc_loc = (By.ID, 'fivecc')  # 点击5大联赛
    findcc_loc = (By.ID, 'findcc')  # 点击筛选banner中的确定
    event_time_count_loc = (By.CSS_SELECTOR, 'div.mi_match_group')  ##获取页面场次的天数
    three_clock_loc = (By.CLASS_NAME, 'i-head_more')  ###右上角。。。
    paintball_play_instruct_loc = (By.CSS_SELECTOR, "li[ontap*='jczpage.showhelp()']")  ##玩法说明定位
    immediately_loc = (By.CSS_SELECTOR, "li[ontap*='score_live_list.html']")  ##即使比分
    enter_analysis_loc = (By.XPATH, '//*[@id="mi_all_match"]/section[1]/ul/li/div')  ##进入赛事分析页面元素定位
    return_homepage_loc = (By.PARTIAL_LINK_TEXT, '首页')  ##返回首页元素定位
    lottery_jczq_button_loc = (By.CLASS_NAME, 'fullbtn')  ##投注竞彩足球按钮定位
    choose_mode_loc = (By.ID, "titletxt")  # 选择投注模式定位--mj20171102
    mix_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='hhtz']")  # 选择“混合投注”模式定位
    spf_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='spf']")  # 选择“胜平负”投注模式
    rqspf_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='rqspf']")  # 选择“让球胜平负”投注模式
    bf_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='bf']")  # 选择“比分”投注模式
    zjq_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='zjq']")  # 选择“总进球”投注模式
    bqc_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='bqc']")  # 选择“半全场”投注模式
    two_s_lottery_loc = (By.CSS_SELECTOR, "div[ontap*='two_s']")  # 选择“2选1”投注模式
    return_link_jl_loc = (By.CSS_SELECTOR, 'a[href="javascript:cp_back()"]')  # 返回首页链接
    return_link_loc = (By.CSS_SELECTOR, "header#title a.return")  # 返回首页链接--mj171031
    #nul_loc = (By.XPATH, '//*[@id="showmt"]/div[1]/div/div/span')  # 竞彩足球，今天显示的赛事场次
    nu_8 = (By.ID, 'v_open_message_content')  # 竞彩足球，提示最多只能选择8场提示框
    know = (By.ID, "v_open_message_btn")
    up = (By.XPATH, '//*[@id="match20171017"]/li[1]/div/div[2]/div[1]')  # 今天第一场赛事的让球定位
    confirm_loc = (By.ID, "showselc")  # 确认选号
    clear_button_loc = (By.CSS_SELECTOR,"div[ontap*='jczdeal.delm()']")#清空所选场次


    def football_id(self,a,n,b,c):
        to = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div[1]/div[%d]/div[%d]' % (a, n, b, c))  # 竞彩足球混合投注，今天赛事选择定位
        print(to)
        return to

    def football_ido(self,a,n,c):
        too = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div[1]/div/div[%d]' % (a, n, c))  # 竞彩足球混合投注，今天赛事选择定位
        return too

    def football_bf(self,a,n):
        n=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div/div[2]/div[2]'%(a,n))
        return n

    session_nu=(By.CSS_SELECTOR,'div.plrtps.ui-avc>div.flex1>span')#竞彩足球，当天显示的赛事场次


    def session(self,n):
        nu=(By.XPATH,'//*[@id="showmt"]/div[%d]/div/div/i'%n)###展开赛事
        return nu



    def VS(self,a,n):
        vs=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[1]/div[3]'%(a,n))###每场赛事的VS定位
        return vs

    def VS_bf(self,a,n):
        nu=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div/div[2]/div[1]/div[2]'%(a,n))
        return nu

    def more(self,a,n):
        mo=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div[2]/i'%(a,n))###展开更多
        return mo

    def cspf_icon(self,n):
        cspf=(By.CSS_SELECTOR,'td[cvalue="9005_%s"]'%n)##猜胜平负结果定位
        return cspf

    def crqspf_icon(self,n):
        crqspf=(By.CSS_SELECTOR,'td[cvalue="9001_%s"]'%n)##猜让球胜平负结果定位
        return crqspf

    def cjqs_icon(self,n):
        cjqs=(By.CSS_SELECTOR,'td[cvalue="9002_%s"]'%n)###猜进球数结果定位
        return cjqs

    def cbf_icon(self,n):
        cbf=(By.CSS_SELECTOR,'td[cvalue="9003_%s"]'%n)####猜比分结果定位
        return cbf

    def cbqc_icon(self,n):
        cbqc=(By.CSS_SELECTOR,'td[cvalue="9004_%s"]'%n)####猜比分结果定位
        return cbqc

    confirm_more = (By.ID, 'selected_match_ok')  ###展开更多页面确认按钮
    confirm_more_bf = (By.CSS_SELECTOR, 'a[href="javascript:jcz_hhtz.confirmC(0);"]')  ###展开更多页面确认按钮

    event_time=(By.CSS_SELECTOR,'ul.game_ul')#####对每天的赛事定位

    this_open=(By.CSS_SELECTOR,'div.game_group')#####判断是否展开定位

    play_fb=(By.CLASS_NAME,'play_f')##选号页面的玩法字样定位

    emptying=(By.CSS_SELECTOR,'div[ontap="javascript:jczpage.jczdeal.delm();"]')###清空按钮

    ##胜平负选择比赛胜负定位--mj20171106
    def event_list_loc(self,event_time,row,column):
        event=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div[%d]'%(event_time,row,column))#竞彩足球今天赛事定位
        return event
    def event_one_loc(self,event_time,column):
        event = (By.XPATH,'//*[@id="%s"]/li/div/div[2]/div[2]/div[%d]'%(event_time,column))
        return event
    def vs_list_loc(self,event_time,row):
        vs_loc = (By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[1]/div[2]'%(event_time,row))##竞彩足球VS元素定位
        return(vs_loc)
    def spread_event_details_loc(self,event_time,row):#展开赛事分析定位
        spread_event = (By.XPATH,'//*[@id="match%s"]/li[%d]/div/div[1]/i'%(event_time,row))
        return spread_event

    def football_bqc(self, a, n):
        n = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div/div[2]/div[2]' % (a, n))
        return n

    def football_zjq(self, a, n, b, c):
        n = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div/div[%d]/div[%d]' % (a, n, b, c))
        return n

    none_event = (By.CSS_SELECTOR,"p.c_9")##暂无赛事元素定位

    play_instruction=(By.CSS_SELECTOR,'li[ontap*="jclpage.showhelp();"]')##玩法说明

    race_basketball=(By.CSS_SELECTOR,'a[href*="shopmicai/shoppage/jcl/jclpage.html"]')##及时比分里，投注竞彩蓝球定位

    def event_analysis_data(self,i,j):
        a=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[1]/i'%(i,j))###赛事数据分析入口定位
        return a

    event_analysis_data_click=(By.CLASS_NAME,'fullwidth')###数据分析


class PaintBallConfirm_leyou_loc():
    add_event=(By.CSS_SELECTOR,'div[ontap="jczpage.jczdeal.retsel();"]')#####添加/编辑赛事 ii
    add_event2=(By.CSS_SELECTOR,'div[ontap="jczdgpage.jczdeal.retsel();"]')
    def n_del(self,n):
        n=(By.XPATH,'//*[@id="buyinfsel"]/ul/li[%d]/div[2]/div[3]/i'%n)####清除一场赛事X定位
        return n

    def del_n(self,n):
        n=(By.CSS_SELECTOR,'#buyinfsel>ul>li:nth-child(%d)>div.jc_cttit.ui-avc.ta_c.c_333>i.i-del'%n)
        return n

    def Dxf_del_n(self,n):
        n=(By.CSS_SELECTOR,'#buyinfsel > ul > li:nth-child(%d) > div.ui-avc.mt_5 > div.bet_w.ta_r > i'%n)
        return n

    nn = (By.CSS_SELECTOR,'li.sum')  ###所有的赛事X定位
    dxf_nn=(By.CLASS_NAME,'i-cartdel') ###所有的赛事X定位
    Bf_nn=(By.CLASS_NAME,'i-del')
    a_nn=(By.CSS_SELECTOR,'li[ontap*="jclpage.jcldeal.openGameBox($(this)"]')###所有的赛事X定位

    pf_del_icon=(By.CLASS_NAME,'i-delback')####删除全部赛事

    btn_less=(By.CLASS_NAME,'btn_less')###倍数 -
    btn_add=(By.CLASS_NAME,'btn_add')###倍数 +
    times_input=(By.ID ,'bs')####倍数输入框
    pf_bonus=(By.CSS_SELECTOR,'a[href="javascript:jczpage.lottery2jjyh();"]')####奖金优化
    pf_pass=(By.ID ,'selectedgs')####过关方式
    ###投注倍数定位
    def throw_times_loc(self,times):
        throw_times_loc = (By.CSS_SELECTOR,"li[val='%d']"%times)
        print(throw_times_loc)
        return throw_times_loc

    def pf_pass_nu(self):
        n = (By.CSS_SELECTOR, 'div#showgg>label>i')  ###定位所有的过关方式
        return n

    def times_number(self, n):
        n = (By.CSS_SELECTOR, 'li[val="%d"]' % n)  ####2-50倍定位
        return n

    times_display = (By.ID, 'sbs')  # 确认页面倍数显示文本
    optimize_award_page_text_loc = (By.CLASS_NAME,"yh_jjtop ")#奖金优化页最上方文本定位
    submit_order_loc = (By.CSS_SELECTOR,"a[href*='javascript:confirmtobuy();'")##奖金优化页面的提交订单给站主-mj20171214
    optimize_add_money_input_loc = (By.ID,'totalMoney')##增加投注金额输入框定位
    maximum_text_loc = (By.ID,'maxjj')##理论最大奖金金额定位
    restroe_button_loc = (By.PARTIAL_LINK_TEXT,'还原选项')#点击还原选项

###########竞彩篮球元素定位---mj20171114

class HaobcChooseNumber_leyou_loc():##选号页元素定位
    sf_mode_loc = (By.CSS_SELECTOR,"div[ontap*='sf']")#选择胜负模式定位
    rfsf_mode_loc = (By.CSS_SELECTOR,"div[ontap*='rfsf']")#让分胜负模式定位
    sfc_mode_loc = (By.CSS_SELECTOR, "div[ontap*='sfc']")#胜负差模式定位
    dxf_mode_loc = (By.CSS_SELECTOR,"div[ontap*='dxf']")#大小分模式定位
    mix_mode_loc = (By.CSS_SELECTOR,"div[ontap*='hhtz']")#混合投注定位
    delete_button_loc = (By.CSS_SELECTOR,"div[ontap*='jcldeal.delm();']")#清除按钮定位
    go_haobc_single_button_loc = (By.CSS_SELECTOR,"div[ontap*='open_page']")#前往竞篮单关按钮元素定位
    back_to_homepage_loc=(By.CSS_SELECTOR,"a[href *= 'cp_back()']")
    def sf_icon(self, n):
        sf = (By.CSS_SELECTOR, 'td[cvalue="10001_%s"]' % n)  ##胜负结果定位
        return sf

    def rfsf_icon(self,n):
        rfsf = (By.CSS_SELECTOR, 'td[cvalue="10002_%s"]' % n)  ##让分胜负结果定位
        return rfsf

    def cdxf_icon(self,n):
        cdxf=(By.CSS_SELECTOR,'td[cvalue="10004_%s"]'%n)###猜大小分定位
        return cdxf

    def csfc_icon(self,n):
        csfc=(By.CSS_SELECTOR,'td[cvalue="10003_%s"]'%n)###猜胜负差定位
        return csfc

    def rfsf_ic(self,a,n,c):
        rfsf = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div[%d]' % (a,n,c))  ##让分胜负结果定位
        return rfsf

    def sfc_ic(self,a,n):
        csfc=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[2]'%(a,n))###胜负差展开投注区
        return csfc

    more_paid=(By.CSS_SELECTOR,'table.jjc_table>tbody>tr:nth-of-type(1)')##混合玩法展开更多页面的paid定位

    confirm_more_ba=(By.ID,'selected_match_ok')##展开更多页面的确定按钮
    emptying = (By.CSS_SELECTOR, 'div[ontap="javascript:jclpage.jcldeal.delm();"]')  ###清空按钮

class HaobcLotteryConfirm_leyou():##竞彩篮球投注确认页
    edit_event_loc=(By.ID,'jcleditmatch')#编辑赛事按钮定位

#######竞足单关元素定位-----mj20171116
class SingleFootChooseNumber_leyou_loc():
    jzdg_play_instruct_loc = (By.CSS_SELECTOR, "li[ontap^='jczdgpage.showhelp()']")
    confirm_more_sfc = (By.ID, 'selected_match_ok')  ###胜负差玩法 ，展开更多页面确认按钮
    confirm_more_pbs = (By.CSS_SELECTOR, 'a[href="javascript:jczdgpage.jczdeal.confirmC(0);"]')  ###展开更多页面确认按钮
    dgp_lottery_loc = (By.CSS_SELECTOR, "div[data-play='dgp']") #单关配模式定位
    dgp_text_loc = (By.ID,"playnametxt")#单关配页面的单关配文本定位

    def paintball_single_mix(self, a, n):
        paintball_single_mix = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div[2]' % (a, n))
        return paintball_single_mix

    def VS_pbs(self, a, n):
        vs = (By.XPATH, '//*[@id="%s"]/li[%d]/div/div[2]/div[1]/div[2]' % (a, n))  ###每场赛事的VS定位
        return vs

    def cjqs_pbs_icon(self, n):
        sf = (By.CSS_SELECTOR, 'td[cvalue="9002_%s"]' % n)  ##胜负结果定位
        return sf

    def cbf_pbs_icon(self, n):
        sf = (By.CSS_SELECTOR, 'td[cvalue="9003_%s"]' % n)  ##胜负结果定位
        return sf

    def cbqc_pbs_icon(self, n):
        sf = (By.CSS_SELECTOR, 'td[cvalue="9004_%s"]' % n)  ##胜负结果定位
        return sf

    def VS_dgp(self, a, n):
        vs = (By.XPATH, '//*[@id="%s"]/li[%d]' % (a, n))  ###每场赛事的VS定位
        return vs

    def VSS(self,a):
        vs=(By.CSS_SELECTOR,'ul#%s>li'%a)
        return vs

    def dgp_vs(self,i):
        dgp_vs=(By.CSS_SELECTOR,'li[data-match="%s"]'%i)
        return dgp_vs

    def csfc_jczq_icon(self,n):
        sf=(By.CSS_SELECTOR,'td[cvalue="10003_%s"]' % n)
        return sf

    def cspf_pbs_icon(self,n):
        sf=(By.CSS_SELECTOR,'td[cvalue="9005_%s"]'%n)#猜胜平负结果定位
        return sf

    more_pbs = (By.CLASS_NAME, 'jjc_table>tbody>tr:nth-of-type(1)')  ###展开更多里的玩法
    emptying_pbs=(By.CSS_SELECTOR,'div[ontap="javascript:jczdgpage.jczdeal.delm();"]')###清空按钮

    def paintball_single_bf(self,a,n):
        paintball_single_bf=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div/div[2]'%(a,n))###比分展开投注区定位
        return paintball_single_bf

    def paintball_single_zjq(self,a,n,b,c):
        zjq=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div/div[%d]/div[%d]'%(a,n,b,c))###总进球赛事结果定位
        return zjq

    def paintball_single_dgp(self,a,n,b,c):
        dgp=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div/div[%d]/div[%d]'%(a,n,b,c))##单关配赛事结果定位
        return dgp

    def paintball_single_dgpo(self,a,n,c):
        dgp=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div[2]/div/div/div[%d]'%(a,n,c))##单关配无让球玩法赛事定位
        return dgp


    def paintball_single_bqc(self,a,n):
        bqc=(By.XPATH,'//*[@id="%s"]/li[%d]/div/div[2]/div/div[2]'%(a,n))##半全场赛事定位
        return bqc

    def dgp_tan(self):
        t=(By.CLASS_NAME,'i-dgpdel')###单关配选号页弹框
        return t

    know_dgp = (By.ID, 'v_open_message_btn')  ###提示投注10倍我知道了


class SingleFootLotteryConfirm_leyou_loc():
    lottery_times_text_loc = (By.ID,"touzhuinfot")#投注倍数文本定位
    back_to_homepage_loc = (By.CSS_SELECTOR, "a[href *= 'cp_back()']")##返回首页链接定位
    lottery_dgp = (By.CSS_SELECTOR, 'strong.red')  ###投注金额

###重庆时时彩选号页元素定位
class CQSSC_ChooseNumber_leyou_loc():
    play_mode_loc = (By.ID, 'Mi_lot_title')  ###玩法定位
    one_star_loc = (By.CSS_SELECTOR,"li[valp='55002']")##一星直选定位
    two_star_loc = (By.CSS_SELECTOR,"li[valp='55003']")##两星直选定位
    three_star_loc = (By.CSS_SELECTOR, "li[valp='55013']")  ##三星直选定位
    five_star_loc = (By.CSS_SELECTOR, "li[valp='55023']")  ##五星直选定位
    big_or_little_loc =(By.CSS_SELECTOR, "li[valp='55001']")##大小单双玩法定位
    def wanwei_choose_number_loc(self,n):
        number_loc = (By.CSS_SELECTOR, "div[id='codes_div'] i[vrq='%d']" %n)
        return number_loc
    def choose_number_loc(self,m,n):
        number_loc = (By.CSS_SELECTOR,"div[id='codes_div%d'] i[vrq='%d']"%(m,n))
        return number_loc

    history_trend_loc = (By.XPATH, '//*[@id="index_page"]/header/div/div[2]/i/ul/li[2]')  ##历史趋势定位
###重庆时时彩投注确认页元素定位---mj20171206
class CQSSC_ConfirmLottery_leyou_loc():
    intelligently_chase_button_loc = (By.ID,"znzh_btn") #智能追号按钮定位
    znzh_issue_num_loc = (By.ID,"znzh_issue_num")#追号期数输入框定位
    totalIssue_loc = (By.ID,"totalIssue")#追号期数定位
    submit_button_loc = (By.ID,"znzh_commit")#智能追号页的提交按钮定位
    revise_button_loc = (By.CLASS_NAME,"s-btn_prog")#修改方案按钮定位
    revise_chase_add_loc = (By.XPATH,"//*[@id='g-progbody']/div/section/ul/li[1]/div/div/i[2]")#修改方案页，追号+按钮定位
    revise_chase_sub_loc = (By.XPATH,'//*[@id="g-progbody"]/div/section/ul/li[1]/div/div/i[1]')#修改方案页，追号—按钮定位
    revise_chase_input_loc = (By.ID,"znzh_qs")#修改方案页，追号输入框定位
    revise_times_input_loc = (By.ID,"znzh_bs")#修改方案页，起始倍数输入框
    revise_times_add_loc = (By.XPATH,'//*[@id="g-progbody"]/div/section/ul/li[2]/div/div/i[2]')#修改方案页，起始倍数+按钮定位
    revise_times_sub_loc = (By.XPATH,'//*[@id="g-progbody"]/div/section/ul/li[2]/div/div/i[1]')#修改方案页，起始倍数-按钮定位
    revise_confirm_loc = (By.ID, "g-ser")  # 修改方案页的确认按钮定位
    revise_cancel_loc = (By.CSS_SELECTOR,'div.m-dialog_submits>a.btn_white.b-flex')  # 修改方案页的取消按钮定位

###############################江西快三
class JXKS_ChooseNumber_leyou_loc():
    def all_play(self,n):
        play=(By.CSS_SELECTOR,'li[valp="%s"]'%n)##江西快三玩法定位
        return play

    assert_play=(By.ID,'g-nav_b')###判断玩法展开或者打开定位
    history_movements=(By.ID,'g-zs')##历史走势
    date_nu=(By.CSS_SELECTOR,'div#zst_div_kj>table.kszs_table.long_zst_section>tr')##历史走势数据
    def date_n(self,n):
        a=(By.CSS_SELECTOR,'div#zst_div_kj>table.kszs_table.long_zst_section>tr:nth-of-type(%d)'%n)##历史走势数据
        return a

    ret=(By.CSS_SELECTOR,'a[href="javascript:hideZstPage();"]')###历史走势，返回按钮

    add_choosenumber=(By.CSS_SELECTOR,'p.empf')####和值选号定位
    da = (By.CLASS_NAME, 'Mi_btn_da')  ##大
    xiao = (By.CLASS_NAME, 'Mi_btn_xiao')  ##小
    dan = (By.CLASS_NAME, 'Mi_btn_dan')  ##单
    shuang = (By.CLASS_NAME, 'Mi_btn_shuang')  ##双
    sthdx_all = (By.CSS_SELECTOR, 'section#select_code_sthdx>ul>li')  ##三同号单选所有选号定位
    sthtx = (By.CLASS_NAME, 'mlr_15')  ###三同号通选选号定位
    ethdx_th = (By.CSS_SELECTOR, 'section#select_code_ethdx>ul:nth-of-type(1)>li>em')  ##二同号单选，同号定位
    ethdx_bth = (By.CSS_SELECTOR, 'section#select_code_ethdx>ul:nth-of-type(2)>li')  ###二同号单选，不同号定位
    ethfx_th = (By.CSS_SELECTOR, 'section#select_code_ethfx>ul:nth-of-type(1)>li>em')  ##二同号复选，定位
    sbth_th = (By.CSS_SELECTOR, 'section#select_code_sbth>ul:nth-of-type(1)>li>em')  ##三不同号，定位

    slhtx_th = (By.CSS_SELECTOR, 'section#select_code_slhtx>ul:nth-of-type(1)>li>em')  ##三不同号，定位
    ebth = (By.CSS_SELECTOR, 'section#select_code_ebth>ul>li')  ###二不同号，选号定位

class JXKS_Confirm_leyou_loc():
    cont=(By.ID,'g-jxxh')##继续选号
    button_add=(By.XPATH,'//*[@id="directly_pay_div"]/div[1]/div[2]/div/div/i[2]')##倍数+号
    button_less=(By.XPATH,'//*[@id="directly_pay_div"]/div[1]/div[2]/div/div/i[1]')##倍数—号

class RX9C_choosenumber_leyou_loc():
    games_nu=(By.CSS_SELECTOR,'#matchList>li')##读取显示的赛事数量

    def games_result(self,i,j):
        a=(By.CSS_SELECTOR,'#match%d>li[chk="%d"]'%(i,j))##赛事结果
        return a

    def games_vs(self,i):
        a=(By.CSS_SELECTOR,'#matchList > li:nth-child(%d) > div > div.b-flex > div > div.vs'%i)###赛事的VS
        return a

    confirm_pick=(By.ID,'todobuy')###确认选号
    clear=(By.CSS_SELECTOR,'div[ontap="clearAll()"]')###清除按钮
    rx9c_play=(By.CSS_SELECTOR,'#g-sm_b>div>section>h3')##玩法说明，任选9场文本定位
    term=(By.ID,'currentIssue')###显示期数

    def term_next(self,n):
        a=(By.CSS_SELECTOR,'#issueList > li:nth-child(%d)'%n)###当前展示的期数的下一期、
        return a

    term_all=(By.CSS_SELECTOR,'#issueList > li')#展示的所有期数
    cont_choose=(By.CSS_SELECTOR,'a[ontap="backsel()"]')##继续选号


class RX9C_ConfirmLottery_leyou_loc():
    submit_station=(By.CSS_SELECTOR,'a[href="javascript:toDoBuy();"]')#提交给站主
    times_add=(By.CLASS_NAME,'btn_add')###倍数+
    times_less=(By.CLASS_NAME,'btn_less')##倍数-

    del_X_nu=(By.CLASS_NAME,'i-del')#显示赛事的X定位
    def del_X(self,n):
        a=(By.CSS_SELECTOR,'i[ontap="del(%d)"]'%n)
        return a
