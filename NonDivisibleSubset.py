class NonDivisibleSubset():
    def __init__(self):
        self.sumCollectionDivisible         = {}
        self.combinatoriesBySetZice         = {}
        self.combinatoriesFirstLevel        = {}

    def nonDivisibleSubset(self, k, S):
        self.fillSumCollectionDvisible(k , S)


    def fillSumCollectionDvisible(self, k ,S):
        lenS = len(S)
        for i in range(0, lenS):
            for j in range(i + 1, lenS):
                sum = S[i] + S[j]
                if ( sum % k ) != 0:
                    print('i : {0} j : {1}  Sum : {2}'.format(S[i],S[j],sum))
                    self.actualizeSumCollectionDivisible(S[i] , S[j])
                    self.actualizeSumCollectionDivisible(S[j] , S[i])


    def getLevelEvaluator(self, listOfSubSets, keyLen):
        nSubSets        = len(listOfSubSets)
        restElements    = nSubSets
        for i in range(0, len(nSubSets)):
            restElements = restElements - 1
            if restElements >= keyLen:
                currentSet   = listOfSubSets[i].copy()
                for j in range((i + 1), nSubSets ):

        return True

    def getCombinatoriesBySetZice(self):
        for iKey in self.sumCollectionDivisible:
            collectionLen = len(self.sumCollectionDivisible[iKey])
            collectionLen = collectionLen + 1 #Tomando en cuenta al valor inicial
            nSet  = set(self.sumCollectionDivisible[iKey])
            nSet.add(iKey)
            if collectionLen in self.combinatoriesBySetZice:
                self.combinatoriesBySetZice[collectionLen].append(nSet)
            else:
                self.combinatoriesBySetZice.update({collectionLen : [ nSet ]})

    def actualizeSumCollectionDivisible(self, index, addedValue):
        if index in self.sumCollectionDivisible:
            self.sumCollectionDivisible[index].append(addedValue)
        else:
            self.sumCollectionDivisible.update({ index : [addedValue] })

if __name__ == '__main__':
    nds = NonDivisibleSubset()
    k = 3
    S = [1,7,2,4,10,80]
    nds.fillSumCollectionDvisible(k, S)
    print(nds.sumCollectionDivisible)
    nds.getCombinatoriesBySetZice()
    print(nds.combinatoriesBySetZice)
