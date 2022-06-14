import yaml
import json


def parser_file(file):
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith('.yaml') or file.endswith('.yml'):
        return yaml.safe_load(open(file))
