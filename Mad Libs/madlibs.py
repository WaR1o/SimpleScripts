#! python3

# TODO: Reads text file
text = open('D:\\code\\mycode\\MadLibs\\text.txt')
# TODO: Finds the words ADJECTIVE, NOUN, ADVERB, VERB.
words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for word in words:
    if word in text:
        print(word)
# TODO: Ask for user input to replace that words.

# TODO: Prints the result and save it to the text file.
