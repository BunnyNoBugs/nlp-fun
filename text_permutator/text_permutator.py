from collections import namedtuple
from random import random, shuffle


class TextPermutator():
    def __init__(self, text):
        self.original_text = []
        for a in text:
            if a.isalpha():
                self.original_text.append(self.Char(a, True, a.isupper()))
            else:
                self.original_text.append(self.Char(a, False, False))
        self.permutated_text = None
        self._is_permutated = False
        self._is_reversed = False

    def permutate(self, prob=0.5, context=3):
        if not self._is_permutated:
            self.permutated_text = self.original_text
            for n, i in enumerate(self.permutated_text):
                if i.to_change:
                    if random() < prob:
                        idx_to_change = list(range(max(0, n - context), min(len(self.permutated_text), n + context)))
                        shuffle(idx_to_change)
                        for m in idx_to_change:
                            if self.permutated_text[m].to_change:
                                (self.permutated_text[n].char, self.permutated_text[m].char) = (
                                    self.permutated_text[m].char,
                                    self.permutated_text[n].char)
                            self.permutated_text[n].to_change, self.permutated_text[m].to_change = False, False
                            break
            self._is_permutated = True

    def reverse(self):
        if not self._is_reversed:
            self.permutated_text = self.permutated_text[::-1]
            self._is_reversed = True

    def __str__(self):
        str_repr = ''
        for i in self.permutated_text:
            if i.upper_case:
                str_repr += i.char.upper()
            else:
                str_repr += i.char.lower()
        return str_repr

    class Char:
        def __init__(self, char: str, to_change: bool, upper_case: bool):
            self.char = char
            self.to_change = to_change
            self.upper_case = upper_case


def main():
    permutator = TextPermutator('sample text')
    permutator.permutate(prob=0.5, context=5)
    permutator.reverse()
    print(permutator)


if __name__ == '__main__':
    main()
