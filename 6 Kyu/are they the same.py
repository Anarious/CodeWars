def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

a = {121, 144, 19, 161, 19, 144, 19, 11}
b = {121, 14641, 20736, 361, 25921, 361, 20736, 371}
print(comp(a, b))
