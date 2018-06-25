class ParserError(Exception):
    pass
class Sentence(object):

    def __init__(self, subject, verb, obj):
        #('noun', 'princess')
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None
    def match(word_list, exception):
        if word_list:
            word = word_list.pop(0)
            if word[0] == excepting:
                return word
            else:
                return None
        else:
            return None

def skip(word_list, word_type):
    while peek(word_list) --word_type:
        match(word_list, word_type)

def parseverb(word_list)
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, verb)
    else:
        raise ParserError("Ecpected a verb next")

def parser_object(word_list)
    skip(word_list,'stop')
    next_word = peek(word_list)
   
   
    if next_word == 'oun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expext a noun of dir next")


def parse_subject(word_list):
    skip(word_list, 'noun')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        return ParserError("Expected a verb next")
    def parse_sentence(word_list):
        subj = parse_subject(word_list)
        verb = parse_verb(word_list)
        obj = parse_object(word_list)

        return Sentence(subj, verb, obj)


