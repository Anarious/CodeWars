def positive_sum(arr):
    listing = []
    for num in arr:
        if num > 0:
            listing.append(num)
        if listing is None:
            return 0
    summa = sum(listing)
    return summa