import unittest,time
from HTMLTestRunner_jpg import HTMLTestRunner
from modle.function import send_mail,screen_shot,logfile

case_dir = "./test_case/lelun"
pattern="*rx9c_*.py"
discover = unittest.defaultTestLoader.discover(case_dir,pattern)
logfile()

if __name__ =='__main__':

    #日期格式化
    times = time.strftime("%Y%m%d%H%M%S")
    report_file="./report/lelun/Lelun_RX9C_case_"+times+".html"
    fp = open(report_file,"wb")

    runner = HTMLTestRunner(stream=fp,
                            title="乐仑任选9场——自动化测试报告",
                            description="运行环境：win7 Chrome")
    try:
        runner.run(discover)
    except:
        print('运行异常')
    finally:
        fp.close()
    send_mail(report_file)