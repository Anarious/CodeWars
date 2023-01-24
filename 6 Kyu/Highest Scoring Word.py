ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

x = input().split(' ')

def high(x):
    maxi= 0
    highest = ''
    for word in x:
        summ = 0
        for c in word:
            for i, k in enumerate(ascii_lowercase):
                if c in k:
                    summ += i+1
            if summ > maxi:
                maxi = summ
                highest = word
    return highest

print(high(x))
