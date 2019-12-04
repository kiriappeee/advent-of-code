import re

def isStringNicePartOne(stringToEvaluate):
    if len(re.findall(r'[aeiou]', stringToEvaluate)) < 3:
        return False
    if len(re.findall(r'([a-z])\1', stringToEvaluate)) == 0:
        return False
    if len(re.findall(r'(ab|cd|pq|xy)', stringToEvaluate)) > 0:
        return False
    return True

def isStringNicePartTwo(stringToEvaluate):
    if len(re.findall(r'([a-z][a-z])[a-z]{0,}\1', stringToEvaluate)) == 0:
        return False
    if len(re.findall(r'([a-z])[a-z]\1', stringToEvaluate)) == 0:
        return False
    return True

def runPartOne():
    f = open('python/day5inputpart1', 'r')
    lines = f.readlines()
    niceCount = 0
    for line in lines:
        if isStringNicePartOne(line):
            niceCount += 1
    print(niceCount)

def runPartTwo():
    f = open('python/day5inputpart1', 'r')
    lines = f.readlines()
    niceCount = 0
    for line in lines:
        if isStringNicePartTwo(line):
            niceCount += 1
    print(niceCount)

if __name__ == "__main__":
    runPartOne()
    runPartTwo()
