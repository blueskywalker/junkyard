#!/usr/bin/env python
""" permutation """

def classic_perm(src):
    'classical loop'
    if len(src) == 1:
        return [src]

    pivot = src[:1]

    result = []

    for sub in classic_perm(src[1:]):
        for i in range(len(src)):
            result.append(sub[:i] + pivot + sub[i:])

    return result


def perm(src):
    """ compact """
    if len(src) == 1:
        return [src]

    pivot = src[:1]
    return [sub[:i] + pivot + sub[i:] for sub in perm(src[1:]) for i in range(len(src))]



def main():
    """ main """
    test = ['a', 'b', 'c', 'd']

    #print classic_perm(test)
    for item in perm(test):
        print item


if __name__ == "__main__":
    main()
