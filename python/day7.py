import struct
import re

circuit = {}
def parseInstruction(instruction):
    instructionBreakDown = dict()
    if re.search(r'AND|OR', instruction):
        result = re.findall(r'(\w+|\d+) (AND|OR) (\w+) -> (\w+)', instruction)[0]
        instructionBreakDown['inputs'] = [result[0], result[2]]
        instructionBreakDown['output'] = result[3]
        instructionBreakDown['operator'] = result[1]
    elif re.search(r'NOT', instruction):
        result = re.findall(r'(NOT) (\w+) -> (\w+)', instruction)[0]
        instructionBreakDown['inputs'] = [result[1]]
        instructionBreakDown['output'] = result[2]
        instructionBreakDown['operator'] = result[0]
    elif re.search(r'(RSHIFT|LSHIFT)', instruction):
        result = re.findall(r'(\w+|\d+) (RSHIFT|LSHIFT) (\d+) -> (\w+)', instruction)[0]
        instructionBreakDown['inputs'] = [result[0]]
        instructionBreakDown['output'] = result[3]
        instructionBreakDown['operator'] = result[1]
        instructionBreakDown['shift'] = int(result[2])
    elif re.search(r'^\w+|\d+ ->', instruction):
        result = re.findall(r'^(\w+|\d+) -> (\w+)', instruction)[0]
        instructionBreakDown['inputs'] = [result[0]]
        instructionBreakDown['output'] = result[1]
        instructionBreakDown['operator'] = ''

    return instructionBreakDown

def execute(instruction):
    global circuit
    instructionBreakDown = parseInstruction(instruction)
    if instructionBreakDown['operator'] == '':
        inputs = instructionBreakDown['inputs']
        output = instructionBreakDown ['output']
        inputs[0] = addInputToCircuit(inputs[0], output)
        addOutputToCircuit(output, inputs[0], None)

    elif instructionBreakDown['operator'] == 'AND' or instructionBreakDown['operator'] == 'OR':
        output = instructionBreakDown ['output']
        inputs = instructionBreakDown['inputs']
        inputs[0] = addInputToCircuit(inputs[0], output)
        inputs[1] = addInputToCircuit(inputs[1], output)
        addOutputToCircuit(output, inputs, instructionBreakDown['operator'])
    elif instructionBreakDown['operator'] == 'NOT':
        output = instructionBreakDown ['output']
        inputs = instructionBreakDown['inputs']
        inputs[0] = addInputToCircuit(inputs[0], output)
        addOutputToCircuit(output, inputs, instructionBreakDown['operator'])
    elif instructionBreakDown['operator'] == 'RSHIFT' or instructionBreakDown['operator'] == 'LSHIFT':
        output = instructionBreakDown ['output']
        inputs = instructionBreakDown['inputs']
        inputs[0] = addInputToCircuit(inputs[0], output)
        addOutputToCircuit(output, inputs, instructionBreakDown['operator'], shift=instructionBreakDown['shift'])


def addInputToCircuit(input, output):
    global circuit
    if input.isdigit():
        input = int(input)
    else:
        if input not in circuit.keys():
            circuit[input] = {'inputs': [], 'operator': None, 'connected': [output]}
        else:
            circuit[input]['connected'].append(output)
    return input

def addOutputToCircuit(output, inputs, operator, shift=None):
    global circuit
    if output not in circuit.keys():
        circuit[output] = {'inputs': inputs,
                'operator': operator, 'connected': []}
    else:
        circuit[output]['inputs'] = inputs
        circuit[output]['operator'] = operator
    if shift:
        circuit[output]['shift'] = shift

def getCircuit():
    global circuit
    return circuit

calculatedValues = {}
def getNodeValue(node):
    global calculatedValues
    global circuit
    nodeItem = circuit.get(node)
    if type(node) is int:
        return node
    if node in calculatedValues.keys():
        return calculatedValues[node]
    if nodeItem['operator'] is None:
        if type(nodeItem['inputs']) is int:
            return nodeItem['inputs']
        else:
            return getNodeValue(nodeItem['inputs'])
    if nodeItem['operator'] == 'AND':
        value = getNodeValue(nodeItem['inputs'][0]) & getNodeValue(nodeItem['inputs'][1])
    if nodeItem['operator'] == 'OR':
        value = getNodeValue(nodeItem['inputs'][0]) | getNodeValue(nodeItem['inputs'][1])
    if nodeItem['operator'] == 'LSHIFT':
        value = getNodeValue(nodeItem['inputs'][0]) << nodeItem['shift']
    if nodeItem['operator'] == 'RSHIFT':
        value = getNodeValue(nodeItem['inputs'][0]) >> nodeItem['shift']
    if nodeItem['operator'] == 'NOT':
        value = struct.unpack('H', struct.pack('h', ~getNodeValue(nodeItem['inputs'][0])))[0]
    calculatedValues[node] = value
    return value

def runPartOne():
    f = open('python/day7input', 'r')
    instructions = f.readlines()
    for instruction in instructions:
        execute(instruction)
    print(getNodeValue('a'))

def runPartTwo():
    global calculatedValues
    f = open('python/day7input', 'r')
    instructions = f.readlines()
    for instruction in instructions:
        execute(instruction)
    valueOfA = getNodeValue('a')
    calculatedValues = {}
    calculatedValues['b'] = valueOfA
    print(getNodeValue('a'))

if __name__ == "__main__":
    runPartOne()
    runPartTwo()
