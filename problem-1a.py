# get first and last digit from each string
# iterate through string to receive first digit
# iterate backwards to receive last digit

# one idea is to convert each string into an array of characters that can be indexed
# another idea is to find first digit, then reverse the string and then find first digit again


def trebuchet(cipher):
    digits = []
    password = [char for char in cipher]
    password_backwards = password[::-1]
    for char in password:
        if char.isdigit() == True:
            digits.append(char)
            break
    for char in password_backwards:
        if char.isdigit() == True:
            digits.append(char)
            break
    number = int(digits[0] + digits[1])
    return number


with open("elves.txt", "r") as file:
    number_list = []
    for line in file:
        number_list.append(trebuchet(line.strip()))

print(sum(number_list))


# cipher = "brandon"
# password = [char for char in cipher]
# password_backwards = password[::-1]

# print(password)
# print(password_backwards)

# oneightwo 12

# jzb1oneightqqr
# j - jz - jzb - jzb1
# r - qr - qqr - tqqr - htqqr
# q - qq - tqq - htqq - ghtqq
# t - ht - ght - ight - eight
