#!/usr/bin/env python

import re
import sys

class CLexer(object):
    """ Lexer """

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


class CalSyntax(object):
    """ syntax """
    def __init__(self):
        self.actions= {
            '+': lambda x,y : x + y,
            '-': lambda x,y : x - y,
            '*': lambda x,y : x * y,
            '/': lambda x,y : x / y
        }

    def apply(self,op,x,y):
        return self.actions[op](x,y)

def main():
    def t_num(t):
        return int(t)

    tokens = [
        ('NUM',r'\d+',t_num),
        ('OP', r'[+-/\*]'),
        ('LPAREN',r'\(',),
        ('RPAREN',r'\)'),
        ('SP', r'\s+','ignore')
    ]

    lex = CLexer(tokens)
    for t in lex.generator("1 + 20 - 13 *  (5 + 34)  / 5 + 1 - 2"):
        print t

    syntax  = CalSyntax()

    print syntax.apply('+',1,2)

if __name__ == '__main__':
    main()
