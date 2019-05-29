class BubbleSort():

    def __init__(self):
        self.numberOfSwaps  = 0
        self.toSortArray    = []

    def swap(self, leftIndex, rightIdex):
        leftValue = self.toSortArray[leftIndex]
        self.toSortArray[leftIndex] = self.toSortArray[rightIdex]
        self.toSortArray[rightIdex] = leftValue

    def bubble(self):
        for i in range(0, len(self.toSortArray) -1):
            for j in range(0, len(self.toSortArray) -1):
                if self.toSortArray[ j ] > self.toSortArray[ j + 1 ]:
                    self.swap(j, j+1)
                    self.numberOfSwaps = self.numberOfSwaps + 1
            if self.numberOfSwaps == 0:
                break
        return self.toSortArray

    def setToSortArray(self, arrayToSort):
        self.toSortArray = arrayToSort

    def sortArray(self, arrayToSort):
        self.setToSortArray(arrayToSort)
        return self.bubble()

if __name__  == '__main__':
    numbers  = [1,4,6,7,5,8,5]
    bs      =  BubbleSort()
    print(bs.sortArray(numbers))
