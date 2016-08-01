import unittest

from user import *

class TestUser(unittest.TestCase):


    def test_user_id_increment(self):
        self.assertEqual(User.next_user_id, 1)

        User('Test Person', 'tp')
        User('John Doe', 'jd')

        self.assertEqual(User.next_user_id, 3)


if __name__ == '__main__':
    unittest.main()
