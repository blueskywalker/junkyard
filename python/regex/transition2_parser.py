

from enum import Enum

class TokenType(Enum):
    DIGIT = 0
    NON_DIGIT = 1
    OPEN = 2
    CLOSE = 3
    SPACE = 4
    NONE = 5


class ExpansionParser(object):

    def __init__(self):
        self.transition =  {
            0 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2 },
            1 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2, TokenType.OPEN : 3, TokenType.CLOSE: 4 },
            2 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2, TokenType.CLOSE: 4 },
            3 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2, TokenType.CLOSE: 4 },
            4 : { TokenType.DIGIT : 1, TokenType.NON_DIGIT : 2}
        }
        self.num_ = []
        self.str_ = []
        self.stack_ = []

    @staticmethod
    def is_digit(achar):
        return achar.isdigit()
    @staticmethod
    def is_nondigit(achar):
        return not achar.isdigit()
    @staticmethod
    def is_open(achar):
        return achar == '['
    @staticmethod
    def is_close(achar):
        return achar == ']'

    def get_token(self, state, achar):
        if self.is_digit(achar):
            return TokenType.DIGIT

        if state ==1 and self.is_open(achar):
                return TokenType.OPEN

        if state in [1, 2, 3] and self.is_close(achar):
                return TokenType.CLOSE

        if self.is_nondigit(achar):
            return TokenType.NON_DIGIT

        return TokenType.NONE

    def get_next_state(self, state, achar):
        canditates = self.transition[state]
        token = self.get_token(state, achar)
        return canditates[token]


    def clean(self):
        self.num_ = []
        self.str_ = []

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
    (3, 1) : acts.add_num,
    (3, 2) : acts.add_str,
    (3, 4) : acts.pop_stack,
    (3, 7) : acts.,
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
        action = actions[(state, next_state)]
        action(item)
        state = next_state

    actions[(state, 7)]()
    result = acts.present()
    return result

def main():
    data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]', 'abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    data = ['abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    for item in data:
        print(item, expansion(item))

if __name__ == "__main__":
    main()
