def remove_stuffed_bits(bit_list: list, codeword_length: int):
    for c in range(0, len(bit_list), codeword_length):
        all_one = (bit_list[c:c + codeword_length-1].count('1') == codeword_length-1)
        all_zero = (bit_list[c:c + codeword_length-1].count('0') == codeword_length-1)
        if all_zero or all_one:
            del bit_list[c + codeword_length]

    return bit_list
