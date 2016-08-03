import unittest

from user import *

class TestUser(unittest.TestCase):


    def test_user_id_increment(self):
        User.next_user_id = 1

        self.assertEqual(User.next_user_id, 1)

        User('Test Person', 'tp')
        User('John Doe', 'jd')

        self.assertEqual(User.next_user_id, 3)

    def test_user_str(self):
        User.next_user_id = 1

        user = User('That Guy', 'guy')

        self.assertEqual(str(user), '1. guy - That Guy')


    def test_user_repr(self):
        User.next_user_id = 1

        user = User('That Guy', 'guy')

        self.assertEqual(repr(user), '1. guy - That Guy')


if __name__ == '__main__':
    unittest.main()
