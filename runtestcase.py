# -*- coding: UTF-8 -*-
import os
import sys
import re
import time
import unittest
from userlib import HTMLTestRunner, userlib
import logging


# 运行测试用例并输出测试报告，
class RunTestcase():
    # 设置全局变量获取文件夹路径
    globalpath = sys.path[0]

    #设置系统默认环境
    def getpath(self):
        for item in sys.path:
            if re.match("^.*?//AutoTest_new$",item):
                self.path = item
                return item
        return self.path

    # 初始项目目录结构
    def initialproject(self):
        testcasepath = self.globalpath + "\\test_case"  # 测试用例文件夹
        reportpath = self.globalpath + "\\report"  # 测试报告文件件
        screenshotpath = reportpath + "\\screenshot"  # 测试报告截图
        logpath = reportpath + "\\log"
        floderpaths = [testcasepath, reportpath, screenshotpath, logpath]
        for i in range(0, floderpaths.__len__()):
            if os.path.exists(floderpaths[i]) is not True:
                os.mkdir(floderpaths[i])
        op = open(logpath+"\\log.log", "wb")
        op.close()
        userlib.Userlib().initallog(logpath)


    # 添加test_case文件夹下所有用例到用例集
    def add_testcase(self):
        testunit = unittest.TestSuite()
        testcasefolder = self.globalpath + "\\test_case"
        discover = unittest.defaultTestLoader.discover(testcasefolder, pattern='testcase01*.py', top_level_dir=None)
        for testsuite in discover:
            for test in testsuite:
                testunit.addTest(test)
        return testunit

    # 测试报告
    def output_report(self):
        reportname = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time())) + "_reasult.html"
        logging.info(reportname)
        reportpath = self.globalpath + "\\report\\" + reportname
        return reportpath

    # 运行测试用例
    def runtestcase(self):
        runner = RunTestcase()
        runner.initialproject()

        testunit = runner.add_testcase()
        reportpath = runner.output_report()
        op = open(reportpath, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=op, title=u"AutoTest", description=u"__YPSH__")
        runner.run(testunit)
        op.close()
        os.system(reportpath)


if __name__ == '__main__':
    runner = RunTestcase()
    runner.runtestcase()
