from math import sqrt

fromPosKey = "fromPos"
toPosKey = "toPos"



#The values that are on their correct position
lockedValues = []

lastWhitePos = [-1, -1]

################ A*

def calcFOf(initialPos,finalPos):
    xA = initialPos[1]
    xB = finalPos[1]

    yA = initialPos[0]
    yB = finalPos[0]

    c = 0
    if(yA-yB == 0):
        c = 0.5

    return sqrt(((xA-xB)**2) + ((yA-yB)**2)) - c


#swap the corresponding positions
def swap(posOne,posTwo,puzzle):
    valueOne = puzzle[posOne[0]][posOne[1]]
    valueTwo = puzzle[posTwo[0]][posTwo[1]]

    puzzle[posOne[0]][posOne[1]] = valueTwo
    puzzle[posTwo[0]][posTwo[1]] = valueOne


def moveToDestiny(initialPos,finalPos,puzzle,fatherPos):
    line0 = initialPos[0]
    col0 = initialPos[1]

    bestOne = bestWhiteNeightboorFor(initialPos,finalPos,fatherPos,puzzle)

    swap(initialPos,bestOne,puzzle)


    if (not (bestOne == finalPos)):
        return moveToDestiny(bestOne,finalPos,puzzle,fatherPos)

################
#return true if corresponding value is on lockedValues
def valueIsLocked(value):
    try:
        colValue = lockedValues.index(value)
        return True
    except ValueError:
        return False

def newSplitMove(fromPos,toPos):
    return {fromPosKey:fromPos,toPosKey:toPos}

#this method gets the corresponding 'value' and return its correct position when puzzle is solved
def finalPosForValue(value):

    line = 0 #value == 1 or value == 2 or value == 3
    col = 0 #value == 1 or value == 4 or value == 7

    if value == 2 or value == 5 or value == 8:
        col = 1
    elif value == 3 or value == 6 or value == 0:
        col = 2

    if value == 4 or value == 5 or value == 6:
        line = 1
    elif value == 7 or value == 8 or value == 0:
        line = 2
    return (line,col)

def posOfValueOn(value,puzzle):
    for line in range(0,3):
        try:
            lineList = puzzle[line]
            colValue = lineList.index(value)
            return (line, colValue)
        except ValueError:
            continue
    return (-1,-1)

#Finds the neightboors valid positions of pos
def findNeightboorsOf(pos):
    neightboors = []
    line = pos[0]
    col = pos[1]
    if(line - 1 >= 0):#same line
        neightboors.append((line - 1,col))
    if (line + 1 <= 2):#same line
        neightboors.append((line + 1, col))

    if (col - 1 >= 0):  # same line
        neightboors.append((line, col - 1))
    if (col + 1 <= 2):  # same line
        neightboors.append((line, col + 1))
    return neightboors


#Calculates the best white pos neightboor to proceed
def bestWhiteNeightboorFor(whitePos,objectivePos,valuePos,puzzle):
    bestPos = (-1,-1)
    bestDist = 1000
    neightboorsPos = findNeightboorsOf(whitePos)
    print("")
    for neightboor in neightboorsPos:

        F = calcFOf(neightboor,objectivePos)
        neightboorValue = puzzle[neightboor[0]][neightboor[1]]
        if (F < bestDist and not valueIsLocked(neightboorValue) and not (valuePos == neightboor) and not(lastWhitePos == neightboor)):
            bestDist = F
            bestPos = neightboor

    lastWhitePos = bestPos

    return bestPos

#Calculates the best position to send white pos and so move selected value
def bestWhitePFor(valuePos,objectivePos,puzzle):
    bestPos = (-1,-1)
    bestDist = 1000
    neightboorsPos = findNeightboorsOf(valuePos)
    print("")
    for neightboor in neightboorsPos:

        F = calcFOf(neightboor,objectivePos)
        neightboorValue = puzzle[neightboor[0]][neightboor[1]]

        if (F < bestDist and not valueIsLocked(neightboorValue)):
            bestDist = F
            bestPos = neightboor

    return bestPos


def findPathAndMove(initialPos,objectivePos,value,puzzle):
    if (objectivePos == initialPos):
        lockedValues.append(value)
        return
    else:

        whitePos = posOfValueOn(0, puzzle)
        whitePDestiny = bestWhitePFor(initialPos, objectivePos, puzzle)
        # put white space nearer to 'value'
        moveToDestiny(whitePos, whitePDestiny, puzzle,initialPos)

        # swap the positions of '0' and 'value'
        swap(initialPos, whitePDestiny, puzzle)

        print(str(puzzle))
        #whitePDestiny new 'value' pos
        return findPathAndMove(whitePDestiny,objectivePos,value,puzzle)

def solvePuzzle(puzzle):
    moves = []
    for value in range(1,9,1):
        objectivePos = finalPosForValue(value)
        initialPos = posOfValueOn(value,puzzle)
        # print("currentObject "+str(value))
        # print("Correct Pos "+str(objective))
        # print("Final Pos "+str(initialPos)+"\n\n")
        findPathAndMove(initialPos,objectivePos,value,puzzle)

def main():
    puzzle = [[0, 8, 2],
              [3, 7, 1],
              [4, 6, 5]]

    solvePuzzle(puzzle)

    #print(puzzle[2][2])
    #print("asdasd")


main()
