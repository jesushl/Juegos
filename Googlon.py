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
        self.pretty_number_len_condition    = 3
        self.pretty_number_min_value        = 81827
        #preposition char requirement
        self.preposition_char_requirement   = 'u'

        self.statistics_collection          = {'prepositions': 0,'verbs': 0}
        self.statistics_collection.update({'subjuntive_verbs' : 0})
        self.statistics_collection.update({'pretty_numbers': 0})
        self.words_dictionary = {}
    #StartPoint
    def getGooglonAnalysis(self, string_message):
        string_message = string_message.lower()
        words_in_message = string_message.split(' ')
        self.build_words_integration(words_in_message)
        return self.statistics_collection

    def build_words_integration(self, words_in_message):
        numbers_set   = set()

        for word in words_in_message:
            if word not in self.words_dictionary:
                word_classification = self.word_classification(word)
                self.words_dictionary.update({word : word_classification})
            word_classification = self.words_dictionary[word]['word_classification_code']
            if word_classification is self.verb_code:
                self.update_statistics('verbs')
            if word_classification is self.verb_subjuntive_code:
                self.update_statistics('subjuntive_verbs')
                self.update_statistics('verbs')
            if word_classification is self.presposition_code:
                self.update_statistics('prepositions')
        self.statistics_collection['pretty_numbers'] = self.get_pretty_numbers(words_in_message)
        return self.words_dictionary

    #This method use words in a message and get all
    # words that value in base twenty is  > 81827
    # and % 3 is zero
    def get_pretty_numbers(self, words_in_message):
        pretty_numbers = 0
        for word in words_in_message:
            if len(word) > self.pretty_number_len_condition:
                base_ten_number = self.get_base_ten_from_base_twenty(word)
                if base_ten_number > self.pretty_number_min_value:
                    if (base_ten_number % 3) == 0:
                        pretty_numbers =  pretty_numbers + 1
        return pretty_numbers

    # Transfors a word to a number using alphabeth values
    # and base 20
    def get_base_ten_from_base_twenty(self, word_base_twenty, base = 20):
        power = 1
        word_len = len(word_base_twenty) -1
        base_ten = 0
        for index in range(word_len,-1,-1): # range iterates in reverse
            if word_base_twenty[index] in self.alphabet:
                char_value = self.alphabet[word_base_twenty[index]]
                base_ten = base_ten + (pow(base, power) * char_value)
                power = power + 1 #power value change by iteration
            else:
                #print('char {0} in word {1} out of alphabeth'.format(word_base_twenty[index], word))
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

    def is_preposition(self, word, len_word = 6):
        is_preposition =  False
        if len(word) == len_word:
            word_chars =  set(word)
            if not self.preposition_char_requirement in word_chars:
                is_preposition = True
        return is_preposition

    def is_char_in_word_index_foo(self, word, index):
        if word[index] in self.foo_letters:
            return True
        return False

    #Use an alphabeth buble sort
    def get_alphabetical_order(self):
        words = list(self.words_dictionary.keys())
        ordered_words = []
        ordered_words.append(words.pop())
        for word in words:
            inserted = False
            for i in range(0,len(ordered_words)):
                is_left = self.is_left(word, ordered_words[i])
                if self.is_left(word, ordered_words[i]):
                    ordered_words.insert(i, word)
                    inserted = True
                    break
            if not inserted:
                ordered_words.append(word)
            #import pdb; pdb.set_trace()
        return ordered_words


    def is_left(self, word_to, word_in):
        len_word_to = len(word_to)
        len_word_in = len(word_in)
        comparation_len = 0
        is_to_bigger = False
        if len_word_to > len_word_in:
            comparation_len = len_word_in
            is_to_bigger = True
        else:
            comparation_len = len_word_to
        for i in range(0, comparation_len):
            if  self.alphabet[word_to[i]] < self.alphabet[word_in[i]]:
                return True
            elif self.alphabet[word_to[i]] > self.alphabet[word_in[i]]:
                return False
        if is_to_bigger:
            return False
        else:
            return True

    def print_result(self, message):
        self.getGooglonAnalysis(message)
        print("1) There are {} prepositions in the text".format(self.statistics_collection['prepositions']))
        print("2) There are {} verbs in the text".format(self.statistics_collection['verbs']))
        print("3) There are {} subjunctive verbs in the text".format(self.statistics_collection['subjuntive_verbs']))
        ordered_words = self.get_alphabetical_order()
        print("4) Vocabulary list: {}".format(' '.join(ordered_words)))

        print("5) There are {} distinct pretty numbers in the text".format(self.statistics_collection['pretty_numbers']))


if __name__ == '__main__':
    gglon = Googlon()
    message = "shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql"
    gglon.print_result(message)
