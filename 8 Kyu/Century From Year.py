def century(year):
    if (year <= 0):
        return -1;
    if (year <= 100):
        return 1;
    if (year % 100 == 0):
        return year / 100;
    else:
        return (year // 100) + 1;