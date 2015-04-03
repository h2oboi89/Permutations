from itertools import permutations

def permute(value):
    values = []
    if type(value) is str:
        for c in value:
            values.append(c)

    elif type(value) is int:
        for c in str(value):
            values.append(int(c))

    elif type(value) is list:
        values = value

    else:
        return None

    return permutations(values)
