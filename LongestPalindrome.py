class LongestPalindrome():
    #@param {string}
    #@return {dict}
    def buildPalindromeDict(self, wordString):
        wordPalindromeDict  = {}
        wordList            = list(wordString)
        for char in wordList:
            if char in wordPalindromeDict:
                wordPalindromeDict[char] = wordPalindromeDict[char] + 1
            else:
                wordPalindromeDict.update({char:1})
        return wordPalindromeDict
    '''
    @param  {dict}
    @return {dict}
    return  {'couple':<coupleSum>, 'odd':<oddSub>}
    '''
    def getAnalysisFromDic(self, wordPalindromeDict):
        analisysResultDict = {'couple' : 0, 'odd': 0}
        for charKey in wordPalindromeDict:
            occurrencies = wordPalindromeDict[charKey]
            if occurrencies > 1 :
                if (occurrencies % 2) == 0:
                    analisysResultDict['couple']   =  analisysResultDict['couple'] + occurrencies
                else :
                    analisysResultDict['couple']    =  analisysResultDict['couple'] + occurrencies -1
                    analisysResultDict['odd']       = 1
            else:
                if occurrencies == 1:
                    analisysResultDict['odd']       = 1
        print(analisysResultDict)
        return analisysResultDict

    def getMaximumLenghtPalindrom(self, analisysResultDict ):
        maxLenght = analisysResultDict['couple']
        if analisysResultDict['odd']:
            maxLenght  = maxLenght + 1
        return maxLenght

    def maxLenghtPalindrom(self, wordString):
        return self.getMaximumLenghtPalindrom(
            self.getAnalysisFromDic(
                self.buildPalindromeDict(wordString)
            )
        )
if __name__ == "__main__":
    lp  = LongestPalindrome()
    wordString   = 'abccccdd'
    print(lp.maxLenghtPalindrom(wordString))
