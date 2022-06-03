import json


def generate_diff(file_1, file_2):
    result = ['{\n']
    result_value = ''
    in_file1 = json.load(open(file_1))
    in_file2 = json.load(open(file_2))
    result_keys = sorted(list(set(in_file1.keys()).union(set(in_file2.keys()))))
    for key in result_keys:
        val1 = in_file1.get(key)
        val2 = in_file2.get(key)
        is_val1 = False if val1 is None else True
        is_val2 = False if val2 is None else True
        if val1 == val2 and is_val1 and is_val2:
            result_value = f'   {key}: {val1}\n'
            result.append(result_value)
        elif val1 != val2 and is_val1 and is_val2:
            result_value = f' - {key}: {val1}\n'
            result.append(result_value)
            result_value = f' + {key}: {val2}\n'
            result.append(result_value)
        elif is_val2 and not is_val1:
            result_value = f' + {key}: {val2}\n'
            result.append(result_value)
        elif not is_val2 and is_val1:
            result_value = f' - {key}: {val1}\n'
            result.append(result_value)
    result.append('}')
    result = ''.join(result)
    return result.lower()
