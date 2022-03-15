import sys
from turtle import position


def get_gamma_and_epilson_rate_for_pos(diagnostics, position):
    zeros = [int(x[position]) for x in diagnostics if int(x[position]) == 0]
    ones = [int(x[position]) for x in diagnostics if int(x[position]) == 1]
    if len(zeros) > len(ones):
        return 0, 1
    else:
        return 1, 0


def get_power_value_from_diagnostics(diagnostics):
    position = 0
    gamma_value = ""
    epilson_value = ""
    while position < len(diagnostics[0]):
        gamma_value_to_add, epilson_value_to_add = get_gamma_and_epilson_rate_for_pos(diagnostics, position)
        gamma_value += str(gamma_value_to_add)
        epilson_value += str(epilson_value_to_add)
        position += 1
    return int(gamma_value, 2) * int(epilson_value, 2)

def get_o2_rating_list_for_pos(diagnostics, position):
    gamma_rating = str(get_gamma_and_epilson_rate_for_pos(diagnostics, position)[0])
    o2_rating_list = []
    for diagnostic in diagnostics:
        if diagnostic[position] == gamma_rating:
            o2_rating_list.append(diagnostic)
    return o2_rating_list

def get_co2_rating_list_for_pos(diagnostics, position):
    epilson_rating = str(get_gamma_and_epilson_rate_for_pos(diagnostics, position)[1])
    co2_rating_list = []
    for diagnostic in diagnostics:
        if diagnostic[position] == epilson_rating:
            co2_rating_list.append(diagnostic)
    return co2_rating_list

def get_life_rating(diagnostics):
    o2_rating_list = diagnostics
    position = 0
    while len(o2_rating_list)>1:
        o2_rating_list = get_o2_rating_list_for_pos(o2_rating_list, position)
        position += 1
    co2_rating_list = diagnostics
    position = 0
    while len(co2_rating_list)>1:
        co2_rating_list = get_co2_rating_list_for_pos(co2_rating_list, position)
        position += 1
    return int(o2_rating_list[0], 2) * int(co2_rating_list[0], 2)

if __name__ == "__main__":
    args = sys.argv
    with open("python/inputday03.txt", "r") as f:
        puzzle_input = [x.strip() for x in f.readlines() if x.strip() != ""]
    if args[1] == "1":
        print(get_power_value_from_diagnostics(puzzle_input))
    elif args[1] == "2":
        print(get_life_rating(puzzle_input))