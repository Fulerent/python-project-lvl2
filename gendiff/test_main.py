import pytest
from gendiff import diff_files


@pytest.fixture
def get_test_data1():
    return 'tests/fixture/test_data1.json'


@pytest.fixture
def get_test_data2():
    return 'tests/fixture/test_data2.json'


@pytest.fixture
def get_template():
    temp = open('tests/fixture/after_diff.txt')

    return temp.read()


def test_diff(get_template, get_test_data1, get_test_data2):
    data1, data2 = get_test_data1, get_test_data2
    result = diff_files.generate_diff(data1, data2)
    
    assert result == get_template
