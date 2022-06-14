from gendiff.gendiff import generate_diff


result = './tests/fixtures/result'
result_plain = './tests/fixtures/result_plain'
file1json = './tests/fixtures/file1.json'
file2json = './tests/fixtures/file2.json'
file1yaml = './tests/fixtures/file1.yaml'
file2yaml = './tests/fixtures/file2.yaml'
file_1_yml = './tests/fixtures/file1.yml'
file_2_yml = './tests/fixtures/file2.yml'


def test_gendiff():
    with open(result, 'r') as res:
        result_str = res.read()
        assert generate_diff(file1json, file2json) == result_str
        assert generate_diff(file1yaml, file2yaml) == result_str
        assert generate_diff(file_1_yml, file_2_yml) == result_str

    with open(result_plain, 'r') as res:
        result_str = res.read()
        assert generate_diff(file1json, file2json,
                             format_name='plain') == result_str
        assert generate_diff(file1yaml, file2yaml,
                             format_name='plain') == result_str
        assert generate_diff(file_1_yml, file_2_yml,
                             format_name='plain') == result_str
