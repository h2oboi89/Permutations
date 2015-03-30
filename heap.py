def generate(values, count = -1):
    if count == -1:
        count = len(values)

    if count == 1:
        yield values
    else:
        for i in range(count):
            for permutation in generate(values, count - 1):
                yield permutation

            if count % 2 == 1:
                j = 0
            else:
                j = i

            values[j], values[count - 1] = values[count - 1], values[j]
