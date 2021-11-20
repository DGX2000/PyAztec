def bits_in_compact_symbol(layers):
    return (88 + 16*layers) * layers


def bits_in_full_symbol(layers):
    return (112 + 16*layers) * layers


def codeword_length_in_bits(layers):
    if layers <= 2:
        return 6
    elif layers <= 8:
        return 8
    elif layers <= 22:
        return 10
    else:
        return 12


def reference_grid(side_length):
    mid_point = int(side_length / 2)
    return [mid_point + i*16 for i in range(-5, 5) if 0 <= mid_point + i*16 < side_length]


def side_length_in_bits(layers, compact: bool):
    if compact:
        side_length = 11
    else:
        side_length = 15
    # layers have a width of 2 bits and are on both sides of the central pattern
    side_length += 2 * layers*2

    # gridlines have a width of 1 bit and are also on both sides of the central pattern
    # with a gap of 16 bits between them
    if not compact:
        side_length += 2 * (3+layers)*2 / 16

    return int(side_length)

