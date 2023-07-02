import pathlib, os
pPath = pathlib.Path(__file__).parent.resolve()

"""
Part: 1
"""


def part_1():
    filename = os.path.join(pPath, "input.txt")
    print(filename)
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    arr = []
    x_index=3
    count =0
    for line_index in range(1, len(Lines)):
        line = Lines[line_index]
        if line[x_index]=='X':
            count+=1
        x_index+=3
    return count



if __name__ == "__main__":
    "part 1"
    # print(find_missing_entries())
    print(part_1())
