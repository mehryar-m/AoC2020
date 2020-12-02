
def is_valid2(password_triple):
    number_letter_min = password_triple["min"]
    number_letter_max = password_triple["max"]
    letter = password_triple["letter"]
    password = password_triple["password"]

    case1 = password[number_letter_min - 1] == letter and password[number_letter_max - 1]
    case2 = password[number_letter_min - 1] != letter and password[number_letter_max - 1] == letter
    case3 = password[number_letter_min - 1] == letter and password[number_letter_max - 1] == letter

    return (case1 or case2) and (not case3)

def is_valid1(password_triple):
    number_letter_min = password_triple["min"]
    number_letter_min_max = password_triple["max"]
    letter = password_triple["letter"]
    password = password_triple["password"]

    count = 0
    for p in password:
        if p == letter:
            count += 1 
    return count >= number_letter_min and count <= number_letter_min_max

def convert_to_map(value):
    password_triple = {}
    array = value.split(" ")
    password_triple["min"], password_triple ["max"] = int(array[0].split("-")[0]) , int(array[0].split("-")[1])
    password_triple["letter"] = array[1].replace(":","")
    password_triple["password"] = array[2]
    return password_triple
    
if __name__ == "__main__":
    input = open("input.txt", "r")
    data = [convert_to_map(line) for line in input.readlines()]
    isValid = [is_valid1(d) for d in data]
    isValid2 = [is_valid2(d) for d in data]
    print("solution to 1 is: " + str(isValid.count(True)))
    print("solution to 2 is: " + str(isValid2.count(True)))