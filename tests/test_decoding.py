import unittest
import sys
import os

import cv2

sys.path.append(os.path.abspath(os.path.join('..', 'pyaztec')))
import pyaztec.decode_bitstring
import pyaztec.sample_image_to_array
import pyaztec.util


def prepare_cropped_image(filename: str):
    img = cv2.imread('cropped_images/' + filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


class DecodingTests(unittest.TestCase):
    """ Test cases for decoding. """

    def test_decoding_cropped_image(self):
        pyaztec.sample_image_to_array.sample_image_to_array(prepare_cropped_image('ABCabc123.png'), 1, True)

    def test_bitstring_decoding(self):
        with open('step_4_data') as f:
            test_cases = f.readlines()

        for case in test_cases:
            bitstring, result = case.split('=', maxsplit=1)
            result = result.strip('\n')
            assert pyaztec.decode_bitstring.decode_bitstring(bitstring) == result

    def test_utility_functions(self):
        assert pyaztec.util.bits_in_compact_symbol(1) == 104
        assert pyaztec.util.bits_in_compact_symbol(4) == 608

        assert pyaztec.util.bits_in_full_symbol(5) == 960
        assert pyaztec.util.bits_in_full_symbol(32) == 19968

        assert pyaztec.util.codeword_length_in_bits(2) == 6
        assert pyaztec.util.codeword_length_in_bits(3) == 8
        assert pyaztec.util.codeword_length_in_bits(8) == 8
        assert pyaztec.util.codeword_length_in_bits(9) == 10
        assert pyaztec.util.codeword_length_in_bits(22) == 10
        assert pyaztec.util.codeword_length_in_bits(23) == 12
        assert pyaztec.util.codeword_length_in_bits(32) == 12

        # TODO: Get more data for gridlines for testing

        assert pyaztec.util.side_length_in_bits(0, True) == 11
        assert pyaztec.util.side_length_in_bits(1, True) == 15
        assert pyaztec.util.side_length_in_bits(2, True) == 19
        assert pyaztec.util.side_length_in_bits(4, True) == 27
        # TODO: Get more data for full-size symbols for testing
        assert pyaztec.util.side_length_in_bits(15, False) == 79


if __name__ == '__main__':
    unittest.main()
