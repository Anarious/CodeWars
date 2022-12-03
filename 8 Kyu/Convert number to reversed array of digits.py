def digitize(n):
    n = str(n)
    result = []
    for integ in n:
        result.append(int(integ))

    return list(reversed(result))