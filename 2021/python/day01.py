import sys

def count_measurement_increase(measurement_list):
    count = 0
    last_measurement = measurement_list[0]
    for measurement in measurement_list[1:]:
        if measurement > last_measurement:
            count += 1
        last_measurement = measurement
    return count


def break_into_window_sums(measurement_list):
    index = 0
    window_list = []
    while index < len(measurement_list)-2:
        window_list.append(sum(measurement_list[index:index+3]))
        index += 1
    return window_list

def count_measurement_increase_by_windows(measurement_list):
    measurement_windws = break_into_window_sums(measurement_list)
    return count_measurement_increase(measurement_windws)

if __name__ == "__main__":
    args = sys.argv
    with open('python/inputday01.txt') as f:
        puzzle_input = [int(x) for x in f.readlines() if x.strip() != ""]

    print(len(puzzle_input))
    if args[1] == "1":
        print(count_measurement_increase(puzzle_input))
    elif args[1] == "2":
        print(count_measurement_increase_by_windows(puzzle_input))

