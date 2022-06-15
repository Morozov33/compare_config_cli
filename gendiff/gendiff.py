from gendiff.diff import diff
from gendiff.parser_file import parser_file
from gendiff.format.stylish import stylish
from gendiff.format.plain import plain
from gendiff.format.json import json_format


def generate_diff(file_1, file_2, format_name='stylish'):
    source_1 = parser_file(file_1)
    source_2 = parser_file(file_2)
    result = diff(source_1, source_2)
    if format_name == 'stylish':
        return stylish(result)
    elif format_name == 'plain':
        return plain(result)
    elif format_name == 'json':
        return json_format(result)
