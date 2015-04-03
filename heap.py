def _generate(values, count = -1):
    if count == -1:
        count = len(values)

    if count == 1:
        yield values
    else:
        for i in range(count):
            for permutation in _generate(values, count - 1):
                yield permutation

            if count % 2 == 1:
                j = 0
            else:
                j = i

            values[j], values[count - 1] = values[count - 1], values[j]

def permute(value):
    values = []
    if type(value) is str:
        for c in value:
            values.append(c)

        return ''.join(_generate(values))

    elif type(value) is int:
        for c in str(value):
            values.append(c)

        return int(''.join(_generate(values)))

    elif type(value) is list:
        return _generate(value)
