
def is_tree(point):
    if point == '#':
        return True
    return False

def countTrees(map, right_steps, down_steps):
    row, column = 0, 0
    num_trees = 0
    number_of_columns = len(map[0])
    while row < len(map):
        if is_tree(map[row][column]):
            num_trees += 1
        column = (column + right_steps) % number_of_columns
        row += down_steps
    return num_trees

def soln2(map):
    list_of_tuples = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    value = 1
    for l in list_of_tuples:
        value = value * countTrees(map, l[0], l[1])
    return value

if __name__ == "__main__":
    input = open("input.txt", "r")
    mountain = [l.strip() for l in input.readlines()]
    print("solution to 1 is: " + str(countTrees(mountain, 1, 1)))
    print("solution to 2 is: " + str(soln2(mountain)))
