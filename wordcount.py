# put your code here.
def countwords(filename):
    openedfile=open(filename)

    wordcount={}
    for line in openedfile:
        finalline=line.rstrip().lower().split(" ")
        for word in finalline:
            if "," in word:
                word=word.replace(",", "")
            
            wordcount[word] = wordcount.get(word, 0) + 1
        print(wordcount)
    for poem_word, count in wordcount.items():
        print(f" {poem_word}: {count}")
countwords('test.txt')