
import logging
import re

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


OPEN=re.compile(r'(\d+)\[')

def find_matched_bracket(data):
    stack=[]
    for i, _ in enumerate(data):
        if data[i] == '[':
            stack.append('[')
        elif data[i] == ']':
            if len(stack) > 0:
                stack.pop()

        if len(stack) == 0:
            return i

    return -1


def expansion(data):
    m = re.search(OPEN, data)
    if m is None:
        return data

    prev = data[:m.start()]
    rest = data[m.end():]

    matched = find_matched_bracket(rest)
    if matched < 0:
        return prev + m.group(0) + rest

    repeat = int(m.group(1)) * expansion(rest[1:matched])

    last = expansion(rest[matched+1:])

    return prev + repeat + last



def main():
    data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]', 'abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    data = ['abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    for item in data:
        print(item, expansion(item))

if __name__ == "__main__":
    main()
