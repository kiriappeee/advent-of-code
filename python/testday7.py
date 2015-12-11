import unittest
import pprint
from . import day7

class TestDay7PartOne(unittest.TestCase):
    def setUp(self):
        day7.circuit = {}
        day7.calculatedValues = {}
    def test_instructionCanBeParsed(self):
        instructionA = 'lf AND lq -> ls'
        result = day7.parseInstruction(instructionA)
        self.assertEqual(result["inputs"], ['lf', 'lq'])
        self.assertEqual(result["output"], 'ls')
        self.assertEqual(result["operator"], 'AND')

        instructionE = 'lf OR lq -> ls'
        result = day7.parseInstruction(instructionE)
        self.assertEqual(result["inputs"], ['lf', 'lq'])
        self.assertEqual(result["output"], 'ls')
        self.assertEqual(result["operator"], 'OR')

        instructionF = '1 AND cc -> cd'
        result = day7.parseInstruction(instructionF)
        self.assertEqual(result["inputs"], ['1', 'cc'])
        self.assertEqual(result["output"], 'cd')
        self.assertEqual(result["operator"], 'AND')

        instructionB = 'NOT lq -> ls'
        result = day7.parseInstruction(instructionB)
        self.assertEqual(result["inputs"], ['lq'])
        self.assertEqual(result["output"], 'ls')
        self.assertEqual(result["operator"], 'NOT')

        instructionC = '123 -> en'
        result = day7.parseInstruction(instructionC)
        self.assertEqual(result["inputs"], ['123'])
        self.assertEqual(result["output"], 'en')
        self.assertEqual(result["operator"], '')

        instructionD = 'fo RSHIFT 1 -> az'
        result = day7.parseInstruction(instructionD)
        self.assertEqual(result["inputs"], ['fo'])
        self.assertEqual(result["output"], 'az')
        self.assertEqual(result["operator"], 'RSHIFT')
        self.assertEqual(result["shift"], 1)

        instructionG = 'fo LSHIFT 22 -> az'
        result = day7.parseInstruction(instructionG)
        self.assertEqual(result["inputs"], ['fo'])
        self.assertEqual(result["output"], 'az')
        self.assertEqual(result["operator"], 'LSHIFT')
        self.assertEqual(result["shift"], 22)

    def test_basicAssignmentCreatesCircuit(self):
        instructionA = '123 -> a'
        day7.execute(instructionA)
        self.assertEqual(day7.getCircuit(), {'a': {'inputs': 123, 'operator': None, 'connected': []}})
    def test_incompleteInstructionCreatesCircuit(self):
        instructionA = '123 -> a'
        day7.execute(instructionA)
        instructionA = 'a AND b -> c'
        day7.execute(instructionA)
        self.assertEqual(day7.getCircuit(), {'a': {'inputs': 123, 'operator': None, 'connected': ['c']},
            'b': {'inputs': [], 'operator': None, 'connected': ['c']},
            'c': {'inputs': ['a', 'b'], 'operator': 'AND', 'connected': []}})

        instructionA = 'NOT d -> b'
        day7.execute(instructionA)
        self.assertEqual(day7.getCircuit(), {'a': {'inputs': 123, 'operator': None, 'connected': ['c']},
            'b': {'inputs': ['d'], 'operator': 'NOT', 'connected': ['c']},
            'c': {'inputs': ['a', 'b'], 'operator': 'AND', 'connected': []},
            'd': {'inputs': [], 'operator': None, 'connected': ['b']}})
        instructionA = 'a RSHIFT 2 -> d'
        day7.execute(instructionA)
        self.assertEqual(day7.getCircuit(), {'a': {'inputs': 123, 'operator': None, 'connected': ['c', 'd']},
            'b': {'inputs': ['d'], 'operator': 'NOT', 'connected': ['c']},
            'c': {'inputs': ['a', 'b'], 'operator': 'AND', 'connected': []},
            'd': {'inputs': ['a'], 'operator': 'RSHIFT', 'shift': 2, 'connected': ['b']}})

    def test_individualValueCanBeCalculatedWhenCircuitIsCompleted(self):
        instruction = 'x AND y -> d'
        day7.execute(instruction)
        instruction = 'x OR y -> e'
        day7.execute(instruction)
        instruction = 'x LSHIFT 2 -> f'
        day7.execute(instruction)
        instruction = 'y RSHIFT 2 -> g'
        day7.execute(instruction)
        instruction = 'NOT x -> h'
        day7.execute(instruction)
        instruction = 'NOT y -> i'
        day7.execute(instruction)
        instruction = '123 -> x'
        day7.execute(instruction)
        instruction = '456 -> y'
        day7.execute(instruction)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(day7.getCircuit())
        self.assertEqual(day7.getNodeValue('x'), 123)
        self.assertEqual(day7.getNodeValue('y'), 456)
        self.assertEqual(day7.getNodeValue('d'), 72)
        self.assertEqual(day7.getNodeValue('e'), 507)
        self.assertEqual(day7.getNodeValue('f'), 492)
        self.assertEqual(day7.getNodeValue('g'), 114)
        self.assertEqual(day7.getNodeValue('h'), 65412)
        self.assertEqual(day7.getNodeValue('i'), 65079)

    def test_recursiveCircuitIsCheckedCorrectly(self):
        instruction = 'x -> a'
        day7.execute(instruction)
        instruction = 'z AND b -> x'
        day7.execute(instruction)
        instruction = 'e AND f -> b'
        day7.execute(instruction)
        instruction = 'e OR f -> z'
        day7.execute(instruction)
        instruction = '1 -> e'
        day7.execute(instruction)
        instruction = '2 -> f'
        day7.execute(instruction)
        print(day7.getNodeValue('a'))

if __name__ == "__main__":
    unittest.main()
