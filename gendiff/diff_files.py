from collections import OrderedDict
from copy import deepcopy
import stylish
import parser_files


def get_all_keys(dict1: dict, dict2: dict) -> list:
    try:
        keys = list(OrderedDict.fromkeys(list(dict1.keys()) + list(dict2.keys())))
        return keys
    except AttributeError:
        if not isinstance(dict1, dict) and dict is not None:
            return list(dict2.keys())
        else:
            return list(dict1.keys())


def generate_diff(file1: str, file2: str) -> list:
    # Create a list where we will be differents
    diff_list = []
    # make deep-copy dictonarys
    d1, d2 = deepcopy(file1), deepcopy(file2)
    # Get keys first and second file. It have not a reapeat.
    # Are join them(save an original odrder)
    keys = get_all_keys(d1, d2)

    def iter_(keys, dict1, dict2, depth=0) -> str:
        if keys == []:
            return diff_list

        key = keys[0] if isinstance(keys, list) else keys
        value1, value2 = dict1.get(key), dict2.get(key)

        if value1 is None and value2 is None:
            return diff_list

        if not isinstance(value1, dict) and not isinstance(value2, dict):
            diff_list.append(((depth, key), (value1, value2)))
            return iter_(keys[1:], dict1, dict2, depth)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff_list.append(((depth, key)))
            next_keys = get_all_keys(value1, value2)
            return iter_(next_keys, value1, value2, depth + 1)
        # TODO: Will do a normal if/else    
        else:
            if not isinstance(value1, dict):
                in_dict = dict2.get(key)
                return (key, {}, in_dict, depth + 1)

            elif not isinstance(value2, dict):
                in_dict = dict1.get(key)
                return (key, in_dict, {}, depth + 1)


    r = list((map(lambda x: iter_(x, d1, d2), keys)))
    # r = iter_(keys, d1, d2)

    print("r === ", r)
    return stylish.format(r)


test_fil1 = parser_files.pars('tests/fixture/test_data1.json')
test_fil2 = parser_files.pars('tests/fixture/test_data2.json')

print(generate_diff(test_fil1, test_fil2))
