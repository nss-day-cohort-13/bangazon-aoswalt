import pickle
import unittest

from quickio import *

class TestQuickio(unittest.TestCase):

    def test_serialize(self):
        filename = 'testfile_ser.dat'

        data = [1, 'a', ['a', 'list']]
        serialize(filename, data)

        with open(filename, 'rb') as read_file:
            test_read = pickle.load(read_file)
            self.assertEqual(test_read, data)

    def test_deserialize(self):
        filename = 'testfile_ser.dat'

        data = [2, 'b', ['a', 'different', 'list']]
        with open(filename, 'wb+') as write_file:
            pickle.dump(data, write_file)

        read_data = deserialize(filename)
        self.assertEqual(read_data, data)


if __name__ == '__main__':
    unittest.main()
