import unittest
from sample.sample import Adder

class TestAdd(unittest.TestCase):
    def testAdd(self):
        x = Adder()
        self.assertEqual(x.add(1,2), 3, "Should be 3")
        self.assertNotEqual(x.add(4,2), 0)

if __name__ == '__main__':
    unittest.main()