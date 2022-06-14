def get_format(value, form, depth=0):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif type(value) is dict:
        if form == 'stylish':
            result = ['{\n']
            for key in sorted(list(value.keys())):
                format_value = get_format(value.get(key), 'stylish',
                                          depth=depth + 4,)
                result.append(depth * ' ' + key + ': '
                              + format_value + '\n')
            result.append(((depth - 4) * ' ' + '}'))
            return ''.join(result)
        elif form == 'plain':
            return '[complex value]'
    else:
        return str(value) if form == 'stylish' else f"'{value}'"
