def find_needle(haystack):
    for i, v in enumerate(haystack):
        if v == 'needle':
            return f"found the needle at position {i}"


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))