

def powerSet(input):

    output = [ [] ]

    for x in reversed(input):
        tmp=[]
        for trace in output:
           tmp.append( [x] + trace)
        output.extend(tmp)
    return output


print(powerSet('abc'))
