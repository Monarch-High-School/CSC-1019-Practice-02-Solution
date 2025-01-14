"""
Unit tests for the anagram checker

Name - Date
"""

# NOTE: Your anagram.py file must have a function called is_anagram(word1: str, word2: str) -> bool

import anagram
import unittest

def test_short_anagram() -> None:
    word1: str = "care"
    word2: str = "race"
    actual: bool = anagram.is_anagram(word1, word2)
    expected: bool = True

    assert actual == expected, f"Checked {word1} and {word2} for angrams. Expected: {expected}. Got {actual}"

   # simply add this code and add one line per test where indicated
def load_tests(loader, tests, pattern) -> unittest.TestSuite:
    suite = unittest.TestSuite()
        # using the pattern below add one line per test
    suite.addTest(unittest.FunctionTestCase(test_short_anagram))
    return suite

if __name__ == "__main__":
    unittest.main()