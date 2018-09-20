#!/usr/bin/env python

# an rpn calculator in python
# > 19 2.14 + 4.5 2 4.3 / - *
# [85.297441860465113]
# only supports two operands and then an operator

import sys
import operator

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv if sys.version_info > (3, 0) else operator.div
}

def eval_exp(tokens, stack):
    for token in tokens:
        if set(token).issubset(set('0123456789.')):
            stack.append(float(token))
        elif token in ops: 
            if len(stack) < 2:
                raise ValueError('Must have at least two parameters to perform op')

            a = stack.pop()
            b = stack.pop()
            op = ops[token]
            stack.append(op(b,a))
        else:
            raise ValueError('WTF? %s' % (token,))

    return stack


if __name__ == '__main__':
    stack = []
    while True:
        in_func = input if sys.version_info> (3, 0) else raw_input
        expr = in_func('> ')
        if expr in ['quit', 'q', 'exit']:
            exit()
        elif expr in ['clear', 'empty']:
            stack = []
            continue
        elif len(expr) == 0:
            continue

        stack = eval_exp(expr.split(), stack)
        print(stack)

