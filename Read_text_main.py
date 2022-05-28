from collections import Counter
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, 'r') as text:
    
        return text.read()


def count_words():
    text = read_file_content("./story.txt")
    slipt_text = text.split()
    count = Counter(slipt_text)

    return count

print(count_words())
