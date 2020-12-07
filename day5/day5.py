import math

def get_row(boardingPass, lower, upper):
    if len(boardingPass) == 1:
        if boardingPass[0] == "F":
            return lower
        else:
            return upper
    else:
        half  = ((upper - lower) + 1) / 2
        if boardingPass[0] == "F":
            return get_row(boardingPass[1:], lower, upper - half)
        else:
   
            return get_row(boardingPass[1:], lower + half , upper)

def get_seat(boardingPass, lower, upper):
    if len(boardingPass) == 1:
        if boardingPass[0] == "L":
            return lower
        else:
            return upper
    else:
        middle =  (upper - lower + 1) /2
        if boardingPass[0] == "L":
            return get_seat(boardingPass[1:], lower, upper - middle)
        else:
            return get_seat(boardingPass[1:], lower + middle, upper)

# 
# 127, 0: [0:63] = 64, [63-127]
# 0 , 63 [0:32] [32:63]
# 32, 63 []

def get_seat_row(boardingPass):
    seat = {}
    seat["row"] = get_row(boardingPass[:(len(boardingPass)-3)], 0, 127)
    seat["seat"] = get_seat(boardingPass[(len(boardingPass) - 3):], 0, 7)
    return seat

if __name__ == "__main__":
    input = [i.strip() for i in open("input.txt", "r").readlines()]

    list_of_seats = [get_seat_row(bp) for bp in input]
    list_of_ids = [seat["row"]* 8 + seat["seat"] for seat in list_of_seats]

    print("solution to 1: " + str(max(list_of_ids)))

    for i in range(0,127):
        for j in range(0, 7):
            row = i * 8 + j
            if row not in list_of_ids and (row + 1 in list_of_ids) and (row - 1 in list_of_ids):
                print("solution to 2: " + str(row))