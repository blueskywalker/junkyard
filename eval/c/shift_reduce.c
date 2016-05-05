#include "stack.h"
#include <ctype.h>

// expr = term [+|-] expr
// term = factor [*|/] expr
// factor = num | ( expr )
// num = [0-9]+
// WS = " "+ // skip
// OP

typedef enum symbol { NONE, OP, NUM ,LPAREN, RPAREN } Symbol;

typedef struct token {
    Symbol type;
    int value;
    char *last;
} Token;


Token num_token(char *data) {
    char buffer[100];
    int len=0;
    Token token;

    while (*data && isdigit(*data)) {
        buffer[len++]=*data;
        data++;
    }

    token.type=NUM;
    buffer[len]=0;
    token.value=atoi(buffer);
    token.last=data;
    return token;
}

Token tokenzie(char *data) {
    Token token;
    int len=0;

    while(*data) {
        swtich(*data) {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            return num_token(data);
        case ' ':
            break;
        case '+':
        case '-':
        case '*':
        case '/':
            token.type = OP;
            token.value = (int)*data;
            token.last = data+1;
            return token;
        case '(':
            token.type = LPAREN;
            token.value = (int)*data;
            token.last = data+1;
            return token;
        case ')':
            token.type = RPAREN;
            token.value = (int)*data;
            token.last = data+1;
        default:
            printf("INVALID LITERAL\n");
            exit(-1);
        }
        data++;
    }

    token.type=NONE;
    token.last=data;
    return token;
}

static Stack *ops;
static Stack *values;

int reduce(int nextOp) {
    int cOp = pop_stack(ops);
    //if cOp > nextOp
    //   do reduce
    //else
    //   skip


}

int shift_reduce(char *data) {
    Token token;
    ops = new_stack();
    values = new_stack();

    while(*data) {
        token = tokenzie(data);

        if(token.type == NONE) {
            data = token.last;
            continue;
        }

        if(token.type==LPAREN) {
            continue;
        } else if (token.type == RPAREN) {
            continue;
        } else if (token.type == OP) {
            ops = push_stack(ops, token.value);
        } else if (token.type == NUM) {
            values = push_stack(values, token.value);
        }
        data=token.last;
    }

    free(ops);
    free(values);
    return 0;
}

int main(int argc,char *argv[]) {

    char *test_data=" 3 + 4 * 3 + (45 / (5 + 4)) * 3 - 12 ";

    int result = shift_reduce(test_data);
    printf("%s = %d\n",test_data,result);

    return 0;
}
