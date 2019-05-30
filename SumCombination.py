"""
From video https://www.youtube.com/watch?time_continue=172&v=XKu_SEDAykw
"""

class SumCombination:
    def __int__(self):
        pass

    def isSumPossible(self, array, numberSum):
        leftIndex       = 0
        rightIndex      = len(array) - 1
        while leftIndex < rightIndex:
            if array[rightIndex] >  numberSum:
                rightIndex = rightIndex -1
            else :
                s = array[rightIndex] + array[leftIndex] # esta suma me genera un conflicto emocional :/
                if s > numberSum:
                     rightIndex = rightIndex - 1
                elif s < numberSum:
                    leftIndex =  leftIndex + 1
                elif s == numberSum:
                    return True
        return False

    def isSumPossileNotSorted(self, array, number):
        passNumbers = {}
        for iNumber in array:
            complement = number - iNumber
            if complement in passNumbers:
                return True
            else :
                passNumbers.update({iNumber : None})
        return False


if __name__ ==  "__main__":
    numbersArray    = [4,9,9,9,9,9]
    sum             = 8
    numbersArray2   = [6,0,5,9,4,9,42,-34]
    sc = SumCombination()
    result = sc.isSumPossible(numbersArray, sum)
    print(result)
    result2 = sc.isSumPossileNotSorted(numbersArray2, 8)
    print(result2)
