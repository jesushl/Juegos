#!/bin/python3

class Googlon:

    #Prepositions len = 6,  not contains 'u', ends with a foo letter
    #Verbs  len >= 6, ends in a bar letter, if stars with a bar letter is in
    #   is in subjuntive form
    #Alphabeth = {s,x,o,c,q,n,m,w,p,f,y,h,e,l,j,r,d,g,u,i}

    #Numbers  Base 20,  [3200000,160000,8000,400,20,1] pretty number if  > 81827
    #Is divisible by 3

    #Find Prepositions, verbs, how many verbs are subjuntive form, a vocabulary
    # in a googlon alphabetical order
    #How many pretty number are on the text

    def __init__(self):
        self.foo_letters = {'u', 'd', 'x', 's', 'm', 'p', 'f'}
        #bar_letters are the rest on the alphabeth
        self.alphabet    = {'s':0,'x':1,'o':2,'c':3,'q':4,'n':5,'m':6,'w':7,'p':8,'f':9,'y':10}
        self.alphabet.update({'h':11,'e':12,'l':13,'j':14,'r':15,'d':16,'g':17,'u':18,'i':19})

        # word classification codes
        self.other_classification           = 0
        self.presposition_code              = 1
        self.verb_code                      = 2
        self.verb_subjuntive_code           = 3
        #Minimum word len to be classified
        self.classification_len_condition   = 6
        self.pretty_number_len_condition    = 4
        self.pretty_number_min_value        = 81827
        #preposition char requirement
        self.preposition_char_requirement   = 'u'

        self.statistics_collection          = {'prepositions': 0,'verbs': 0}
        self.statistics_collection.update({'subjuntive_verbs' : 0})
        self.statistics_collection.update({'prety_numbers': 0})

    #StartPoint
    def getGooglonAnalysis(self, string_message):
        string_message = string_message.lower()
        words_in_message = string_message.split(' ')
        self.build_words_integration(words_in_message)
        return self.statistics_collection

    def build_words_integration(self, words_in_message):
        words_dictionary = {}
        numbers_set   = set()

        for word in words_in_message:
            if word not in words_dictionary:
                word_classification = self.word_classification(word)
                words_dictionary.update({word : word_classification})
            word_classification = words_dictionary[word]['word_classification_code']
            if word_classification is self.other_classification:
                numbers_set.add(word)
            if word_classification is self.verb_code:
                self.update_statistics('verbs')
            if word_classification is self.verb_subjuntive_code:
                self.update_statistics('subjuntive_verbs')
            if word_classification is self.presposition_code:
                self.update_statistics('prepositions')

        self.statistics_collection['pretty_numbers'] = self.get_pretty_numbers(numbers_set)


    def get_pretty_numbers(self, numbers_set):
        pretty_numbers = 0
        for number in numbers_set:
            if len(number) > self.pretty_number_len_condition:
                base_ten_number = self.get_base_two_from_base_ten(number)
                print(base_ten_number)
                if base_ten_number > self.pretty_number_min_value:
                    if (base_ten_number % 3) == 0:
                        pretty_numbers =  pretty_numbers + 1
        return pretty_numbers

    def get_base_two_from_base_ten(self, word_base_twenty):
        power = 1
        word_len = len(word_base_twenty) -1
        base_ten = 0
        for index in range(word_len,-1,-1):
            if word_base_twenty[index] in self.alphabet:
                char_value = self.alphabet[word_base_twenty[index]]
                base_ten = base_ten + (pow(20,power) * char_value)
                power = power + 1
            else:
                print('char {0} in word {1} out of alphabeth'.format(word_base_twenty[index], word))
                return 0
        return base_ten

    def update_statistics(self, statistics_key):
        self.statistics_collection[statistics_key] = self.statistics_collection[statistics_key] + 1

    #Codify the three posibilities
    # if is a preposition is state 1
    # if is a Verb is a state 2
    # if is a verb in a subjuntive form is a 3
    def word_classification(self, word):
        collection_result   = {'word_classification_code' : self.other_classification}

        if len(word) >= self.classification_len_condition:
            if self.is_verb(word):
                if self.is_subjuntive(word):
                    collection_result['word_classification_code'] = self.verb_subjuntive_code
                else:
                    collection_result['word_classification_code'] = self.verb_code
            elif self.is_preposition(word):
                collection_result['word_classification_code'] = self.presposition_code
        return collection_result

    def is_verb(self, word):
        return not self.is_char_in_word_index_foo(word,-1)

    def is_subjuntive(self, word):
        return not self.is_char_in_word_index_foo(word, 0)

    def is_preposition(self, word):
        is_preposition =  False
        if len(word) == 6:
            word_chars =  set(word)
            if not self.preposition_char_requirement in word_chars:
                is_preposition = True
        return is_preposition

    def is_char_in_word_index_foo(self, word, index):
        if word[index] in self.foo_letters:
            return True
        return False

if __name__ == '__main__':
    gglon = Googlon()
    message = 'Un mensaje sencillo aaaaaf ansaje xssss'
    #print(gglon.getGooglonAnalysis(message))
    print(gglon.get_base_two_from_base_ten('xssss'))
