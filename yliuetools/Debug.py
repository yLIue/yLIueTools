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
        # 内部信息打印
        self.__showIntoLog = False
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
        # 项目的本地路径
        self.__localPath = None

        # 尝试激活cmd中的ANSI功能
        Color.initANSI()

        if self.__cmd:
            _tPath = __file__[:-8] + 'TrackLog.py'
            if os.path.exists('.log'):
                while True:
                    try:
                        if os.path.exists('.log'):
                            shutil.rmtree('.log')
                        break
                    except PermissionError:
                        time.sleep(0.1)
            os.system(f'start cmd /c "python {_tPath} path {self.__tempPath} color {self.__color}"')
            self.initTempFile()



    def showDebugLog(self):
        self.__showIntoLog = True

    def initTempFile(self):
        _rootPath = '.log'
        if not os.path.exists(_rootPath):
            os.makedirs(_rootPath)
            subprocess.run(f'attrib +h "{_rootPath}"', shell=True, check=True)
            with open(self.__tempPath, 'w'):
                pass
            time.sleep(1)

    @staticmethod
    def __getTypeStr(_type: str) -> str:
        # ing ok 正常运行 run启动
        if _type == 'ING' or _type == 'OK' or _type == 'RUN' or _type == 'INFO':
            _typeStr = Color.green(_type)
        # 错误
        elif _type == 'ERR':
            _typeStr = Color.red(_type)
        # Debug内部打印
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

    def __getLogStr(self, _msg, _func, _type, _into=False) -> tuple[str, str]:
        self.__layer += 1
        _layer = self.__layer

        _time = self.__logTime()
        _project = self.__project
        if _into:
            _project = 'Debug'

        # 默认填写函数名
        if self.__fillFunc:
            if _func == 'default':
                _func = inspect.stack()[_layer].function
                if _func == '<module>':
                    _func = 'main'

        _strLog = f'{_time}{_type} {_project}.{_func}: {_msg}'

        if _into:
            _project = Color.yellow(_project)
        _time = Color.purple(_time)
        _type = self.__getTypeStr(_type)

        _colorLog = f'{_time}{_type} {_project}{Color.grey(f".{_func}")} {_msg}'
        return _strLog, _colorLog

    def __logTime(self) -> str:
        if self.__time:
            _time = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
            _time = f'[{_time}] '
            return _time
        return ''

    def __intoLog(self, _msg='', _type: str = 'INFO', _func: str = 'default') -> None:
        if not self.__showIntoLog:
            return
        _strLog, _colorLog = self.__getLogStr(_msg, _func, _type, True)
        _str = _strLog

        # 是否输出颜色
        if self.__color:
            _str = _colorLog

        self.__logPrint(_str)

    def __filter(self, _str: str, _func: str, _type: str):
        # 筛选器
        if self.__filterType == 'all' and self.__filterFunc == 'all':
            self.__logPrint(_str)
            return
        if self.__filterType == 'all' or self.__filterFunc == 'all':
            if self.__filterType == _type:
                self.__logPrint(_str)
                return
            if self.__filterFunc == _func:
                self.__logPrint(_str)
                return
        if self.__filterType != _type or self.__filterFunc != _func:
            return
        self.__logPrint(_str)
        return

    def __logPrint(self, _msg: str):
        self.__layer = 0
        if not self.__switch:
            return
        if self.__cmd:
            self.__logSave(_msg)
            return
        print(_msg)

    def __logSave(self, _msg: str):
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

    def logOk(self, _msg, _func: str = 'default'):
        self.__layer += 1
        self.log(_msg, 'OK', _func)

    def logError(self, _msg: str, _func: str = 'default'):
        self.__layer += 1
        self.log(_msg, 'ERR', _func)

    def logEnd(self, _msg: str, _func: str = 'default'):
        self.__layer += 1
        self.log(_msg, 'END', _func)

    def log(self, _msg='', _type: str = 'INFO', _func: str = 'default'):
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
            self.__logPrint('')
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

    def setLocalPath(self, _localPath: str):
        self.__localPath = _localPath

    def DebugPath(self, _defaultPath: str):
        _localPath = self.__localPath
        try:
            _path = _localPath + '\\.debug'
        except TypeError:
            self.logError('初始化debug文件失败:没有设置本地路径,请用Debug.setLocalPath')
            return _defaultPath
        if self.__switch:
            try:
                os.mkdir(_path)
            except FileExistsError:
                pass
            except FileNotFoundError:
                self.logError(f'初始化debug文件失败:项目本地路径不存在:{_localPath}')
                return _localPath
            return _path + '\\'

        try:
            shutil.rmtree(_path)
            self.__intoLog('删除.debug文件', 'OK')
        except FileNotFoundError:
            pass
        return _localPath

    def cleanDebug(self):
        if not self.__switch:
            return
        self.__layer += 1
        _localPath = self.__localPath
        if _localPath:
            _debugPath = _localPath + '\\.debug'
            self.__intoLog('尝试清除.debug文件', _func='cleanDebug')
            try:
                self.__layer += 1
                shutil.rmtree(_debugPath)
                self.__intoLog('清除成功', 'OK', 'cleanDebug')
            except FileNotFoundError:
                self.__intoLog('清除失败:文件不存在', 'ERR', 'cleanDebug')

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
