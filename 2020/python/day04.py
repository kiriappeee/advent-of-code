import sys
import re

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

def validate_birth_year(birth_year_string):
  birth_year = int(birth_year_string.split(':')[1])
  return birth_year >= 1920 and birth_year <= 2002 and len(birth_year_string.split(":")[1]) == 4

def validate_issue_year(issue_year_string):
  issue_year = int(issue_year_string.split(':')[1])
  return issue_year >= 2010 and issue_year <= 2020 and len(issue_year_string.split(":")[1]) == 4

def validate_expiry_year(expiry_year_string):
  expiry_year = int(expiry_year_string.split(':')[1])
  return expiry_year >= 2020 and expiry_year <= 2030 and len(expiry_year_string.split(":")[1]) == 4

def validate_height(height_string):
  height_string = height_string.replace('hgt:', '')
  if re.search('^\d{3}cm$|\d{2}in$', height_string):
    if height_string.endswith('cm'):
      height = int(height_string[:3])
      return height >=150 and height <= 193
    else:
      height = int(height_string[:2])
      return height >= 59 and height <= 76
  else:
    return False

def validate_hair_colour(hair_colour_string):
  hair_colour = hair_colour_string.replace("hcl:", "")
  return re.search('^#[0-9a-f]{6}$', hair_colour) is not None

def validate_eye_colour(eye_colour_string):
  eye_colour = eye_colour_string.replace("ecl:", "")
  return re.search('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', eye_colour) is not None

def validate_passport_id(passport_id_string):
  passport_id = passport_id_string.replace("pid:", "")
  return re.search('^[0-9]{9}$', passport_id) is not None

def passport_is_valid_with_new_rules(passport_string_to_test):
  if not passport_is_valid(passport_string_to_test):
    return False
  
  passport_variables = passport_string_to_test.split(" ")
  for pv in passport_variables:
    
    if pv.startswith('byr') and not validate_birth_year(pv):
      print(f'Invalidated byr {pv} for {passport_string_to_test}')
      return False
    elif pv.startswith('iyr') and not validate_issue_year(pv):
      print(f'Invalidated iyr {pv} for {passport_string_to_test}')
      return False
    elif pv.startswith('eyr') and not validate_expiry_year(pv):
      print(f'Invalidated eyr {pv} for {passport_string_to_test}')
      return False
    elif pv.startswith('hgt') and not validate_height(pv):
      print(f'Invalidated hgt {pv} for {passport_string_to_test}')
      return False
    elif pv.startswith('ecl') and not validate_eye_colour(pv):
      print(f'Invalidated ecl {pv} for {passport_string_to_test}')
      return False
    elif pv.startswith('hcl') and not validate_hair_colour(pv):
      print(f'Invalidated hcl {pv} for {passport_string_to_test}')
      return False
    elif pv.startswith('pid') and not validate_passport_id(pv):
      print(f'Invalidated pid {pv} for {passport_string_to_test}')
      return False
  return True
    


if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday04.txt') as f:
    passport_batch_string = f.read()
  
  count = 0
  passport_list = break_input_into_individual_passports(passport_batch_string)
  if args[1] == "1":
    for passport_string in passport_list:
      if passport_is_valid(passport_string):
        count+=1
    print(count)
  elif args[1] == "2":
    for passport_string in passport_list:
      if passport_is_valid_with_new_rules(passport_string):
        count+=1
    print(count)
