def soln1(adaptors):
    chain = []
    first = 0
    one_jolt = 0
    three_jolt = 0
    for i in range(0, len(adaptors)):
        choices = []
        if first + 1 in adaptors:
            choices.append(adaptors[adaptors.index(first+1)])
        if first + 2 in adaptors: 
            choices.append(adaptors[adaptors.index(first+2)])
        if first + 3 in adaptors: 
            choices.append(adaptors[adaptors.index(first+3)])
        if min(choices) == first + 1:
            one_jolt += 1
        if min(choices) == first + 3:
            three_jolt += 1
        first = min(choices)
        chain.append(min(choices))
    print(chain)
    return one_jolt * three_jolt

if __name__ == "__main__":
    input = [int(i.strip()) for i in open("input.txt", "r").readlines()]
    print(soln1(input + [max(input) + 3]))
    last = max(input)
    index = [1] + [0] * last + [0, 0]
    print(index)
    for r in sorted(input):
        index[r] = index[r-1] + index[r-2] + index[r-3]
        if r == last:
            print(index[r])
            break
