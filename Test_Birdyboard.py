import unittest

from birdyboard import *

class TestBirdyboard(unittest.TestCase):

    def make_fresh_birdy(self):
        """
        Initizlize a Birdy for expected defaults

        Returns:
            the fresh birdy
        """

        # define and clear test data files
        Birdy.users_file = 'testfile_user.dat'
        Birdy.chirps_file = 'testfile_chirp.dat'

        # clear files for fresh testing
        open(Birdy.users_file, 'w+').close()
        open(Birdy.chirps_file, 'w+').close()

        return Birdy()


    def test_create_user(self):
        birdy = self.make_fresh_birdy()
        birdy.create_user('Test Case', 'test')
        birdy.create_user('Some Guy', 'guy')
        user = birdy.create_user('Bob Jones', 'bobj')

        self.assertEqual(user.id, 3)
        self.assertEqual(user.full_name, 'Bob Jones')
        self.assertEqual(user.screen_name, 'bobj')
        self.assertEqual(birdy.current_user, user)


    def test_select_user(self):
        birdy = self.make_fresh_birdy()
        user1 = birdy.create_user('Test Case', 'test')
        user2 = birdy.create_user('Some Guy', 'guy')
        user3 = birdy.create_user('Bob Jones', 'bobj')
        user = birdy.select_user(user2)

        self.assertEqual(user.id, 2)
        self.assertEqual(user.full_name, 'Some Guy')
        self.assertEqual(user.screen_name, 'guy')
        self.assertEqual(birdy.current_user, user)


    def test_get_public_chirps(self):
        birdy = self.make_fresh_birdy()
        chirp1 = birdy.create_chirp(1, 'An initial message')
        chirp2 = birdy.create_chirp(2, 'A solid response', parent=1)
        chirp3 = birdy.create_chirp(1, 'A quick rebuttal', parent=2)
        chirp4 = birdy.create_chirp(1, 'A different thread')
        chirp5 = birdy.create_chirp(1, 'A followup message', parent=4)

        public_threads = birdy.get_public_chirps()
        test_thread_list = [chirp1, chirp4]

        self.assertEqual(public_threads, test_thread_list)


    def test_get_users_private_chirps(self):
        birdy = self.make_fresh_birdy()
        chirp1 = birdy.create_chirp(1, 'A directed secret', to=2, private=True)
        chirp2 = birdy.create_chirp(2, 'A secret response', parent=1, private=True)
        chirp3 = birdy.create_chirp(2, 'Someone else\'s private thread', to=3, private=True)
        chirp4 = birdy.create_chirp(1, 'Private thread to 3', to=3, private=True)

        private_threads = birdy.get_private_chirps(1)
        test_thread_list = [chirp1, chirp4]

        self.assertEqual(private_threads, test_thread_list)


    def test_get_chirps_from_thread(self):
        birdy = self.make_fresh_birdy()
        chirp1 = birdy.create_chirp(1, 'An initial message')
        chirp2 = birdy.create_chirp(2, 'A solid response', parent=1)
        chirp3 = birdy.create_chirp(1, 'A quick rebuttal', parent=2)
        chirp4 = birdy.create_chirp(1, 'A different thread')
        chirp5 = birdy.create_chirp(1, 'A followup message', parent=4)
        chirp6 = birdy.create_chirp(2, 'A later response', parent=3)

        chirps = birdy.get_chirps_with_replies(chirp3)
        test_chirp_list = [chirp1, chirp2, chirp3, chirp6]

        self.assertEqual(chirps, test_chirp_list)


    def test_make_new_public_chirp(self):
        birdy = self.make_fresh_birdy()
        chirp = birdy.create_chirp(1, 'An initial message')

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.author, 1)
        self.assertEqual(chirp.message, 'An initial message')
        self.assertEqual(chirp.parent, 0)
        self.assertEqual(chirp.to, 0)
        self.assertEqual(chirp.private, False)


    def test_make_reply_public_chirp(self):
        birdy = self.make_fresh_birdy()
        parent = birdy.create_chirp(1, 'An initial message')
        reply = birdy.create_chirp(2, 'A solid response', parent=1)

        self.assertNotEqual(reply.id, 0)
        self.assertEqual(reply.author, 2)
        self.assertEqual(reply.message, 'A solid response')
        self.assertEqual(reply.parent, 1)
        self.assertEqual(reply.child, 0)
        self.assertEqual(reply.to, 1)
        self.assertEqual(reply.private, False)

        self.assertEqual(parent.child, 2)


    def test_make_new_private_chirp(self):
        birdy = self.make_fresh_birdy()
        chirp = birdy.create_chirp(1, 'A directed secret', to=2, private=True)

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.author, 1)
        self.assertEqual(chirp.message, 'A directed secret')
        self.assertEqual(chirp.parent, 0)
        self.assertEqual(chirp.to, 2)
        self.assertEqual(chirp.private, True)


    def test_make_reply_private_chirp(self):
        birdy = self.make_fresh_birdy()
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
