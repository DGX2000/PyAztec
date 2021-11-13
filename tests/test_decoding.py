import unittest
import pyaztec


class DecodingTests(unittest.TestCase):
    """ Test cases for decoding. """

    def test_bitstring_decoding(self):
        with open('step_4_data') as f:
            test_cases = f.readlines()

        for case in test_cases:
            bitstring, result = case.split('=', maxsplit=1)
            result = result.strip('\n')
            assert pyaztec.decode_bitstring(bitstring) == result


if __name__ == '__main__':
    unittest.main()
