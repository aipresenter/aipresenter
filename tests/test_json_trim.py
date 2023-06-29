import unittest
from ai_presenter.tools.json_trim import json_trim


class TestJsonTrim(unittest.TestCase):
    def test_json_trim(self):
        # Test case with improper JSON format
        input_string = '{ "name": "John", "age": 30, "city": "New York" '
        expected_output = '{' + '}'
        self.assertEqual(json_trim(input_string), expected_output)

        # Test case with proper JSON format
        input_string = '{"name": "John", "age": 30, "city": "New York"}'
        expected_output = '{"name": "John", "age": 30, "city": "New York"}'
        self.assertEqual(json_trim(input_string), expected_output)

        # Test case with proper JSON format but other lines outside braces
        input_string = 'Some text\n{"name": "John", "age": 30}\ntext'
        expected_output = '{"name": "John", "age": 30}'
        self.assertEqual(json_trim(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
