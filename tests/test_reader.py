import unittest
from ai_presenter.reader import Reader


class TestReader(unittest.TestCase):
    def testReader(self):
        x = Reader('tests/text.yml')
        a = x.get_actors()
        s = x.get_scenes()
        db = x.get_db()

        for actor in ['John Doe', 'Jane Smith', 'Michael Johnson']:
            self.assertIn(actor, a)

        for scene in ['Cabin', 'Interrogation Room',
                      'Laboratory', 'Courtroom']:
            self.assertIn(scene, s)

        self.assertDictEqual(a, db.actors)
        self.assertDictEqual(s, db.scenes)


if __name__ == '__main__':
    unittest.main()
