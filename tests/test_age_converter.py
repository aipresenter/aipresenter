import unittest
from ai_presenter.tools.age_converter import age_converter


class TestAgeConverter(unittest.TestCase):
    def test_age_converter(self):
        # exception raised for invalid age(age < 0)
        with self.assertRaises(Exception):
            age_converter(-4)

        # exception raised for non int age
        with self.assertRaises(Exception):
            age_converter('middle_aged')

        # returns 'young' between 0 and 34
        expected = 'young'
        recieved = age_converter(0)
        self.assertEqual(expected, recieved)

        recieved = age_converter(34)
        self.assertEqual(expected, recieved)

        # returns 'middle-aged' between 35 and 49
        expected = 'middle_aged'
        recieved = age_converter(35)
        self.assertEqual(expected, recieved)

        recieved = age_converter(49)
        self.assertEqual(expected, recieved)

        # returns 'old' for ages 50 and older
        expected = 'old'
        recieved = age_converter(50)
        self.assertEqual(expected, recieved)

        recieved = age_converter(80)
        self.assertEqual(expected, recieved)


if __name__ == '__main__':
    unittest.main()
