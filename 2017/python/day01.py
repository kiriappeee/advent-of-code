def solve_captcha(captcha_string):
    length_of_captcha_string = len(captcha_string)
    values_to_add=[]
    i = 0
    while i<len(captcha_string):
        if i==(len(captcha_string)-1):
            current_value = captcha_string[i]
            next_value = captcha_string[0]
        else:
            current_value = captcha_string[i]
            next_value = captcha_string[i+1]
        if current_value == next_value:
            values_to_add.append(int(current_value))
        i+=1
    return sum(values_to_add)

def solve_captcha_part_two(captcha_string):
    halfway_length = len(captcha_string)//2
    input_length = len(captcha_string)
    values_to_add = []
    i = 0
    while i<input_length:
        current_value = captcha_string[i]
        if i+halfway_length>=input_length:
            next_value = captcha_string[i + halfway_length - input_length]
        else:
            next_value = captcha_string[i + halfway_length]
        if current_value == next_value:
            values_to_add.append(int(current_value))
        i+=1
    return sum(values_to_add)

def solve_challenge_part_1():
    puzzle_input_file = open('python/day1part1input.txt', 'r')
    puzzle_input = puzzle_input_file.read()
    print(solve_captcha(puzzle_input.strip()))

def solve_challenge_part_2():
    puzzle_input_file = open('python/day1part1input.txt', 'r')
    puzzle_input = puzzle_input_file.read()
    print(solve_captcha_part_two(puzzle_input.strip()))

if __name__ == "__main__":
    print("=== Part 1 ===")
    solve_challenge_part_1()
    print("=== Part 2 ===")
    solve_challenge_part_2()