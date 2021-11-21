def remove_stuffed_bits(bit_list: list, codeword_length: int):
    mark_for_deletion = []
    for c in range(0, len(bit_list), codeword_length):
        all_one = (bit_list[c:c + codeword_length-1].count('1') == codeword_length-1)
        all_zero = (bit_list[c:c + codeword_length-1].count('0') == codeword_length-1)
        if all_zero or all_one:
            mark_for_deletion.append(c + codeword_length-1)

    mark_for_deletion.sort(reverse=True)
    for deletion in mark_for_deletion:
        del bit_list[deletion]

    return bit_list
