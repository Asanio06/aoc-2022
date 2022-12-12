

isStringNoContainsLettersRepeat = lambda substr: len(substring) == len(set(substring))

with open('input') as f:
    letterList = []
    line = f.readline()

    for i in range(4,len(line)):
        substring = line[i-4:i]
        if isStringNoContainsLettersRepeat(substring):
            print(substring, set(substring),i)
            break





