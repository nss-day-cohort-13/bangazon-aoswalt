import unittest

from chirp import *

class TestChirp(unittest.TestCase):


    def test_chirp_id_increment(self):
        Chirp.next_chirp_id = 1
        
        self.assertEqual(Chirp.next_chirp_id, 1)

        Chirp(1, 'An initial message')
        Chirp(2, 'A solid response', parent=1)
        Chirp(1, 'A different thread')

        self.assertEqual(Chirp.next_chirp_id, 4)


if __name__ == '__main__':
    unittest.main()
