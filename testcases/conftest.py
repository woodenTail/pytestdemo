import pytest
import requests

session = None
def read_yaml():
    return ['甄子丹','成龙','菜10']

# autouse自动执行
@pytest.fixture(scope="package")
def excute_sql():
    print("执行数据库的验证。查询数据库")
    yield
    print("关闭数据库的连接")

@pytest.fixture(scope="session")
def get_session():
    session = requests.session()  # 获得请求的session对象
    return session