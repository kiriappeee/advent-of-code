import sys

valid_fields = [
  "byr",
  "iyr",
  "eyr",
  "hgt",
  "hcl",
  "ecl",
  "pid",
]

optional_fields = [
  "cid"
]

def break_input_into_individual_passports(passport_batch_string):
  passports = []
  passport_strings = passport_batch_string.split('\n')
  current_passport = ""
  for passport_string in passport_strings:
    if passport_string.strip():
      current_passport += f"{passport_string.strip()} "
    else:
      passports.append(current_passport.strip())
      current_passport = ""
  passports.append(current_passport.strip())
  return passports

def passport_is_valid(passport_string_to_test):
  for valid_field in valid_fields:
    if f"{valid_field}:" not in passport_string_to_test:
      print(f"{passport_string_to_test} is not valid. Field {valid_field} is missing")
      return False
  return True

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday04.txt') as f:
    passport_batch_string = f.read()
  if args[1] == "1":
    count = 0
    passport_list = break_input_into_individual_passports(passport_batch_string)
    print(passport_list)
    print(len(passport_list))
    
    for passport_string in passport_list:
      if passport_is_valid(passport_string):
        count+=1
      
    print(count)

  if args[1] == "2":
    pass
