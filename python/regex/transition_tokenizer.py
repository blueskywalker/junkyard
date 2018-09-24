

from enum import Enum

class TokenType(Enum):
    DIGIT = 0
    NON_DIGIT = 1
    OPEN = 2
    CLOSE = 3
    SPACE = 4
    NONE = 5

transition= {   
    0 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2},
    1 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2, TokenType.OPEN : 3 },
    2 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2},
    3 : { TokenType.DIGIT : 4, TokenType.NON_DIGIT : 5, TokenType.CLOSE: 6 },
    4 : { TokenType.DIGIT : 4, TokenType.NON_DIGIT : 5, TokenType.CLOSE: 6, TokenType.OPEN : 3 },
    5 : { TokenType.DIGIT : 4, TokenType.NON_DIGIT : 5, TokenType.CLOSE: 6 },
    6 : { TokenType.DIGIT : [1, 4], TokenType.NON_DIGIT : [2, 5], TokenType.CLOSE: 6},
    7 : {}
}

def is_digit(achar):
    return achar.isdigit()

def is_nondigit(achar):
    return not achar.isdigit()

def is_open(achar):
    return achar == '['

def is_close(achar):
    return achar == ']'

def get_token(state, achar):
    if is_digit(achar):
        return TokenType.DIGIT

    if state in [ 1, 4 ]:
        if is_open(achar):
            return TokenType.OPEN

    if state in [ 3, 4, 5, 6 ]:
        if is_close(achar):
            return TokenType.CLOSE

    if is_nondigit(achar):
        return TokenType.NON_DIGIT

    return TokenType.NONE

def get_next_state(state, achar):
    canditates = transition[state]
    token = get_token(state, achar)
    return canditates[token]
    

class ActionTable(object):

    def clean(self):
        self.num_ = []
        self.str_ = []

    def __init__(self):
        self.num_ = []
        self.str_ = []
        self.stack_ = []

    def add_num(self, achar):
        self.num_.append(achar)

    def add_str(self, achar):
        self.str_.append(achar)

    def copy2str(self, achar=None):
        self.str_.extend(self.num_)
        self.num_ = []
        if achar is not None:
            self.add_str(achar)

    def push_to_stack(self, achar=None):
        repeat =  int(''.join(self.num_)) if len(self.num_) > 0 else 1
        self.stack_.append((''.join(self.str_), repeat, achar))
        self.clean()


    def pop_stack(self, achar):
        content = ''.join(self.str_)
        self.clean()

        if len(self.stack_) > 0:
            last = self.stack_.pop()
            merge = last[0] + last[1] * content
            self.str_ = list(merge)
        else:
            raise SyntaxError('No Matched []')

    def present(self):

        if len(self.stack_) > 0:
            raise SyntaxError("No Matched []")

        return ''.join(self.str_)

    def is_in_bracket(self):
        if len(self.stack_) == 0:
            return False

        item = self.stack_[-1]
        if item[2] == '[':
            return True
        return False


    def nothing(self, a=None):
        pass

acts = ActionTable()

actions = {
    (0, 1) : acts.add_num,
    (0, 2) : acts.add_str, 
    (0, 7) : acts.nothing,
    (1, 1) : acts.add_num,
    (1, 2) : acts.copy2str,
    (1, 3) : acts.push_to_stack,
    (1, 7) : acts.copy2str,
    (2, 1) : acts.add_num,
    (2, 2) : acts.add_str,
    (2, 7) : acts.nothing,
    (3, 4) : acts.add_num,
    (3, 5) : acts.add_str,
    (3, 6) : acts.pop_stack,
    (3, 7) : acts.nothing,
    (4, 3) : acts.push_to_stack,
    (4, 4) : acts.add_num,
    (4, 5) : acts.copy2str,
    (4, 6) : acts.push_to_stack,
    (4, 7) : acts.copy2str,
    (5, 4) : acts.add_num,
    (5, 5) : acts.add_str,
    (5, 6) : acts.pop_stack,
    (5, 7) : acts.nothing,
    (6, 1) : acts.add_num,
    (6, 2) : acts.add_str,
    (6, 4) : acts.add_num,
    (6, 5) : acts.add_str,
    (6, 6) : acts.pop_stack,
    (6, 7) : acts.nothing
 }

def expansion(data):
    acts.__init__()
    state = 0
    for item in data:
        next_state = get_next_state(state, item)
        if type(next_state) is list:
            if acts.is_in_bracket():
                next_state = next_state[1]
            else:
                next_state = next_state[0]
        action = actions[(state, next_state)]
        action(item)
        state = next_state

    actions[(state, 7)]()
    result = acts.present()
    return result

