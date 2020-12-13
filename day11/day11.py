def is_occupied(value):
    if value == "#":
        return 1
    return 0

# def count_first_seat(input, i, j):
#     edge
#     first_seats = [] 
#     #  





def count_adjacent(input,i,j):
    i = i-1
    j = j -1
    count = 0
    for k in range(0,8):
        count += is_occupied(input[i][j])
        if 0 <= k <= 1:
            j += 1
        if 2 <= k <=3:
            i += 1
        if 4 <= k <=5:
            j -= 1
        if 6 <= k <= 7:
            i -=1
    return count

        
        


def soln1(input):
    changed = True
    count_occupied = 0
    count_empty = 0
    # new_input = [['.' for i in range(1, len(input[0]) + 1)] for i in range(1, len(input)+1)]
    while changed:
        changed = False 
        new_input = [['.' for i in range(1, len(input[0]) + 1)] for i in range(1, len(input)+1)]
        for i in range(1, len(input) - 1):
            for j in range(1, len(input[0]) - 1):
                if input[i][j] == "L":
                    if count_adjacent(input, i, j) == 0:
                        new_input[i][j] = "#"
                        changed = True
                    else:
                        new_input[i][j] = input[i][j]
                elif input[i][j] == "#":

                    if count_adjacent(input, i, j) >= 4:
                        new_input[i][j] = "L"
                        changed = True
                    else:
                        new_input[i][j] = input[i][j]
                else:
                    new_input[i][j] = input[i][j]
        input = new_input
    count = 0
    for row in input:
        count += row.count("#")

    return count



if __name__ == "__main__":
    input = [list("0" + i.strip() + "0") for i in open("input.txt", "r").readlines()]
    pad = ["0" for i in input[0]]
    input = [pad] + input + [pad]
    print(soln1(input))
