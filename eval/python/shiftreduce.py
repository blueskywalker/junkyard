#!/usr/bin/env python

import re
import sys


class SyntaxError(Exception):
    pass


class Token(object):

    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __repr__(self):
        return 'Token(name={name}, value={value})'.format(**self.__dict__)


class CLexer(object):
    """ Lexer """

    def __init__(self):
        self.tokens = [
            (re.compile(r'\d+'), lambda match: Token('NUM', int(match))),
            (re.compile(r'[+-/\*]'), lambda match: Token('OP')),
            (re.compile(r'\('), lambda match: Token('LPAREN')),
            (re.compile(r'\)'), lambda match: Token('RPAREN')),
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


class CalSyntax(object):
    """ syntax """
    def __init__(self):

        self.rules = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

        ##
        # EXP
        # EXP  = EXP [+|-] TERM
        # TERM = TERM [*|/] ELEM
        # ELEM = NUM | ( EXP )
        #
        self.stack = []

    def _shift(self, token):
        self.stack.append(token)

    def _reduce(self, token):
        self.stack.pop()

    def _apply(self, op, x, y):
        return self.actions[op](x, y)

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
