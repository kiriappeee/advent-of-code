def lookAndSay(input):
    output = ''
    counter = 0
    currentNum = input[0]
    for num in input:
        if currentNum != num:
            output += str(counter) + str(currentNum)
            counter = 1
            currentNum = num
        else:
            counter += 1
    output += str(counter) + str(currentNum)
    return output

def runPartOne():
    initString = '3113322113'
    for i in range(0, 40):
        initString = lookAndSay(initString)
    print(len(initString))

def runPartTwo():
    initString = '3113322113'
    for i in range(0, 50):
        initString = lookAndSay(initString)
    print(len(initString))


if __name__ == "__main__":
    runPartOne()
    runPartTwo()
