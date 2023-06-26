import unittest
from ai_presenter.tools.json_trim import json_trim


class TestJsonTrim(unittest.TestCase):
    def test_json_trim(self):
        # Test case with improper JSON format
        input_string = '{ "name": "John", "age": 30, "city": "New York" '
        expected_output = ''
        self.assertEqual(json_trim(input_string), expected_output)

        # Test case with proper JSON format
        input_string = '{"name": "John", "age": 30, "city": "New York"}'
        expected_output = '{"name": "John", "age": 30, "city": "New York"}'
        self.assertEqual(json_trim(input_string), expected_output)

        # Test case with proper JSON format but other lines outside braces
        input_string = 'Some text\n{"name": "John", "age": 30}\ntext'
        expected_output = '{"name": "John", "age": 30}'
        self.assertEqual(json_trim(input_string), expected_output)

        input_string = """
        {
            "characters":[
                {
                    "name":"John Doe",
                    "personality":"Charismatic detective",
                    "emotion":"Focused"
                },
                {
                    "name":"Jane Smith",
                    "personality":"Brilliant
                    scientist",
                    "emotion":"Eager"
                },
                {
                    "name":"Michael
                    Johnson",
                    "personality":"Wise mentor",
                    "emotion":"Serious"
                }
            ],
            "dialogue":[
                {
                    "speaker":"John
                    Doe",
                    "emotion":"Focused",
                    "message":"I need to
                    examine the evidence
                    carefully."
                },
                {
                    "speaker":"Jane
                    Smith",
                    "emotion":"Eager",
                    "message":"Let's analyze
                    the DNA samples."
                },
                {
                    "speaker":"Michael
                    Johnson",
                    "emotion":"Serious",
                    "message":"This is a
                    delicate matter that
                    requires your keen
                    expertise. John, be
                    careful with how you
                    proceed with analyzing
                    the evidence."
                },
                {
                    "speaker":"John
                    Doe",
                    "emotion":"Focused",
                    "message":"I understand
                    the gravity of this
                    situation, Michael.
                    There's no room for
                    error here."
                },
                {
                    "speaker":"Jane
                    Smith",
                    "emotion":"Eager",
                    "message":"I'll get the
                    necessary equipment
                    ready. We need to
                    start analyzing the
                    samples as soon as
                    possible."
                },
                {
                    "speaker":"John
                    Doe",
                    "emotion":"Focused",
                    "message":"Let's stay
                    vigilant and keep our
                    eyes peeled for
                    anything suspicious.
                    We'll need to use
                    every tool at our
                    disposal to solve this
                    case."
                }
            ]
        }

        As the investigation unfolds, John Doe
        becomes more focused and determined to
        uncover the truth. Jane Smith is eager
        to analyze the DNA samples, knowing that
        every detail counts. Michael Johnson, the
        wise mentor, warns John to be careful,
        knowing that one mistake could cost them
        everything. Despite the risks, John
        remains focused on the task at hand,
        realizing that the truth must be
        uncovered at all costs.
        """

        expected_output = """
          {
            "characters":[
                {
                    "name":"John Doe",
                    "personality":"Charismatic detective",
                    "emotion":"Focused"
                },
                {
                    "name":"Jane Smith",
                    "personality":"Brilliant
                    scientist",
                    "emotion":"Eager"
                },
                {
                    "name":"Michael
                    Johnson",
                    "personality":"Wise mentor",
                    "emotion":"Serious"
                }
            ],
            "dialogue":[
                {
                    "speaker":"John
                    Doe",
                    "emotion":"Focused",
                    "message":"I need to
                    examine the evidence
                    carefully."
                },
                {
                    "speaker":"Jane
                    Smith",
                    "emotion":"Eager",
                    "message":"Let's analyze
                    the DNA samples."
                },
                {
                    "speaker":"Michael
                    Johnson",
                    "emotion":"Serious",
                    "message":"This is a
                    delicate matter that
                    requires your keen
                    expertise. John, be
                    careful with how you
                    proceed with analyzing
                    the evidence."
                },
                {
                    "speaker":"John
                    Doe",
                    "emotion":"Focused",
                    "message":"I understand
                    the gravity of this
                    situation, Michael.
                    There's no room for
                    error here."
                },
                {
                    "speaker":"Jane
                    Smith",
                    "emotion":"Eager",
                    "message":"I'll get the
                    necessary equipment
                    ready. We need to
                    start analyzing the
                    samples as soon as
                    possible."
                },
                {
                    "speaker":"John
                    Doe",
                    "emotion":"Focused",
                    "message":"Let's stay
                    vigilant and keep our
                    eyes peeled for
                    anything suspicious.
                    We'll need to use
                    every tool at our
                    disposal to solve this
                    case."
                }
            ]
        }
        """
        self.assertEqual(json_trim(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
