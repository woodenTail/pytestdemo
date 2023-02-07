#读取config.yml文件

import os


import yaml

#获取项目路径
def get_object_path():
        return os.getcwd().split('common')[0]

def read_config_file(one_node, two_node):
    with open(get_object_path()+"/config.yml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[one_node][two_node]


def read_extract_file(node_name):
    with open(get_object_path()+"/extract.yml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[node_name]


def write_extract_file(data):
    # mode=a追加写入
    with open(get_object_path()+"/extract.yml", encoding="utf-8", mode='a') as f:
       yaml.dump(data, stream=f, allow_unicode=True)


def clear_extract_file():
    with open(get_object_path() + "/extract.yml", encoding="utf-8", mode='w') as f:
        f.truncate()

#读取yaml测试用例文件
def read_testcase_file(yaml_path):
    with open(get_object_path()+yaml_path, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value



if __name__ == '__main__':
    print(read_config_file('base','base_gzh_url'))