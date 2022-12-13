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


with open('input') as f:
    letterList = []
    lines = f.readlines()

    grid = []

    for line in lines:
        grid.append(list(map(int, line.replace('\n', ''))))

    [print(l) for l in grid]
    visibleInTheInteriorCount = 0
    size = len(grid)
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i])-1):

            if (isVisibleTree(j, i, grid)):
                print(i, j, grid[i][j])
                visibleInTheInteriorCount+=1

    numberOfBoundaryElement = (size * 4 ) - 4
    print(visibleInTheInteriorCount + numberOfBoundaryElement)