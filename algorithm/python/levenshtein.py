

def levenshtein(x: str, y: str) -> int :

    # empty string
    if len(x) == 0: return len(y)
    if len(y) == 0: return len(x)

    # test if last characters of the strings match
    cost=0
    if x[-1] == y[-1]:
        cost = 0
    else:
        cost = 1

    return min(levenshtein(x[:-1], y) + 1,
               levenshtein(x, y[:-1]) + 1,
               levenshtein(x[:-1], y[:-1]) + cost)


print(levenshtein('story','history'))
print(levenshtein('machine','marine'))
