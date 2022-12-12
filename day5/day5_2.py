import re

size = 9


def getValuesFromStringTemplate(strTemplate):
    m = re.match(r'move (.*) from (.*) to (.*)', strTemplate)

    return list(map(int, [m.group(1), m.group(2), m.group(3)]))


def initialStacksToDict(initialStacks):
    stacks = {}
    for i in range(0, size):
        stacks[i + 1] = []

    for idx, stack in enumerate(initialStacks):
        if idx != len(initialStacks) - 1:
            for i in range(0, size):
                val = stack[(i * 4):(i * 4) + 3]
                if bool(val.strip()):
                    stacks[i + 1].append(val)

    return stacks


with open('input') as f:
    letterList = []
    lines = f.readlines()
    moveDisplay = False
    moves = []
    initialsStacksStr = []
    for line in lines:

        if line == '\n':
            moveDisplay = True
            continue

        if moveDisplay:
            moves.append(line)
        else:
            initialsStacksStr.append(line)

    stackDict = initialStacksToDict(initialsStacksStr)
    for move in moves:
        numberToTake, origin, destination = getValuesFromStringTemplate(move)
        # print(numberToTake, origin, destination,stackDict[origin])
        elementsToMove = stackDict[origin][:numberToTake]

        stackDict[origin] = stackDict[origin][numberToTake:]
        stackDict[destination] = elementsToMove + stackDict[destination]

    end = ""
    for key in stackDict:
        strVal = stackDict.get(key)[0]

        end += strVal[1:-1]

    print(end)
