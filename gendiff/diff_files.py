from collections import OrderedDict
from copy import deepcopy

# import stylish
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


def is_not_dict(value):
    return not isinstance(value, dict)


n = 0


def generate_diff(file1: dict, file2: dict) -> list:
    diff_list = list()
    # make deep-copy dictonarys
    dict1, dict2 = deepcopy(file1), deepcopy(file2)
    # Get keys first and second file.
    first_level_keys = get_all_keys(dict1, dict2)

    def iter_(d1=dict1, d2=dict2, keys=first_level_keys, depth: int = 0) -> list:
        print("key === ", keys)
        key = keys[0] if isinstance(keys, list) else keys

        # if keys == []:
        # return result

        value1 = d1.get(key) if isinstance(d1, dict) else None
        value2 = d2.get(key) if isinstance(d2, dict) else None

        if is_not_dict(value1) and is_not_dict(value2):
            return {
                "key": key,
                "depth": depth,
                "old_value": value1,
                "new_value": value2,
            }

        next_keys = sorted(get_all_keys(value1, value2))
        result = []
        result.append(
            {"key": key, "depth": depth, "old_value": None, "new_value": None}
        )

        for key in next_keys:
            result.append(iter_(value1, value2, key, depth + 1))

        return result

    diff_list = list(map(lambda x: iter_(keys=x), first_level_keys))

    return diff_list


""" 
for tests:

test_fil1 = parser_files.pars('tests/fixture/test_data1.json')
test_fil2 = parser_files.pars('tests/fixture/test_data2.json')

r = generate_diff(test_fil1, test_fil2)

"""
