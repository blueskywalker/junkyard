/*
 * calc.c
 *
 *  Created on: Apr 29, 2016
 *      Author: kkim
 */


#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdarg.h>

typedef enum {
    ADD,
    MULTIPLY,
    SUBTRACT,
    DIVIDE,
    LPAREN,
    RPAREN,
    NUM
} Type;

typedef union {
    int  num;
    char op;
} Value;

typedef struct {
    Type  type;
    Value value;
} Token;

typedef struct Node{
    Token token;
    struct Node * prev;
    struct Node * next;
} Node;

typedef struct List {
    Node *head;
    Node *tail;
} List;

typedef struct {
    int  length;
    char value[512];
} StringBuffer;

void memory_allocation_error() {
    fprintf(stderr,"memory allocation error");
    exit(-1);
}


void * check_null(void *value) {
    if(!value)
        memory_allocation_error();
    return value;
}

#define new_of(TYPE) (TYPE*) check_null(calloc(1,sizeof(TYPE)))

Node *new_node() {
    return new_of(Node);
}

List *new_list() {
    return new_of(List);
}


Node *nodedup(Node *node) {
    Node *new = new_node();
    new->token= node->token;
    return new;
}


void node_memory_free(Node *node) {
    if (node==NULL)
        return;
    free(node);
}

void list_memory_free(List *list) {
    Node *node = NULL;
    Node *next = NULL;

    if(list==NULL)
        return;

    node = list->head;

    while(node!=NULL) {
        next = node->next;
        node_memory_free(node);
        node = next;
    }

    free(list);
}

void list_insert_node(List *self,Node *node) {
    if (self==NULL || node==NULL)
        return;

    if (self->tail==NULL) {
        assert(self->head==NULL);
        self->head = node;
        self->tail = node;
    } else {
        node->prev = self->tail;
    	self->tail->next = node;
        self->tail=node;
    }
}

void list_push_node(List *self,Node *node) {
    if (self==NULL || node==NULL)
        return;

    if (self->tail==NULL) {
        assert(self->head==NULL);
        self->head = node;
        self->tail = node;
    } else {
    	node->next = self->head;
    	self->head = node;
    }

}
Node *list_popup_node(List *self) {
    Node *ret=NULL;

    if (self==NULL || self->head==NULL) {
        return NULL;
    }
    ret = self->head;

    self->head = ret->next;
    return ret;
}

void list_insert_value(List *self,Token token) {
    Node *node;
    if(self == NULL)
        return;

    node = new_node();
    node->token = token;
    list_insert_node(self,node);
}

#define append list_insert_value

void add_token(List *tokens,StringBuffer *buffer,Type type) {
    Token token;
    token.type = type;

    switch(type) {
    case NUM:
        if (buffer->length>0) {
            buffer->value[buffer->length]=0;
            token.value.num = atoi(buffer->value);
            buffer->length=0;
            append(tokens,token);
        }
        break;
    case ADD:
        token.value.op = '+';
        append(tokens,token);
        break;
    case SUBTRACT:
        token.value.op = '-';
        append(tokens,token);
        break;
    case MULTIPLY:
        token.value.op = '*';
        append(tokens,token);
        break;
    case DIVIDE:
        token.value.op = '/';
        append(tokens,token);
        break;
    case LPAREN:
        token.value.op = '(';
        append(tokens,token);
        break;
    case RPAREN:
        token.value.op = ')';
        append(tokens,token);
        break;
    }
}

void print_token(Token token) {
    if(token.type==NUM) {
        printf("NUM[%d]",token.value.num);
    } else {
        printf("OP[%c]",token.value.op);
    }
}

void print_list(FILE *out,List *list) {
    Node *node=NULL;

    if(out==NULL || list==NULL)
        return;

    node=list->head;
    fprintf(out,"[");
    while(node!=NULL) {
        print_token(node->token);
        node = node->next;
        if(node!=NULL) {
            fprintf(out,",");
        }
    }
    fprintf(out,"]");
}

void print_reverse_list(FILE *out,List *list) {
    Node *node=NULL;

    if(out==NULL || list==NULL)
        return;

    node=list->tail;
    fprintf(out,"[");
    while(node!=NULL) {
        print_token(node->token);
        node = node->prev;
        if(node!=NULL) {
            fprintf(out,",");
        }
    }
    fprintf(out,"]");
}


List * tokenizing(char *input) {
    List *tokens=new_list();
    char *ch=input;
    StringBuffer buffer;

    while(*ch) {
        switch(*ch) {
        case ' ':
            add_token(tokens,&buffer,NUM);
            break;
        case '+':
            add_token(tokens,&buffer,NUM);
            add_token(tokens,NULL,ADD);
            break;
        case '-':
            add_token(tokens,&buffer,NUM);
            add_token(tokens,NULL,SUBTRACT);
            break;
        case '*':
            add_token(tokens,&buffer,NUM);
            add_token(tokens,NULL,MULTIPLY);
            break;
        case '/':
            add_token(tokens,&buffer,NUM);
            add_token(tokens,NULL,DIVIDE);
            break;
        case '(':
            add_token(tokens,&buffer,NUM);
            add_token(tokens,NULL,LPAREN);
            break;
        case ')':
            add_token(tokens,&buffer,NUM);
            add_token(tokens,NULL,RPAREN);
            break;
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
            buffer.value[buffer.length++]=*ch;
            break;
        default:
            printf("ERROR : WRONG CHARACTER");
            exit(-1);
        }
        ch++;
    }
    return tokens;
}

Node *findParen(List *list) {
    Node *node=NULL;
    node=list->head;

    assert(node->token.type==LPAREN);
    node = node->next;

    while(node!=list->tail) {
        if(node->token.type == RPAREN) {
            return node;
        }
        node=node->next;
    }
    return node;
}

Node *find_factor(List *list) {
    Node *node;
    List tmp;

    if(list==NULL)
        return NULL;

    node = list->head;
    while(node!=list->tail) {
        switch (node->token.type) {
        case NUM:
            break;
        case MULTIPLY:
        case DIVIDE:
            return node;
        case LPAREN:
            tmp.head = node;
            tmp.tail = list->tail;
            node = findParen(&tmp);
            if(node==list->tail)
                return node;
            break;
        case ADD:
        case SUBTRACT:
            break;
        case RPAREN:
            break;
        }
        node = node->next;
    }
    return node;
}

Node *find_term(List *list) {
    Node *node;
    List tmp;

    if(list==NULL)
        return NULL;

    node = list->head;
    while(node!=list->tail) {
        switch (node->token.type) {
        case NUM:
        case MULTIPLY:
        case DIVIDE:
            break;
        case LPAREN:
            tmp.head = node;
            tmp.tail = list->tail;
            node = findParen(&tmp);
            if(node==list->tail)
                return node;
            break;
        case ADD:
        case SUBTRACT:
            return node;
        case RPAREN:
            break;
        }
        node = node->next;
    }
    return node;
}


void debug_msg(const char *msg,List *tokens) {
    printf("%s",msg);
    if(tokens) print_list(stdout,tokens);
    printf("\n");
}

#ifdef DEBUG
#define debug_print(m,t) debug_msg(m,t)
#else
#define debug_print(m,t)
#endif

int expr(List *);

/*
 *  factor :=  NUM | ( expr )
 *
 */

int factor(List *tokens) {

    if(tokens==NULL)
        return 0;

    debug_print("factor",tokens);

    if (tokens->head->token.type == LPAREN &&
        tokens->tail->token.type == RPAREN) {
        List paren;
        paren.head = tokens->head->next;
        paren.tail = tokens->tail->prev;
        return expr(&paren);
    }

    if (tokens->head->token.type == NUM) {
        return tokens->head->token.value.num;
    }

    fprintf(stderr,"Syntax Error");
    exit(1);
    return 0;
}

/*
 * term = factor(tokens) [*|/] expr(tokens)
 */

int term(List *tokens) {
    Node *node=NULL;
    List left,right;

    if(tokens==NULL)
        return 0;

    debug_print("term",tokens);

    node = find_factor(tokens);

    if(node==tokens->tail) {
        return factor(tokens);
    }

    left.head=tokens->head;left.tail=node->prev;left.tail->next=NULL;
    right.head=node->next;right.tail=tokens->tail;

    if(node->token.type==MULTIPLY) {
        debug_print("factor * expr",NULL);
        return factor(&left) * expr(&right);
    } else if (node->token.type==DIVIDE) {
        debug_print("factor / expr",NULL);
        return factor(&left) / expr(&right);
    } else {
        fprintf(stderr,"SYNTAX ERROR\n");
        exit(1);
    }

    return 0;
}


/*
 *  expr -> term [(+|-)] exp
 *
 */


int expr(List *tokens) {
    Node *node=NULL;
    List left,right;

    if(tokens==NULL)
        return 0;

    debug_print("expr",tokens);

    node = find_term(tokens);

    if(node==tokens->tail) {
        return term(tokens);
    }

    left.head=tokens->head;left.tail=node->prev;left.tail->next=NULL;
    right.head=node->next;right.tail=tokens->tail;

    if(node->token.type==ADD) {
        debug_print("term + expr",NULL);
        return term(&left) + expr(&right);
    } else if (node->token.type==SUBTRACT) {
        debug_print("term - expr",NULL);
        return term(&left) - expr(&right);
    } else {
        fprintf(stderr,"SYNTAX ERROR\n");
        exit(1);
    }

    return 0;
}

int main(int argc,char *argv[])
{
    char *test_data=" 13 + 14 - 4 + 11 * 3 + (50 / 5 + 4) * 3 - 12 ";
    List *tokens = tokenizing(test_data);
    int result;

    //print_list(stdout,tokens);
    result = expr(tokens);

    printf("%s = %d\n",test_data,result);
    list_memory_free(tokens);
    return 0;
}
