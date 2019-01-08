import unittest,time
from HTMLTestRunner_jpg import HTMLTestRunner
from modle.function import send_mail,screen_shot,logfile

case_dir = "./test_case/LeXiu"
pattern="*arrang_five_*.py"
discover = unittest.defaultTestLoader.discover(case_dir,pattern)

logfile()
if __name__ =='__main__':

    ##日期格式
    times = time.strftime("%Y%m%d%H%M%S")
    report_file="./report/lexiu/LexiuCP_Arrang_Five_case_"+times+".html"
    fp = open(report_file,"wb")

    runner = HTMLTestRunner(stream=fp,
                            title="乐秀排列5——自动化测试报告",
                            description="运行环境：win7 Chrome")
    try:
        runner.run(discover)
    except:
        print('运行列表错误')
    finally:
        fp.close()
    send_mail(report_file)