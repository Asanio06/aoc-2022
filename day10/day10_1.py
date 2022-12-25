def findValueByCycleNumber(dict, cycle):
    if cycle in dict:
        return dict[cycle]

    else:
        return findValueByCycleNumber(dict, cycle - 1)


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

    print(sum(findValueByCycleNumber(valueByCycleNumber, cycle) * cycle for cycle in cyclesToObserve))

