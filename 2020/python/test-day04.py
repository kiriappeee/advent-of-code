import unittest
from . import day04

class TestDay04(unittest.TestCase):
  def test_passport_batch_can_be_broken_into_passports(self):
    passport_batch = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    expected_batch = [
      "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
      "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
      "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
      "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"
    ]
    result_batch = day04.break_input_into_individual_passports(passport_batch)
    self.assertEqual(result_batch, expected_batch)
  
  def test_valid_passport_can_be_recognized(self):
    test_passport = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    self.assertTrue(day04.passport_is_valid(test_passport))
    test_passport = "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
    self.assertFalse(day04.passport_is_valid(test_passport))
    test_passport = "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
    self.assertTrue(day04.passport_is_valid(test_passport))
    self.assertFalse(day04.passport_is_valid("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"))

  def test_birth_year_is_validated_correctly(self):
    self.assertTrue(day04.validate_birth_year("byr:2002"))
    self.assertTrue(day04.validate_birth_year("byr:1920"))
    self.assertTrue(day04.validate_birth_year("byr:1990"))
    self.assertTrue(day04.validate_birth_year("byr:2000"))
    self.assertFalse(day04.validate_birth_year("byr:2003"))
    self.assertFalse(day04.validate_birth_year("byr:2010"))
    self.assertFalse(day04.validate_birth_year("byr:1919"))
    self.assertFalse(day04.validate_birth_year("byr:1910"))
    self.assertFalse(day04.validate_birth_year("byr:20"))

  def test_issue_year_is_validated_correctly(self):
    self.assertTrue(day04.validate_issue_year("iyr:2010"))
    self.assertTrue(day04.validate_issue_year("iyr:2020"))
    self.assertTrue(day04.validate_issue_year("iyr:2015"))
    self.assertFalse(day04.validate_issue_year("iyr:2009"))
    self.assertFalse(day04.validate_issue_year("iyr:2021"))
    self.assertFalse(day04.validate_issue_year("iyr:2001"))
    self.assertFalse(day04.validate_issue_year("iyr:2001"))

  def test_expiry_year_is_validated_correctly(self):
    self.assertTrue(day04.validate_expiry_year("eyr:2020"))
    self.assertTrue(day04.validate_expiry_year("eyr:2030"))
    self.assertTrue(day04.validate_expiry_year("eyr:2025"))
    self.assertFalse(day04.validate_expiry_year("eyr:2019"))
    self.assertFalse(day04.validate_expiry_year("eyr:2036"))
    self.assertFalse(day04.validate_expiry_year("eyr:2010"))

  def test_height_is_validated_correctly(self):
    self.assertTrue(day04.validate_height("hgt:150cm"))
    self.assertTrue(day04.validate_height("hgt:193cm"))
    self.assertTrue(day04.validate_height("hgt:165cm"))
    self.assertTrue(day04.validate_height("hgt:59in"))
    self.assertTrue(day04.validate_height("hgt:76in"))
    self.assertTrue(day04.validate_height("hgt:65in"))
    self.assertFalse(day04.validate_height("hgt:200cm"))
    self.assertFalse(day04.validate_height("hgt:140cm"))
    self.assertFalse(day04.validate_height("hgt:45in"))
    self.assertFalse(day04.validate_height("hgt:80in"))
    self.assertFalse(day04.validate_height("hgt:in"))
    self.assertFalse(day04.validate_height("hgt:60"))

  def test_hair_colour_is_validated_correctly(self):
    self.assertTrue(day04.validate_hair_colour("hcl:#602927"))
    self.assertTrue(day04.validate_hair_colour("hcl:#602abc"))
    self.assertFalse(day04.validate_hair_colour("hcl:602abc"))
    self.assertFalse(day04.validate_hair_colour("hcl:#602ab"))
    self.assertFalse(day04.validate_hair_colour("hcl:#602abg"))
    self.assertFalse(day04.validate_hair_colour("hcl:dab227"))

  def test_eye_colour_is_validated_correctly(self):
    for ec in "amb blu brn gry grn hzl oth".split(" "):
      self.assertTrue(day04.validate_eye_colour(f"ecl:{ec}"))
    self.assertFalse(day04.validate_eye_colour("ecl:pnk"))

  def test_passport_id_is_validated_correctly(self):
    self.assertTrue(day04.validate_passport_id("pid:012533040"))
    self.assertFalse(day04.validate_passport_id("pid:3556412378"))

  def test_invalid_passports_can_be_detected_with_more_rules(self):
    invalid_passports = [
      "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
      "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
      "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
      "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"
    ]

    for ip in invalid_passports:
      print(ip)
      self.assertFalse(day04.passport_is_valid_with_new_rules(ip))

  def test_valid_passports_can_be_detected_with_more_rules(self):
    valid_passports = [
      "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
      "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
      "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
      "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
    ]

    for vp in valid_passports:
      print(vp)
      self.assertTrue(day04.passport_is_valid_with_new_rules(vp))

if __name__ == "__main__":
  unittest.main()
