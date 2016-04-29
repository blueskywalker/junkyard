package org.blueskywalker.test;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by kkim on 3/26/16.
 */
public class Calc {


    public static List<String> tokenizer(String input) throws Exception {
        List<String> tokens = new ArrayList<>();

        StringBuilder sb = new StringBuilder();

        for (char c : input.toCharArray()) {
            switch (c) {
            case ' ':
                if (sb.length() > 0) {
                    tokens.add(sb.toString());
                    sb.setLength(0);
                }
                break;
            case '+':
            case '-':
            case '*':
            case '/':
            case '(':
            case ')':
                if (sb.length() > 0) {
                    tokens.add(sb.toString());
                    sb.setLength(0);
                }
                tokens.add(String.valueOf(c));
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
                sb.append(c);
                break;
            default:
                throw new Exception("Illegal Character");
            }
        }

        if (sb.length() > 0)
            tokens.add(sb.toString());

        return tokens;
    }

    public static boolean isNum(String token) {
        try {
            Integer.parseInt(token);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static int findParenthesis(List<String> tokens,int start, int end) throws Exception {
        if(tokens.get(start).equals("(")) {
            for(int i=start+1;i<end;i++)
                if(tokens.get(i).equals(")"))
                    return i;

            throw new Exception("Not Matched Parenthsis");
        }
        return -1;
    }

    public static int findTerm(List<String> tokens) throws Exception {
        for(int i=0;i<tokens.size();i++) {
            int paren = findParenthesis(tokens,i,tokens.size());
            if (paren>0) {
                i = paren;
                continue;
            }
            if (tokens.get(i).equals("+") ||
                tokens.get(i).equals("-"))
                return i;
        }
        return -1;
    }

    public static int findFactor(List<String> tokens) throws Exception {
        for(int i=0;i<tokens.size();i++) {
            int paren = findParenthesis(tokens,i,tokens.size());
            if (paren>0) {
                i = paren;
                continue;
            }
            if (tokens.get(i).equals("*") ||
                tokens.get(i).equals("/"))
                return i;
        }
        return -1;
    }

    //
    // exp    -> term   [ (+|-)  exp ]
    // term   -> factor [ (*|/)  exp ]
    // factor -> num | ( exp )

    public static int exp(List<String> tokens) throws Exception {
        //System.out.printf("exp:%s\n",tokens);

        int op=findTerm(tokens);

        if (op<0)
            return term(tokens);

        if (tokens.get(op).equals("+"))
            return term(tokens.subList(0,op)) + exp(tokens.subList(op+1,tokens.size()));

        return term(tokens.subList(0,op)) - exp(tokens.subList(op+1,tokens.size()));
    }


    public static int term(List<String> tokens) throws Exception {
        //System.out.printf("factor:%s\n",tokens);

        int op = findFactor(tokens);

        if (op<0)
            return factor(tokens);

        if (tokens.get(op).equals("*"))
            return factor(tokens.subList(0,op)) * exp(tokens.subList(op+1,tokens.size()));

        return factor(tokens.subList(0,op)) / exp(tokens.subList(op+1,tokens.size()));
    }

    public static int factor (List<String> tokens) throws Exception {
        //System.out.printf("term:%s\n",tokens);

        if(tokens.size()>0) {
            int paren = findParenthesis(tokens, 0, tokens.size());

            if (paren > 0)
                return exp(tokens.subList(1, paren));

            try {
                return Integer.parseInt(tokens.get(0));
            } catch (Exception e) {
                throw new Exception("Syntax Error");
            }
        }
        else
            throw new Exception("Syntax Error");
    }

    public static void main(String[] args) {
        try {
            String test = " 3 + 4 * 3 + (50 / 5 + 4) * 3 - 12 ";
            List<String> tokens = Calc.tokenizer(test);
            System.out.println(String.format("%s = %d",test,Calc.exp(tokens)));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
