import unittest
from . import day07

class TestDay7(unittest.TestCase):
    def test_thruster_output_is_obtained(self):
        program_to_execute = [int(c) for c in '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'.split(',')]
        phase_setting_sequence = [int (c) for c in '4,3,2,1,0'.split(',')]
        self.assertEqual(day07.get_thruster_signal([program_to_execute]*5, phase_setting_sequence), 43210)
        program_to_execute = [int(c) for c in '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'.split(',')]
        phase_setting_sequence = [int (c) for c in '0,1,2,3,4'.split(',')]
        self.assertEqual(day07.get_thruster_signal([program_to_execute]*5, phase_setting_sequence), 54321)
    

    def test_max_thruster_signal_can_be_found(self):
        program_to_execute = [int(c) for c in '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'.split(',')]
        self.assertEqual(day07.find_max_signal(program_to_execute), 43210)
        program_to_execute = [int(c) for c in '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'.split(',')]
        self.assertEqual(day07.find_max_signal(program_to_execute), 54321)


    def thruster_output_is_obtained_in_feedback_loop_mode(self):
        amplifier_program = [ int(c) for c in '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')]
        phase_setting_sequence = [int(c) for c in '9,8,7,6,5'.split(',')]
        self.assertEqual(day07.get_thruster_signal([amplifier_program]*5, phase_setting_sequence, with_feedback_loop=True), 139629729)
    
    def test_amplifier_feedback_loop_program(self):
        amplifier_program = [ int(c) for c in '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')]
        self.assertEqual(day07.find_max_signal(amplifier_program, with_feedback_loop=True), 139629729)
if __name__ == "__main__":
    unittest.main()