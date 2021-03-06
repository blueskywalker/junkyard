#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "stack.h"

static void *check_malloc(size_t size) {
    void *ret = malloc(size);

    if(ret==NULL) {
        fprintf(stderr,"Memmory Allocation Error\n");
        exit(-1);
    }

    return ret;
}

#define new_object(T,S) (T*) check_malloc(S)
#define EXPAND_SIZE  1024
#define stack_mem_size(S) (S + 2*sizeof(size_t))

Stack * new_stack() {
    Stack *new = new_object(Stack,stack_mem_size(EXPAND_SIZE));
    new->size = EXPAND_SIZE;
    new->len = 0;
    return new;
}

Stack * push_stack(Stack *stack,int value) {
    Stack *new;
    if (stack->len == stack->size) {
        size_t new_size = stack->size + EXPAND_SIZE;
        new = new_object(Stack,new_size);
        memcpy(new,stack,stack_mem_size(new_size));
        free(stack);
        stack=new;
    }
    (&(stack->data))[stack->len++] = value;

    return stack;
}

int pop_stack(Stack *stack) {

    if(stack->len>0) {
        return (&(stack->data))[--(stack->len)];
    }
    return -1;
}

int peek_stack(Stack *stack) {
    if(stack->len>0) {
        return (&(stack->data))[stack->len-1];
    }
    return -1;
}

void print_stack(Stack *stack) {
    int i;

    printf("[");
    for(i=0;i<stack->len;i++) {
        printf("%d",(&stack->data)[i]);
        if (i < stack->len-1)
            printf(",");
    }
    printf("]\n");
}


//#define TEST_MAIN_
#ifdef TEST_MAIN_
int main(int argc, char *aragv[]) {

    Stack *test = new_stack();

    test = push_stack(test, 1);
    test = push_stack(test, 2);
    test = push_stack(test, 3);
    test = push_stack(test, 4);
    test = push_stack(test, 5);


    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));
    printf("%d\n",pop_stack(test));

    return 0;
}
#endif /*TEST_MAIN_*/
