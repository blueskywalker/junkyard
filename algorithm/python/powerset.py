
def powerset1(given):
    size=pow(2,len(given))
    f = "{:0%db}" % (len(given),)

    ret=[]
    for i in range(size):
        shape=f.format(i)
        ret.append([ given[index] for index in range(len(given)) if shape[index] == '1'])
    return ret


def powerset(given):
    size=pow(2,len(given))
    ret=[]
    for i in range(size):
        ret.append([ given[index] for index in range(len(given)) if (1 << index) & i])
    return ret

test=['a', 'b', 'c']
print(powerset(test))

