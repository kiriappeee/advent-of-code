import re
import copy

def createBaseGrid(width, height):
    grid = []
    for i in range(0, height):
        grid.append([0]*width)
    return grid

def parseInstruction(instruction):
    a,b,c = re.findall(r'(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)', instruction)[0]
    instructionType = a
    startPoint = tuple([int(x) for x in b.split(',')])
    endPoint = tuple([int(x) for x in c.split(',')])
    return instructionType, startPoint, endPoint

def executeInstruction(instruction, grid):
    instructionType, startPoint, endPoint = parseInstruction(instruction)
    for row in range(startPoint[1],endPoint[1]+1):
        for column in range(startPoint[0],endPoint[0]+1):
            grid[row][column]
            if instructionType == "turn on":
                grid[row][column] = 1
            if instructionType == "turn off":
                grid[row][column] = 0
            if instructionType == "toggle":
                grid[row][column] = 0 if grid[row][column] == 1 else 1
    return grid

def executeInstructionDayTwo(instruction, grid):
    instructionType, startPoint, endPoint = parseInstruction(instruction)
    for row in range(startPoint[1],endPoint[1]+1):
        for column in range(startPoint[0],endPoint[0]+1):
            grid[row][column]
            if instructionType == "turn on":
                grid[row][column] += 1
            if instructionType == "turn off":
                grid[row][column] -= 1
                if grid[row][column] < 0:
                    grid[row][column] = 0
            if instructionType == "toggle":
                grid[row][column] += 2
    return grid

def countSwitchedOnLights(grid):
    count = 0
    for row in grid:
        for column in row:
            if column == 1:
                count += 1
    return count

def calculateBrightness(grid):
    brightness = 0
    for row in grid:
        for column in row:
            brightness += column
    return brightness

def runPartOne():
    f = open('python/day6input', 'r')
    instructions = f.readlines()
    grid = createBaseGrid(1000,1000)
    count = 0
    for instruction in instructions:
        count+=1
        grid = executeInstruction(instruction, grid)
        print(count)
    print(countSwitchedOnLights(grid))
    f.close()

def runPartTwo():
    f = open('python/day6input', 'r')
    instructions = f.readlines()
    grid = createBaseGrid(1000,1000)
    count = 0
    for instruction in instructions:
        count+=1
        grid = executeInstructionDayTwo(instruction, grid)
        print(count)
    print(calculateBrightness(grid))
    f.close()
if __name__ == "__main__":
    runPartOne()
    runPartTwo()
