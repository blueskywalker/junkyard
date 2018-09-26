
data=['super','high', 'way', 'highway', 'superhighway', 'bus','stop','busstop', 'schoolzone', 'school', 'zone', 'hello', 'google' ]

lookup=set()

for item in data:
    lookup.add(item)


def decomposition(word):
    def candidate(w):
        ret = []
        for i in range(1,len(w)+1):
            if w[:i] in lookup:
                ret.append(w[:i])

        return ret

    if len(word) == 0:
        return [[]]

    result = []
    for item in candidate(word):
        for subitem in decomposition(word[len(item):]):
            #print('{} + {}'.format(item, subitem))
            result.append([item] + subitem)

    return result

def main():
    for item in data:
        print(item, decomposition(item))


main()
