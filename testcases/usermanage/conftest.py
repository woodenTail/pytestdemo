import pytest


@pytest.fixture(scope="function")
def user_setup():
    print("用户管理的共性")