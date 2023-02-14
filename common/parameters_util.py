import csv
import json
import traceback

import yaml

from common.logger_util import write_log, error_log
from common.yaml_util import get_object_path


def read_csv_file(csv_path):
    csv_data_list = []
    with open(get_object_path() + "/" +csv_path, encoding="utf-8") as f:
        csv_data = csv.reader(f)
        for row in csv_data:
            csv_data_list.append(row)
    return csv_data_list#读取yaml测试用例文件

def read_testcase_file(yaml_path):
    try:
        with open(get_object_path()+yaml_path, encoding="utf-8") as f:
            caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
            if len(caseinfo)>=2:
                return caseinfo
            caseinfo_keys = dict(*caseinfo).keys()
            if 'parameters' in caseinfo_keys:
                new_caseinfo = analysis_parameters(*caseinfo)
                return new_caseinfo
            else:
                return caseinfo
    except Exception as f:
        error_log("读取用例文件报错，异常：%s"%str(traceback.format_exc()))


#分析参数化
def analysis_parameters(caseinfo):
    try:
        caseinfo_keys = dict(caseinfo).keys()
        if 'parameters' in caseinfo_keys:
            for key, value in dict(caseinfo['parameters']).items():
                caseinfo_str = json.dumps(caseinfo)
                key_list = str(key).split('-')
                # print(key_list)
                csv_data_list = read_csv_file(value)
                # 规范csv数据的写法
                one_row_csv_data = csv_data_list[0]
                length_flag = True
                for csv_data in csv_data_list:
                    if len(csv_data) != len(one_row_csv_data):
                        length_flag = False
                        break
                # 解析
                new_caseinfo = []
                if length_flag:
                    for x in range(1, len(csv_data_list)):
                        temp_caseinfo = caseinfo_str
                        for y in range(0, len(csv_data_list[x])):  # 列循环
                            if csv_data_list[0][y] in key_list:
                                temp_caseinfo = temp_caseinfo.replace("$csv{" + csv_data_list[0][y] + "}",
                                                                      csv_data_list[x][y])
                        new_caseinfo.append(json.loads(temp_caseinfo))
                    return new_caseinfo
                else:
                    return caseinfo
    except Exception as f:
        error_log("分析parameters参数异常：%s" % str(traceback.format_exc()))
if __name__ == '__main__':
    print(read_csv_file('data/get_token.csv'))