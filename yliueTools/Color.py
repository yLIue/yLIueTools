class Color(object):
    PURPLE = '\033[35m'
    # PURPLE = '\033[95m'
    GREY = '\033[37m'
    GREEN = '\033[32m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END = '\033[0m'

    CYAN = '\033[96m'
    # DARKCYAN = '\033[36m'
    # GREEN = '\033[92m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

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


if __name__ == '__main__':
    print(Color.cyan("Hello World!"))
    print(Color.blue("Hello World!"))
    print(Color.grey('Hello World!'))
