def is_valid(passport):
    valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if "cid" in passport:
        passport.remove("cid")
    
    return set(valid) == set(passport)
    
def is_valid_year(year, lower_bound, upper_bound):
    return len(year) == 4 and lower_bound <= int(year) <= upper_bound

def is_valid_hgt(height):
    return True

def is_valid_hcl(haircolour):
    return True

def is_valid_eyecolor(ecl):
    return True

def is_valid_pid(password):
    return True

def create_list_of_passports(data):
    list_of_passports = []
    passport = []
    increment = 0
    for l in data:
        if l != "":
            split_key_value = l.split(' ')
            keys = [k.split(':')[0] for k in split_key_value]
            passport = passport + keys
        else:
            list_of_passports.append(passport)
            passport = []
    list_of_passports.append(passport)
    return list_of_passports

if __name__ == "__main__":
    input = open("input.txt", "r")

    data = [l.strip() for l in input.readlines()]
    list_of_passports = create_list_of_passports(data)
    number_of_valid_passports = [is_valid(p) for p in list_of_passports].count(True)

    print("solution to 1 is: " + str(number_of_valid_passports))
    print("solution to 2 is: ")
