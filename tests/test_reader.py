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

        for actor in ['Captain Ryan Thompson',
                      'Lieutenant Ava Ramirez',
                      'Sergeant Marcus Chen',
                      'Dr. Sophia Collins']:
            self.assertIn(actor, a)

        for scene in ['Spaceship Bridge', 'Europa\'s Orbit',
                      'Europa\'s Surface', 'Europa Research Outpost']:
            self.assertEqual(scene, s[counter].location)
            counter += 1

        for location in ['Spaceship Bridge']:
            self.assertIn(location, loc)

        self.assertDictEqual(a, db.actors)
        self.assertListEqual(s, db.scenes)
        self.assertDictEqual(loc, db.locations)


if __name__ == '__main__':
    unittest.main()
