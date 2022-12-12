def convertLetterToValue(letter):
    asciiValue = ord(letter)

    return asciiValue - 96 if asciiValue >= 97 else asciiValue - 38


with open('input') as f:
    letterList = []
    lines = f.readlines()
    for line in lines:
        size = len(line) // 2
        first, second = line[:size], line[size:]
        commonLetters = list(set(first).intersection(second))
        letterList += commonLetters

    print(sum(map(convertLetterToValue, letterList)))
