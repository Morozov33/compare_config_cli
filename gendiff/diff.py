def diff(file1, file2):
    result = {}
    keys_1 = set(file1.keys())
    keys_2 = set(file2.keys())
    keys = list(keys_1.union(keys_2))
    for key in keys:
        value1 = file1.get(key, 'empty')
        value2 = file2.get(key, 'empty')
        result[key] = {}
        if type(value1) is dict and type(value2) is dict:
            if value1 != 'empty' and value2 != 'empty':
                result[key]['change'] = 'not_change'
            elif value1 == 'empty':
                result[key]['change'] = 'add'
            elif value2 == 'empty':
                result[key]['change'] = 'delete'
            result[key]['children'] = diff(value1, value2)
        else:
            if value1 == value2:
                result[key]['change'] = 'not_change'
            elif value1 == 'empty':
                result[key]['change'] = 'add'
            elif value2 == 'empty':
                result[key]['change'] = 'delete'
            else:
                result[key]['change'] = 'change'
            result[key]['in_file1'] = value1
            result[key]['in_file2'] = value2
    return result
