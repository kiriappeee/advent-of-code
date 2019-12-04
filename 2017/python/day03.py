def getCoordinatesForNumber(number_to_get_coordinates_for):
    current_coordinates = (0,0)
    current_number = 1
    current_ring_counter = 0
    current_direction = 'right'
    spiral_corners = get_spiral_corners_for_given_ring(ring_counter=current_ring_counter)
    while current_number < number_to_get_coordinates_for:
        if current_coordinates == spiral_corners['bottom_right']:
            current_ring_counter += 1
            spiral_corners = get_spiral_corners_for_given_ring(ring_counter=current_ring_counter)
        elif current_coordinates == spiral_corners['starting_position']:
            current_direction = "up"
        elif current_coordinates == spiral_corners['top_right']:
            current_direction = "left"
        elif current_coordinates == spiral_corners['top_left']:
            current_direction = "down"
        elif current_coordinates == spiral_corners['bottom_left']:
            current_direction = "right"
        if current_direction == "up":
            current_coordinates = (current_coordinates[0], current_coordinates[1]+1)
        elif current_direction == "right":
            current_coordinates = (current_coordinates[0]+1, current_coordinates[1])
        elif current_direction == "left":
            current_coordinates = (current_coordinates[0]-1, current_coordinates[1])
        elif current_direction == "down":
            current_coordinates = (current_coordinates[0], current_coordinates[1]-1)
        current_number += 1
    return current_coordinates

def get_spiral_corners_for_given_ring(ring_counter=0):
    return {
        'starting_position': (ring_counter, (ring_counter-1)*-1) if ring_counter > 0 else (0,0),
        'top_right': (ring_counter, ring_counter),
        'top_left': (ring_counter*-1, ring_counter),
        'bottom_left': (ring_counter*-1, ring_counter*-1),
        'bottom_right': (ring_counter, ring_counter*-1),
    }

def get_manhattan_distance_for_given_number(number):
    coordinates = getCoordinatesForNumber(number)
    return abs(coordinates[0]) + abs(coordinates[1])

def get_adjacent_square_coordinates(coordinate):
    return [
        (coordinate[0]-1, coordinate[1]),
        (coordinate[0]-1, coordinate[1]+1),
        (coordinate[0], coordinate[1]+1),
        (coordinate[0]+1, coordinate[1]+1),
        (coordinate[0]+1, coordinate[1]),
        (coordinate[0]+1, coordinate[1]-1),
        (coordinate[0], coordinate[1]-1),
        (coordinate[0]-1, coordinate[1]-1),
    ]

def generate_ring(count=-1, number_check=-1):
    current_coordinates = (0,0)
    current_number = 1
    current_ring_counter = 0
    current_direction = 'right'
    spiral_corners = get_spiral_corners_for_given_ring(ring_counter=current_ring_counter)
    current_ring = {}
    while True: 
        adjacent_squares = get_adjacent_square_coordinates(current_coordinates)
        number_to_insert = sum([current_ring[C] for C in adjacent_squares if C in current_ring]) or 1
        current_ring[current_coordinates] = number_to_insert
        if count == current_number:
            break
        if number_to_insert > number_check and number_check != -1:
            break
        if current_coordinates == spiral_corners['bottom_right']:
            current_ring_counter += 1
            spiral_corners = get_spiral_corners_for_given_ring(ring_counter=current_ring_counter)
        elif current_coordinates == spiral_corners['starting_position']:
            current_direction = "up"
        elif current_coordinates == spiral_corners['top_right']:
            current_direction = "left"
        elif current_coordinates == spiral_corners['top_left']:
            current_direction = "down"
        elif current_coordinates == spiral_corners['bottom_left']:
            current_direction = "right"
        if current_direction == "up":
            current_coordinates = (current_coordinates[0], current_coordinates[1]+1)
        elif current_direction == "right":
            current_coordinates = (current_coordinates[0]+1, current_coordinates[1])
        elif current_direction == "left":
            current_coordinates = (current_coordinates[0]-1, current_coordinates[1])
        elif current_direction == "down":
            current_coordinates = (current_coordinates[0], current_coordinates[1]-1)
        current_number += 1
    return current_ring, current_coordinates
def get_input():
    return int(open('python/inputday03.txt', 'r').readlines()[0])

def run_part_one():
    input_number = get_input()
    return get_manhattan_distance_for_given_number(input_number)

def run_part_two():
    generated_ring, current_coordinates = generate_ring(number_check=get_input())
    return generated_ring[current_coordinates]

if __name__ == "__main__":
    print("== DAY 3 - PART ONE ==")
    print(run_part_one())
    print("== DAY 3 - PART TWO ==")
    print(run_part_two())
