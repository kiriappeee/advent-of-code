import re
import itertools
from . import computer

def get_input():
    return [int(c) for c in open('python/inputday07.txt', 'r').read().strip().split(',')]

def get_thruster_signal(amplifier_programs, phase_setting_sequence, with_feedback_loop=False):
    count = 0
    if not with_feedback_loop:
        val = [0]
        for amplifier_program in amplifier_programs:
            _, val, _ = computer.run_program(amplifier_program.copy(), list_of_inputs=[phase_setting_sequence[count], val[0]])
            count += 1
        return val[0]
    else:
        starting_pointers = [0]*5
        val = [0]
        completed = False
        total_loops = 0
        for amplifier_program in amplifier_programs:
            program_being_executed, outputs, instruction_pointer = computer.run_program(amplifier_program, list_of_inputs=[phase_setting_sequence[count]], starting_pointer=starting_pointers[count], end_on_manual_read = True)
            if instruction_pointer is not None:
                starting_pointers[count] = instruction_pointer
            count += 1
        count = 0
        while not completed and total_loops < 2:
            count = 0
            for amplifier_program in amplifier_programs:
                program_being_executed, outputs, instruction_pointer = computer.run_program(amplifier_program, list_of_inputs=[val[-1]], starting_pointer=starting_pointers[count], end_on_manual_read = True)
                print(outputs)
                val = outputs.copy()
                print(instruction_pointer)
                if instruction_pointer is not None:
                    starting_pointers[count] = instruction_pointer
                else:
                    if not count == len(amplifier_programs) - 1:
                        starting_pointers[count] = -1
                    else:
                        return val[-1]
                #print(starting_pointers)
                
                count += 1
            if starting_pointers == [-1,-1,-1,-1,0]:
                completed = True
            total_loops+=1
            print('====')
        return val[-1]    

def find_max_signal(program_to_execute, with_feedback_loop = False):
    checked_values = []
    if not with_feedback_loop:
        combinations = list(itertools.permutations('12340', 5))
    else:
        combinations = list(itertools.permutations('56789', 5))
    amplifier_programs = [program_to_execute.copy()]*5
    # combinations = ['0' * (5-len(str(c)))+str(c) for c in range(0, 44445) if not re.search('[5-9]', str(c))]
    for combination in combinations:
        checked_values.append(get_thruster_signal(amplifier_programs, [int(n) for n in combination], with_feedback_loop=with_feedback_loop))
    return max(checked_values)
def run_part_one():
    puzzle_input = get_input()
    return find_max_signal(puzzle_input)

def run_part_two():
    puzzle_input = get_input()
    return find_max_signal(puzzle_input, with_feedback_loop=True)

if __name__ == "__main__":
    print("== DAY 7 PART 1 ==")
    print(run_part_one())
    print("== DAY 7 PART 2 ==")
    print(run_part_two())