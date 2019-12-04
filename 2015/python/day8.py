import re

def numberOfCharacters(inputString):
    mainString = inputString[1:-1]
    i = 0
    numberOfQuotedCharacters = 0
    numberOfBackSlashes = 0
    numberOfHexCharacters = 0
    while i < len(mainString):
        if mainString[i] == '\\':
            if mainString[i+1] == '"':
                numberOfQuotedCharacters += 1
                i+=1
            elif mainString[i+1] == '\\':
                numberOfBackSlashes += 1
                i+=1
            elif re.search(r'\\x[0-9a-z][0-9a-z]',mainString[i:i+4]):
                numberOfHexCharacters += 1
                i+=3
        i+=1
    return len(mainString) - numberOfQuotedCharacters - numberOfBackSlashes - (numberOfHexCharacters*3)

def encode(inputString):
    mainString = inputString[1:-1]
    newString = '\\"'
    i = 0
    while i < len(mainString):
        if mainString[i] == '\\':
            newString += '\\\\'
        elif mainString[i] == '"':
            newString += '\\"'
        else:
            newString += mainString[i]
        i+=1
    newString += '\\"'
    return newString
def numberOfCharactersOfCode(inputString):
    return len(inputString)

def runPartOne():
    f = open('python/day8input', 'r')
    lines = f.readlines()
    totalNumberOfCharacters = 0
    totalNumberOfCharactersInCode = 0
    for line in lines[:]:
        totalNumberOfCharactersInCode += numberOfCharactersOfCode(line.strip('\n'))
        totalNumberOfCharacters += numberOfCharacters(line.strip('\n'))
    print("Total number of characters:", totalNumberOfCharacters)
    print("Total number of characters in code:", totalNumberOfCharactersInCode)
    print("Difference:", totalNumberOfCharactersInCode - totalNumberOfCharacters)
    f.close()
def runPartTwo():
    f = open('python/day8input', 'r')
    lines = f.readlines()
    totalNumberOfCharacters = 0
    totalNumberOfCharactersInCode = 0
    for line in lines[:]:
        totalNumberOfCharactersInCode += numberOfCharactersOfCode(line.strip('\n'))
        totalNumberOfCharacters += len(encode(line.strip('\n'))) + 2
    print("Total number of characters:", totalNumberOfCharacters)
    print("Total number of characters in code:", totalNumberOfCharactersInCode)
    print("Difference:", totalNumberOfCharacters - totalNumberOfCharactersInCode )
    f.close()

if __name__ == "__main__":
    runPartOne()
    runPartTwo()
