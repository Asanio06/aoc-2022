def convertStrToRange(str):
    val1, val2 = map(int, str.split('-'))
    return [*range(val1, val2 + 1)]


def convertStringRangeToList(strRange):
    ranges = list(map(convertStrToRange, strRange.split(',')))

    return ranges


def isRangeContainElementOfOther(range1, range2):
    if len(set(range1) & set(range2)) > 0:
        return True
    else:
        return False


with open('input') as f:
    letterList = []
    lines = f.readlines()
    count = 0
    for line in lines:
        range1, range2 = convertStringRangeToList(line)

        if (isRangeContainElementOfOther(range1, range2)):
            count += 1

    print(count)
