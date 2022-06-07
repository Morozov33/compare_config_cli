from gendiff.gendiff import generate_diff


result = """{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}"""

file_1_json = './tests/fixtures/file1.json'
file_2_json = './tests/fixtures/file2.json'
file_1_yaml = './tests/fixtures/file1.yaml'
file_2_yaml = './tests/fixtures/file2.yaml'
file_1_yml = './tests/fixtures/file1.yml'
file_2_yml = './tests/fixtures/file2.yml'


def test_gendiff():
    assert generate_diff(file_1_json, file_2_json) == result
    assert generate_diff(file_1_yaml, file_2_yaml) == result
    assert generate_diff(file_1_yml, file_2_yml) == result
