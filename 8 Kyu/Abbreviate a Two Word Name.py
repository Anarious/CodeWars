import string
def abbrev_name(name):
    return '.'.join(i for i in string.capwords(name) if i.isupper())