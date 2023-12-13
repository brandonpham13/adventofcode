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
        if cipher[index].isdigit():
            digits.append(int(cipher[index]))
            found = True
            break
        for sub_index in range(index, len(cipher)):
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
    # range here is incorrect
    for index in range(len(cipher) - 1, 0, -1):
        if found:
            break
        num_checker = []
        if cipher[index].isdigit():
            digits.append(int(cipher[index]))
            found = True
            break
        for sub_index in range(index, len(cipher)):
            num_checker.append(cipher[sub_index])
            if len(num_checker) >= 3:
                candidate = "".join(num_checker)
                if candidate in number_dict:
                    digits.append(number_dict[candidate])
                    found = True
                    break
            if len(num_checker) >= 5:
                break
    number = int(str(digits[0]) + str(digits[1]))
    return number


print(trebuchet("4f"))

# with open("elves.txt", "r") as file:
#     number_list = []
#     for line in file:
#         number_list.append(trebuchet(line.strip()))

# print(sum(number_list))
