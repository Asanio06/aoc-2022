pointByResult = {'lost': 0, 'draw': 3, 'won': 6}
pointByAction = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

letterToAction = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

winTable = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

letterToResult = {'X': 'lost', 'Y': 'draw', 'Z': 'won'}


# function to return key for any value
def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def getResult(opponent, me):
    if opponent == me:
        return 'draw'
    elif winTable[me] == opponent:
        return 'won'

    return 'lost'


def getActionFromDesiredResult(opponent, result):
    if result == "draw":
        return opponent
    elif result == "lost":
        return winTable[opponent]

    return get_key(winTable, opponent)


with open('input') as f:
    carryingCalory = []
    lines = f.readlines()
    score = 0
    for line in lines:
        opponentLetter, myLetter = line.split()
        opponentAction = letterToAction[opponentLetter]
        desiredResult = letterToResult[myLetter]

        myAction = getActionFromDesiredResult(opponentAction, desiredResult)
        score += pointByResult[desiredResult]
        score += pointByAction[myAction]

    print(score)
