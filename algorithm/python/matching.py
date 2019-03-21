#!/usr/bin/env python

closing = {'{': '}', '[': ']', '(': ')'}


def verify(src):
    print src
    stack=[]

    for c in src:
        if c in closing:
            stack.append(closing[c])
        else:
            if len(stack) == 0:
                return False

            expected = stack.pop()
            if expected != c:
                return False

    if len(stack) != 0:
        return False

    return True


def main():
    print verify("{([])}")
    print verify("}(){}[]")
    print verify("(){}[")
    print verify("({}[]")

if __name__ == "__main__":
    main()
