import unittest

from birdyboard import *

class TestBirdyboard(unittest.TestCase):

    def test_user_id_increment(self):
        birdy = Birdy()

        self.assertEqual(birdy.next_user_id, 1)

        birdy.create_user('Test Person', 'tp')
        birdy.create_user('John Doe', 'jd')

        self.assertEqual(birdy.next_user_id, 3)


    def test_create_user(self):
        birdy = Birdy()
        birdy.create_user('Test Case', 'test')
        birdy.create_user('Some Guy', 'guy')
        user = birdy.create_user('Bob Jones', 'bobj')

        self.assertEqual(user.id, 3)
        self.assertEqual(user.full_name, 'Bob Jones')
        self.assertEqual(user.screen_name, 'bobj')


    def test_select_user(self):
        birdy = Birdy()
        birdy.create_user('Test Case', 'test')
        birdy.create_user('Some Guy', 'guy')
        birdy.create_user('Bob Jones', 'bobj')
        user = birdy.select_user(2)

        self.assertEqual(user.id, 2)
        self.assertEqual(user.full_name, 'Some Guy')
        self.assertEqual(user.screen_name, 'guy')


    def test_chirp_id_increment(self):
        birdy = Birdy()

        self.assertEqual(birdy.next_chirp_id, 1)

        birdy.create_chirp(1, 'An initial message')
        birdy.create_chirp(2, 'A solid response', parent=1)
        birdy.create_chirp(1, 'A different thread')

        self.assertEqual(birdy.next_chirp_id, 4)


    def test_get_public_chirps(self):
        birdy = Birdy()
        chirp1 = birdy.create_chirp(1, 'An initial message')
        chirp2 = birdy.create_chirp(2, 'A solid response', parent=1)
        chirp3 = birdy.create_chirp(1, 'A quick rebuttal', parent=2)
        chirp4 = birdy.create_chirp(1, 'A different thread')
        chirp5 = birdy.create_chirp(1, 'A followup message', parent=4)

        public_threads = birdy.get_public_chirps(1)
        test_thread_list = [chirp1, chirp4]

        self.assertEqual(public_threads, test_thread_list)


    def test_get_users_private_chirps(self):
        birdy = Birdy()
        chirp1 = birdy.create_chirp(1, 'A directed secret', to=2, private=True)
        chirp2 = birdy.create_chirp(2, 'A secret response', parent=1, private=True)
        chirp3 = birdy.create_chirp(2, 'Someone else\'s private thread', to=3, private=True)
        chirp4 = birdy.create_chirp(1, 'Private thread to 3', to=3, private=True)

        private_threads = birdy.get_private_chirps(1)
        test_thread_list = [chirp1, chirp4]

        self.assertEqual(private_threads, test_thread_list)


    def test_get_chirps_from_thread(self):
        birdy = Birdy()
        chirp1 = birdy.create_chirp(1, 'An initial message')
        chirp2 = birdy.create_chirp(2, 'A solid response', parent=1)
        chirp3 = birdy.create_chirp(1, 'A quick rebuttal', parent=2)
        chirp4 = birdy.create_chirp(1, 'A different thread')
        chirp5 = birdy.create_chirp(1, 'A followup message', parent=4)
        chirp6 = birdy.create_chirp(2, 'A later response', parent=3)

        chirps = birdy.get_chirps_with_replies(initial)
        test_chirp_list - [chirp1, chirp2, chirp3, chirp6]

        self.assertEqual(chirps, test_chirp_list)


    def test_make_new_public_chirp(self):
        birdy = Birdy()
        chirp = birdy.create_chirp(1, 'An initial message')

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.author, 1)
        self.assertEqual(chirp.message, 'An initial message')
        self.assertEqual(chirp.parent, 0)
        self.assertEqual(chirp.to, 0)
        self.assertEqual(chirp.private, False)


    def test_make_reply_public_chirp(self):
        birdy = Birdy()
        birdy.create_chirp(1, 'An initial message')
        chirp = birdy.create_chirp(2, 'A solid response', parent=1)

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.author, 2)
        self.assertEqual(chirp.message, 'A solid response')
        self.assertEqual(chirp.parent, 1)
        self.assertEqual(chirp.to, 1)
        self.assertEqual(chirp.private, False)


    def test_make_new_private_chirp(self):
        birdy = Birdy()
        chirp = birdy.create_chirp(1, 'A directed secret', to=2, private=True)

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.author, 1)
        self.assertEqual(chirp.message, 'A directed secret')
        self.assertEqual(chirp.parent, 0)
        self.assertEqual(chirp.to, 2)
        self.assertEqual(chirp.private, True)


    def test_make_reply_private_chirp(self):
        birdy = Birdy()
        birdy.create_chirp(1, 'A directed secret', to=2, private=True)
        chirp = birdy.create_chirp(2, 'A secret response', parent=1, private=True)

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.author, 2)
        self.assertEqual(chirp.message, 'A secret response')
        self.assertEqual(chirp.parent, 1)
        self.assertEqual(chirp.to, 1)
        self.assertEqual(chirp.private, True)


if __name__ == '__main__':
    unittest.main()
