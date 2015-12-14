import re

def generateNextPassword(currentPassword):
    newPassword = currentPassword
    characterToIncrement = newPassword[-1]
    if re.search('[iol]', newPassword):
        indexOfOffender = min(newPassword.find('i'),newPassword.find('o'),newPassword.find('l'), key=keyFunc)
        characterToIncrement = newPassword[indexOfOffender]
        newPassword = newPassword[:indexOfOffender] + chr(ord(characterToIncrement)+1) +'a'*(8-indexOfOffender-1)
        return newPassword
    if characterToIncrement == 'z':
        newPassword = generateNextPassword(newPassword[:-1])+'a'
    else:
        newPassword = newPassword[:-1] + chr(ord(characterToIncrement)+1)
    return newPassword

def keyFunc(value):
    if value == -1:
        return 9
    else:
        return value
def isPasswordValid(password):
    if re.search('[iol]', password):
        return False
    if not len(re.findall(r'([a-z])\1', password))>1:
        return False
    else:
        matches = re.findall(r'([a-z])\1', password) 
        uniqueMatchList = []
        for match in matches:
            if match not in uniqueMatchList:
                uniqueMatchList.append(match)
        if len(uniqueMatchList) == 1:
            return False
    if not re.findall(r'(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password):
        return False
    return True

def generateNewPassword(oldPassword):
    password = generateNextPassword(oldPassword)
    while not isPasswordValid(password):
        password = generateNextPassword(password)
        print(password)
    return password

def runPartOne():
    input = 'cqjxjnds'
    print(generateNewPassword(input))

def runPartTwo():
    input = 'cqjxjnds'
    newPassword = generateNewPassword(input)
    print(generateNewPassword(newPassword))
if __name__ == "__main__":
    runPartOne()
    runPartTwo()
