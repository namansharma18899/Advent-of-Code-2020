import pathlib, os
pPath = pathlib.Path(__file__).parent.resolve()

"""
Part: 1
"""


def part_1_optmz():
    filename = os.path.join(pPath, "input.txt")
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    arr = []
    x_index=4
    y_index = 1
    count =0
    for line_index in range(1, len(Lines)):
        line = Lines[line_index].split('\n')[0]
        ln_len = len(line)
        """
        strat -> posi / len_of_pattern....remaineder is posi of the tree
        """
        relative_point_posi=x_index
        if (int(x_index%ln_len))==0:
            relative_point_posi=ln_len-1
        else:
            relative_point_posi=(int(x_index%ln_len))-1    
        # relative_point_posi = ln_len if int(x_index%ln_len)==0 else int(x_index%ln_len)
        # print('line -> ',line, ' x_index ', x_index, ' rel -> ', relative_point_posi-1)
        if line[relative_point_posi]=='#':
            count+=1
        x_index+=3
    return count


def part_1_brute_force():
    filename = os.path.join(pPath, "input.txt")
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    arr = []
    x_index=3
    y_index = 1
    count =0
    for line_index in range(1, len(Lines)):
        line = Lines[line_index].split('\n')[0]
        line = 40*line
        if line[x_index]=='#':
            count+=1
        x_index+=3
    return count


if __name__ == "__main__":
    "part 1"
    # print(find_missing_entries())
    print(part_1_brute_force())
