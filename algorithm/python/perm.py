#!/usr/bin/env python
""" permutation """

'''
    abc =>
    a * P('bc') + b * P('ac') + c * P('ab')
    bc  => b *P(c) + c * P(b)
'''
import itertools

def permutation(src):
    ''' permutation '''

    if len(src) == 1:
        return [src]

    result = []

    for index in range(len(src)):
        src[0], src[index] = src[index], src[0]
        for sub in permutation(src[1:]):
            result.append([src[0]] + sub)
        src[0], src[index] = src[index], src[0]

    return result

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
    test = ['a', 'b', 'c']

    print permutation(test)
    for item in itertools.permutations(test):
        print item
    # for item in permutation(test):
    #     print item


if __name__ == "__main__":
    main()
