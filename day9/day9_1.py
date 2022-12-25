def isUpOfOtherPoint(point, other_point):
    x1, y1 = point
    x2, y2 = other_point

    return y1 > y2


def isDownOfOtherPoint(point, other_point):
    x1, y1 = point
    x2, y2 = other_point

    return y1 < y2


def isLeftOfOtherPoint(point, other_point):
    x1, y1 = point
    x2, y2 = other_point

    return x1 < x2


def isRightOfOtherPoint(point, other_point):
    x1, y1 = point
    x2, y2 = other_point

    return x1 > x2


def isOnDiagonalOfOtherPoint(point, other_point):
    x, y = other_point

    if point == (x - 1, y + 1):
        return True

    if point == (x + 1, y + 1):
        return True

    if point == (x - 1, y - 1):
        return True
    if point == (x + 1, y - 1):
        return True

    return False



def next_head_position(position, _move):
    x, y = position

    if _move == 'L':
        new_position = (x - 1, y)
    elif _move == 'R':
        new_position = (x + 1, y)
    elif _move == 'U':
        new_position = (x, y + 1)
    else:
        new_position = (x, y - 1)

    return new_position


def next_tail_position(position, head_position, _move):
    x, y = head_position

    if position == head_position:
        return head_position
    elif isOnDiagonalOfOtherPoint(position, head_position):
        return position
    elif isUpOfOtherPoint(position, head_position) and _move == 'D':
        return (x, y + 1)
    elif isDownOfOtherPoint(position, head_position) and _move == 'U':
        return (x, y - 1)
    elif isLeftOfOtherPoint(position, head_position) and _move == 'R':
        return (x - 1, y)
    elif isRightOfOtherPoint(position, head_position) and _move == 'L':
        return (x + 1, y)

    else:
        return position



with open('input') as f:
    lines = f.readlines()
    tailsPositions = []
    currentHeadPosition = (0, 0)
    currentTailPosition = (0, 0)

    for line in lines:
        move, number = line.split()

        for i in range(int(number)):
            currentHeadPosition = next_head_position(currentHeadPosition, move)
            currentTailPosition = next_tail_position(currentTailPosition, currentHeadPosition, move)

            tailsPositions.append(currentTailPosition)

    print(len(set(tailsPositions)))
