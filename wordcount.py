# import test.txt

def counts_words(file):
    open_file = open(file)      #opens file
    word_count = {} #dictionary with words and their count
    for line in open_file:
        for word in line:
            word_count[word] = word_count.get(word, 0) + 1   
    print(word_count)
    return word_count

counts_words('test.txt')