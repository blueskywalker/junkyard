grammar Calculator;
INT    : [0-9]+;
DOUBLE : [0-9]+'.'[0-9]+;
PI     : 'pi';
E      : 'e';
POW    : '^';
NL     : '\n';
WS     : [ \t\r]+ -> skip;
ID     : [a-zA-Z_][a-zA-Z_0-9]*;

PLUS  : '+';
EQUAL : '=';
MINUS : '-';
MULT  : '*';
DIV   : '/';
LPAR  : '(';
RPAR  : ')';

input
    : setVar NL input
    | plusOrMinus NL? EOF
    ;

setVar
    : ID EQUAL plusOrMinus
    ;


plusOrMinus
    : plusOrMinus PLUS multOrDiv
    | plusOrMinus MINUS multOrDiv
    | multOrDiv
    ;

multOrDiv
    : multOrDiv MULT pow
    | multOrDiv DIV pow
    | pow
    ;

pow
    : unaryMinus (POW pow)?
    ;

unaryMinus
    : MINUS unaryMinus
    | atom
    ;

atom
    : PI
    | E
    | DOUBLE
    | INT
    | ID
    | LPAR plusOrMinus RPAR
    ;
