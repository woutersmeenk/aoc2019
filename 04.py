def valid(password):
    prev_digit = '0'
    num_matching_digits = 1
    found_two_matching_digits = False
    for digit in password:
        if digit == prev_digit:
            num_matching_digits += 1
        else:
            if num_matching_digits == 2:
                found_two_matching_digits = True
            num_matching_digits = 1
        if int(digit) < int(prev_digit):
            return False
        prev_digit = digit
    if num_matching_digits == 2:
        found_two_matching_digits = True
    return found_two_matching_digits


if __name__ == "__main__":
    count = 0
    for password in range(372037, 905157+1):
        if valid(str(password)):
            count += 1

    print(f"Part 2: {count}")
