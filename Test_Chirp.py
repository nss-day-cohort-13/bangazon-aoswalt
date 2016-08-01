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


    def test_chirp_str(self):
        Chirp.next_chirp_id = 1

        chirp = Chirp(1, 'A simple chirp')

        self.assertEqual(str(chirp), 'A simple chirp')


    def test_chirp_repr(self):
        Chirp.next_chirp_id = 1

        chirp = Chirp(1, 'A simple chirp')

        test_repr = '''
msg:     A simple chirp
from:    1
to:      0
parent:  0
child:   0
private: False
'''

        self.assertEqual(repr(chirp), test_repr)


if __name__ == '__main__':
    unittest.main()
