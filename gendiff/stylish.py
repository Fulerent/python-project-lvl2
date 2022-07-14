import itertools


def format(diff: list, indient='  ') -> str:
    resp = list()

    n = 1

    for elem in diff:
        print('elem === ', elem)
        if not isinstance(elem[0], tuple):
            depth = int(elem[0]) + 1
            element_indent = indient * depth
            name_parent = elem[1]
            resp.append('{0}{1} : '.format(element_indent, name_parent) + '{')
        else:
            depth = int(elem[0][0]) + 1
            name_element = elem[0][1]
            value_file1 = finalize_data(elem[1][0])
            value_file2 = finalize_data(elem[1][1])
           # print("name_element === ", name_element)
           # print("value_file1 === ", value_file1)
           # print("value_file2 === ", value_file2)
            final_str = get_elemt_with_sign(value_file1,
                                            value_file2, name_element)
            # print("final_str === ", final_str)

            if isinstance(final_str, str):
                resp.append('{0}{1}'.format(element_indent, final_str))
            else:
                elem1, elem2 = final_str[0], final_str[1]
                print('elem1 === ', elem1)
                print('elem2 === ', elem2)
                resp.append('{0}{1}'.format(element_indent, elem1))
                resp.append('{0}{1}'.format(element_indent, elem2))

    # print(resp)
    return "\n".join(resp)


def finalize_data(value: str) -> str or dict:
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        value = 'true' if value is True else 'false'
        return value

    return value


def get_elemt_with_sign(l1: str, l2: str, name: str) -> str:
    if l1 == l2:
        print_str = '{0} : {1}'.format(name, l1)

        return print_str
    elif l1 == 'null' or l2 == 'null':
        sign = '+' if l1 == 'null' else '-'
        print_str = '{0} {1} : {2}'.format(sign, name, l2)

        return print_str
    else:
        print_str1 = '- {0} : {1}'.format(name, l1)
        print_str2 = '+ {0} : {1}'.format(name, l2)

        return [print_str1, print_str2]


test = [(0, 'common'), ((1, 'follow'), ('null', 'false')), ((1, 'setting1'), ('Value 1', 'Value 1')), ((1, 'setting3'), ('true', 'null')), ((1, 'setting4'), ('null', 'blah blah')), ((2, 'key5'), ('null', 'value5')), ((1, 'setting5'), ('null', [...])), (1, 'setting6'), ((2, 'key'), ('value', 'value')), ((2, 'ops'), ('null', 'vops')), (2, 'doge'), ((3, 'wow'), ('', 'so much'))]

print(format(test))