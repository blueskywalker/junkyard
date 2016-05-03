/*
 * eval.c
 *
 *  Created on: May 3, 2016
 *      Author: kkim
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef int Bool;
#define TRUE 1
#define FALSE 0

typedef struct string {
    int  len;
    char *start;
} String;


int Strchar(String data, char ch) {
    int i;

    for(i=0;i<data.len;i++) {
        if (data.start[i]==ch)
            return i;
    }

    return -1;
}

int operator_match(String data,char *tokens) {
    int len=strlen(tokens);
    int index=0,i=0;
    int NotInParen=1;

    for(index=0;index<data.len;index++) {
    	if(NotInParen && data.start[index]=='('){
            NotInParen=0;
            continue;
    	} else if (!NotInParen && data.start[index]==')') {
            NotInParen=1;
            continue;
    	}

        for(i=0;NotInParen && i<len;i++) {
            if (data.start[index] == tokens[i])
                return index;
        }
    }
    return -1;
}


void syntax_error(int lineno) {
    printf("SYNTAX ERRPR - %d\n",lineno);
    exit(1);
}


void debug_print(char *prefix,String data) {
    char buffer[1024];
    memcpy(buffer,data.start,data.len);
    buffer[data.len]=0;
    printf("%s-%s\n",prefix,buffer);
}

#ifdef DEBUG
#define debugprint(P,S) debug_print(P,S)
#else
#define debugprint(P,S)
#endif

int expr(String data);


// num = [0-9]
// WS = skip
//
int num(String data) {
    int i=0;
    char buffer[100];
    int len=0;

    debugprint("num",data);

    while(i<data.len && data.start[i]==' ')
        i++;
    while (i<data.len && isdigit(data.start[i])) {
        buffer[len++]=data.start[i++];
    }
    while(i<data.len && data.start[i]==' ')
        i++;

    if (i<data.len) {
        syntax_error(__LINE__);
    }
    buffer[len]=0;
    return atoi(buffer);
}

// factor = NUM | ( expr )

int factor (String data) {
    int index=0;
    debugprint("factor",data);

    index = Strchar(data,'(');

    if (index==-1)
        return num(data);
    else {
        String subexpr;
        subexpr.start = data.start+index+1;
        subexpr.len = data.len - index -1;
        index = Strchar(subexpr,')');

        if (index==-1) {
            syntax_error(__LINE__);
        } else {
            subexpr.len = index;
            return expr(subexpr);
        }
    }
    return 0;
}

// term = factor [*|/] expr

int term(String data) {
    int index=0;
    String left,right;

    debugprint("term",data);

    index=operator_match(data,"*/");

    if(index ==-1)
        return factor(data);
    else {
        left.start = data.start;
        left.len = index;
        right.start = data.start+index+1;
        right.len = data.len - index-1;

        if (data.start[index]=='*') {
            return factor(left) * expr(right);
        } else {
            return factor(left) / expr(right);
        }
    }

    return 0;
}

// expr = term [+|-] expr
int expr(String data) {
    int index=0;
    String left,right;

    debugprint("expr",data);

    index=operator_match(data,"+-");

    if(index ==-1)
        return term(data);
    else {
        left.start = data.start;
        left.len = index;
        right.start = data.start+index+1;
        right.len = data.len - index-1;

        if (data.start[index]=='+') {
            return term(left) + expr(right);
        } else {
            return term(left) - expr(right);
        }
    }
}

int main(int argc,char *argv[])
{
    char *test_data=" 3 + 4 * 3 + (50 / 5 + 4) * 3 - 12 ";

    int result;

    //print_list(stdout,tokens);
    String data;
    data.len = strlen(test_data);
    data.start=test_data;
    result = expr(data);

    printf("%s = %d\n",test_data,result);

    return 0;
}
