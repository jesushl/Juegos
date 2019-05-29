class LinkedListRemoveDup():
    def __init__(self):
        pass


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head,data):
            p = Node(data)
            if head == None:
                head = p
            elif head.next == None:
                head.next = p
            else:
                start = head
                while(start.next != None):
                    start = start.next
                start.next = p
            return head

    def display(self,head):
        current = head
        while current:
            print(current.data, end = ' ')
            current = current.next

    def removeDuplicates(self,head):
        uniqueMemory = {}
        newNode      = None
        while head:
            if head.data not in uniqueMemory:
                uniqueMemory.update({ head.data : None })
            head = head.next
        for value in uniqueMemory.keys():
            newNode = self.insert(newNode, value)
        return newNode


if __name__ == '__main__':
    myList      =   Solution()
    head        =   None
    values      = [1,1,3,1,2,1]
    for value in values:
        head = myList.insert(head, value)
    myList.display(head)
    head2  = myList.removeDuplicates(head)
    print()
    myList.display(head2)
