import json


def generate_diff(file_1, file_2):
    result = ['{\n']
    in_file1 = json.load(open(file_1))
    in_file2 = json.load(open(file_2))
    set_keys_1 = set(in_file1.keys())
    set_keys_2 = set(in_file2.keys())
    keys = sorted(list(set_keys_1.union(set_keys_2)))
    for key in keys:
        val1 = in_file1.get(key)
        val2 = in_file2.get(key)
        if val1 == val2:
            add_str(result, key, val1, '   ')
        elif val1 is None:
            add_str(result, key, val2, ' + ')
        elif val2 is None:
            add_str(result, key, val1, ' - ')
        else:
            add_str(result, key, val1, ' - ')
            add_str(result, key, val2, ' + ')
    result.append('}')
    result = ''.join(result)
    return result.lower()


def add_str(sourse, key, value, sumbol):
    return sourse.append(f'{sumbol}{key}: {value}\n')
