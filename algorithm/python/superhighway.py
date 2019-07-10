
data=['super','high', 'way', 'highway', 'superhighway', 'bus','stop','busstop', 'schoolzone', 'school', 'zone', 'hello', 'google' ]

lookup=set(data)

def decomposition(word):
    def candidate(w):
        for i in range(1,len(w)+1):
            if w[:i] in lookup:
                yield w[:i]


    if len(word) == 0:
        yield []

    for item in candidate(word):
        for subitem in decomposition(word[len(item):]):
            #print('{} + {}'.format(item, subitem))
            yield [item] + subitem


def main():
    for item in data:
        print(item, list(decomposition(item)))

main()
