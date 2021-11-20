import numpy as np
import util


def symbol_to_bit_list(symbol: np.ndarray, layers: int, codeword_length: int, compact: bool):
    if compact:
        total_bits = util.bits_in_compact_symbol(layers)
    else:
        total_bits = util.bits_in_full_symbol(layers)

    symbol_size = symbol.shape[0]

    # TODO: Clean this bit-skipping business up
    skip_bits = True if abs(total_bits / codeword_length - round(total_bits / codeword_length)) > 0.1 else False

    bit_list = []
    for i in range(layers):
        offset_l = i * 2

        start_x = offset_l
        start_y = offset_l

        if skip_bits:
            start_x = 1
            skip_bits = False

        # Left side
        for x in range(start_x, symbol_size - i*2 - 2):
            bit_list.append(symbol[x][start_y])
            bit_list.append(symbol[x][start_y + 1])

        # Bottom side
        for y in range(start_y, symbol_size - i*2 - 2):
            bit_list.append(symbol[symbol_size - i*2 - 1][y])
            bit_list.append(symbol[symbol_size - i*2 - 2][y])

        # Right side
        for x in range(symbol_size - i*2 - 1, i * 2 + 1, -1):
            bit_list.append(symbol[x][symbol_size - i*2 - 1])
            bit_list.append(symbol[x][symbol_size - i*2 - 2])

        # Top side
        for y in range(symbol_size - i*2 - 1, i*2 + 1, -1):
            bit_list.append(symbol[i*2][y])
            bit_list.append(symbol[i*2 + 1][y])

    return bit_list
