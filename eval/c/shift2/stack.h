#ifndef _MY_STACK_H_
#define _MY_STACK_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stack {
    size_t size;
    size_t len;
    int data;
} Stack;

extern Stack * new_stack();
extern Stack * push_stack(Stack *stack,int value);
extern int pop_stack(Stack *stack);
extern int peek_stack(Stack *stack);
extern void print_stack(Stack *stack);

#endif /*_MY_STACK_H_*/
