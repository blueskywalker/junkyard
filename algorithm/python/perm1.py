
#
# [1, 2, 3]
# n=0 [[]]
# n=1 [[3]]
# n=2 [[2, 3],[3, 2]]
# n=3 [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
#
#

def permutation(src):

    if len(src) == 0:
        return [[]]

    pivot = src[0]
    rest = src[1:]
    ret = []
    for item in permutation(rest):
        for i in range(len(item)+1):
            ret.append(item[:i] + [pivot] + item[i:])


    return ret

def perm1(src):
    if len(src) == 0:
        return [[]]

    pivot = src[0]
    rest = src[1:]
    return [ item[:i] + [pivot] + item[i:] for item in perm1(rest) for i in range(len(item)+1) ]

def perm2(src):
    if len(src) == 0:
        return [[]]
    pivot,rest = src[0], src[1:]
    return [ item[:i] + [pivot] + item[i:] for item in perm2(rest) for i in range(len(item)+1) ]


test=[1, 2, 3]

print(perm2(test))


