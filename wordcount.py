
def counts_words(file):
    open(file)      #opens file
    word_count = {} #dictionary with words and their count
    for letter in file:
        word_count[letter] = word_count.get(letter, 0) + 1   
    return word_count
