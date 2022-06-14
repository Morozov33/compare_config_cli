from gendiff.format.get_format import get_format


def stylish(source, depth=2):
    result = ['{\n']
    for key in sorted(list(source.keys())):
        result_str = ' ' * depth
        children = source.get(key).get('children')
        if children is not None:
            if source[key]['change'] == 'not_change':
                result_str = result_str + '  ' + key + ': '
            elif source[key]['change'] == 'add':
                result_str = result_str + '+ ' + key + ': '
            elif source[key]['change'] == 'delete':
                result_str = result_str + '- ' + key + ': '
            result.append(result_str)
            result.append(stylish(children, depth=depth + 4))
        else:
            value1 = get_format(source[key]['in_file1'], 'stylish',
                                depth=depth + 6)
            value2 = get_format(source[key]['in_file2'], 'stylish',
                                depth=depth + 6)
            if source[key]['change'] == 'not_change':
                result_str = (depth * ' ' + '  ' + key + ': ' +
                              value1 + '\n')
            elif source[key]['change'] == 'add':
                result_str = (depth * ' ' + '+ ' + key + ': ' +
                              value2 + '\n')
            elif source[key]['change'] == 'delete':
                result_str = (depth * ' ' + '- ' + key + ': ' +
                              value1 + '\n')
            elif source[key]['change'] == 'change':
                result_str = (depth * ' ' + '- ' + key + ': ' + value1 + '\n' +
                              depth * ' ' + '+ ' + key + ': ' + value2 + '\n')
            result.append(result_str)
    result.append((depth - 2) * ' ' + '}\n')
    return ''.join(result)
