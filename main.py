from string import ascii_lowercase as alc

def wordcount(book):
    return len(book.split())

def lettercount(book):
    book = book.lower()
    frequency = {}
    for letter in alc:
        frequency[letter] = book.count(letter)
    return frequency

exit = False
while(not exit):
    filepath = input("Enter file path for book to be analyzed or enter 0 to exit: ")

    if filepath == "0":
        exit = True

    else:
        with open(filepath) as file:
            book = file.read()
            print("--- Begin report of " + filepath + " ---")
            print(str(wordcount(book)) + " words found in the document")
            print()
            sortedlettercount = dict(sorted(lettercount(book).items(), key = lambda x:x[1], reverse = True))
            for letter in sortedlettercount.keys():
                print("The \'" + letter + "\' character was found " + str(sortedlettercount[letter]) + " times")
            print("--- End report ---")

