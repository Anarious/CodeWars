def is_isogram(string):
    new_string = string.lower()
    list = []
    for char in new_string:
        if char.isalpha():
            if char in list:
                return False
            list.append(char)
    return True
