pointByResult = {'lost': 0, 'draw': 3, 'won': 6}
pointByAction = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

letterToAction = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

winTable = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}


def getResult(opponent, me):
    if opponent == me:
        return 'draw'
    elif winTable[me] == opponent:
        return 'won'

    return 'lost'


with open('input') as f:
    carryingCalory = []
    lines = f.readlines()
    score = 0
    for line in lines:
        opponentAction, myAction = map(lambda x: letterToAction[x], line.split())
        result = getResult(opponentAction, myAction)
        score += pointByResult[result]
        score += pointByAction[myAction]

    print(score)
