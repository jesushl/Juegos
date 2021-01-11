class Quicksort():
    
    def quicksort(self, array, lo, hi):
        if lo < hi:
            p = self.partition(array, lo, hi)
            self.quicksort(array, lo, p-1)
            self.quicksort(array, p +1, hi )

    def partition(self, array, lo, hi):
        pivot = array[hi]
        print('lo: {lo}   hi: {hi}'.format(lo=lo, hi=hi))
        i = lo 
        print('Pivot: {pivot}'.format(pivot=pivot))
        for j in range( lo, hi+1 ):
            print('Compare pivot: {pivot} with {value}'.format( pivot=pivot, value=array[j] ))
            if array[j] < pivot:
                print('Shuffle j: {j} -> {left} to right i:{i}-> {right}'.format(left=array[j], right=array[i], i=i, j=j))
                _ = array[j]
                array[j] = array[i]
                array[i] = _ 
                i = i + 1
                print('new i : {}'.format(i))
                print('\t{}'.format(array))
        _ = array[i]
        array[i] = array[hi]
        array[hi] = _
        print(array)
        print('Partition index:{i}, value: {val}'.format(i=i, val=array[i]))
        return i

if  __name__ == '__main__':
    array = [1,9,2,8,3,8,4,7,5,6]
    qs = Quicksort()
    print(array)
    qs.quicksort(array, 0, len(array)-1)
    print(array)