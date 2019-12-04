def is_passphrase_valid(passphrase_to_validate):
    phrases = passphrase_to_validate.split(' ')
    if len(phrases) > len(list(set(phrases))):
        return False
    else:
        return True

def is_passphrase_valid_with_new_rules(passphrase_to_validate):
    if not is_passphrase_valid(passphrase_to_validate):
        return False
    else:
        phrases = passphrase_to_validate.split(' ')
        checked_phrases_list = [''.join(sorted(phrase)) for phrase in phrases]
        if len(phrases) > len(list(set(checked_phrases_list))):
            return False
    return True

def get_input():
    return open('python/inputday04.txt', 'r').read().split('\n')

def run_part_one():
    passphrase_list = get_input()
    valid_passphrase_count = 0
    for passphrase in passphrase_list:
        if is_passphrase_valid(passphrase):
            valid_passphrase_count += 1
    return valid_passphrase_count

def run_part_two():
    passphrase_list = get_input()
    valid_passphrase_count = 0
    for passphrase in passphrase_list:
        if is_passphrase_valid_with_new_rules(passphrase):
            valid_passphrase_count += 1
    return valid_passphrase_count


if __name__ == "__main__":
    print("== DAY 4 - PART ONE ==")
    print(run_part_one())
    print("== DAY 4 - PART TWO ==")
    print(run_part_two())