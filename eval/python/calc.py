#!/usr/bin/env python
import re

NUM_REG=r'\d+'
OP_REG=r'[+-/*\(\)]'
SPACE_REG=r'\s+'

def tokenizer(src):
    while src:
        match = re.match(NUM_REG,src,re.U)
        if match:
            yield ('NUM',int(src[match.start(): match.end()]))
            src = src[match.end():]
            continue

        match = re.match(OP_REG,src,re.U)
        if match:
            yield ('OP',src[match.start():match.end()])
            src = src[match.end():]
            continue

        match = re.match(SPACE_REG,src,re.U)
        if match:
            src = src[match.end():]
            continue

        print "Nothing match"
        break

# 
#  exp = exp +|- term
#  term = exp *|/ factor 
#  factor = NUM | ( exp )
# 
def find_term(tok):
    in_paren = False
    for i, tup in reversed(list(enumerate(tok))):
        sym, val = tup
        
        if sym == 'OP' and val == ')':
            in_paren = True
            continue
        if in_paren and sym == 'OP' and val == '(':
            in_paren = False

        if not in_paren and sym == 'OP' and ( val == '+' or val == '-' ):
            return i
    return -1

def exp(tok):
    index = find_term(tok)
    if index < 0:
        return term(tok)

    if tok[index][1] == '+':
        return exp(tok[0:index]) + term(tok[index+1:])
    else:
        return exp(tok[0:index]) - term(tok[index+1:])


def find_factor(tok):
    in_paren = False
    for i, tup in reversed(list(enumerate(tok))):
        sym, val = tup        
        if sym == 'OP' and val == ')':
            in_paren = True
            continue
        if in_paren and sym == 'OP' and val == '(':
            in_paren = False

        if not in_paren and sym == 'OP' and ( val == '*' or val == '/' ):
            return i
    return -1

def term(tok):
    index = find_factor(tok)

    if index < 0:
        return factor(tok)

    if tok[index][1] == '*':
        return exp(tok[0:index]) * factor(tok[index+1:])
    else:
        return exp(tok[0:index]) / factor(tok[index+1:])

def factor(tok):
    sym, val = tok[0]
    if sym == 'NUM':
        return tok[0][1]

    if sym == 'OP' and val == '(':
        return exp(tok[1:-1])

    raise Exception("syntax")

def main():
    test = "1 + 20 - 13 *  (5 + 34)  / 5 + 1 - 2"
    print test
    tokens = list(tokenizer(test))

    print exp(tokens)

if __name__ == '__main__':
    main()
