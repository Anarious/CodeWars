def printer_error(s):
    count = 0
    bad_letters = ('n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    for key, value in enumerate(bad_letters):
        for i in range(len(s)):
            if s[i] == value:
                count += 1
    return f"{count}/{len(s)}"