

import re

OPEN=r'(\d+)\['

def expansion(data):

    stack = []

    i = 0
    while i < len(data):
        if len(stack) > 0:
            re.search(OPEN, data[i:])


def main():
    data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]', 'abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    data = ['abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    for item in data:
        print(item, expansion(item))

if __name__ == "__main__":
    main()