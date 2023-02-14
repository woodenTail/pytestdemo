import logging
import time

from common.yaml_util import get_object_path, read_config_file


class LoggerUtil:

    def create_log(self, logger_name='log'):
        # 创建一个日志对象
        self.logger = logging.getLogger(logger_name)
        # 设置全局的日志级别
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:

            # 文件日志
            # 获得日志文件的名称
            self.file_log_path = get_object_path()+'/logs/'+read_config_file('log','log_name')+str(int(time.time()))+ '.log'
            # 创建文件日志的控制器
            self.file_handler = logging.FileHandler(self.file_log_path, encoding='utf-8')
            # 设置文件日志的级别
            file_log_level = str(get_object_path() + '/logs/' + read_config_file('log', 'log_level')).lower()
            if file_log_level == 'debug':
                self.file_handler.setLevel(logging.DEBUG)
            elif file_log_level == 'info':
                self.file_handler.setLevel(logging.INFO)
            elif file_log_level == 'warning':
                self.file_handler.setLevel(logging.WARNING)
            elif file_log_level == 'error':
                self.file_handler.setLevel(logging.ERROR)
            elif file_log_level == 'critical':
                self.file_handler.setLevel(logging.CRITICAL)
            # 设置文件日志的格式
            self.file_handler.setFormatter(logging.Formatter(read_config_file('log','log_format')))
            #将控制器加到日志对象
            self.logger.addHandler(self.file_handler)

            # 控制台日志
            # 创建文件日志的控制器
            self.console_handler = logging.StreamHandler()
            # 设置文件日志的级别
            console_log_level = str(get_object_path() + '/logs/' + read_config_file('log', 'log_level')).lower()
            if console_log_level == 'debug':
                self.console_handler.setLevel(logging.DEBUG)
            elif console_log_level == 'info':
                self.console_handler.setLevel(logging.INFO)
            elif console_log_level == 'warning':
                self.console_handler.setLevel(logging.WARNING)
            elif console_log_level == 'error':
                self.console_handler.setLevel(logging.ERROR)
            elif console_log_level == 'critical':
                self.console_handler.setLevel(logging.CRITICAL)
            # 设置文件日志的格式
            self.console_handler.setFormatter(logging.Formatter(read_config_file('log', 'log_format')))
            # 将控制器加到日志对象
            self.logger.addHandler(self.console_handler)
        return self.logger

#函数：输出日志
def write_log(log_message):
    LoggerUtil().create_log().info(log_message)

def error_log(log_message):
    LoggerUtil().create_log().info(log_message)
    raise Exception(log_message)


if __name__ == '__main__':
    write_log("fdsfv发")
    write_log("发送到")
