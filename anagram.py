"""
This program checks whether two words are anagrams of each other.
Input format:
word1,word2

Output:
word1,word2 -> anagrams
OR
word1,word2 -> not anagrams


J. Cihlar - January 2025
"""

def is_anagram(word1:str, word2:str) -> bool:
    """
    Determines whether two words are anagrams of each other.
    Parameters:
        word1(str): the first word
        word2(str): the second word
    
    Return:
        bool: Whether the words are anagrams of each other
    """
        # remove spaces
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    
        # make lower case
    word1 = word1.lower()
    word2 = word2.lower()
    
        # words cannot be equal or of different length
    if word1 == word2 or len(word1) != len(word2):
        return False
    
        # loop through each letter and replace it in the 
        # second word with "" once
    for c in word1:
        word2 = word2.replace(c, "", 1)

        # if the second word is an empty string then it's an anagram
    print(word2)
    return word2 == ""

def main() -> None:
        # get input and split
    line: str = input()
    word1,word2 = line.split(",")
    if is_anagram(word1, word2):
        print(f"{line} -> anagrams")
    else:
        print(f"{line} -> not anagrams")

if __name__ == "__main__":
    main()
