import sys

def get_row(row_input):
  current_row_area = [0,127]
  for step in row_input:
    if step == 'F':
      current_row_area = [current_row_area[0], sum(current_row_area)//2]
    else:
      current_row_area = [sum(current_row_area)//2+1, current_row_area[1]]
  return current_row_area[0]

def get_column(column_input):
  current_column_area = [0,7]
  for step in column_input:
    if step == 'L':
      current_column_area = [current_column_area[0], sum(current_column_area)//2]
    else:
      current_column_area = [sum(current_column_area)//2+1, current_column_area[1]]
  return current_column_area[0]

def get_seat_id(seat_position):
  return seat_position[0]*8 + seat_position[1]

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday05.txt') as f:
    seats = [x.strip() for x in f.readlines() if x.strip() != ""]
  if args[1] == "1":
    largest_id = 0
    for seat in seats:
      seat_row = get_row(seat[:7])
      seat_column = get_column(seat[7:])
      seat_id = get_seat_id([seat_row, seat_column])
      largest_id = max(largest_id, seat_id)
    print(largest_id)

  if args[1] == "2":
    pass
