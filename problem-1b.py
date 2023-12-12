# make a dictionary correlating spelled numbers with their integer value

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def trebuchet(cipher):
    digits = []
    found = False
    # find first number
    for index, char in enumerate(cipher):
        if found:
            break
        num_checker = []
        for sub_index in range(index, len(cipher)):
            if cipher[sub_index].isdigit():
                digits.append(int(cipher[sub_index]))
                found = True
                break
            num_checker.append(cipher[sub_index])
            if len(num_checker) >= 3:
                candidate = "".join(num_checker)
                if candidate in number_dict:
                    digits.append(number_dict[candidate])
                    found = True
                    break
            if len(num_checker) >= 5:
                break
    # find last number
    found = False
    # need to figure out how to index this backwards
    for index in reversed(list(enumerate(cipher))):
        if found:
            break
        num_checker = []
        for sub_index in range(len(cipher) - 1, index, -1):
            if cipher[sub_index].isdigit():
                digits.append(int(cipher[sub_index]))
                found = True
                break
            num_checker.insert(0, cipher[sub_index])
            if len(num_checker) >= 3:
                candidate = "".join(num_checker)
                if candidate in number_dict:
                    digits.append(number_dict[candidate])
                    found = True
                    break
            if len(num_checker) >= 5:
                break

    return digits


print(trebuchet("kjdbfg2threek"))


#     for char in password_backwards:
#         if char.isdigit() == True:
#             digits.append(char)
#             break
#         else:
#             continue
#     number = int(digits[0] + digits[1])
#     return number


# with open("elves.txt", "r") as file:
#     number_list = []
#     for line in file:
#         number_list.append(trebuchet(line.strip()))

# print(sum(number_list))
