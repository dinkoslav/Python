def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)
    score = 0
    count = 0
    for beer in beers:
        score = score + (beers[count] * fries[count])
        count = count + 1
    return score

print(max_score([10, 11], [1, 5]))
print(max_score([5], [5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
