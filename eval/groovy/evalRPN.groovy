#!/usr/bin/env groovy

def evalRPN(expr) {
    def stack = [] as Stack
    def binaryOp  = { action -> return { action.call(stack.pop(), stack.pop()) }}
    def actions = [
        '+': binaryOp { a,b -> b + a },
        '-': binaryOp { a,b -> b - a },
        '*': binaryOp { a,b -> b * a },
        '/': binaryOp { a,b -> b / a },
        '^': binaryOp { a,b -> b ** a }
    ]

    expr.split(' ').each { item ->
        def action = actions[item] ?: { item as BigDecimal }
        stack.push(action.call())

        println "$item: $stack"
    }

    assert stack.size() == 1 : "Unbalanced Expression: $expr ($stack)"
    stack.pop()
}

println evalRPN('3 4 2 * 1 5 - 2 3 ^ ^ / +')
