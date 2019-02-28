
def perm(input):

    if len(input) == 1:
        return [input]

    pivot = input[0] 
    rest = input[1:]

    #output= []
    #for sub in perm(rest):
    #    for i in xrange(len(sub)+1):
    #        output.append(sub[:i] + pivot + sub[i:])
    #return output

    return [ sub[:i] + pivot + sub[i:] for sub in perm(rest) for i in xrange(len(sub)+1) ]

print perm('abcd')
