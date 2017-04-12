import Cannibals_Missionaries as cm


def deepSearch(executedMoves,actualMove):
    if cm.isTheEnd(actualMove):
        executedMoves.append(actualMove)
        return executedMoves

    validMoves = cm.possibleMovesForDad(actualMove)
    if validMoves.__len__() > 0:
        executedMoves.append(actualMove)
        actualMove[cm.sons_key] = validMoves
        return deepSearch(executedMoves,actualMove[cm.sons_key][0])
    elif executedMoves.__len__() > 0:#This is the end of road return to last moves and get another way if possible

        #you have another way to get
        lastExecutedMove = executedMoves[executedMoves.__len__() - 1]
        numbOfSons = lastExecutedMove[cm.sons_key].__len__() #numb of sons of lastExecutedMove

        while numbOfSons <= 1 :# return to older steps until find someone with more than one son or while possible
            executedMoves.pop(executedMoves.__len__()- 1)
            if executedMoves.__len__() == 0: return [] # no answer
            lastExecutedMove = executedMoves[executedMoves.__len__() - 1]
            numbOfSons = lastExecutedMove[cm.sons_key].__len__()

        lastExecutedMove[cm.sons_key].pop(0) # remove actualMove from sons because this not a right move to find answer
        sonsMoves = lastExecutedMove[cm.sons_key]
        newActualMove = sonsMoves[0]
        return deepSearch(executedMoves,newActualMove)

    else:# executedMoves == 0 so you have nothing to do
        return [] # no answer


def showMoves(executedMoves):
    for move in executedMoves:
        marginOne = move[cm.margin_one_key]
        marginTwo = move[cm.margin_two_key]

        cannibalsOne = marginOne[cm.cannibals_key]
        missionariesOne = marginOne[cm.missionaries_key]

        cannibalsTwo = marginTwo[cm.cannibals_key]
        missionariesTwo = marginTwo[cm.missionaries_key]

        print "margin one:"+"[c: "+str(cannibalsOne)+" m: "+str(missionariesOne)+"] - "+"margin two:"+"[c: "+str(cannibalsTwo)+" m: "+str(missionariesTwo)+"]"

def main():
    initial = cm.newMove(cm.newMargin(3,3),cm.newMargin(0,0),cm.on_margin_one,None)
    executedMoves = deepSearch([],initial)
    print "Using DeepSearch"
    print "Answer: "
    showMoves(executedMoves)


main()