def alphabet_position(text):
    txt = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in text.lower():
        if i in alpha:
            txt += str(ord(i) - 96) + ' '

    return txt[:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))