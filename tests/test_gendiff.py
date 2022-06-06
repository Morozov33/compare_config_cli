from gendiff.gendiff import generate_diff


result = """{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}"""

file_1 = './tests/fixtures/file1.json'
file_2 = './tests/fixtures/file2.json'


def test_gendiff():
    assert generate_diff(file_1, file_2) == result

