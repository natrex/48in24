import math
vocab_words = ['en', 'close', 'joy', 'lighten']
#vocab_words = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']

def add_prefix(prefix, word):
    return prefix + word

def make_word_groups(vocab_words):
    new_list = [vocab_words[0]]

    for count, value in enumerate(vocab_words, start=1):
        if count == 1:
            continue
        new_list.append(add_prefix(vocab_words[0],value))

    return ' :: '.join(new_list)

print(make_word_groups(vocab_words))

word = 'sadness'
#word = 'heaviness'

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    new_word = word.split('ness')
    if new_word[0][-1] == 'i': 
        return word.split('iness')[0] + 'y'
        
    return new_word[0]


print(remove_suffix_ness(word))
def add_suffix(word, suffix):
    return  word + suffix
def adjective_to_verb(sentence, index):
    new_sentence = sentence.split(' ')
    return add_suffix(new_sentence[index].split('.')[0], 'en')
            


sent = 'It got dark as the sun set.'
#adjective_to_verb('I need to make that bright.', -1 )
print(adjective_to_verb(sent, 2))


