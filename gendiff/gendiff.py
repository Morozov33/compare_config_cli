import json


def generate_diff(file_1, file_2):
    result = ['{\n']
    in_file1 = json.load(open(file_1))
    in_file2 = json.load(open(file_2))
    keys = sorted(list(set(in_file1.keys()).union(set(in_file2.keys()))))
    for key in keys:
        val1 = in_file1.get(key)
        val2 = in_file2.get(key)
        if val1 is not None and val2 is not None:
            if val1 == val2:
                result.append(f'   {key}: {val1}\n')
            else:
                result.append(f' - {key}: {val1}\n')
                result.append(f' + {key}: {val2}\n')
        elif val1 is None and val2 is not None:
            result.append(f' + {key}: {val2}\n')
        else:
            result.append(f' - {key}: {val1}\n')
    result.append('}')
    result = ''.join(result)
    return result.lower()
