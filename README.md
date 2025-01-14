# CSC 1019 Practice 02

## Anagram checker
An anagram is a word game where you form one word from another. Two words are anagrams if they are different AND contain exactly the same number of letters.

For example:
```
pot,top -> anagrams
pits,spit -> anagrams
ate,tea -> anagrams
Rome,more -> anagrams (assume case does not matter)
racecar,racecar -> not anagrams
feel,leaf -> not anagrams
super tree,tree purse -> anagrams
super tree,Per Use tree -> anagrams
```

## Task
1. Write a program that determines whether two words are anagrams of each other. Case does not matter. The number of spaces also does not matter.
2. Make sure that your program contains the following function `is_anagram(word1: str, word2: str) -> bool`.  Make sure the function has an appropriate docstring.

## Input
The input will be one line with two words separated by commas.

Example:
```
file,life
```

```
tree,tier
```

## Output
You should output the line you received as input and whether they are anagrams with an -> arrow.

Examples:
```
file,life -> anagrams
```

```
tree,tier -> not anagrams
```

## Hint!
Anagrams will have the same number of letters. An easy way would be to *go through* each letter in one word, and remove one instance of it from the other word. If the other word is the empty string "" at the end, it's an anagram.

## Extension
Complete the unit test in the tests folder. Why do this?
- I write great letters of recommendations when you go above and beyond class requirements. Even if you're a senior, I can still give job references...
- This is an industry practice, so why not show that you have real life skills?
- It's good critical thinking practice (what edge test cases can you think of?)