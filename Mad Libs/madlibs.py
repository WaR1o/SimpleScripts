#! python3

# Reads text file
text = open('D:\\code\\mycode\\MadLibs\\text.txt')
# Finds the words ADJECTIVE, NOUN, ADVERB, VERB.
words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for word in words:
    if word in text:
        print(word)
