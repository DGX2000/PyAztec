import numpy as np
import sample_image_to_array
import util


def decode_cropped_image(img: np.ndarray, layers: int, compact: bool):
    symbol = sample_image_to_array.sample_image_to_array(img, layers, compact)
    codeword_length = util.codeword_length_in_bits(layers)
    # bitstring = symbol_to_bitstring(symbol, layers, codeword_length)
