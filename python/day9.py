import re

distances = {}
def addDistance(instruction):
    global distances
    instructionBreakDown = re.findall(r'\w+', instruction)
    cityA, cityB, distance = instructionBreakDown[0], instructionBreakDown[2], int(instructionBreakDown[3])
    if cityA not in distances.keys():
        distances[cityA] = {cityB: distance}
    else:
        distances[cityA][cityB] = distance
    if cityB not in distances.keys():
        distances[cityB] = {cityA: distance}
    else:
        distances[cityB][cityA] = distance

def getShortestPath():
    global distances
    paths = {}
    pathDistances = {}
    for location in distances.keys():
        paths[location]=getShortestTravelPathAcrossAllLocations(location)
        pathDistances[location] = getDistanceForPath(paths[location])

    shortestDistanceStartLocation = min(pathDistances, key = pathDistances.get)
    return paths[shortestDistanceStartLocation]

def getDistanceForPath(path):
    global distance
    distance = 0
    i = 0
    while i < len(path) - 1:
        startPoint = path[i]
        endPoint = path[i+1]
        distance+=distances[startPoint][endPoint]
        i+=1
    return distance

def getShortestTravelPathAcrossAllLocations(location, visited = None):
    global distances
    if visited is None:
        visited = [location]
    valuesToCheck = {key: distances[location][key] for key in distances.keys() if key not in visited}
    if valuesToCheck:
        shortestDistanceToNextLocation = min(valuesToCheck, key=valuesToCheck.get) 
        visited.append(shortestDistanceToNextLocation)
        return getShortestTravelPathAcrossAllLocations(shortestDistanceToNextLocation, visited)
    else:
        return visited

def getLongestPath():
    global distances
    paths = {}
    pathDistances = {}
    for location in distances.keys():
        paths[location]=getLongestTravelPathAcrossAllLocations(location)
        pathDistances[location] = getDistanceForPath(paths[location])

    shortestDistanceStartLocation = max(pathDistances, key = pathDistances.get)
    return paths[shortestDistanceStartLocation]

def getLongestTravelPathAcrossAllLocations(location, visited = None):
    global distances
    if visited is None:
        visited = [location]
    valuesToCheck = {key: distances[location][key] for key in distances.keys() if key not in visited}
    if valuesToCheck:
        longestDistanceToNextLocation = max(valuesToCheck, key=valuesToCheck.get) 
        visited.append(longestDistanceToNextLocation)
        return getLongestTravelPathAcrossAllLocations(longestDistanceToNextLocation, visited)
    else:
        return visited
def runPartOne():
    print(getShortestPath())
    print(getDistanceForPath(getShortestPath()))

def runPartTwo():
    print(getLongestPath())
    print(getDistanceForPath(getLongestPath()))

if __name__ == "__main__":
    global distances
    f = open('python/day9input', 'r')
    lines = f.readlines()
    for line in lines:
        addDistance(line.strip('\n'))
    f.close()
    runPartOne()
    runPartTwo()
