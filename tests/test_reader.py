import unittest
from sample.reader import Reader

class TestAdd(unittest.TestCase):
    def testReader(self):
        x = Reader('tests/text.yml')
        a = x.get_actors()
        s = x.get_scenes()
        l = x.get_locations()
        for actor in ['John Doe', 'Jane Smith', 'Michael Johnson']:
            self.assertIn(actor, a)
        
        for scene in ['Crime Scene', 'Interrogation Room', 'Laboratory']:
            self.assertIn(scene, s)
            
        for location in ['Mountains', 'Cabin']:
            self.assertIn(location, l)
            
            
if __name__ == '__main__':
    unittest.main()