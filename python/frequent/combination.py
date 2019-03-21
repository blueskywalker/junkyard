

# def powerSet(input):
#     output = [ [] ]
#     for x in reversed(input):
#         tmp=[]
#         for trace in output:
#            tmp.append( [x] + trace)
#         output.extend(tmp)
#     return output


def powerSet(src):
    if src is None:
        return None
    
    if len(src) == 0:
        return [[]]

    pivot, rest = src[0], src[1:]
    last = powerSet(rest)
    return last + [ item + [pivot] for item in last]

print(powerSet('abc'))
