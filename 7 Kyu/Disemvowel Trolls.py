def disemvowel(string):
    return ''.join(i for i in string if i not in 'aeiouAEIOU')

print(disemvowel('hello my name ia ansar'))

