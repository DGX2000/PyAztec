from encode_bitstring import encode
import util
import cv2.cv2 as cv2
import numpy as np


def guess_total_bits(encoded_message: str) -> int:
    # heuristic for total bits in data, padding, and error correction
    return int(1.23 * len(encoded_message)) + 30


def determine_symbol_size(total_bits: int):
    import math

    def layers_compact(bits):
        return math.ceil((-88.0 + math.sqrt(88 ** 2 + 4 * 16 * bits)) / 32.0)

    def layers_full(bits):
        return math.ceil((-112.0 + math.sqrt(112 ** 2 + 4 * 16 * bits)) / 32.0)

    layers = layers_compact(total_bits)
    if layers > 4:
        layers = layers_full(total_bits)
        return 'full', layers
    else:
        return 'compact', layers


def count_bit_stuffings(bit_string: str, codeword_length: int):
    count = 0
    for c in range(0, len(bit_string), codeword_length):
        all_one = (bit_string[c:c + codeword_length - 1].count('1') == codeword_length - 1)
        all_zero = (bit_string[c:c + codeword_length - 1].count('0') == codeword_length - 1)
        if all_zero or all_one:
            count += 1

    return count


def lay_out_bits(symbol_size: str, layers: int, message_bits: int, stuffing_bits: int):
    codeword_length = util.codeword_length_in_bits(layers)
    available_bits = util.bits_in_compact_symbol(layers)
    if symbol_size == 'full':
        available_bits = util.bits_in_full_symbol(layers)

    data_bits = message_bits + stuffing_bits
    available_bits -= data_bits

    data_padding_bits = codeword_length - (data_bits % codeword_length)
    available_bits -= data_padding_bits
    ecc_padding_bits = available_bits % codeword_length
    available_bits -= ecc_padding_bits

    return data_bits, data_padding_bits + ecc_padding_bits, available_bits


def add_stuffing_bits(bit_list: list, codeword_length: int):
    additions = []
    for c in range(0, len(bit_list), codeword_length):
        all_one = (bit_list[c:c + codeword_length - 1].count('1') == codeword_length - 1)
        all_zero = (bit_list[c:c + codeword_length - 1].count('0') == codeword_length - 1)
        if all_zero or all_one:
            additions.append((c + codeword_length - 1, '0' if all_one else '1'))

    additions.sort(key=lambda x: x[0], reverse=True)
    for index, stuffing in additions:
        bit_list.insert(index, stuffing)

    return bit_list


def compute_mode_message(layers: int, data_words: int, compact: bool):
    # TODO: Add reed-solomon encoding
    # TODO: Add mode message for full symbol
    if compact:
        mode_message = '{:02b}'.format(layers-1) + '{:05b}'.format(data_words-1) + '0'*21
    else:
        mode_message = "123456"
    return list(mode_message)


def write_bulls_eye(symbol: list, compact: bool):
    mid = len(symbol) // 2
    symbol[mid][mid] = '1'
    pass


def generate_image(filename: str, message: str):
    encoded_string = encode(message)

    # figure out correct symbol size + layers
    total_bits = guess_total_bits(encoded_string)
    while True:
        symbol_size, layers = determine_symbol_size(total_bits)
        codeword_length = util.codeword_length_in_bits(layers)

        stuffing_bits = count_bit_stuffings(encoded_string, codeword_length)
        data_bits, padding_bits, ecc_bits = lay_out_bits(symbol_size, layers, len(encoded_string), stuffing_bits)

        total_bits = data_bits + padding_bits + ecc_bits
        bits_in_symbol = util.bits_in_compact_symbol(layers) if symbol_size == 'compact' else \
            util.bits_in_full_symbol(layers)
        if total_bits > bits_in_symbol:
            continue

        if layers > 32:
            raise OverflowError
        else:
            break

    encoded_list = list(encoded_string)
    add_stuffing_bits(encoded_list, codeword_length)
    encoded_list.extend(['1'] * padding_bits)
    # TODO: If all-one codeword at end => flip last bit to '0'
    encoded_list.extend(['0'] * ecc_bits)
    # TODO: reed-solomon data correction

    mode_message = compute_mode_message(layers, (data_bits+padding_bits) // codeword_length, symbol_size == 'compact')

    side_length = util.side_length_in_bits(layers, symbol_size == 'compact')
    symbol = [['0'] * side_length for i in range(side_length)]

    write_bulls_eye(symbol, symbol_size == 'compact')
    #write_mode_message(symbol, mode_message, symbol_size == 'compact')
    #write_data(symbol, encoded_list, symbol_size == 'compact')

    # TODO: get rid of this transformation step after refactoring
    symbol = [[int(c)*255 for c in row] for row in symbol]

    image = cv2.bitwise_not(np.array(symbol, dtype=np.uint8))
    # TODO: magnify (maybe?)
    cv2.imwrite(filename, image)


generate_image("file.png", "ABCabc123")
