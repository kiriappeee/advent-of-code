def howManyHouses(inputString):
    uniqueHouseCount = 1
    row = 0
    column = 0
    movedList = [(0,0)]
    for input in inputString:
        row, column = move(input, row, column)
        if (row, column) not in movedList:
            movedList.append((row,column))
            uniqueHouseCount += 1
    return uniqueHouseCount

def move(input, row, column):
    if input == '>':
        return (row, column + 1)
    if input == '<':
        return (row, column - 1)
    if input == '^':
        return (row - 1, column)
    if input == 'v':
        return (row + 1, column)

def howManyHousesWithRoboSanta(inputString):
    uniqueHouseCount = 1
    santaRow = 0
    santaColumn = 0
    roboRow = 0
    roboColumn = 0
    santaMoving = True
    movedList = [(0,0)]
    for input in inputString:
        if santaMoving:
            santaRow, santaColumn = move(input, santaRow, santaColumn)
            movedPosition = (santaRow, santaColumn)
            santaMoving = False
        else:
            roboRow, roboColumn = move(input, roboRow, roboColumn)
            movedPosition = (roboRow, roboColumn)
            santaMoving = True

        if movedPosition not in movedList:
            movedList.append(movedPosition)
            uniqueHouseCount += 1
    return uniqueHouseCount
def runPartOne():
    f = open('python/day3input', 'r')
    inputString = f.read().strip()
    print(howManyHouses(inputString))
    f.close()

def runPartTwo():
    f = open('python/day3input', 'r')
    inputString = f.read().strip()
    print(howManyHousesWithRoboSanta(inputString))
    f.close()
if __name__ == "__main__":
    runPartOne()
    runPartTwo()
