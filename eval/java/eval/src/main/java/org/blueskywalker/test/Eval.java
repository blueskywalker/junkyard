package org.blueskywalker.test;



public class Eval {

    int operator_match(String data, String operators) throws SyntaxError {
        int inParen=0;

        for(int i=data.length()-1;i>-1;i--) {
            if (data.charAt(i)==')') {
                inParen++;
                continue;
            } else if (inParen>0 && data.charAt(i)=='(') {
                inParen--;
                continue;
            } else if (inParen==0 && data.charAt(i)=='(')
                throw new SyntaxError();

            for (int j=0;inParen==0 && j<operators.length();j++) {
                if (operators.charAt(j)==data.charAt(i))
                    return i;
            }
        }
        return -1;
    }

    int matched_parenthesis(String data) throws SyntaxError {
        int inParen=0;

        for(int i=0;i<data.length();i++) {
            if (data.charAt(i) == '(') {
                inParen++;
                continue;
            } else if (inParen > 0 && data.charAt(i) == ')') {
                inParen--;
                if (inParen==0)
                    return i;
                continue;
            } else if (inParen == 0 && data.charAt(i) == ')')
                throw new SyntaxError();
        }
        return -1;
    }

    public static class SyntaxError extends Exception {
        public SyntaxError() {
            super("Syntax Error");
        }
    }

    //
    // factor =  num | ( expr )
    //
    int factor(String data) throws SyntaxError {

        int index = data.indexOf('(');

        if (index==-1) {
            return Integer.valueOf(data.trim());
        } else {
            int endindex = matched_parenthesis(data);
            if (endindex==-1)
                throw new SyntaxError();

            return expr(data.substring(index+1,endindex));
        }
    }

    //
    // term =  factor [*|/] expr
    //
    int term(String data) throws SyntaxError {
        int index = operator_match(data,"*/");

        if (index==-1) {
            return factor(data);
        } else {
            if (data.charAt(index)== '*')
                return expr(data.substring(0,index)) * factor(data.substring(index+1,data.length()));
            else
                return expr(data.substring(0,index)) / factor(data.substring(index+1,data.length()));
        }
    }

    // expr = term [+|-] expr
    //
    public int expr(String data) throws SyntaxError {

        int index = operator_match(data,"+-");

        if (index==-1) {
            return term(data);
        } else {
            if (data.charAt(index)== '+')
                return expr(data.substring(0,index)) + term(data.substring(index+1,data.length()));
            else
                return expr(data.substring(0,index)) - term(data.substring(index+1,data.length()));
        }
    }

    public static void main(String [] args) {

        Eval evaluator = new Eval();

        String test = " 3 + 4 - 7 * 3 + (45 / (5 + 4)) * 3 - 12 ";

        try {
            int result = evaluator.expr(test);
            System.out.println(String.format("%s = %d",test,result));
        } catch (SyntaxError syntaxError) {
            syntaxError.printStackTrace();
        }


    }

}
