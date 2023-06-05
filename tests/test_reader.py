import unittest
from sample.reader import Reader

class TestAdd(unittest.TestCase):
    def testReader(self):
        x = Reader('sample/text.yml')
        x.read_file()
        a = x.get_actors()
        expected_dict = {'name': 'John Doe', 'description': 'A charismatic detective', 'voice_type': 'Baritone', 'age': 35, 'height': '6 feet'}
        self.assertDictEqual(a[0], expected_dict)
            
            
if __name__ == '__main__':
    unittest.main()