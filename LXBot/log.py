from colorama import Fore, Style
import logging
import json
import datetime

class ColoredFormatter(logging.Formatter):

    # 定义日志级别颜色映射
    COLOR_MAPPING = {
        'INFO': Fore.GREEN,
        'ERROR': Fore.RED,
        'WARNING': Fore.YELLOW,
        'DEBUG': Fore.BLUE,
        'CRITICAL': Fore.MAGENTA
    }

    def format(self, record):
        # 根据日志级别获取对应颜色
        level_color = self.COLOR_MAPPING.get(record.levelname, Fore.WHITE)
        # 给日志级别添加颜色
        record.levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        # 给记录的名字添加颜色
        record.name = f"{Fore.LIGHTBLUE_EX}{record.name}{Style.RESET_ALL}"
        # 返回格式化后的记录
        return super().format(record)

def setup_logging():
    """设置日志记录，包括文件日志和控制台日志"""
    # 从配置文件中加载日志配置
    config = json.load(open('config/config.json', 'r', encoding='utf-8'))
    log_level = config['log_level'].upper()  # 获取日志级别并转换为大写
    # 设置日志文件名，包含当前的日期和时间
    log_filename = "logs/log_{}.log".format(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))

    # 移除所有已存在的日志处理器
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # 创建文件处理器
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel("DEBUG")  # 设置文件处理器的日志级别为DEBUG
    # 添加格式化器到文件处理器
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

    # 设置根日志记录器的日志级别
    logging.getLogger().setLevel(log_level)
    # 添加文件处理器到根日志记录器
    logging.getLogger().addHandler(file_handler)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)  # 设置控制台处理器的日志级别
    # 添加格式化器到控制台处理器
    console_handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%H:%M:%S'))

    # 刷新文件处理器
    file_handler.flush()
    # 添加控制台处理器到根日志记录器
    logging.getLogger().addHandler(console_handler)

logger = logging.getLogger(__name__)