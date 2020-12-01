#PART 1
def calculateArea(length,width,height):
    return (2*length*width) + (2*width*height) + (2*length*height)

def calculateSlack(length, width, height):
    return min(length*width,width*height,length*height)

def parseLine(line):
    inputs = [int(s) for s in line.split('x')]
    return inputs[0], inputs[1], inputs[2]

def getTotalWrappingRequired(lineInfo):
    length,width,height = parseLine(lineInfo)
    totalRequired = calculateArea(length,width,height) + calculateSlack(length,width,height)
    return totalRequired

def runPartOne():
    f = open('python/day2inputpart1', 'r')
    lines = f.readlines()
    totalWrappingRequired = 0
    for line in lines:
        totalWrappingRequired += getTotalWrappingRequired(line)
    print(totalWrappingRequired)
    f.close()

#PART 2
def calculateSmallestPerimeter(length,width,height):
    sides = [length,width,height]
    smallestSideA = min(sides)
    sides.remove(smallestSideA)
    smallestSideB = min(sides)
    return (2*smallestSideA) + (2*smallestSideB)

def calculateCubicFeet(length,width,height):
    return length * width * height

def getTotalRibbonRequired(lineInfo):
    length,width,height = parseLine(lineInfo)
    return calculateSmallestPerimeter(length,width,height) + calculateCubicFeet(length,width,height)
    
def runPartTwo():
    f = open('python/day2inputpart1', 'r')
    lines = f.readlines()
    totalRibbonRequired = 0
    for line in lines:
        totalRibbonRequired += getTotalRibbonRequired(line)
    print(totalRibbonRequired)
    f.close()
