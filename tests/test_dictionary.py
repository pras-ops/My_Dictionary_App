import unittest
import sys
import os

# Add the 'src' directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from dictionary import dictionary

class TestDictionary(unittest.TestCase):
    def test_existing_word(self):
        # Test for an existing word in the dictionary
        word = "apple"
        result = dictionary(word)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_title_case_word(self):
        # Test for a word in title case
        word = "Hello"
        result = dictionary(word)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_upper_case_word(self):
        # Test for a word in uppercase
        word = "PYTHON"
        result = dictionary(word)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_close_match_word(self):
        # Test for a close match word suggestion
        word = "aplle"
        result = dictionary(word)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_non_existing_word(self):
        # Test for a word that does not exist in the dictionary
        word = "x"
        result = dictionary(word)
        self.assertEqual(result, "word not found")

    def test_invalid_input(self):
        # Test for invalid input (e.g., empty string)
        word = ""
        result = dictionary(word)
        self.assertEqual(result, "Word not found in dictionary")

if __name__ == "__main__":
    unittest.main()
