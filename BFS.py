from BinaryTree import  Solution
class BFS():
    def __init__(self):
        self.bfsArray = []

    def bfs(self, node):
        queue = []
        if node :
            queue.append(node)
            while(queue):
                currentNode = queue.pop(0)
                self.bfsArray.append(currentNode.data)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)


if __name__ == "__main__":
    numbers = [3, 5, 4, 7, 2, 1]
    myTree          = Solution()
    root            = None
    for i in numbers:
        root        = myTree.insert( root, i )
    bfs =  BFS()
    bfs.bfs(root)
    print(bfs.bfsArray)
