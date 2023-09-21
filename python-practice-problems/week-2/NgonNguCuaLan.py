from enum import Enum

Gender = Enum('Gender', ['MASCULINE', "FEMININE"])
WordType = Enum('WordType', ['ADJECTIVE', 'NOUN', 'VERB'])

masculine_postfixes = ['lios', 'etr', 'initis']
feminine_postfixes = ['liala', 'etra', 'inites']
postfixes = masculine_postfixes + feminine_postfixes

adjective_postfixes = []
noun_postfixes = []
verb_postfixes = []

adjective_postfixes.append(masculine_postfixes[0])
adjective_postfixes.append(feminine_postfixes[0])
noun_postfixes.append(masculine_postfixes[1])
noun_postfixes.append(feminine_postfixes[1])
verb_postfixes.append(masculine_postfixes[2])
verb_postfixes.append(feminine_postfixes[2])

def is_word_valid(word):
    for postfix in postfixes:
        if word.endswith(postfix):
            return True
    return False

def get_word_gender(word):
    for postfix in masculine_postfixes:
        if word.endswith(postfix):
            return Gender.MASCULINE
    for postfix in feminine_postfixes:
        if word.endswith(postfix):
            return Gender.FEMININE

def get_word_type(word):
    for adjective_postfix in adjective_postfixes:
        if word.endswith(adjective_postfix):
            return WordType.ADJECTIVE
    for noun_postfix in noun_postfixes:
        if word.endswith(noun_postfix):
            return WordType.NOUN
    for verb_postfix in verb_postfixes:
        if word.endswith(verb_postfix):
            return WordType.VERB
        
def verify(sentence):
    # If sentence has only 1 VALID word => YES, else
    # If there is no or more than 1 NOUN => NO
    # Determine Gender for whole sentence using the first word, if Gender of a word != Gender of sentence => NO
    # Sentence must maintain the order: ADJECTIVE + NOUN + VERB, and only has 1 NOUN
    #   if ADJECTIVE then next word must be ADJECTIVE or NOUN
    #   if NOUN then next word must be VERB
    #   if VERB then next word must be VERB
    words = sentence.split()
    word_count = len(words)

    if word_count == 1:
        return 'YES' if is_word_valid(word=words[0]) else 'NO'
    if word_count == 0:
        return 'NO'

    # Check properties
    gender = get_word_gender(words[0])        
    noun_count = 0
    for word in words:
        if not is_word_valid(word=word):
            return 'NO'
        if get_word_gender(word=word) != gender:
            return 'NO'
        for noun_postfix in noun_postfixes:
            if word.endswith(noun_postfix):
                noun_count += 1
                break
    if noun_count != 1:
        return 'NO'
    
    # Check ADJECTIVE, NOUN and VERB ordering
    for i in range(word_count - 1):
        current_word_type = get_word_type(word=words[i])
        next_word_type = get_word_type(word=words[i + 1])

        if current_word_type == WordType.ADJECTIVE:
            if next_word_type == WordType.VERB:
                return 'NO'
        elif current_word_type == WordType.NOUN:
            if next_word_type != WordType.VERB:
                return 'NO'
        elif current_word_type == WordType.VERB:
            if next_word_type != WordType.VERB:
                return 'NO'

    return 'YES'

sentence = input()
print(verify(sentence=sentence))