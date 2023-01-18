def high_and_low(numbers):
    result = [int(i) for i in numbers.split(' ')]
    res = str(max(result)), str(min(result))
    return ' '.join(res)


print(high_and_low('42 -9'))