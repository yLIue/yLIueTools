import inspect
import os
import shutil
import time
from datetime import datetime
from yliueTools import Color


class Debug(object):
    def __init__(self, _project: str, _debug: bool = True, _expt: bool = False):
        # 项目名称
        self.project = _project
        # debug的开关
        self.switch = _debug
        # 名称过滤器 全部all 默认函数名
        self.__filterFunc = 'all'
        # 类型过滤器 type类型 全部all 运行ING 错误ERR 内部PRIVATE
        self.__filterType = 'all'
        # 是否开启提示
        self.tips = True
        # 是否开启颜色
        self.color = True
        # 是否开启实验内容
        self.expt = _expt
        # 默认填写函数名
        self.__fillFunc = False
        # 是否时间显示
        self.__time = True

    @staticmethod
    def __getTypeStr(_type: str) -> str:
        if _type == 'ING':
            _typeStr = Color.green(_type)
        elif _type == 'ERR':
            _typeStr = Color.red(_type)
        elif _type == 'PRIVATE':
            _typeStr = Color.blue(_type)
        elif _type == 'TIPS':
            _typeStr = Color.cyan(_type)
        elif _type == 'GLOBAL' or _type == 'OUTPUT':
            _typeStr = Color.yellow(_type)
        else:
            _typeStr = _type
        return _typeStr

    def __logTime(self) -> str:
        if self.__time:
            _time = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
            _time = f'[{_time}] '
            if self.color:
                _time = Color.purple(_time)
            return _time
        return ''

    def log(self, _msg='', _func: str = 'default', _type: str = 'ING'):
        # debug关闭
        if not self.switch:
            return

        # 打印空白行
        if _msg == '':
            print()
            return

        # 默认填写函数名
        if self.__fillFunc:
            if _func == 'default':
                _func = inspect.stack()[1].function
                if _func == '<module>':
                    _func = 'main'

        _logTime = self.__logTime()
        _str = _logTime + f'{_type} {self.project}.{_func}: {_msg}'

        # 如果是提示
        if _type == 'TIPS':
            if not self.tips:
                return

        # 是否输出颜色
        if self.color:
            _str = _logTime + f'{self.__getTypeStr(_type)} {Color.grey(f"{self.project}.{_func}:")} {_msg}'

        # 筛选器
        if self.__filterType == 'all' and self.__filterFunc == 'all':
            print(_str)
            return
        if self.__filterType == 'all' or self.__filterFunc == 'all':
            if self.__filterType == _type:
                print(_str)
                return
            if self.__filterFunc == _func:
                print(_str)
                return
        if self.__filterType != _type or self.__filterFunc != _func:
            return

        print(_str)
        return

    def logSet(self, _tips: bool = 'default', _color: bool = 'default',
               _fillFunc: bool = 'default', _time: bool = 'default'):
        if _tips != 'default':
            # 是否开启提示
            self.tips = _tips
        if _color != 'default':
            # 是否开启颜色
            self.color = _color
        if _fillFunc != 'default':
            # 是否默认填写函数名
            self.__fillFunc = _fillFunc
        if _time != 'default':
            # 是否显示时间
            self.__time = _time
        return

    def logSetReset(self):
        # 重置输出设置
        self.tips = True
        self.color = True
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

    def rMain(self, _tips: bool = True):
        if not self.switch:
            return
        self.log(Color.red('正在本地环境运行'), 'debug.rMain', 'PRIVATE')
        if _tips and self.tips:
            self.log("返回新的Path路径,路径为./Debug,请注意更新全局变量", 'debug.rMain', 'TIPS')
        return f'{os.getcwd()}\\Debug'

    def rEnd(self, _tips: bool = True):
        if not self.switch:
            return
        _path = f'{os.getcwd()}\\Debug'
        if not os.path.exists(_path):
            if _tips and self.tips:
                self.log("未检测出debug文件夹", 'debug.rEnd', 'TIPS')
            return
        shutil.rmtree(_path)
        if _tips and self.tips:
            self.log("删除debug文件夹", 'debug.rEnd', 'TIPS')

    def end(self):
        if not self.switch:
            return
        self.log(Color.red('运行结束'), 'debug.end', 'PRIVATE')

    def rFor(self, _functionName, _parameter, _epochs, _tips: bool = True):
        _startTime = time.time()
        if not self.switch:
            return
        self.log(f"初始化迭代器,循环次数[{_epochs}]", 'debug.rFor', 'PRIVATE')
        for _step in range(_epochs):
            self.log(f"迭代器迭代次数{_step + 1}/{_epochs}", 'debug.rFor', 'PRIVATE')
            self.log(f'迭代对象激活', 'debug.rFor', 'PRIVATE')
            _functionName(_parameter)
        _endTime = time.time()
        _time = (_endTime - _startTime) * 1000
        self.log(f"迭代结束,用时 {round(_time, 3)}ms", 'debug.rFor', 'PRIVATE')


if __name__ == '__main__':
    pass
