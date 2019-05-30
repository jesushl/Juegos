
class BinarySearch:
    def __init__(self):
        pass

    def binarySearch(self, array, number):
        rightIdex = len(array) -1
        leftIndex = 0
        if array:
            while leftIndex <= rightIdex:
                middle = int( ( rightIdex + leftIndex ) / 2 )
                if array[middle] < number:
                    leftIndex = middle + 1
                elif array[middle] > number:
                    rightIdex =  middle -1
                else:
                    return middle
        return False


if  __name__ == "__main__":
    numbers     =  [1,2,3,4,5,6,7,8,9,22,55,44,36,87,95,100]
    bs          =  BinarySearch()
    result      = bs.binarySearch(numbers, 44)
    print(result)
