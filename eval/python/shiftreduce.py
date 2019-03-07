#!/usr/bin/env python

import re
import sys
from collections import namedtuple

class SyntaxError(Exception):
    pass


class Token(object):

    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __repr__(self):
        return 'Token(name={name}, value={value})'.format(**self.__dict__)

    def __hash__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.name == other.name
        raise ValueError(other)


class CLexer(object):
    """ Lexer """

    def __init__(self):
        self.tokens = [
            (re.compile(r'\d+'), lambda match: Token('NUM', int(match))),
            (re.compile(r'\+'), lambda match: Token('add', match)),
            (re.compile(r'-'), lambda match: Token('sub', match)),
            (re.compile(r'\*'), lambda match: Token('mul', match)),
            (re.compile(r'/'), lambda match: Token('div', match)),
            (re.compile(r'\('), lambda match: Token('LPAREN', match)),
            (re.compile(r'\)'), lambda match: Token('RPAREN', match)),
            (re.compile(r'\s+'), lambda match: None)
        ]

    def generator(self, source):
        text = source
        while text:
            for token in self.tokens:
                m = token[0].match(text)
                if m:
                    tok = token[1](m.group())
                    if tok:
                        yield tok
                    text = text[m.end():]
                    break
            else:
                raise SyntaxError("Not defined Symbol:[{}]".format(text))




##
# EXP
# EXP  = EXP [+|-] TERM | TERM
# TERM = TERM [*|/] FACTOR | FACTOR
# FACTOR = NUM | ( EXP )
# NUM = r'd+'

class CalSyntax(object):
    """ syntax """

    def __init__(self):
        self.stack =[]

    @staticmethod
    def binary_op(op, x, y):
        rules = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        return rules[op](x, y)


    ##
    # EXP
    # EXP  = EXP [+|-] TERM | TERM
    # TERM = TERM [*|/] FACTOR | FACTOR
    # FACTOR = NUM | ( EXP )
    # NUM = r'd+'

    def table(self):
        tab = []
        tab.append(('exp', '+', 'term', lambda l, op, r: Token('exp', l.value + r.value)))
        tab.append(('exp', '-', 'term'))
        tab.append(('term', '*', 'factor'))
        tab.append(('term', '/', 'factor'))
        tab.append(('NUM', None, None))
        tab.append(('factor', None, None))
        tab.append(('term', None, None))
        return tab

    def _shift(self, token):
        self.stack.append(token)

    def _reduce(self):
        token = self.stack.pop()

    def parse(self, data):
        lex = CLexer(self.tokens)
        for token in lex.generator(data):
            pass


def main():
    data = "1 + 20 - 13 *  (5 + 34)  / 5 + 1 - 2"
    lex = CLexer()
    for t in lex.generator(data):
        print(t)

    # syntax = CalSyntax()
    # syntax.parse(data)


if __name__ == '__main__':
    main()
