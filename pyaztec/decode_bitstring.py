code_dictionary = {
    0: ['P/S', 'P/S', 'P/S', 'F/S', 'P/S'],
    1: [' ', ' ', ' ', '\n', ' '],
    2: ['A', 'a', '^A', '\n', '0'],
    3: ['B', 'b', '^B', '. ', '1'],
    4: ['C', 'c', '^C', ', ', '2'],
    5: ['D', 'd', '^D', ': ', '3'],
    6: ['E', 'e', '^E', '!', '4'],
    7: ['F', 'f', '^F', '"', '5'],
    8: ['G', 'g', '^G', '#', '6'],
    9: ['H', 'h', '^H', '$', '7'],
    10: ['I', 'i', '^I', '%', '8'],
    11: ['J', 'j', '^J', '&', '9'],
    12: ['K', 'k', '^K', '\'', ','],
    13: ['L', 'l', '^L', '(', '.'],
    14: ['M', 'm', '^M', ')', 'U/L'],
    15: ['N', 'n', '^[', '*', 'U/S'],
    16: ['O', 'o', '^\\', '+', ''],
    17: ['P', 'p', '^]', ',', ''],
    18: ['Q', 'q', '^^', '-', ''],
    19: ['R', 'r', '^_', '.', ''],
    20: ['S', 's', '@', '/', ''],
    21: ['T', 't', '\\', ':', ''],
    22: ['U', 'u', '^', ';', ''],
    23: ['V', 'v', '_', '<', ''],
    24: ['W', 'w', '`', '=', ''],
    25: ['X', 'x', '|', '>', ''],
    26: ['Y', 'y', '~', '?', ''],
    27: ['Z', 'z', '^?', '[', ''],
    28: ['L/L', 'U/S', 'L/L', ']', ''],
    29: ['M/L', 'M/L', 'U/L', '{', ''],
    30: ['D/L', 'D/L', 'P/L', '}', ''],
    31: ['B/S', 'B/S', 'B/S', 'U/L', '']
}

mode_length_dictionary = {
    'U': 5,
    'L': 5,
    'M': 5,
    'P': 5,
    'D': 4,
    'B': 5,
    'BE': 11,
    'BR': 8,
    'F': 3,
    'FD': 4
}

decode_function_dictionary = {
    'U': lambda bits: code_dictionary[int(bits, 2)][0],
    'L': lambda bits: code_dictionary[int(bits, 2)][1],
    'M': lambda bits: code_dictionary[int(bits, 2)][2],
    'P': lambda bits: code_dictionary[int(bits, 2)][3],
    'D': lambda bits: code_dictionary[int(bits, 2)][4],
    'B': lambda bits: int(bits, 2),
    'BE': lambda bits: int(bits, 2),
    'BR': lambda bits: chr(int(bits, 2)),
    'F': lambda bits: int(bits, 2),
    'FD': lambda bits: code_dictionary[int(bits, 2)][4]
}

non_printing_codes = ['P/S', 'F/S', 'U/L', 'U/S', 'L/L', 'L/S', 'M/L', 'M/S', 'D/L', 'D/S', 'P/L', 'P/S', 'B/S']


def decode_bitstring(bitstring: str):
    output = []

    mode_countdown = 0
    latched_mode = 'U'
    current_mode = 'U'

    i = 0
    while True:
        if mode_countdown == 0:
            current_mode = latched_mode
        else:
            mode_countdown -= 1

        # gets the next string of bits to decode
        bits_to_retrieve = mode_length_dictionary[current_mode]
        bits = bitstring[i:i+bits_to_retrieve]
        i += bits_to_retrieve

        if i > len(bitstring):
            break

        decoded_bits = decode_function_dictionary[current_mode](bits)

        if isinstance(decoded_bits, int):
            if current_mode == 'B':
                if decoded_bits == 0:
                    mode_countdown = 1
                    current_mode = 'BE'
                else:
                    mode_countdown = decoded_bits
                    current_mode = 'BR'

            if current_mode == 'BE':
                mode_countdown = decoded_bits + 31
                current_mode = 'BR'

            if current_mode == 'F1':
                mode_countdown = decoded_bits
                current_mode = 'F2'
        elif decoded_bits in non_printing_codes:
            decoded_mode = decoded_bits[0]
            if decoded_bits[-1] == 'L':
                latched_mode = decoded_mode
                mode_countdown = 0
            else:
                current_mode = decoded_mode
                mode_countdown = 1
        else:
            output += decoded_bits

    return ''.join(output)
