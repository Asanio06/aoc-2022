def isVisibleFromLeft(x, y, grid):
    return grid[y][x] > max(grid[y][i] for i in range(0, x))


def isVisibleFromRight(x, y, grid):
    size = len(grid)
    return grid[y][x] > max(grid[y][i] for i in range(x + 1, size))


def isVisibleFromUp(x, y, grid):
    return grid[y][x] > max(grid[i][x] for i in range(y))


def isVisibleFromBottom(x, y, grid):
    size = len(grid)
    return grid[y][x] > max(grid[i][x] for i in range(y + 1, size))


def isVisibleTree(x, y, grid):
    return isVisibleFromLeft(x, y, grid) \
           or isVisibleFromRight(x, y, grid) \
           or isVisibleFromUp(x, y, grid) \
           or isVisibleFromBottom(x, y, grid)


def numberOfElementInListBeforeReachingSuperiorOrEqualValue(value, list):
    count = 0
    for val in list:
        count += 1
        if val >= value:
            break

    return count


def leftViewingDistance(x, y, grid):
    list = [grid[y][i] for i in range(0, x)]
    list.reverse()

    return numberOfElementInListBeforeReachingSuperiorOrEqualValue(grid[y][x], list)


def rightViewingDistance(x, y, grid):
    size = len(grid)
    return numberOfElementInListBeforeReachingSuperiorOrEqualValue(grid[y][x], [grid[y][i] for i in range(x + 1, size)])


def upViewingDistance(x, y, grid):
    list = [grid[i][x] for i in range(y)]
    list.reverse()
    return numberOfElementInListBeforeReachingSuperiorOrEqualValue(grid[y][x], list)


def bottomViewingDistance(x, y, grid):
    size = len(grid)
    return numberOfElementInListBeforeReachingSuperiorOrEqualValue(grid[y][x], [grid[i][x] for i in range(y + 1, size)])


def scenicScore(x, y, grid):

    return leftViewingDistance(x, y, grid) * \
           rightViewingDistance(x, y, grid) * \
           upViewingDistance(x, y, grid) * \
           bottomViewingDistance(x, y, grid)


with open('input') as f:
    letterList = []
    lines = f.readlines()

    grid = []

    for line in lines:
        grid.append(list(map(int, line.replace('\n', ''))))

    scores = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            scores.append(scenicScore(j, i, grid))

    print(max(scores))
