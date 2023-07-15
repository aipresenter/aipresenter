import unittest
from ai_presenter.reader import Reader


class TestScenes(unittest.TestCase):
    def testScenes(self):
        x = Reader('tests/duplicate_scenes.yml')
        s = x.get_scenes()
        db = x.get_db()
        counter = 0
        num_scenes = 4

        for scene in ['Cabin', 'Interrogation Room',
                      'Interrogation Room', 'Cabin']:
            self.assertEqual(scene, s[counter].name)
            counter += 1

        self.assertListEqual(s, db.scenes)
        self.assertEqual(counter, num_scenes)


if __name__ == '__main__':
    unittest.main()
