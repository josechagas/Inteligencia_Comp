import random

margin_one_key = "margin_one"
margin_two_key = "margin_two"
boat_key = "boat"
sons_key = "sons"
dad_key = "dad"
cannibals_key = "cannibals"
missionaries_key = "missionaries"
boat_position_key = "boat_position"
on_margin_one = 1
on_margin_two = 2


boatOptions = [(1,1),(1,0),(0,1),(2,0),(0,2)]

#n_cannibals = numero de canibais
#n_missionaries = numero missionarios
def newMargin(n_cannibals,n_missionaries):
    #margin = collect.namedtuple("Margin",["cannibals","missionaries"])
    margin = {cannibals_key: n_cannibals, missionaries_key: n_missionaries}
    return margin

# marginOne = dictionary da margem 1
# marginTwo = dictionary da margem 2
# boat = dictionary com os dados do barco
# dad = dictionary com os dados do pai(estado anterior)
def newMove(marginOne,marginTwo,boatPosition,dad):
    #node = collect.namedtuple("Node",["margin_one","margin_two","boat","sons","dad"])
    node = {margin_one_key: marginOne, margin_two_key: marginTwo, boat_position_key: boatPosition, sons_key: [], dad_key: dad}
    return node


# this method receives a node, that represents an state or move and return if its a valid one
def isAValidMove(node):
    marginOne = node[margin_one_key]
    marginTwo = node[margin_two_key]

    valid = False

    cannibalsOne = marginOne[cannibals_key]
    missionariesOne = marginOne[missionaries_key]

    cannibalsTwo = marginTwo[cannibals_key]
    missionariesTwo = marginTwo[missionaries_key]

    if missionariesOne > 0:
        valid = cannibalsOne <= missionariesOne
    elif missionariesOne == 0:
        valid = True
    else:# < 0
        valid = False

    if missionariesTwo > 0:
        valid = valid and cannibalsTwo <= missionariesTwo
    elif missionariesTwo == 0:
        valid = valid and True
    else:# < 0
        valid = valid and False

    return valid

def isARepeatedMove(move,dad):
    if dad is None:
        return False

    dadMarginOne = dad[margin_one_key]
    moveMarginOne = move[margin_one_key]

    if dadMarginOne[missionaries_key] == moveMarginOne[missionaries_key] and dadMarginOne[cannibals_key] == moveMarginOne[cannibals_key]:
        return True
    return isARepeatedMove(move,dad[dad_key])


def isTheEnd(node):
    marginTwo = node[margin_two_key]
    return marginTwo[cannibals_key] == marginTwo[missionaries_key] and marginTwo[cannibals_key] == 3

def possibleMovesForDad(dad):
    validMoves = []

    dadMarginOne = dad[margin_one_key]
    dadMarginTwo = dad[margin_two_key]
    dadBoatPos = dad[boat_position_key]

    random.shuffle(boatOptions)

    newBoatPos =on_margin_one
    if dadBoatPos == on_margin_one: newBoatPos = on_margin_two

    for option in boatOptions:

        marginOne = None
        marginTwo = None

        if newBoatPos == on_margin_one:
            marginOne = newMargin(dadMarginOne[cannibals_key]+option[0],dadMarginOne[cannibals_key]+option[1])
            marginTwo = newMargin(dadMarginTwo[cannibals_key]-option[0],dadMarginTwo[cannibals_key]-option[1])
        else:
            marginOne = newMargin(dadMarginOne[cannibals_key] - option[0], dadMarginOne[cannibals_key] - option[1])
            marginTwo = newMargin(dadMarginTwo[cannibals_key] + option[0], dadMarginTwo[cannibals_key] + option[1])

        possibleMove = newMove(marginOne,marginTwo,newBoatPos,dad)

        if isAValidMove(possibleMove):# check if its a valid one
            if not isARepeatedMove(possibleMove,dad):# check if its repeating an older move
                validMoves.append(possibleMove)

    return validMoves
