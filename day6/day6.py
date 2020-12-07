def soln1(surveys):
    count = 0
    survey = set()
    for s in surveys:
        if s == "":
            count += len(survey)
            survey = set()
        else:
            [survey.add(answer) for answer in s]
    count += len(survey)
    return count

def soln2(surveys):
    count = 0
    set_list = []
    for s in surveys:
        if s == "":
            common_answers = set_list[0].intersection(*set_list[1:])
            count += len(common_answers)
            set_list = []
        else:
            set_list.append(set(s))
    
    common_answers = set_list[0].intersection(*set_list[1:])
    count += len(common_answers)
    return count


if __name__ == "__main__":
    input = [i.strip() for i in open("input.txt", "r").readlines()]
    print("Solution 1: " +  str(soln1(input)))
    print("Solution 2: " +  str(soln2(input)))