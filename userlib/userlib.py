# -*- coding: UTF-8 -*-
import os
import sys
import time

reload(sys)
import unittest
import HTMLTestRunner
import logging
from selenium import webdriver


# 运行测试用例并输出测试报告
class Userlib():
    # 设置全局变量获取文件夹路径
    globalpath = sys.path[0]
    #截图
    def sceenshot(self, driver, folderpath):
        self.driver = driver
        picname = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time())) + "_shot.png"
        picpath = self.globalpath + "\\report\\screenshot\\" + picname
        try:
            self.driver.get_screenshot_as_file(picpath)
            print "screenshot:"+ picpath
            # logging.info("screenshot：" + picpath )
        except:
            logging.info("sceenshot failed")
        return picpath

    def initallog(self,logpath):
        # 设置全局日志
        if logpath != "":
            self.logpath = logpath
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(filename)s -- %(funcName)s s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%Y-%M-%d %H:%M:%S',
                                filename='report\\log\\log.log',
                                filemode='w'
                                )  # filemode='w' 模式覆盖原日志

            #################################################################################################
            # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
            console.setFormatter(formatter)
            logging.getLogger('').addHandler(console)
            #################################################################################################
        else:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(filename)s -- %(funcName)s s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%Y-%M-%d %H:%M:%S',
                                filename='log.log'
                                )  # filemode='w' 模式覆盖原日志

            #################################################################################################
            # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
            console.setFormatter(formatter)
            logging.getLogger('').addHandler(console)
            #################################################################################################

    def getpath(self):
        return self.globalpath





if __name__ == '__main__':
   print Userlib().getpath()