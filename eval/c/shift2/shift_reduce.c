#include "stack.h"
#include <ctype.h>

/*
// expr = term [+|-] expr
// term = factor [*|/] expr
// factor = num | ( expr )
// num = [0-9]+
// WS = " "+ // skip
// OP
*/

int add(int x, int y) { return x + y; }
int substract(int x, int y) { return x - y; }
int multiply(int x, int y) { return x * y; }
int divide(int x, int y) { return x / y;}

typedef enum symbol { END, NUM , ADD, SUBSTRACT, MULTIPLY, DIVIDE, LPAREN, RPAREN } Symbol;
const char *symbol_name [] = {"END","NUM","ADD","SUBSTRACT","MULTIPLY","DIVIDE","LPARAM","RPAREN"};
int precedence [] = { 0, 0, 10,10,50,50,5,5 };
int (*fn[])(int,int)= {NULL,NULL,add,substract,multiply,divide,NULL,NULL};

typedef struct token {
    Symbol type;
    int    value;
    char   *last;
} Token;


void print_token(Token token) {
    printf("[%s],",symbol_name[token.type]);
    if (token.type == NUM)
        printf("%d,",token.value);
    else
        printf("%c,",(char)token.value);

    printf("%s\n",token.last);
}

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

void syntax_error(char at) {
    printf("Syntax Error at %c\n",at);
    exit(1);
}

Token fill_token(Symbol type, char *data) {
    Token token;
    token.type = type;
    token.value = (int) *data;
    token.last = data+1;
    return token;
}

Token tokenize(char *data) {
    Token token;

    while(*data) {
        switch(*data) {
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
            return fill_token(ADD,data);
        case '-':
            return fill_token(SUBSTRACT,data);
        case '*':
            return fill_token(MULTIPLY,data);
        case '/':
            return fill_token(DIVIDE,data);
        case '(':
            return fill_token(LPAREN,data);
        case ')':
            return fill_token(RPAREN,data);
        default:
            printf("INVALID LITERAL-[%c]\n",*data);
            exit(-1);
        }
        data++;
    }

    token.type=END;
    token.last=data;
    return token;
}

static Stack *ops;
static Stack *values;

int reduce(int next_op) {
    while (ops->len>0) {
        int c_op = peek_stack(ops);
        if (c_op == LPAREN) {
            if (next_op == RPAREN)
                pop_stack(ops);
            break;
        } else if (precedence[c_op] >= precedence[next_op]) {
            int x,y;
            c_op = pop_stack(ops);
            y = pop_stack(values);
            x = pop_stack(values);
            //printf("%d %s %d\n",x,symbol_name[cOp],y);
            values = push_stack(values,fn[c_op](x,y));
        } else {
            break;
        }
    }
    return 0;
}

int shift_reduce(char *data) {
    Token token;

    while(*data) {
        token = tokenize(data);
        if (token.type == END) {
            reduce(token.type);
        } else if (token.type == LPAREN) {
            push_stack(ops,token.type);
        } else if (token.type == RPAREN) {
            reduce(token.type);
        } else if (token.type == NUM) {
            values = push_stack(values, token.value);
        } else {
            reduce(token.type);
            ops = push_stack(ops, token.type);
        }
        data = token.last;
    }

    return pop_stack(values);
}

int main(int argc,char *argv[]) {

    char *test_data=" 3 + 4 -2 * 3 + (45 / (5 + 4)) * 3 - 12 ";
    //char *test_data=" 3 + 4 * 3 + 45 / 5 + 4 * 3 - 12 ";

    ops = new_stack();
    values = new_stack();

    int result = shift_reduce(test_data);
    printf("%s = %d\n",test_data,result);

    free(ops);
    free(values);

    return 0;
}
