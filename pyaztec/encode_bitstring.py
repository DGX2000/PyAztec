from decode_bitstring import code_dictionary


encoding_table = list(code_dictionary.values())
encoding_modes = {'U': 0, 'L': 1, 'M': 2, 'P': 3, 'D': 4, 'B': 5}
encoding_modes_reverse = {0: 'U', 1: 'L', 2: 'M', 3: 'P', 4: 'D', 5: 'B'}


def merge_mode_c(mode_characters):
    count_mode_strings = []

    count, last_mode, string = 0, mode_characters[0][0], []
    for mode, character in mode_characters:
        if mode != last_mode:
            count_mode_strings.append((count, last_mode, string))
            count, last_mode, string = 0, mode, []
        string.append(character)
        count += 1
    count_mode_strings.append((count, last_mode, string))

    return count_mode_strings


def find_shift(origin_mode, target_mode):
    shift_dict = {
        ('U', 'U'): [],      ('U', 'L'): ['L/L'], ('U', 'M'): ['M/L'],
        ('U', 'P'): ['P/S'], ('U', 'D'): ['D/L'], ('U', 'B'): ['B/S'],

        ('L', 'U'): ['U/S'], ('L', 'L'): [],      ('L', 'M'): ['M/L'],
        ('L', 'P'): ['P/S'], ('L', 'D'): ['D/L'], ('L', 'B'): ['B/S'],

        ('M', 'U'): ['U/L'], ('M', 'L'): ['L/L'], ('M', 'M'): [],
        ('M', 'P'): ['P/S'], ('M', 'D'): None,    ('M', 'B'): ['B/S'],

        ('P', 'U'): ['U/L'], ('P', 'L'): None, ('P', 'M'): None,
        ('P', 'P'): [],      ('P', 'D'): None, ('P', 'B'): None,

        ('D', 'U'): ['U/S'], ('D', 'L'): None, ('D', 'M'): None,
        ('D', 'P'): ['P/S'], ('D', 'D'): [],   ('D', 'B'): ['B/S'],

        ('B', 'U'): [], ('B', 'L'): [], ('B', 'M'): [],
        ('B', 'P'): [], ('B', 'D'): [], ('B', 'B'): [],
    }
    return shift_dict[(encoding_modes_reverse[origin_mode],
                       encoding_modes_reverse[target_mode])]


def find_latch(origin_mode, target_mode):
    latch_dict = {
        ('U', 'U'): [],             ('U', 'L'): ['L/L'], ('U', 'M'): ['M/L'],
        ('U', 'P'): ['M/L', 'P/L'], ('U', 'D'): ['D/L'], ('U', 'B'): ['B/S'],

        ('L', 'U'): ['D/S', 'U/L'], ('L', 'L'): [],      ('L', 'M'): ['M/L'],
        ('L', 'P'): ['M/L', 'P/L'], ('L', 'D'): ['D/L'], ('L', 'B'): ['B/S'],

        ('M', 'U'): ['U/L'], ('M', 'L'): ['L/L'],           ('M', 'M'): [],
        ('M', 'P'): ['P/L'], ('M', 'D'): ['U/L', 'D/L'],    ('M', 'B'): ['B/S'],

        ('P', 'U'): ['U/L'], ('P', 'L'): ['U/L', 'L/L'], ('P', 'M'): ['U/L', 'M/L'],
        ('P', 'P'): [],      ('P', 'D'): ['U/L', 'D/L'], ('P', 'B'): ['U/L', 'B/S'],

        ('D', 'U'): ['U/L'], ('D', 'L'): ['U/S', 'L/L'], ('D', 'M'): ['U/S', 'M/L'],
        ('D', 'P'): ['P/S'], ('D', 'D'): [],             ('D', 'B'): ['U/S', 'B/S'],

        ('B', 'U'): [], ('B', 'L'): [], ('B', 'M'): [],
        ('B', 'P'): [], ('B', 'D'): [], ('B', 'B'): [],
    }
    return latch_dict[(encoding_modes_reverse[origin_mode],
                       encoding_modes_reverse[target_mode])]


def add_mode_switches(previous_latched_mode, count_mode_strings):
    switch_list = []
    for i, (count, mode, string) in enumerate(count_mode_strings):
        if count == 1:
            switch = find_shift(previous_latched_mode, mode)
            if switch is None:
                switch = find_latch(previous_latched_mode, mode)
        else:
            switch = find_latch(previous_latched_mode, mode)
            if switch is None:
                switch = find_shift(previous_latched_mode, mode)

        switch_list.append((i, (count, previous_latched_mode, switch)))
        # remember previously latched mode
        if len(switch) > 0:
            if switch[-1][2] == 'L':
                previous_latched_mode = encoding_modes[switch[-1][0]]

    for i, switch in reversed(switch_list):
        count_mode_strings.insert(i, switch)


def encode_in_mode(count, mode, codes):
    def find_encoding_for_character(code):
        if mode != encoding_modes['B']:
            for i, characters in enumerate(encoding_table):
                if code == characters[mode]:
                    if mode <= 3:
                        return '{:05b}'.format(i)
                    else:
                        return '{:04b}'.format(i)
        else:
            return '{:08b}'.format(ord(code))
        return -1

    encoded_codes = []
    for c in codes:
        encoded_codes.append(find_encoding_for_character(c))
        if c == 'B/S':
            if count <= 31:
                encoded_codes.append('{:05b}'.format(count))
            else:
                encoded_codes.append('{:011b}'.format(count-31))

    return encoded_codes


def encode(msg: str):
    def find_mode(c: str):
        for i, characters in enumerate(encoding_table):
            if c in characters:
                return characters.index(c)
        return encoding_modes['B']
    # TODO: Handle two-character strings (e.g. in Punctuation/Mixed mode)
    mode_characters = [(find_mode(c), c) for c in msg]
    count_mode_strings = merge_mode_c(mode_characters)
    # TODO: Merge B/S strings that are close together (less than 3 chars in between)
    add_mode_switches(encoding_modes['U'], count_mode_strings)

    code_list = []
    for count, mode, string in count_mode_strings:
        code_list.extend(encode_in_mode(count, mode, string))
    return ''.join(code_list)
