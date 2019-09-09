# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

r2i = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def romanToInt(s: str) -> int:
    result = 0
    prev = None
    for item in s:
        result += r2i[item]
        if prev is not None and prev < r2i[item]:
            result -= (2 * prev)
        prev = r2i[item]

    return result

data='MCMXCIV'
print(romanToInt(data))
