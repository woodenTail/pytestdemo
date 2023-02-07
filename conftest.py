import pytest

from common.yaml_util import clear_extract_file

@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_extract_file()