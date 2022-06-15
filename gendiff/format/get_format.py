def get_format(value, form, depth=0):
    result_str = ''
    if value is True:
        result_str = 'true'
    elif value is False:
        result_str = 'false'
    elif value is None:
        result_str = 'null'
    elif type(value) is dict:
        if form == 'stylish':
            result = ['{\n']
            for key in list(value.keys()):
                format_value = get_format(value.get(key), 'stylish',
                                          depth=depth + 4,)
                result.append(f"{depth * ' '}{key}: {format_value}\n")
            result.append(((depth - 4) * ' ' + '}'))
            result_str = ''.join(result)
        elif form == 'plain':
            result_str = '[complex value]'
    else:
        result_str = str(value) if form == 'stylish' else f"'{value}'"
    return result_str
