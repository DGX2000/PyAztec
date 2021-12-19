import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..', 'pyaztec')))
import pyaztec.encode_bitstring
import pyaztec.generate_image


class EncodingTests(unittest.TestCase):
    """ Test cases for encoding. """

    def test_bitstring_encoding(self):
        with open('decode_bitstring_data') as f:
            test_cases = f.readlines()

        for case in test_cases:
            case = case.strip('\n')
            result, bitstring = case.split('=', maxsplit=1)
            assert pyaztec.encode_bitstring.encode(bitstring) == result

    def test_code_generation(self):
        pyaztec.generate_image("generated_images/test.png", "ABCabc123")


if __name__ == '__main__':
    unittest.main()
