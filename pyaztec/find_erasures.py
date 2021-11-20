def find_erasures(bit_list: list, codeword_length: int, data_words: int):
    erasures = []
    for c in range(0, codeword_length*data_words, codeword_length):
        all_one = (bit_list[c:c+codeword_length].count('1') == codeword_length)
        all_zero = (bit_list[c:c+codeword_length].count('0') == codeword_length)
        if all_zero or all_one:
            erasures.append(c)

    return erasures
