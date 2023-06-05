import unittest
from sample.reader import Reader

class TestAdd(unittest.TestCase):
    def testReader(self):
        x = Reader('tests/text.yml')
        a = x.get_actors()
        for actor in ['John Doe', 'Jane Smith', 'Michael Johnson']:
            self.assertIn(actor, a)
        
            
            
if __name__ == '__main__':
    unittest.main()