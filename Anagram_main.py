# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if sorted(word.lower()) == sorted(anagram.lower()):
        return True

    else:
        return False
ana = find_anagram('hello','check')
print(ana)
anagram = find_anagram("below", "elbow")
print(anagram)
