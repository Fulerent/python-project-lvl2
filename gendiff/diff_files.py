from collections import OrderedDict
from copy import deepcopy
import stylish
import parser_files


def get_all_keys(dict1: dict, dict2: dict) -> list:
    try:
        keys = OrderedDict.fromkeys(list(dict2.keys()) + list(dict1.keys()))
        return list(keys)
    except AttributeError:
        if not isinstance(dict1, dict):
            return list(dict2.keys())
        else:
            return list(dict1.keys())


def is_dict(value):
    return isinstance(value, dict)


def generate_diff(file1: str, file2: str) -> list:
    # Create a list where we will be differents
    diff_list = []
    # make deep-copy dictonarys
    d1, d2 = deepcopy(file1), deepcopy(file2)
    # Get keys first and second file.
    # Are join them(save an original odrder)
    first_level_keys = get_all_keys(d1, d2)

    def iter_(keys, dict1, dict2, depth=0) -> str:
        if keys == []:
            return diff_list

        key = keys[0] if isinstance(keys, list) else keys
        print("key === ", key)
        value1, value2 = dict1.get(key), dict2.get(key)

        if value1 is None and value2 is None:
            return diff_list

        if not is_dict(value1) and not is_dict(value2):
            diff_list.append(((depth, key), (value1, value2)))
        elif is_dict(value1) and is_dict(value2):
            diff_list.append(((depth, key)))
            next_keys = get_all_keys(value1, value2)
            print("next_keys === ", next_keys)

            return iter_(next_keys, value1, value2, depth + 1)
        elif not is_dict(value1) and is_dict(value2):
            new_dict = dict2.get(key)
            new_keys = list(new_dict.keys())

            return iter_(new_keys, {}, new_dict, depth + 1)
        elif is_dict(value1) and not is_dict(value2):
            new_dict = dict1.get(key)
            new_keys = list(new_dict.keys())
            # print("new_keys === ", new_keys)
            return iter_(new_keys, new_dict, {}, depth + 1)

        return iter_(keys[1:], dict1, dict2, depth)


    r = list(map(lambda x: iter_(x, d1, d2), first_level_keys))
    # r = iter_(keys, d1, d2)

    # diff_list = iter_(keys, d1, d2)
    return stylish.format(r)


test_fil1 = parser_files.pars('tests/fixture/test_data1.json')
test_fil2 = parser_files.pars('tests/fixture/test_data2.json')

print(generate_diff(test_fil1, test_fil2))
