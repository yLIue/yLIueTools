import os
import time

from yliuetools import *

# debug
# debug = Debug('yLIueToolsTest')
debug = Debug('yLIueToolsTest', _cmd=True)  # 测试cmd
debug.showDebugLog()


def TestText():
    debug.log('测试文本,default')
    debug.log('测试文本,Fun', _func='Fun')
    debug.logOk('测试文本,ok,default')
    debug.logError('测试文本,error,Fun', _func='Fun')
    debug.logEnd('测试文本,end,default')


def ColorTest():
    debug.log()
    debug.log('关闭颜色')
    debug.logSet(_color=False)
    debug.log()
    TestText()
    debug.logSetReset()


def FillFuncTest():
    debug.log()
    debug.log('自动填充函数名')
    debug.logSet(_fillFunc=True)
    debug.log()
    TestText()
    debug.logSetReset()


def TimeTest():
    debug.log()
    debug.log('关闭时间显示')
    debug.logSet(_time=False)
    debug.log()
    TestText()
    debug.logSetReset()


def FilterTest():
    debug.log()
    debug.log('开启筛选,Fun,err')
    debug.filter('Fun', 'ERR')
    TestText()
    debug.filterReset()
    debug.log('开启筛选,INFO')
    debug.filter(_type='INFO')
    TestText()
    debug.filterReset()


def DebugPathTest():
    debug.log()
    debug.log('开启Debug路径')
    _path = os.getcwd()
    debug.setLocalPath(_path)
    _debugPath = debug.DebugPath(_path)
    debug.log(f'DebugPath:{_debugPath}', 'OUTPUT')
    debug.logError('5秒后清除.debug文件')
    time.sleep(5)


def CleanDebug():
    debug.log()
    debug.log('清除debug文件')
    debug.cleanDebug()


if __name__ == '__main__':
    debug.log('开始测试')
    debug.log()
    TestText()

    ColorTest()
    FillFuncTest()
    TimeTest()
    FilterTest()
    DebugPathTest()
    CleanDebug()


