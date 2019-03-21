
def pascal(n):
    if n <= 0:
        return []

    if n == 1:
        return [1]

    prev = pascal(n-1)
    mid =map(sum,zip(prev[1:], prev[:-1]))
    return [prev[0]] + list(mid) + [prev[-1]]

def pascal1(n):
    def my_zip(alist, blist):
        ret = []
        i = 0
        while i < len(alist) or i < len(blist):
            ret.append(alist[i] + blist[i])
            i += 1
        return ret

    if n == 1:
        return [1]

    prev = pascal1(n-1)
    mid = my_zip(prev[1:], prev[:-1])
    return [prev[0]] + mid + [prev[-1]]

for i in range(1,6):
    print(pascal1(i))

