import random

from common.yaml_util import read_extract_file, read_config_file


class DebugTalk:

    #获取随机数的方法
    def get_random_number(self,low, max):
        return random.randint(int(low), int(max))

    def get_extract_data(self, node_name):
        return read_extract_file(node_name)

    def get_base_url(self, node_name):
        return read_config_file('base',node_name)