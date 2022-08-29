import pytest
from gendiff import diff_files
from gendiff import parser_files


def get_template(path):
    temp = open(path)

    return temp.read()


@pytest.mark.parametrize("input_path, expected_format", [
                        ("../test.yml", 'yml'),
                        ("tests/fixture/test.json", "json")])
def test_get_format(input_path, expected_format):
    format = parser_files.get_format(input_path)

    assert format == expected_format


def test_diff_json():
    file_path1 = 'tests/fixture/test_data1.json'
    file_path2 = 'tests/fixture/test_data2.json'
    file_path_template = 'tests/fixture/after_diff_json.txt'
    data1 = parser_files.pars(file_path1)
    data2 = parser_files.pars(file_path2)
    result = diff_files.generate_diff(data1, data2)

    assert result == get_template(file_path_template)


def test_diff_yml():
    file_path1 = 'tests/fixture/test_data3.yml'
    file_path2 = 'tests/fixture/test_data4.yml'
    file_path_template = 'tests/fixture/after_diff_yml.txt'
    data1 = parser_files.pars(file_path1)
    data2 = parser_files.pars(file_path2)
    result = diff_files.generate_diff(data1, data2)

    assert result == get_template(file_path_template)


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

#TODO: Сделать тесты для форматера и вынести их в отдельный файл
#TODO: Проверить, что вызывается необходимая функция standart_formater с помощью mock unittest
