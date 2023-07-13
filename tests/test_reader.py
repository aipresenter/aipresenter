import unittest
from ai_presenter.reader import Reader


class TestReader(unittest.TestCase):
    def testReader(self):
        x = Reader('tests/text.yml')
        a = x.get_actors()
        s = x.get_scenes()
        loc = x.get_locations()
        db = x.get_db()
        counter = 0

        for actor in ['John Doe', 'Jane Smith', 'Michael Johnson']:
            self.assertIn(actor, a)

        for scene in ['Cabin', 'Interrogation Room',
                      'Laboratory', 'Courtroom']:
            self.assertEqual(scene, s[counter][0])
            counter += 1

        for location in ['Mountains', 'Cabin']:
            self.assertIn(location, loc)

        self.assertDictEqual(a, db.actors)
        self.assertListEqual(s, db.scenes)
        self.assertDictEqual(loc, db.locations)


if __name__ == '__main__':
    unittest.main()
