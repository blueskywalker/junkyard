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

typedef enum symbol { END, NUM , ADD, SUBSTRACT, MULTIPLY, DIVIDE, PAREN } Symbol;
const char *symbol_name [] = {"NONE","NUM","ADD","SUBSTRACT","MULTIPLY","DIVIDE","PARAM"};
int precedence [] = { 0, 0, 10,10,50,50,0 };
int (*fn[])(int,int)= {NULL,NULL,add,substract,multiply,divide,NULL,NULL};

typedef struct token {
    Symbol type;
    int value;
    int index;
} Token;


typedef struct string {
    int  len;
    char *start;
} String;

String make_string(int len,char *start) {
    String str;
    str.len = len;
    str.start = start;
    return str;
}

void print_token(Token token) {
    printf("[%s],",symbol_name[token.type]);
    if (token.type == NUM)
        printf("%d,",token.value);
    else
        printf("%c,",(char)token.value);

    printf("%d\n",token.index);
}

Token num_token(String data,int index) {
    char buffer[100];
    int len=0;
    Token token;

    while (index< data.len && isdigit(data.start[index])) {
        buffer[len++]=data.start[index++];
    }

    token.type=NUM;
    buffer[len]=0;
    token.value=atoi(buffer);
    token.index=index;
    return token;
}

void syntax_error(char at) {
    printf("Syntax Error at %c\n",at);
    exit(1);
}

Token paren_token(String data,int index) {
    int paren_cnt=0;
    Token token;

    while(index < data.len) {
        if (data.start[index]=='(') {
            if (paren_cnt==0)
                token.value=index;
            paren_cnt++;
        } else if (paren_cnt>0 && data.start[index]==')') {
            paren_cnt--;
            if (paren_cnt==0) {
                token.type = PAREN;
                token.index = ++index;
                return token;
            }
        } else if (paren_cnt==0 && data.start[index]==')') {
            syntax_error(data.start[index]);
        }
        index++;
    }
    syntax_error('(');
    token.type = END;
    token.index = index;
    return token;
}

Token fill_token(Symbol type,int value, int index) {
    Token token;
    token.type = type;
    token.value = value;
    token.index = index+1;
    return token;
}

Token tokenize(String data,int index) {
    Token token;
    char current;

    while(index<data.len) {
        current = data.start[index];
        switch(current) {
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
            return num_token(data,index);
        case ' ':
            break;
        case '+':
            return fill_token(ADD,(int)current,index);
        case '-':
            return fill_token(SUBSTRACT,(int)current,index);
        case '*':
            return fill_token(MULTIPLY,(int)current,index);
        case '/':
            return fill_token(DIVIDE,(int)current,index);
        case '(':
            return paren_token(data,index);
        case ')':
            syntax_error(data.start[index]);
        default:
            printf("INVALID LITERAL-[%c]\n",current);
            exit(-1);
        }
        index++;
    }

    token.type=END;
    token.index=index;
    return token;
}

static Stack *ops;
static Stack *values;

int reduce(int nextOp) {

    while (ops->len>0) {
        int cOp = pop_stack(ops);
        if (precedence[cOp] >= precedence[nextOp]) {
            if (cOp) {
                if(fn[cOp]!=NULL) {
                    int x,y;
                    y = pop_stack(values);
                    x = pop_stack(values);
                    values = push_stack(values,fn[cOp](x,y));
                } else {
                    printf("OP[%s]\n",symbol_name[cOp]);
                }
            }
        } else {
            ops=push_stack(ops,(Symbol)cOp);
            break;
        }
    }
    return 0;
}

int shift_reduce(String data) {
    Token token;
    int index=0;

    while(index<data.len) {
        token = tokenize(data,index);
        if (token.type == END) {
            reduce(token.type);
        } else if (token.type == PAREN) {
            String sub;
            sub.len = token.index - token.value - 2; /* () */
            sub.start = data.start + token.value + 1;
            push_stack(values,shift_reduce(sub));
        } else if (token.type == NUM) {
            values = push_stack(values, token.value);
        } else {
            reduce(token.type);
            ops = push_stack(ops, token.type);
        }
        index=token.index;
    }

    return pop_stack(values);
}

int main(int argc,char *argv[]) {

    char *test_data=" 3 + 4 * 3 + (45 / (5 + 4)) * 3 - 12 ";
    //char *test_data=" 3 + 4 * 3 + 45 / 5 + 4 * 3 - 12 ";

    ops = new_stack();
    values = new_stack();

    String data;
    data.len = strlen(test_data);
    data.start = test_data;
    int result = shift_reduce(data);
    printf("%s = %d\n",test_data,result);

    free(ops);
    free(values);

    return 0;
}
