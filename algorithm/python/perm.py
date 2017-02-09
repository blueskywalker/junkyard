#!/usr/bin/env python


def perm(src):

    if len(src) == 1:
        return [src]

    pivot = src[:1]
    return [sub[:i] + pivot + sub[i:] for i in range(len(src)) for sub in perm(src[1:]) ]




def main():
    test=['a','b','c']

    print perm(test)


if __name__ == "__main__":
    main()
