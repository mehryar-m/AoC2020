def soln1(earliest_arrival, list_of_buses):
    ids_of_bus = [(int(window), int(window) - (earliest_arrival % int(window))) for  window in list_of_buses]
    result = min(ids_of_bus, key= lambda t:t[1])

    return result[0] * result[1]


## shit doesn't work...
def soln2(input_part2):
    t, step = 0, 1
    for mins, bus_id in input_part2:
        while (t + mins) % bus_id != 0:
            t += step
        step *= bus_id
    return t

if __name__ == "__main__":
    input = [i.strip() for i in open("input.txt", "r").readlines()]
    earliest_arrival = int(input[0])
    list_of_buses = set(input[1].split(",")).difference(set('x'))
    list_of_times = input[1].split(",")
    sol2_input = [(i, int(list_of_times[i])) for i in range(0, len(list_of_times)) if list_of_times[i] != 'x']
    print(sol2_input)
    print(soln2(sol2_input))
    print(soln1(earliest_arrival, list_of_buses))
