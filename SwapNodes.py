import os
import sys

def swapNodes(indexes, queries):
    pass


class TreeSwapper():

    def __init__(self):
        self.root = Node(1)
        self.root.setDeep(0)

    def fillTree(self, indexes):
        currentNode             = self.root
        currentNodesLevelArray   = [currentNode]
        while  currentNodesLevelArray:
            listation = lambda n : n.val
            for indexation in indexes:
                currentNodesLevelArray = currentNodesLevelArray + self.addChildNodes(currentNodesLevelArray.pop(0), indexation)
            print('currentNodesLevelArray : {}'.format(list(map(listation, currentNodesLevelArray ))))
        return self.root

    def addChildNodes(self, parent, childIndexation):
        indexedNodes    = []
        leftChild       = childIndexation[0]
        rightChild      = childIndexation[1]
        if leftChild    != -1 :
            leftChildNode = Node( leftChild )
            leftChildNode.setDeep( parent.getDeepLevel() + 1 )
            parent.setLeftChild( leftChildNode )
            indexedNodes.append( leftChildNode )

        if rightChild   != -1 :
            rightChildNode = Node( rightChild )
            rightChildNode.setDeep(parent.getDeepLevel() + 1)
            parent.setRightNode( rightChildNode )
            indexedNodes.append( rightChildNode )
        listation = lambda n : n.val
        print(list(map(listation, indexedNodes )))
        return indexedNodes


class Node():

    def __init__(self, val):
        self.leftChild  = None
        self.rightChild = None
        self.val        = val
        self.inOrderArr = []

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setLeftChild(self, node):
        print('{0} -> {1} Left'.format(self.getVal(), node.getVal()))
        self.leftChild =  node

    def setRightNode(self, node):
        print('{0} -> {1} Right'.format(self.getVal(), node.getVal()))
        self.rightChild =  node

    def getVal(self):
        return self.val

    def setDeep(self, deepLevel):
        self.deepLevel = deepLevel

    def getDeepLevel(self):
        return self.deepLevel

    def in_order(self):
        if self.leftChild:
            self.leftChild.in_order()
        print(self.getVal())
        if self.rightChild:
            self.rightChild.in_order()
        #self.inOrderArr.append(self.getVal())








    def is_leaf(self):
        if not self.leftChild and not self.rightChild:
            return True
        else:
            return False

if __name__ == "__main__":
    indexes = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    queries = [2,4]
    ts = TreeSwapper()
    root = ts.fillTree(indexes)
    root.in_order()

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
"""
