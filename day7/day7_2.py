actualDir = "/"
totalDiskSpace = 70_000_000
spaceNeedForUpdate = 30_000_000


def is_dir(line_display):
    return line_display.split()[0] == 'dir'


def join_path(path1, path2):
    return path1 + (f'/{path2}' if path1 != '/' else path2)


def getCommandToExec(commandLine):
    splittedLine = commandLine.split()
    if len(splittedLine) >= 3:
        return splittedLine[1], splittedLine[2]

    return splittedLine[1]


def updateCurrentDir(path, current_dir):
    if path[0] == '/':
        new_dir = path

    elif path == '..':
        splittedDir = current_dir.split('/')[:-1]
        new_dir = '/'.join(splittedDir) if current_dir != '/' and len('/'.join(splittedDir)) > 0 else '/'
    else:
        new_dir = current_dir + (f'/{path}' if current_dir != '/' else path)

    return new_dir


def get_dir_size(path, dirs_information):
    dir_information = dirs_information[path]
    total_size = 0
    for file_type, file_path, file_size in dir_information:
        if file_type == 'file':
            total_size += int(file_size)
        else:
            total_size += get_dir_size(file_path, dirs_information)

    return total_size


isCommandLine = lambda line: line[0] == '$'

lastCommandLineResult = []

dirContents = {}

with open('input') as f:
    letterList = []
    lines = f.readlines()

    for line in lines:
        if isCommandLine(line):

            command, arg = getCommandToExec(line)

            if command == 'cd':
                lastD = actualDir
                actualDir = updateCurrentDir(arg, actualDir)
                if (actualDir == ''): print(lastD, line)
                if actualDir not in dirContents:
                    dirContents[actualDir] = []

        else:
            if is_dir(line):
                dirFound = line.split()[1]
                dirContents[actualDir].append(('dir', join_path(actualDir, dirFound), 0))
            else:
                size, fileName = line.split()
                dirContents[actualDir].append(('file', join_path(actualDir, fileName), size))

    outermostDirectorySize = get_dir_size('/', dirContents)
    spaceFree = totalDiskSpace - outermostDirectorySize

    sizeToDeleteToMakeUpdate = spaceNeedForUpdate - spaceFree

    dirsWithSizeOverSizeToDelete = [(dir, get_dir_size(dir, dirContents)) for dir in dirContents if
                                    get_dir_size(dir, dirContents) >= sizeToDeleteToMakeUpdate]

    dirsThatCanBeDeletedSortBySize = sorted(dirsWithSizeOverSizeToDelete, key=lambda dirWithSize: dirWithSize[1])
    print(dirsThatCanBeDeletedSortBySize[0])
