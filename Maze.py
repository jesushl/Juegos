"""
Este programa esta pensado para usar maquinas de estados en procesadores paralelos
que resuelvan un laberinto de 1 y 0
siendo la letra J dentro del laverint el premio,
el número 1 un muro y el numero 0 un pasillo
la tarea es
encontrar la ruta mas corta  al gol

Laberinto muestra1
0001001000
0001010000
1001010010
0001010010
0100010111
10100J0000
0000000000
1111111111
1111111111
1111111111

Laberinto Muestra 2
0100000000
0010000000
0001000000
0001111000
0001J01000
0000001000
0000000000
0001000000
0000101000
"""

class Runner():

    def __init__(self, posX, posY, learnHistoryArr, maze, winnerPaths):
        self.posX               = posX
        self.posY               = posY
        self.learnHistoryArr    = learnHistoryArr
        self.maze               = maze
        self.xLarge             = len(maze[0])
        self.yLarge             = len(maze)
        self.winnerPaths        = winnerPaths
        self.goal = 'J'
        self.wall = '1'
        self.hall = '0'
        #print(learnHistoryArr)
        self.runnerPropagation()


    def isGoal(self, posX, posY):
        if self.maze[posX][posY] == self.goal :
            return True
        else:
            return False

    def isWall(self, posX, posY):
        if self.maze[posX][posY] == self.wall :
            return True
        return False

    def isTouched(self, posX, posY):
        if (posX, posY) in self.learnHistoryArr:
            return True
        return False

    def runTop(self):
        nYPos = self.posY + 1
        if nYPos < self.yLarge and nYPos > 0:
            currentHistoryArr = self.learnHistoryArr[:]
            currentHistoryArr.append((self.posX, nYPos))
            if self.isGoal(self.posX, nYPos):
                currentHistoryArr.append((self.posX, nYPos))
                self.winnerPaths.append(currentHistoryArr)
                return
            else:
                if not self.isWall(self.posX, nYPos) and not self.isTouched(self.posX, nYPos):
                    r = Runner(self.posX, nYPos, currentHistoryArr, self.maze, self.winnerPaths)

    def runButton(self):
        nYPos = self.posY - 1
        if nYPos < self.yLarge and nYPos > 0:
            currentHistoryArr = self.learnHistoryArr[:]
            currentHistoryArr.append((self.posX, nYPos))
            if self.isGoal(self.posX, nYPos):
                currentHistoryArr.append((self.posX, nYPos))
                self.winnerPaths.append(currentHistoryArr)
                return
            else:
                if not self.isWall(self.posX, nYPos)  and not self.isTouched(self.posX, nYPos):
                    r = Runner(self.posX, nYPos, currentHistoryArr, self.maze, self.winnerPaths)

    def runDown(self):
        nXPos = self.posX - 1
        if nXPos < self.xLarge and nXPos > 0:
            currentHistoryArr = self.learnHistoryArr[:]
            currentHistoryArr.append((nXPos, self.posY))
            if self.isGoal(nXPos, self.posY):
                currentHistoryArr.append((nXPos, self.posY))
                self.winnerPaths.append(currentHistoryArr)
                return
            else:
                if not self.isWall(nXPos, self.posY) and not self.isTouched(nXPos, self.posY):
                    r = Runner(nXPos, self.posY, currentHistoryArr, self.maze, self.winnerPaths)

    def runBack(self):
        nXPos = self.posX + 1
        if nXPos < self.xLarge and nXPos > 0:
            currentHistoryArr = self.learnHistoryArr[:]
            currentHistoryArr.append((nXPos, self.posY))
            if self.isGoal(nXPos, self.posY):
                currentHistoryArr.append((nXPos, self.posY))
                self.winnerPaths.append(currentHistoryArr)
                return
            else:
                if not self.isWall(nXPos, self.posY) and not self.isTouched(nXPos, self.posY):
                    r = Runner( nXPos, self.posY, currentHistoryArr, self.maze, self.winnerPaths)


    def runnerPropagation(self):
        self.runTop()
        self.runButton()
        self.runDown()
        self.runBack()

    def getBestResult(self, pathWinnersArray):
        lowest = len(pathWinnersArray[0])
        BWinner = pathWinnersArray[0]
        for winner in pathWinnersArray:
            if len(winner) < lowest:
                lowest = len(winner)
                BWinner  = winner
        return BWinner

    def printMazePath(self, path):
        cMaze  = self.maze[:]
        for position in path:
            cMaze[position[0]][position[1]]  = '#'
        for row in cMaze:
            print(row)


if __name__ is "__main__":
    maze1 = [
        ['0','0','0','1','0','0','1','0','0','0'],
        ['0','0','0','1','0','1','0','0','0','0'],
        ['1','0','0','1','0','1','0','0','1','0'],
        ['0','0','0','1','0','1','0','0','1','0'],
        ['0','1','0','0','0','1','0','1','1','1'],
        ['1','0','1','0','0','J','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0'],
        ['1','1','1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1','1','1'],
    ]
    winnerPaths = []
    initialXPossition = 0
    initialYPossition = 0
    r           =  Runner(initialXPossition, initialYPossition, [], maze1, winnerPaths)

    print('Is doin something')
    bWinner = r.getBestResult(winnerPaths)
    r.printMazePath([])
    print()
    print('Best Winner path : {}'.format(bWinner))
    print()
    r.printMazePath(bWinner)
