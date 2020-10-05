# import test.txt

def counts_words(file):
    open_file = open(file)      #opens file
    word_count = {} #dictionary with words and their count
    for line in open_file:
        list_words = line.split(' ')
        for word in list_words:
            word_count[word] = word_count.get(word, 0) + 1   
    return word_count

word_count = counts_words('test.txt')
print(word_count)