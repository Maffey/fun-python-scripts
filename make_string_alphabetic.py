#! python
# Removes letter from word to make characters go alphabetically.
# It doesn't work all the time, but is efficient.

import unittest


class TestRemoveLettersAlphabet(unittest.TestCase):
    def test_object1(self):
        self.assertEqual(letters_to_remove('mateusz'), 3)

    def test_object2(self):
        self.assertEqual(letters_to_remove('cba'), 2)

    def test_object3(self):
        self.assertEqual(letters_to_remove('dirt'), 0)

    def test_object4(self):
        self.assertEqual(letters_to_remove('jablko'), 2)

    def test_repeating_letters1(self):
        self.assertEqual(letters_to_remove('gabriela'), 5)

    def test_repeating_letters2(self):
        self.assertEqual(letters_to_remove('banana'), 3)

    def test_repeating_letters3(self):
        self.assertEqual(letters_to_remove('apple'), 2)


def letters_to_remove(string: str) -> int:
    string = list(string)
    sorted_string = sorted(string)
    letters_removed = 0
    remaining_string = ""
    for character in sorted_string:
        index = string.index(character)
        to_remove = string[:index]
        letters_removed += len(to_remove)
        for letter in to_remove:
            string.remove(letter)
            sorted_string.remove(letter)
        remaining_string += character
        string.remove(character)

    print(f"[+] Remaining string: {remaining_string}")
    return letters_removed


if __name__ == "__main__":
    unittest.main()

