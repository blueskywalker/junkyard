
import re


OPEN=r'(\d+)\['

def matched_length(t):
    return t[1] - t[0]

def find_match(data):
    m = re.match(OPEN, data)
    if m is None:
        raise ValueError('wrong string {data}'.format(**locals()))

    last=m.end()
    rest = data[last:]

    while last< len(data):
        close = rest.index(']')
        if close == -1:
            raise SyntaxError()

        m = re.search(OPEN, rest)
        if m is None:
            return last + close

        start = m.start()
        if close < start:
            return last + close

        submatch = find_match(rest[m.start():])
        last = last+ start+submatch+1
        rest = data[last:]


    raise ValueError(data)

def expansion(data):

    m = re.search(OPEN, data)

    if m is None:
        return data

    prev = data[:m.start()]
    rest = data[m.start():]

    matched = find_match(rest)
    expr = rest[matched_length(m.span()):matched]
    repeated = int(m.group(1)) * expansion(expr)
    last = expansion(rest[matched+1:])
    return prev + repeated + last

def main():

    data = ['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]', 'abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]' ]
    #data = ['abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    for item in data:
        print(item, expansion(item))

        
if __name__ == "__main__":
    main()
