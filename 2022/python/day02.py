import sys

SCORES = {
  "X":{
    "beats": "C",
    "draws": "A",
    "score": 1
  },
  "Y":{
    "beats": "A",
    "draws": "B",
    "score": 2
  },
  "Z":{
    "beats": "B",
    "draws": "C",
    "score": 3
  }
}

RESPONSES = {
  "A":{
    "beats": "C",
    "loses": "B",
    "score": 1
  },
  "B":{
    "beats": "A",
    "loses": "C",
    "score": 2
  },
  "C":{
    "beats": "B",
    "loses": "A",
    "score": 3
  }
}

def get_round_result(round_details):
  if SCORES[round_details[1]]["beats"] == round_details[0]:
    return SCORES[round_details[1]]["score"] + 6
  elif SCORES[round_details[1]]["draws"] == round_details[0]:
    return SCORES[round_details[1]]["score"] + 3
  else:
    return SCORES[round_details[1]]["score"] + 0

def get_response(round_instructions):
  if round_instructions[1] == "X": #lose
    return RESPONSES[round_instructions[0]]["beats"]
  elif round_instructions[1] == "Y": #draw
    return round_instructions[0]
  elif round_instructions[1] == "Z": #win
    return RESPONSES[round_instructions[0]]["loses"]

def solve_part_one(puzzle_input):
  scores = []
  for round in puzzle_input:
    scores.append(get_round_result(round))
  print(sum(scores))
  return(sum(scores))

def solve_part_two(puzzle_input):
  calibaration = {"A": "X", "B": "Y", "C": "Z"}
  score = 0
  for round in puzzle_input:
    correct_response = get_response(round)
    calibarated_response = calibaration[correct_response]  # type: ignore
    score += get_round_result((round[0], calibarated_response))
  print(score)
  return score

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday02.txt") as f:
    puzzle_input = [(x.strip().split(" ")[0], x.strip().split(" ")[1]) for x in f.readlines() if x.strip() != ""]
  if args[1] == "1":
    solve_part_one(puzzle_input)
  elif args[1] == "2":
    solve_part_two(puzzle_input)
  else:
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
