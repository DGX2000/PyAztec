import numpy as np
import decode_bitstring
import find_erasures
import remove_stuffed_bits
import sample_image_to_array
import symbol_to_bit_list
import util


def decode_cropped_image(img: np.ndarray, layers: int, compact: bool, data_words: int):
    symbol = sample_image_to_array.sample_image_to_array(img, layers, compact)
    codeword_length = util.codeword_length_in_bits(layers)
    bit_list = symbol_to_bit_list.symbol_to_bit_list(symbol, layers, codeword_length, compact)

    erasures = find_erasures.find_erasures(bit_list, codeword_length, data_words)
    # TODO: Reed-Solomon error correction

    # Reed-Solomon error correction check words are stripped after they were used previously
    bit_list = bit_list[0:codeword_length*data_words]

    bit_list = remove_stuffed_bits.remove_stuffed_bits(bit_list, codeword_length)

    bit_string = ''.join(bit_list)
    return decode_bitstring.decode_bitstring(bit_string)
