def valid(password):
    prev_digit = '0'
    num_digits = 1
    found_matching_digits = False
    for digit in password:
        if digit == prev_digit:
            num_digits += 1
        else:
            if num_digits == 2:
                found_matching_digits = True
            num_digits = 1
        #print(f"{digit} - {prev_digit} - {num_digits}")
        if int(digit) < int(prev_digit):
            return False
        prev_digit = digit
    if num_digits == 2:
        found_matching_digits = True
    return found_matching_digits


if __name__ == "__main__":
    print(f"{valid('111111')}")
    print(f"{valid('223450')}")
    print(f"{valid('123789')}")
    print(f"{valid('112233')}")
    print(f"{valid('123444')}")
    print(f"{valid('111122')}")

    count = 0
    for password in range(372037, 905157+1):
        if valid(str(password)):
            count += 1
            print(password)

    print(f"count: {count}")
