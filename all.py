import os
import time

import pytest

if __name__ == '__main__':
    # 输出报告到指定路径
    # pytest.main(['-vs', '--html=reports/report.html'])

    # 允许测试用例名称中包含指定字符串的用例
    # pytest.main(['-vs', '-k','weiwei or baili'])

    #指定模块运行
    # pytest.main(['-vs','testcases/test_api2.py'])

    pytest.main()
    time.sleep(3)
    # os.system("allure generate reports/temps -o reports/allures --clean")