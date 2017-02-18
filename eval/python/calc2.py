#!/usr/bin/env python

import re
import types

class TokenDef(object):
    """ DEFINE """

    def __init__(self,tuple):
        self.name=tuple[0]
        self.regex=tuple[1]
        self.func = None

        if len(tuple) > 2 and tuple[2]:
            self.func = tuple[2]

    def __str__(self):
        return "TokenDef[{},{},{}]".format(self.name,self.regex,self,func)

class Token(object):
    """ Token """

    def __init__(self,tuple):
        self.sym=tuple[0]
        self.value=tuple[1]

    def __str__(self):
        return "Token[{},{}]".format(self.sym,self.value)


class TokenStream(object):
    """ Stream """

    def __init__(self,gen):
        self.tokens = list(gen)
        self.index = 0

    def advance(self):
        if index + 1 == len(tokens):
            return None
        return self.tokens[self.index + 1]

    def eat(self):
        if index+1 == len(tokens):
            return None

        self.index += 1
        return self.tokens[self.index]

    def __str__(self):
        return "TokenStream({},{})".format(self.tokens,self.index)

    def __iter__(self):
        return self.tokens.__iter__()


class CLexer(object):
    """ Lexer """

    def __init__(self, tokens):
        self.tokendef = tokens

    def lex(self, source):
        text = source
        while text:
            not_matched = True
            for k in self.tokendef:
                m = re.match(k.regex, text)
                if m:
                    v = text[m.start():m.end()]
                    if k.func:
                        if type(k.func) == types.FunctionType:
                            value = k.func(v)
                            yield Token((k.name, value))
                    else:
                        yield Token((k.name, v))

                    text = text[m.end():]
                    not_matched = False
                    break

            if not_matched:
                raise Exception("Not defined Symbol")


    def stream(self,source):
        return TokenStream(self.lex(source))


  # exp = term | term + term | term - term
  # term = factor | factor * factor | facotr / factor
  # factor = NUM | ( exp )

def exp(toks):




def main():
    def t_num(t):
        return int(t)

    tokens = [
        TokenDef(('NUM',r'\d+',t_num)),
        TokenDef(('OP', r'[+-/\*]')),
        TokenDef(('LPAREN',r'\(',)),
        TokenDef(('RPAREN',r'\)')),
        TokenDef(('SP', r'\s+','ignore'))
    ]
    lexer = CLexer(tokens)

    tok = lexer.stream("1 + 20 - 13 *  (5 + 34)  / 5 + 1 - 2")

    for t in tok:
        print t

if __name__ == '__main__':
    main()
