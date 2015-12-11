from hashlib import md5

def makeHash(input, validHashTest):
    i = 0
    while True:
        hash = md5((input + str(i)).encode('utf-8')).hexdigest()
        if validHashTest(hash):
            return i, hash
        i += 1

def isHashValidPartOne(hash):
    return hash.startswith('00000')

def isHashValidPartTwo(hash):
    return hash.startswith('000000')

def runPartOne():
    input = 'ckczppom'
    print(makeHash(input, isHashValidPartOne))
def runPartTwo():
    input = 'ckczppom'
    print(makeHash(input, isHashValidPartTwo))

if __name__ == "__main__":
    runPartOne()
    runPartTwo()
