import pathlib, os
pPath = pathlib.Path(__file__).parent.resolve()

"""
Part: 1
"""


def find_missing_entries():
    filename = os.path.join(pPath, "input.txt")
    print(filename)
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    n = list()
    for line in Lines:
        n.append(int(line.strip()))
    to_be_found = set()
    for each in n:
        if each in to_be_found:
            return int(each) * int(2020 - each)
        else:
            to_be_found.add(int(2020 - each))


"""
Part 2
"""


def find_3_entries():
    filename = os.path.join(pPath, "input.txt")
    print(filename)
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    n = list()
    for line in Lines:
        n.append(int(line.strip()))
    for index_p in range(0, len(n)):
        primary = n[index_p]
        to_be_found = set()
        new_sum = 2020 - primary
        for index_s in range(index_p + 1, len(n)):
            secondary = n[index_s]
            if (secondary) in to_be_found:
                return primary * secondary * int(new_sum - secondary)
            else:
                to_be_found.add(new_sum - secondary)


if __name__ == "__main__":
    "part 1"
    # print(find_missing_entries())
    print(find_3_entries())
