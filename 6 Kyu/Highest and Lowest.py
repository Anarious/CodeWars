def duplicate_count(text):
    d = {}
    res = 0
    for c in text.lower():
        d[c] = d.get(c, 0) + 1
    for v in d.values():
        if v > 1:
            res += 1
    return res

x = duplicate_count('aabbcd')
print(x)