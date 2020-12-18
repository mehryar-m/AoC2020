
def helper_forward(face, position, direction):
    if face == "N":
        position["ns"] += direction['V']
    if face == "S":
        position["ns"] -= direction['V']
    if face == "E":
        position["ew"] += direction['V']
    if face == "W":
        position["ew"] -= direction['V']
    return position

def helper_rotate(pos, direction):
    faces = ["E", "S", "W", "N"]
    steps = direction['V'] / 90
    current = faces.index(pos)
    if direction['A'] == "L":
        return faces[(current - steps) % 4]
    else:
        return faces[(current + steps) % 4]

def soln1(input):
    position = {"ns": 0, "ew": 0}
    face = "E"

    for direction in input:
        if direction['A'] == "N":
            position["ns"] += direction['V']
        if direction['A'] == "S":
            position["ns"] -= direction['V']
        if direction['A'] == "E":
            position["ew"] += direction['V']
        if direction['A'] == "W":
            position["ew"] -= direction['V']
        if direction['A'] == "R" or direction['A'] == "L":
            face = helper_rotate(face, direction)
        if direction['A'] == "F":
            position = helper_forward(face,position,direction)
    
    return abs(position["ns"]) + abs(position["ew"])



    
if __name__ == "__main__":
    input = [{"A": i.strip()[0], "V": int(i.strip()[1:])} for i in open("input.txt", "r").readlines()]
    print(soln1(input))
    