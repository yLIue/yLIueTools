import os


class Color(object):
    MAGENTA = '\033[35m'  # 品红
    PURPLE = '\033[38;5;93m'  # 256色
    GREY = '\033[90m'  # 灰色 亮黑
    GREEN = '\033[92m'  # 绿色 亮绿
    RED = '\033[91m'  # 红色 亮红
    BLUE = '\033[94m'  # 蓝色 亮蓝
    YELLOW = '\033[93m'  # 黄色 亮黄
    CYAN = '\033[96m'  # 青色 亮青

    END = '\033[0m'  # 结束标记

    @staticmethod
    def magenta(_msg: str) -> str:
        return f'{Color.MAGENTA}{_msg}{Color.END}'

    @staticmethod
    def purple(_msg: str) -> str:
        return f"{Color.PURPLE}{_msg}{Color.END}"

    @staticmethod
    def grey(_msg: str) -> str:
        return f"{Color.GREY}{_msg}{Color.END}"

    @staticmethod
    def green(_msg: str) -> str:
        return f"{Color.GREEN}{_msg}{Color.END}"

    @staticmethod
    def red(_msg: str) -> str:
        return f"{Color.RED}{_msg}{Color.END}"

    @staticmethod
    def blue(_msg: str) -> str:
        return f"{Color.BLUE}{_msg}{Color.END}"

    @staticmethod
    def yellow(_msg: str) -> str:
        return f"{Color.YELLOW}{_msg}{Color.END}"

    @staticmethod
    def cyan(_msg: str) -> str:
        return f"{Color.CYAN}{_msg}{Color.END}"

    @staticmethod
    def initANSI():
        os.system('')
