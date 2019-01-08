from selenium.webdriver.common.by import By
from element_operate.base import Page
from element_position.lemi import Login_loc
from element_position.lexiu import Login_lexiu_loc
from element_operate.base import Page_lexiu
from element_position.leyou import Login_leyou_loc
from element_operate.base import Page_leyou
from element_position.lelun import Login_lelun_loc
from element_operate.base import Page_lelun


class Login(Page,Login_loc):

    #################################元素操作###############################################
    #点击“新用户登录”标签
    def new_user_login_tab(self):
        self.wait_element_located(self.driver, self.new_user_login_tab_loc)
        self.find_element(*self.new_user_login_tab_loc).click()

    #输入用户手机号
    def username(self,text):
        self.find_element(*self.username_loc).clear()#清除用户名文本
        self.find_element(*self.username_loc).send_keys(text)#输入登录用户名

    #输入用名密码
    def password(self,text):
        self.find_element(*self.password_loc).clear()#清除用户密码文本
        self.find_element(*self.password_loc).send_keys(text)#输入用户密码

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #登录操作的封装
    def login(self):
        self.new_user_login_tab()
        self.username("17602882784")
        self.password("123456")
        self.login_button()
    ##没有余额的账户登录
    def login_nomoney(self):
        self.new_user_login_tab()
        self.username("13524926965")
        self.password("123456AAA")
        self.login_button()

class Login_lexiu(Page_lexiu,Login_lexiu_loc):
    # 输入用户手机号
    def username_lexiu(self, text):
        self.find_element(*self.username_loc).clear()  # 清除用户名文本
        self.find_element(*self.username_loc).send_keys(text)  # 输入登录用户名

    # 输入用名密码
    def password_lexiu(self, text):
        self.find_element(*self.password_loc).clear()  # 清除用户密码文本
        self.find_element(*self.password_loc).send_keys(text)  # 输入用户密码

    def login_button_lexiu(self):
        self.find_element(*self.login_button_loc).click()

    #登录操作的封装
    def login_lexiu(self):
        #self.new_user_login_tab()
        self.username_lexiu("17602882784")
        self.password_lexiu("123456")
        self.login_button_lexiu()
    ##没有余额的账户登录
    def login_nomoney_lexiu(self):
        #self.new_user_login_tab()
        self.username_lexiu("13524926965")
        self.password_lexiu("123456AAA")
        self.login_button_lexiu()

class Login_leyou(Page_leyou,Login_leyou_loc):
    # 输入用户手机号
    def username_leyou(self, text):
        self.find_element(*self.username_loc).clear()  # 清除用户名文本
        self.find_element(*self.username_loc).send_keys(text)  # 输入登录用户名

    # 输入用名密码
    def password_leyou(self, text):
        self.find_element(*self.password_loc).clear()  # 清除用户密码文本
        self.find_element(*self.password_loc).send_keys(text)  # 输入用户密码

    def login_button_leyou(self):
        self.find_element(*self.login_button_loc).click()

    #登录操作的封装
    def login_leyou(self):
        #self.new_user_login_tab()
        self.username_leyou("17602882784")
        self.password_leyou("123456")
        self.login_button_leyou()
    ##没有余额的账户登录
    def login_nomoney_leyou(self):
        #self.new_user_login_tab()
        self.username_leyou("13524926965")
        self.password_leyou("123456AAA")
        self.login_button_leyou()


class Login_lelun(Page_lelun,Login_lelun_loc):
    # 输入用户手机号
    def username_lelun(self, text):
        self.find_element(*self.username_loc).clear()  # 清除用户名文本
        self.find_element(*self.username_loc).send_keys(text)  # 输入登录用户名

    # 输入用名密码
    def password_lelun(self, text):
        self.find_element(*self.password_loc).clear()  # 清除用户密码文本
        self.find_element(*self.password_loc).send_keys(text)  # 输入用户密码

    def login_button_lelun(self):
        self.find_element(*self.login_button_loc).click()

    #登录操作的封装
    def login_lelun(self):
        #self.new_user_login_tab()
        self.username_lelun("17602882784")
        self.password_lelun("123456sxl")
        self.login_button_lelun()
    ##没有余额的账户登录
    def login_nomoney_lelun(self):
        #self.new_user_login_tab()
        self.username_lelun("13524926965")
        self.password_lelun("123456AAA")
        self.login_button_lelun()


