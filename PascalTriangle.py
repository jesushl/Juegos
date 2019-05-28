
class PascalTriangle():
    def __init__(self):
        pass

    def solveTriangle(self, triangleLevel):
        triangle = [[1]]
        for i in range(1,triangleLevel+1):
            self.addNewRowToPascalTriangle(triangle)
        return triangle


    def getSumValue(self, arrayPos, pascalMatrix):
        x   = 0
        y   = 1
        leftTopValue    = 0
        rightTopValue   = 0
        topLeftPossition  = (arrayPos[x] - 1, arrayPos[y] -1)
        topRightPossition = (arrayPos[x] - 1, arrayPos[y])
        #Get right top Value
        try :
            rightTopValue = pascalMatrix[topRightPossition[x]][topRightPossition[y]]
        except IndexError as ie:
            pass
        #get left top value
        try:
            if topLeftPossition[1] == -1:
                leftTopValue = 0
            else:
                leftTopValue  = pascalMatrix[topLeftPossition[x]][topLeftPossition[y]]
        except IndexError as ie :
            pass
        return leftTopValue + rightTopValue

    def addNewRowToPascalTriangle(self, pascalMatrix):
        y   = 1
        x   = 0
        xIndex      = len(pascalMatrix) ##Deep pascal Matrix level
        yIndex      = 0
        #print("deep : {}".format(xIndex) )
        newRow = []
        currentPascalPosition   = [xIndex, yIndex]
        currentPascalValue      =   1 #Control value
        while currentPascalValue > 0:
            #print('Current Pascal Possition : {}'.format(currentPascalPosition))
            currentPascalValue =  self.getSumValue(currentPascalPosition,pascalMatrix)
            if currentPascalValue != 0:
                newRow.append(currentPascalValue)
            yIndex =  yIndex + 1
            currentPascalPosition[y] = yIndex
            #print(newRow)
        pascalMatrix.append(newRow)
        return pascalMatrix


if __name__ == "__main__":
    import argparse
    import pprint
    pt = PascalTriangle()
    argparseConf = {}
    argparseConf.update({'description' :'Create pascal trinagles'})
    argparseConf.update({'prog':'PascalTRiangle'})
    argparseConf.update({'usage':'This program generate pascal triangles in a nLogn time, try "python3 PascalTriangle -l 5"'})
    argparseConf.update({'epilog':'This program generates a pascal trinagles in O(nLogn) time '})
    argparseConf.update({'add_help':'This program needs pprint "pip3 install pprint"'})
    parser = argparse.ArgumentParser()
    parser.add_argument('--level', help = 'Triagle level to build', type=int)
    args = parser.parse_args()
    level = args.level
    print(level)
    pprint.pprint(pt.solveTriangle(level))
