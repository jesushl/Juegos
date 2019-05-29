class PossibleNumberDecoding():

    def __init__(self):
        self.resultsList  = []
        self.alphabetColl = {}
    """
    @params{char, char}
    @return{yield<char>}
    """
    def char_range(self,c1,c2):
        for c in range(ord(c1), ord(c2) + 1):
            yield chr(c)

    """
    @params{None}
    @returns{dict}
    """
    def buildAlphabetColl(self):
        alphabetColl    =  {}
        index           = 1
        for c in self.char_range('a', 'z'):
            alphabetColl.update({index : c})
            index = index + 1
        self.alphabetColl = alphabetColl
        return self.alphabetColl

    """
    @params{Int, dict, arr<int>}
    @return{list}
    """
    def solveString(self, numbersCodeInt, currentPosibility):
        #print(numbersCodeInt)
        try:
            if numbersCodeInt[0] > 0:
                localNumbersCodeInt = numbersCodeInt.copy()
                currentPosibilityLocal = currentPosibility.copy()
                currentPosibilityLocal.append(localNumbersCodeInt.pop(0))
                if localNumbersCodeInt:
                    self.solveString(localNumbersCodeInt, currentPosibilityLocal)
                else:
                    self.resultsList.append(currentPosibilityLocal)
        except IndexError as ie:
            pass
            #print('Indice superado en individuales')
        try:
            #print('Pares 0 : {0} y 1 : {1}'.format(numbersCodeInt[0], numbersCodeInt[1]))
            if numbersCodeInt[0] < 3 and numbersCodeInt[0] > 0  and numbersCodeInt[1] < 7 :
                #print('Posibilidad')
                localNumbersCodeInt2 = numbersCodeInt.copy()
                composeNumber = int(str('{0}{1}'.format(localNumbersCodeInt2[0],
                    localNumbersCodeInt2[1])))
                localNumbersCodeInt2 = localNumbersCodeInt2[2:]
                #print(composeNumber)
                if ( composeNumber < 25 )  and (composeNumber > 0):

                    currentPosibilityLocalDup = currentPosibility.copy()
                    currentPosibilityLocalDup.append(composeNumber)

                    if localNumbersCodeInt2:
                        self.solveString(localNumbersCodeInt2, currentPosibilityLocalDup)
                    else :
                        self.resultsList.append(currentPosibilityLocalDup)

        except IndexError as ie:
            print('Indice superado en pares')
    """
    """
    def numWays(self, numbersCodeStr):
        numbersCode = list(map(int,numbersCodeStr))
        self.buildAlphabetColl()
        print(self.alphabetColl)
        self.solveString(numbersCode, [])
        print(self.resultsList)
        return len(self.resultsList)


if __name__ == '__main__':
    pos_num_dec = PossibleNumberDecoding()
    #print(pos_num_dec.buildIntegerArray())
    pos_num_dec.numWays('27345')
