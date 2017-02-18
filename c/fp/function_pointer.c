
#include <stdio.h>

typedef int (*BinaryIntType)(int,int) ;

int sum(int x,int y) { return x + y; }
int minus(int x, int y) { return x - y; }
int multiply(int x, int y) { return x * y; }
int divide(int x, int y) { return x / y; }

BinaryIntType  binary_function(char op) {
    switch (op) {
        case '+': return sum;
        case '-': return minus;
        case '*': return multiply;
        case '/': return divide;
    }
    return NULL;
}

int main(int argc,char *arv[]) {
    BinaryIntType f = binary_function('+');

    printf("%d\n",f(3,5));

    return 0;
}
