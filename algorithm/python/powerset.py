
def powerset1(given):
    size=pow(2,len(given))
    f = "{:0%db}" % (len(given),)

    ret=[]
    for i in range(size):
        shape=f.format(i)
        ret.append([ given[index] for index in range(len(given)) if shape[index] == '1'])
    return ret


def powerset2(given):
    size=pow(2,len(given))
    ret=[]
    for i in range(size):
        ret.append([ given[index] for index in range(len(given)) if (1 << index) & i])
    return ret


def powerset(given):
    if len(given) == 0:
        return [[]]

    pivot = given[0]
    prev=powerset(given[1:])

    ret=[]
    ret.extend(prev)
    for item in prev:
        ret.append([pivot] + item)
    return ret


test=['a', 'b', 'c']
print(powerset(test))

