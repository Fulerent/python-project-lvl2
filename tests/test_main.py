import pytest
from gendiff import diff_files
from gendiff import parser_files


@pytest.fixture
def get_test_data1():
    return 'tests/fixture/test_data1.yml'


@pytest.fixture
def get_test_data2():
    return 'tests/fixture/test_data2.yml'


@pytest.fixture
def get_template():
    temp = open('tests/fixture/after_diff.txt')

    return temp.read()


@pytest.mark.parametrize("input_path, expected_format", [
                        ("fixture/test_data1.yml", 'yml'),
                        ("tests/fixture/test_data1.json", "json")])
def test_get_format(input_path, expected_format):
    format = parser_files.get_format(input_path)

    assert format == expected_format


def test_diff(get_template, get_test_data1, get_test_data2):
    data1 = parser_files.pars(get_test_data1)
    data2 = parser_files.pars(get_test_data2)
    result = diff_files.generate_diff(data1, data2)

    assert result == get_template


def test_invalid_format():
    invalid_format = 'tests/fixture/test_data1.xml'
    result = parser_files.get_format(invalid_format)

    assert result == 'xml'


def test_invalid_path():
    with pytest.raises(Exception) as e:
        valid_path = parser_files.pars('tests/fixture/test_data1.yml')
        invalid_path = parser_files.pars('no_point_from_file_name/folder')
        diff_files.generate_diff(valid_path, invalid_path)

    assert str(e.value) == \
        "[Errno 2] No such file or directory: 'no_point_from_file_name/folder'"
