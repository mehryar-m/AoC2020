import re

def recursivesonln1(data, all_bags, parents, count):
    if len(parents) == 0:
        return len(all_bags)
    new_parents = []
    for d in data:
        for p in parents:
            if p in d[1]:
                count += 1
                new_parents.append(d[0].replace(" bags", ""))
                all_bags.add(d[0].replace(" bags", ""))
    return recursivesonln1(data, all_bags, new_parents, count)

def soln1(data):
    count = 0
    parents = []
    all_bags = set()
    for d in data:
            if "shiny gold" in d[1]:
                count += 1
                parents.append(d[0].replace(" bags", ""))
                all_bags.add(d[0].replace(" bags", ""))
    return recursivesonln1(data, all_bags, parents, count)

def recursivesonln2(data, bags_left, count):
    if len(bags_left) == 0:
        return count
    new_bags = []
    for d in data:
        for b in bags_left:
            if b in d[0]:
                if d[0] != "n":
                    for e in d[1:]:
                        count += int(e[0])

    return recursivesonln2(data, [], [], count)

def soln2(data):
    sum = 0
    for d in data:
        if "shiny gold" in d[0]:
            print(d)
            for e in d[1:]:
                sum += int(e[0])
    
    return sum
            

if __name__ == "__main__":
    input = [i.strip().replace('.','') for i in open("input.txt", "r").readlines()]
    data = [re.split(' contain', i) for i in input]
    sol2 = [re.split(' contain |, ', i) for i in input]
    print("solution to 1: " + str(soln1(data)))
    print("solution to 1: " + str(soln2(sol2)))