import unittest
from cesarCipher import CeasarCipher


class TestCesarCipher(unittest.TestCase):
    # ERRORS
    def test_raise_error_when_key_is_too_high(self):
        self.assertRaises(ValueError, CeasarCipher.encode, "test", 2000)

    def test_raise_error_when_key_is_too_low(self):
        self.assertRaises(ValueError, CeasarCipher.encode, "test", -2000)

    def test_raise_error_when_key_is_not_integer(self):
        # ENCODING
        self.assertRaises(TypeError, CeasarCipher.encode, "test", "not an integer")
        # DECODING
        self.assertRaises(TypeError, CeasarCipher.decode, "test", "not an integer")

    def test_raises_error_when_message_is_not_string(self):
        self.assertRaises(TypeError, CeasarCipher.encode, 1, 1)
        self.assertRaises(TypeError, CeasarCipher.encode, arg1=[1, 2, 3], key=1)
        self.assertRaises(TypeError, CeasarCipher.encode, True, 1)

    # ENCODING
    def test_encodes_correctly_short_lower_case_message_from_start_of_alphabet(self):
        self.assertEqual(CeasarCipher.encode("abc", 1), "bcd")

    def test_encodes_correctly_message_with_capital_letter(self):
        self.assertEqual(CeasarCipher.encode("ABC", 1), "bcd")

    def test_encodes_correctly_message_from_end_of_alphabet(self):
        self.assertEqual(CeasarCipher.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23), "xyzabcdefghijklmnopqrstuvw")

    def test_encodes_correctly_message_with_special_character(self):
        self.assertEqual(CeasarCipher.encode("AB c", 1), "bc d")
        self.assertEqual(CeasarCipher.encode("Hi, how are you?", 1), "ij, ipx bsf zpv?")

    # DECODING
    def test_decodes_message_from_start_of_alphabet(self):
        self.assertEqual(CeasarCipher.decode("bcd", 1), "abc")

    def test_decodes_message_with_capital_letter(self):
        self.assertEqual(CeasarCipher.decode("BCD", 1), "abc")

    def test_decodes_message_from_end_of_alphabet(self):
        self.assertEqual(CeasarCipher.decode("XYZABCDEFGHIJKLMNOPQRSTUVW", 23), "abcdefghijklmnopqrstuvwxyz")

    def test_decodes_message_with_special_character(self):
        self.assertEqual(CeasarCipher.decode("Ij, ipx bsf zpv?", 1), "hi, how are you?")


if __name__ == '__main__':
    unittest.main()
