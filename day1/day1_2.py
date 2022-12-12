with open('input') as f:
    carryingCalory = []
    lines = f.readlines()
    s = 0
    for line in lines:
        if line == '\n':
            carryingCalory.append(s)
            s = 0
        else:
            s += int(line)

    print(sum(sorted(carryingCalory, reverse=True)[0:3]))
