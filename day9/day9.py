def sum_exists(value, array):
    is_it_a_sum_of_2_previous_numbers = False
    for element in array:
        if (value - element) in array:
            return True
    return is_it_a_sum_of_2_previous_numbers

def soln1(input, preamble_size):
    i,j = 0, preamble_size - 1
    while not j >= len(input):
        if not sum_exists(input[j+1], input[i:j+1]):
            return input[j+1]
        i += 1
        j += 1

    return -1

def soln2(input, invalid_number):
    i, j = 0,2
    top_range = 2 # start with sequences of size 3, remember that we already know that no pair exists
    while not top_range >= len(input): 
        if j >= len(input):
            top_range += 1
            i, j = 0, top_range
        if sum(input[i: j+1]) == invalid_number:
            result = sorted(input[i: j+1])[0] + sorted(input[i:j+1])[j-i]
            return result
        i += 1
        j += 1

if __name__ == "__main__":
    input = [int(i.strip()) for i in open("input.txt", "r").readlines()]
    print("Solution 1 is: " + str(soln1(input, 25)))
    print("Solution 2 is: " + str(soln2(input, 3199139634)))

