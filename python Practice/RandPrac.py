dictionary = {}

key = 'Tokyo'.lower()
value = ['東京','hiragana']

dictionary[key] = value

word = input('Enter word to be translated\n').lower()

while True:
    if word == 'exit' or word == 'quit':
        break
    elif word in dictionary:
        print('  {} -> {}'.format(word,dictionary[word]))
    else:
        print('Sorry, I don\'t know that word')
    word = input('Enter word to be translated\n').lower()
