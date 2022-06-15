from gendiff.format.get_format import get_format


def plain(source):
    def plain_to_way(source, way):
        result = []
        for key in list(source.keys()):
            way_key = way + key
            result_str = ''
            children = source.get(key).get('children')
            if children is None:
                change = source.get(key).get('change')
                value1 = get_format(source.get(key).get('in_file1'), 'plain')
                value2 = get_format(source.get(key).get('in_file2'), 'plain')
                if change == 'add':
                    result_str = f"Property '{way_key}' was added "\
                                 f"with value: {value2}\n"
                elif change == 'change':
                    result_str = f"Property '{way_key}' was updated. "\
                                 f"From {value1} to {value2}\n"
                elif change == 'delete':
                    result_str = f"Property '{way_key}' was removed\n"
            else:
                result_str = plain_to_way(children, way_key + '.')
            result.append(result_str)
        return ''.join(result)
    return ''.join(plain_to_way(source, ''))[:-1:]
