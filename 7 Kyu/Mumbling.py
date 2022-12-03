def accum(s):
    res =''
    for i in range(len(s)):
        res += (s[i] * (i+1)).capitalize() + '-'
    return res[:-1]