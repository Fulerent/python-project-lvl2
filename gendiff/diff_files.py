from collections import OrderedDict


def generate_diff(file1, file2):
    # Create a list where we will be differents
    diff_list = ['{']
    # Получаем ключе обоих файлов без повторов и объеденяем в исходном порядке
    keys = list(OrderedDict.fromkeys(list(file1.keys()) + list(file2.keys())))
    # задача 5* - переписать все на map and reduce

    for key in keys:
        value1, value2 = file1.get(key), file2.get(key)
        if value1 is not None and value2 is not None:
            if value1 == value2:
                diff_list.append('{0} : {1}'.format(key, value1))
            elif value1 != value2:
                diff_list.append('- {0} : {1}'.format(key, value1))
                diff_list.append('+ {0} : {1}'.format(key, value2))
        elif value2 is None:
            diff_list.append('- {0} : {1}'.format(key, value1))
        else:
            diff_list.append('+ {0} : {1}'.format(key, value2))

    return '\n\t'.join(diff_list) + '\n}\n'
