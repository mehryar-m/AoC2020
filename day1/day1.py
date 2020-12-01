# https://adventofcode.com/2020/day/1

def soln1(list_of_expenses, value):
    for index in range(0, len(list_of_expenses)):
        remainder = value - list_of_expenses[index]
        if remainder <= value:
            if remainder in list_of_expenses[index + 1:]:
                print("Found: " +  str(list_of_expenses[index]) + " and " +  str(remainder))
                return list_of_expenses[index] * remainder
    return 0

def soln2(list_of_expenses):
    for index in range(0,len(list_of_expenses)):
        remainder = 2020 - list_of_expenses[index]
        if remainder <= 2020:
            value = soln1(list_of_expenses[index+1:], remainder)
            if value != 0:
                print("Found: " + str(list_of_expenses[index]))
                return value * list_of_expenses[index]
    return 0

if __name__ == "__main__":
    input = open("input.txt", "r")
    data = [int(line) for line in input.readlines()]
    print("solution to 1 is: " + str(soln1(data, 2020)))
    print("solution to 2 is: " + str(soln2(data)))



