def findValueByCycleNumber(dict, cycle):
    if cycle in dict:
        return dict[cycle]

    else:
        return findValueByCycleNumber(dict, cycle - 1)


def getSpritePixelsPosition(valueByCycleNumber, cycle):
    value = findValueByCycleNumber(valueByCycleNumber, cycle)
    return [value - 1, value, value + 1]


def getCrtValue(valueByCycleNumber, cycle):
    spritePixels = getSpritePixelsPosition(valueByCycleNumber, cycle)
    position = (cycle - 1)%40
    return "#" if position in spritePixels else "."


def getCrtOnRange(valueByCycleNumber, begin, end):
    s = ""

    for i in range(begin, end):
        s += getCrtValue(valueByCycleNumber, i)

    return s


with open('input') as f:
    lines = f.readlines()

    valueByCycleNumber = {}

    XForCalcul = 1
    currentX = 1
    cycleNumber = 0

    for line in lines:
        lineStr = line.split()
        cycleNumber += 1
        if cycleNumber not in valueByCycleNumber:
            valueByCycleNumber[cycleNumber] = currentX
        else:
            currentX = valueByCycleNumber[cycleNumber]

        if lineStr[0] == 'addx':
            XForCalcul += int(lineStr[1])
            valueByCycleNumber[cycleNumber + 2] = XForCalcul
            cycleNumber += 1

    cyclesToObserve = [20, 60, 100, 140, 180, 220]

    [print(getCrtOnRange(valueByCycleNumber, i + 1, i + 41)) for i in range(0, 220, 40)]

