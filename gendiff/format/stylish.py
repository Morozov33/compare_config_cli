from gendiff.format.get_format import get_format


def stylish(source):
    def stylish_result(source, depth=2):
        result = ['{\n']
        for key in list(source.keys()):
            result_str = ' ' * depth
            children = source.get(key).get('children')
            change = source.get(key).get('change')
            if children is not None:
                if change == 'not_change':
                    result_str = f"{result_str}  {key}: "
                elif change == 'add':
                    result_str = f"{result_str}+ {key}: "
                elif change == 'delete':
                    result_str = f"{result_str}- {key}: "
                result.append(result_str)
                result.append(stylish_result(children, depth=depth + 4))
            else:
                value1 = get_format(source.get(key).get('in_file1'), 'stylish',
                                    depth=depth + 6)
                value2 = get_format(source.get(key).get('in_file2'), 'stylish',
                                    depth=depth + 6)
                if change == 'not_change':
                    result_str = f"{result_str}  {key}: {value1}\n"
                elif change == 'add':
                    result_str = f"{result_str}+ {key}: {value2}\n"
                elif change == 'delete':
                    result_str = f"{result_str}- {key}: {value1}\n"
                elif change == 'change':
                    result_str = f"{result_str}- {key}: {value1}\n"\
                                 f"{result_str}+ {key}: {value2}\n"
                result.append(result_str)
        result.append((depth - 2) * ' ' + '}\n')
        return ''.join(result)
    return stylish_result(source)[:-1:]
