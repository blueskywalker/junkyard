#!/usr/bin/env python

import re
import sys

class CLexer(object):
    def __init__(self, tokens):
        self.tokendef = tokens

    def generator(self,source):
        text=source
        while text:
            not_matched=True
            for k in self.tokendef:
                m = re.match(k[1],text)
                if m:
                    v = text[m.start():m.end()]

                    if len(k)>2 and k[2]:
                        if k[2] !='ignore':
                            value = k[2](v)
                            yield (k[0],value)
                    else:
                        yield (k[0],v)

                    text=text[m.end():]
                    not_matched=False
                    break

            if not_matched:
                raise Exception("Not defined Symbol")


def main():
    def t_num(t):
        return int(t)

    tokens = [
        ('NUM',r'\d+',t_num),
        ('OP', r'[+-/\*\(\)]'),
        ('SP', r'\s+','ignore')
    ]

    lex = CLexer(tokens)
    for t in lex.generator("1 + 20 - 13 *  (5 + 34)  / 5 + 1 - 2"):
        print t


if __name__ == '__main__':
    main()
