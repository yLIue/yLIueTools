from yliuetools import Debug
import os
import time
import sys
import shutil
import win32api
# pywin32


class TrackLog:
    def __init__(self, _trackPath: str, _encoding: str = 'utf-8', _color: bool = True):
        # 传参赋值 追踪路径 编码
        self.trackPath = _trackPath
        self.encoding = _encoding

        # 运行内部参数 运行标记符 追踪文件大小
        self.isRunning = False
        self.trackSize = 0
        self.isStop = False

        # Debug
        self.debug = Debug('TrackLog')
        self.debug.logSet(_fillFunc=True, _time=False, _color=_color)

        win32api.SetConsoleCtrlHandler(self.stop, True)

    def getFileSize(self):
        try:
            return os.path.getsize(self.trackPath)
        except OSError:
            return 0

    def read(self):
        try:
            with open(self.trackPath, 'r', encoding=self.encoding) as f:
                # 移动光标
                f.seek(self.trackSize)
                _newContent = f.read()
                self.trackSize = f.tell()
                return _newContent
        except PermissionError:
            return None
        except Exception as e:
            self.debug.logError(str(e))
            return None

    @staticmethod
    def showLog(_msg: str):
        print(_msg, end='', flush=True)

    def run(self):
        # os.system('cls')
        print('TrackLog v0.1')
        print(f'文件路径{self.trackPath}')
        self.debug.log('开始追踪', _type='RUN')
        print('-:')

        while self.isRunning:
            if not os.path.exists(self.trackPath):
                self.debug.log()
                self.debug.logError(f'文件被删除,停止追踪')
                break
            _sizeIng = self.getFileSize()
            # 如果添加了新内容
            if _sizeIng > self.trackSize:
                _content = self.read()
                if _content is not None:
                    self.showLog(_content)
        if not self.isStop:
            self.stop()

    def stop(self, *_stopType):
        # stopType 0 ctrl+c
        # stopType 2 点关闭
        self.isStop = True
        # self.debug.log(_stopType, _type='STOP_TYPE')
        if _stopType == (0,):
            # ctrl+c
            self.debug.log()
            self.debug.logError('用户中断')
            self.isStop = False
            self.isRunning = False
            return True
        self.debug.logEnd('追踪结束')
        while True:
            try:
                if os.path.exists('.log'):
                    shutil.rmtree('.log')
                break
            except PermissionError:
                time.sleep(0.1)
        print('5秒后关闭程序')
        time.sleep(5)
        return True

    def start(self):
        _path = self.trackPath
        if not os.path.exists(_path):
            self.debug.logError(f'路径:{_path} 文件不存在,等待文件创建')
            while not os.path.exists(_path):
                time.sleep(0.2)

        # 初始化
        self.trackSize = self.getFileSize()
        self.isRunning = True

        # 运行
        self.run()


if __name__ == '__main__':
    args = sys.argv[1:]
    trackLog = TrackLog(args[1], _color=bool(args[3]))
    trackLog.start()
