import os
import shutil
import time
from datetime import datetime
from yliueTools import Color


class Debug(object):
    def __init__(self, _project: str, _debug: bool = True, _filterType: str = 'all', _filterName: str = 'all',
                 _tips: bool = True, _color: bool = True):
        # 项目名称
        self.project = _project
        # debugLog的开关
        self.switch = _debug
        # 类型过滤器 type类型 全部all 运行ING 错误ERR 内部PRIVATE
        self.filterType = _filterType
        # 名称过滤器 全部all 默认default
        self.filterName = _filterName
        # 是否开启提示
        self.tips = _tips
        self.color = _color

    @staticmethod
    def getTypeStr(_type: str) -> str:
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

    def log(self, _msg, _name: str = 'default', _type: str = 'ING'):
        if not self.switch:
            return
        _time = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
        _str = f'[{_time}] {_type} {self.project}.{_name}: {_msg}'
        if _type == 'TIPS':
            if not self.tips:
                return
        if self.color:
            _str = f'{Color.purple(f"[{_time}]")} {Debug.getTypeStr(_type)} {Color.grey(f"{self.project}.{_name}:")} {_msg}'
        if self.filterType == 'all' and self.filterName == 'all':
            print(_str)
            return
        if self.filterType == 'all' or self.filterName == 'all':
            if self.filterType == _type:
                print(_str)
                return
            if self.filterName == _name:
                print(_str)
                return
        if self.filterType != _type or self.filterName != _name:
            return
        print(_str)
        return 0

    def rMain(self, _tips: bool = True):
        if not self.switch:
            return
        Debug.log(self, Color.red('正在本地环境运行'), 'debug.rMain', 'PRIVATE')
        if _tips and self.tips:
            Debug.log(self, "返回新的Path路径,路径为./Debug,请注意更新全局变量", 'debug.rMain', 'TIPS')
        return f'{os.getcwd()}\\Debug'

    def rEnd(self, _tips: bool = True):
        if not self.switch:
            return
        _path = f'{os.getcwd()}\\Debug'
        if not os.path.exists(_path):
            if _tips and self.tips:
                Debug.log(self, "未检测出debug文件夹", 'debug.rEnd', 'TIPS')
            return
        shutil.rmtree(_path)
        if _tips and self.tips:
            Debug.log(self, "删除debug文件夹", 'debug.rEnd', 'TIPS')

    def end(self):
        if not self.switch:
            return
        Debug.log(self, Color.red('运行结束'), 'debug.end', 'PRIVATE')

    def rFor(self, _functionName, _parameter, _epochs, _tips: bool = True):
        _startTime = time.time()
        if not self.switch:
            return
        Debug.log(self, f"初始化迭代器,循环次数[{_epochs}]", 'debug.rFor', 'PRIVATE')
        for _step in range(_epochs):
            Debug.log(self, f"迭代器迭代次数{_step + 1}/{_epochs}", 'debug.rFor', 'PRIVATE')
            Debug.log(self, f'迭代对象激活', 'debug.rFor', 'PRIVATE')
            _functionName(_parameter)
        _endTime = time.time()
        _time = (_endTime - _startTime) * 1000
        Debug.log(self, f"迭代结束,用时 {round(_time, 3)}ms", 'debug.rFor', 'PRIVATE')


if __name__ == '__main__':
    debug = Debug("Debug")
    debug.log('Hello World!')
    # debug.rMain()
