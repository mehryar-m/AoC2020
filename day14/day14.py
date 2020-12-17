def get_all_memory_addresses(bit):
    if "X" not in bit:
        return [bit]
    index =  bit.index("X")
    option_1 = bit[:index] + "1" + bit[index + 1:]
    option_2 = bit[:index] + "0" + bit[index + 1:]
    return get_all_memory_addresses(option_1) + get_all_memory_addresses(option_2)


def convert_with_mask(input_value, mask):
    new_value = ""
    for i in range(0, 36):
        if mask[i] != 'X':
            new_value = new_value  + mask[i]
        else:
            new_value = new_value + input_value[i]
    return new_value
    
def convert_with_vol_mask(input_value, mask):
    new_value = ""
    for i in range(0, 36):
        if mask[i] != '0':
            new_value = new_value  + mask[i]
        else:
            new_value = new_value + input_value[i]
    return new_value

def soln1(input):
    mem = {}
    mask = ""
    for i in input:
        if i[0] == "mask":
            mask = i[2]
        else:
            mem_location = int(i[0][4:len(i[0])-1])
            bit_representation = "{0:b}".format(int(i[2]))
            bit_representation = "0" * (36 - len(bit_representation)) + bit_representation
            mem[mem_location] = int(convert_with_mask(bit_representation, mask), 2)
    return sum(mem.values())

def soln2(input):
    mem = {}
    mask = ""
    addresses = set()
    for i in input:
        if i[0] == "mask":
            mask = i[2]
        else:
            mem_location = int(i[0][4:len(i[0])-1])
            bit_representation = "{0:b}".format(mem_location)
            bit_representation = "0" * (36 - len(bit_representation)) + bit_representation
            list_of_mem_Address = get_all_memory_addresses(convert_with_vol_mask(bit_representation, mask))
            for mem_address in list_of_mem_Address:
                mem[int(mem_address,2)] = int(i[2])
    return sum(mem.values())
        



if __name__ == "__main__":
    input = [i.strip().split(" ") for i in open("input.txt", "r").readlines()]
    print("solution 1: ")
    print(soln1(input))
    print("solution 2: ")
    print(soln2(input))
    
