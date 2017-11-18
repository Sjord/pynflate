class Codec:
    def __init__(self):
        self.letters = {}
        self.codes = {}

    def update(self, letter, code):
        self.letters[code] = letter
        self.codes[letter] = code

    def encode(self, s):
        return ''.join(self.codes[letter] for letter in s)

    def _decode(self, s):
        code = ''
        for c in s:
            code += c

            if code in self.letters:
                yield self.letters[code]
                code = ''

        assert code == ''

    def decode(self, s):
        return ''.join(self._decode(s))


def _min_letter(frequencies):
    min_freq = min(frequencies.values())
    min_letter, = [letter for letter in frequencies
                   if frequencies[letter] == min_freq]
    return min_letter


def huffman(frequencies):
    min_letter = _min_letter(frequencies)
    del frequencies[min_letter]

    min_letter2 = _min_letter(frequencies)

    return {min_letter: '0', min_letter2: '1'}
