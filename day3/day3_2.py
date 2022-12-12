def convertLetterToValue(letter):
    asciiValue = ord(letter)

    return asciiValue - 96 if asciiValue >= 97 else asciiValue - 38


with open('input') as f:
    letterList = []
    lines = f.readlines()
    groupsBadge = []
    groupRucksacks = []

    for idx, line in enumerate(lines):
        groupRucksacks.append(line.replace('\n', ''))
        if (idx + 1) % 3 == 0:
            first, second, third = groupRucksacks
            badges = set(first).intersection(second).intersection(third)
            print(groupRucksacks, sum(map(convertLetterToValue, badges)))
            groupsBadgePriority = sum(map(convertLetterToValue, badges))
            groupsBadge.append(groupsBadgePriority)
            groupRucksacks.clear()

    print(sum(groupsBadge))
