
def word_count(file_path):
    wordcount = {}
    for line in file_path:
        stripped_line = line.strip()
        words = stripped_line.split(" ")
        for word in words:
            # if wordcount.get(word,0) != 0:
            #     wordcount[word] += 1
            # else:
            #     wordcount[word] = 1
            wordcount[word] = wordcount.get(word, 0) + 1

    for word, number in wordcount.iteritems():
        print word, number


word_count(open("twain.txt"))