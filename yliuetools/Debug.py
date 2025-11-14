import inspect
import os
import shutil
import time
from datetime import datetime
from yliuetools import Color
import subprocess


class Debug(object):
    def __init__(self, _project: str, _debug: bool = True, _cmd: bool = False):
        # 项目名称
        self.__project = _project
        # debug的开关
        self.__switch = _debug
        # 是否用cmd单独显示
        self.__cmd = _cmd

        # 名称过滤器 全部all 默认函数名
        self.__filterFunc = 'all'
        # 类型过滤器 type类型 全部all 运行ING 错误ERR 内部PRIVATE
        self.__filterType = 'all'
        # 是否开启提示
        self.__tips = True
        # 是否开启颜色
        self.__color = True
        # 是否开启实验内容
        self.__expt = False
        # 默认填写函数名
        self.__fillFunc = False
        # 是否时间显示
        self.__time = True
        # 临时文件路径
        self.__tempPath = '.log\\log.txt'
        # 函数传递层数
        self.__layer = 0

        # 尝试激活cmd中的ANSI功能
        Color.initANSI()

        if self.__cmd:
            _tPath = __file__[:-8] + 'TrackLog.py'
            os.system(f'start cmd /k "python {_tPath} path {self.__tempPath} color {self.__color}"')
            self.initTempFile()

    def initTempFile(self):
        _rootPath = '.log'
        if not os.path.exists(_rootPath):
            os.makedirs(_rootPath)
            subprocess.run(f'attrib +h "{_rootPath}"', shell=True, check=True)
            with open(self.__tempPath, 'w'):
                pass
            time.sleep(1)

    def cmdOff(self):
        if self.__cmd:
            while True:
                try:
                    if os.path.exists('.log'):
                        shutil.rmtree('.log')
                    break
                except PermissionError:
                    time.sleep(0.1)

    @staticmethod
    def __getTypeStr(_type: str) -> str:
        if _type == 'ING' or _type == 'OK' or _type == 'RUN':
            _typeStr = Color.green(_type)
        elif _type == 'ERR':
            _typeStr = Color.red(_type)
        elif _type == 'PRIVATE':
            _typeStr = Color.blue(_type)
        elif _type == 'TIPS':
            _typeStr = Color.cyan(_type)
        elif _type == 'GLOBAL' or _type == 'OUTPUT' or _type == 'SUCCESS':
            _typeStr = Color.yellow(_type)
        elif _type == 'END':
            _typeStr = Color.grey(_type)
        else:
            _typeStr = _type
        return _typeStr

    def __getLogStr(self, _msg, _func, _type) -> tuple[str, str]:
        self.__layer += 1
        _layer = self.__layer
        _time = self.__logTime()

        # 默认填写函数名
        if self.__fillFunc:
            if _func == 'default':
                _func = inspect.stack()[_layer].function
                if _func == '<module>':
                    _func = 'main'

        self.__layer = 0

        _strLog = f'{_time}{_type} {self.__project}.{_func}: {_msg}'

        _time = Color.purple(_time)
        _type = self.__getTypeStr(_type)

        _colorLog = f'{_time}{_type} {self.__project}{Color.grey(f".{_func}")} {_msg}'
        return _strLog, _colorLog

    def __logTime(self) -> str:
        if self.__time:
            _time = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
            _time = f'[{_time}] '
            return _time
        return ''

    def __filter(self, _str: str, _func: str, _type: str):
        # 筛选器
        if self.__filterType == 'all' and self.__filterFunc == 'all':
            self.logPrint(_str)
            return
        if self.__filterType == 'all' or self.__filterFunc == 'all':
            if self.__filterType == _type:
                self.logPrint(_str)
                return
            if self.__filterFunc == _func:
                self.logPrint(_str)
                return
        if self.__filterType != _type or self.__filterFunc != _func:
            return
        self.logPrint(_str)
        return

    def logPrint(self, _msg: str):
        if self.__cmd:
            self.logSave(_msg)
            return
        print(_msg)

    def logSave(self, _msg: str):
        if self.__cmd:
            while True:
                try:
                    with open(self.__tempPath, 'a+', encoding='utf-8') as f:
                        f.write(f'{_msg}\n')
                    break
                except FileNotFoundError:
                    return
                except PermissionError:
                    time.sleep(0.1)

    def logError(self, _msg: str, _func: str = 'default'):
        self.__layer += 1
        self.log(_msg, _func, 'ERR')

    def logEnd(self, _msg: str, _func: str = 'default'):
        self.__layer += 1
        self.log(_msg, _func, 'END')

    def log(self, _msg='', _func: str = 'default', _type: str = 'ING'):
        self.__layer += 1

        # debug关闭
        if not self.__switch:
            return
        # 如果是提示
        if _type == 'TIPS':
            if not self.__tips:
                return
        # 打印空白行
        if _msg == '':
            self.logPrint('')
            return

        _strLog, _colorLog = self.__getLogStr(_msg, _func, _type)
        _str = _strLog

        # 是否输出颜色
        if self.__color:
            _str = _colorLog
        # 筛选
        self.__filter(_str, _func, _type)

    def logSet(self, _tips: bool = 'default', _color: bool = 'default',
               _fillFunc: bool = 'default', _time: bool = 'default'):
        if _tips != 'default':
            # 是否开启提示
            self.__tips = _tips
        if _color != 'default':
            # 是否开启颜色
            self.__color = _color
        if _fillFunc != 'default':
            # 是否默认填写函数名
            self.__fillFunc = _fillFunc
        if _time != 'default':
            # 是否显示时间
            self.__time = _time
        return

    def logSetReset(self):
        # 重置输出设置
        self.__tips = True
        self.__color = True
        self.__fillFunc = False
        self.__time = True

    def filter(self, _func: str = 'default', _type: str = 'default'):
        if _func != 'default':
            self.__filterFunc = _func
        if _type != 'default':
            self.__filterType = _type
        return

    def filterReset(self):
        # 重置过滤器
        self.__filterFunc = 'all'
        self.__filterType = 'all'

    # 测试内容
    def __rMain(self, _tips: bool = True):
        if not self.__switch:
            return
        self.log(Color.red('正在本地环境运行'), 'debug.rMain', 'PRIVATE')
        if _tips and self.__tips:
            self.log("返回新的Path路径,路径为./Debug,请注意更新全局变量", 'debug.rMain', 'TIPS')
        return f'{os.getcwd()}\\Debug'

    def __rEnd(self, _tips: bool = True):
        if not self.__switch:
            return
        _path = f'{os.getcwd()}\\Debug'
        if not os.path.exists(_path):
            if _tips and self.__tips:
                self.log("未检测出debug文件夹", 'debug.rEnd', 'TIPS')
            return
        shutil.rmtree(_path)
        if _tips and self.__tips:
            self.log("删除debug文件夹", 'debug.rEnd', 'TIPS')

    def __end(self):
        if not self.__switch:
            return
        self.log(Color.red('运行结束'), 'debug.end', 'PRIVATE')

    def __rFor(self, _functionName, _parameter, _epochs, _tips: bool = True):
        _startTime = time.time()
        if not self.__switch:
            return
        self.log(f"初始化迭代器,循环次数[{_epochs}]", 'debug.rFor', 'PRIVATE')
        for _step in range(_epochs):
            self.log(f"迭代器迭代次数{_step + 1}/{_epochs}", 'debug.rFor', 'PRIVATE')
            self.log(f'迭代对象激活', 'debug.rFor', 'PRIVATE')
            _functionName(_parameter)
        _endTime = time.time()
        _time = (_endTime - _startTime) * 1000
        self.log(f"迭代结束,用时 {round(_time, 3)}ms", 'debug.rFor', 'PRIVATE')
