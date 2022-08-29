def main(diff: list, type_formater="std") -> list:
    # return "\n".join((__standart_formater__(x) for x in diff))
    return __standart_formater__(diff)


def __standart_formater__(lst: list) -> str: # noqa
    # result = []

    def wrap(elements):
        print("elements === ", elements, end="\n\n")
        for elem in elements:
            # print("elem === ", elem)
            if isinstance(elem, list):
                return wrap(elem)

            depth = elem["depth"] * "  "
            key = elem["key"]
            old_value = elem["old_value"]
            new_value = elem["new_value"]

            if old_value == new_value:
                finish_value = __finalize_data__(old_value)
                result_str = f"{depth}{key}: {finish_value} \n"
                return result_str
            elif old_value is None or new_value is None:
                char = "-" if new_value is None else "+"
                finish_value = __finalize_data__(
                    old_value if char == "-" else new_value
                )
                result_str = f"{depth}{char} {key}: {finish_value} \n"
                return result_str
            elif isinstance(old_value, list) and isinstance(new_value, list):
                result_str = "{0}{1}: {\n".format(depth, key) # noqa
                return result_str
            else:
                result_str = f"{depth}- {key}: {__finalize_data__(old_value)}\n\
                {depth}+ {key}: {__finalize_data__(new_value)}\n"
                result_str_new_value = (
                    f"{depth}+ {key}: {__finalize_data__(new_value)}\n"
                )
                return result_str, result_str_new_value

    r = list(map(lambda x: wrap(x), lst))

    return r


def __finalize_data__(value: str) -> str:
    if value is None:
        return "null"
    elif isinstance(value, bool):
        value = "true" if value is True else "false"
        return value

    return str(value)


""" for tests:
# test = [[{'key': 'common', 'depth': 0, 'old_value': None, 'new_value': None}, {'key': 'follow', 'depth': 1, 'old_value': None, 'new_value': False}, {'key': 'setting1', 'depth': 1, 'old_value': 'Value 1', 'new_value': 'Value 1'}, {'key': 'setting2', 'depth': 1, 'old_value': 200, 'new_value': None}, {'key': 'setting3', 'depth': 1, 'old_value': True, 'new_value': None}, {'key': 'setting4', 'depth': 1, 'old_value': None, 'new_value': 'blah blah'}, [{'key': 'setting5', 'depth': 1, 'old_value': None, 'new_value': None}, {'key': 'key5', 'depth': 2, 'old_value': None, 'new_value': 'value5'}], [{'key': 'setting6', 'depth': 1, 'old_value': None, 'new_value': None}, [{'key': 'doge', 'depth': 2, 'old_value': None, 'new_value': None}, {'key': 'wow', 'depth': 3, 'old_value': '', 'new_value': 'so much'}], {'key': 'key', 'depth': 2, 'old_value': 'value', 'new_value': 'value'}, {'key': 'ops', 'depth': 2, 'old_value': None, 'new_value': 'vops'}]], [{'key': 'group1', 'depth': 0, 'old_value': None, 'new_value': None}, {'key': 'baz', 'depth': 1, 'old_value': 'bas', 'new_value': 'bars'}, {'key': 'foo', 'depth': 1, 'old_value': 'bar', 'new_value': 'bar'}, [{'key': 'nest', 'depth': 1, 'old_value': None, 'new_value': None}, {'key': 'key', 'depth': 2, 'old_value': 'value', 'new_value': None}]], [{'key': 'group3', 'depth': 0, 'old_value': None, 'new_value': None}, [{'key': 'deep', 'depth': 1, 'old_value': None, 'new_value': None}, [{'key': 'id', 'depth': 2, 'old_value': None, 'new_value': None}, {'key': 'number', 'depth': 3, 'old_value': None, 'new_value': 45}]], {'key': 'fee', 'depth': 1, 'old_value': None, 'new_value': 100500}], [{'key': 'group2', 'depth': 0, 'old_value': None, 'new_value': None}, {'key': 'abc', 'depth': 1, 'old_value': 12345, 'new_value': None}, [{'key': 'deep', 'depth': 1, 'old_value': None, 'new_value': None}, {'key': 'id', 'depth': 2, 'old_value': 45, 'new_value': None}]]] # noqa

print(main(test))

"""
