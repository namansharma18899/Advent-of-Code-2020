import pathlib, os

pPath = pathlib.Path(__file__).parent.resolve()
from collections import Counter

"""
Password Philosophy: PART 1
"""


def validate_pass(policy, char, password):
    policy = [int(x) for x in policy.split("-")]
    min, max = policy[0], policy[1]
    char = char.split(":")[0]
    cn = Counter(password)[char]
    return True if cn >= min and cn <= max else False

def validate_pass2(policy, char, password):
    policy = [int(x) for x in policy.split("-")]
    min, max = policy[0], policy[1]
    char = char.split(":")[0]
    if password[min-1]==password[max-1] and password[min-1]==char:
        return False
    elif password[min-1]==char or password[max-1]==char:
        return True
    else:
        return False


def pass_phil():
    filename = os.path.join(pPath, "input.txt")
    print(filename)
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    n = list()
    count = 0
    for line in Lines:
        ln = line.strip()
        spl = ln.split(" ")
        if validate_pass(spl[0], spl[1], spl[2]):
            count += 1
    return count

def part_2():
    filename = os.path.join(pPath, "input.txt")
    print(filename)
    file1 = open(filename, "r")
    Lines = file1.readlines()
    # Strips the newline character
    n = list()
    count = 0
    for line in Lines:
        ln = line.strip()
        spl = ln.split(" ")
        if validate_pass2(spl[0], spl[1], spl[2]):
            count += 1
    return count

if __name__ == "__main__":
    "part 1"
    # print(find_missing_entries())
    print(part_2())
