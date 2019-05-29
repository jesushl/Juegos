class BinaryTree():
    def __init__(self):
        pass

"""
From : https://www.hackerrank.com/challenges/30-binary-search-trees/problem
"""
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        self.maxHeight = 0
        self.treeJumper(root, -1)
        return self.maxHeight

    def treeJumper(self, node, jumps):
        jumps = jumps + 1
        if self.is_leaf(node):
            if jumps > self.maxHeight:
                self.maxHeight =  jumps
        else:
            if node.right:
                self.treeJumper(node.right, jumps)
            if node.left:
                self.treeJumper(node.left, jumps)


    def is_leaf(self, node):
        if not node.right and not node.left :
            return True
        else:
            return False



if __name__ == '__main__':
    numbers         = [3,5,2,1,4,6,7]
    myTree          = Solution()
    root            = None
    for i in numbers:
        root        = myTree.insert( root, i )
    height          = myTree.getHeight(root)
    print(height)
