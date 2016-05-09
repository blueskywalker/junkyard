package org.blueskywalker.test;


import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.regex.Pattern;
import java.util.regex.Matcher;



public class Shift {

    static enum Type {
        END,
        ADD,
        SUBTRACT,
        MULTIPLY,
        DIVIDE,
        LPAREN,
        RPAREN,
        NUM
    }

    static final Map<Type, Integer> precedence =
            new HashMap<>();

    static {
        precedence.put(Type.ADD, 10);
        precedence.put(Type.SUBTRACT, 10);
        precedence.put(Type.MULTIPLY, 20);
        precedence.put(Type.DIVIDE, 20);
        precedence.put(Type.LPAREN, 5);
        precedence.put(Type.RPAREN, 5);
        precedence.put(Type.END,0);
        precedence.put(Type.NUM,0);
    }

    static class Token {
        Type type;
        int value;

        public Token(Type type,int value) { this.type=type; this.value=value; }


        @Override
        public String toString() {
            return String.format("%s(%d)",type.name(),value);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Token token = (Token) o;

            return type == token.type;

        }

        @Override
        public int hashCode() {
            return type != null ? type.hashCode() : 0;
        }
    }

    public class Tokenizer {
        final String input;
        int index;
        Pattern p = Pattern.compile("\\d+");

        public Tokenizer(String data) {
            this.input = data;
            this.index = 0;
        }

        public Token token() throws Exception {
            while (index < input.length()) {
                switch (input.charAt(index)) {
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
                        Matcher m = p.matcher(input.substring(index));
                        m.find();
                        index += m.end();
                        return new Token(Type.NUM,Integer.valueOf(m.group()));
                    case '+':
                        index++;
                        return new Token(Type.ADD,0);
                    case '-':
                        index++;
                        return new Token(Type.SUBTRACT,0);
                    case '*':
                        index++;
                        return new Token(Type.MULTIPLY,0);
                    case '/':
                        index++;
                        return new Token(Type.DIVIDE,0);
                    case ' ':
                        index++;
                        break;
                    case '(':
                        index++;
                        return new Token(Type.LPAREN,0);
                    case ')':
                        index++;
                        return new Token(Type.RPAREN,0);
                    default:
                        throw new Exception("Syntax Error :" + input.charAt(index));
                }
            }
            return new Token(Type.END,0);
        }
    }

    Stack<Integer> values;
    Stack<Token> ops;

    public Shift() {
        values = new Stack<Integer>();
        ops = new Stack<Token>();
    }

    int calc(Token token, int x, int y) {

        switch (token.type) {
            case ADD:
                return x + y;
            case SUBTRACT:
                return x - y;
            case MULTIPLY:
                return x * y;
            case DIVIDE:
                return x / y;
        }

        return 0;
    }

    public void reduce(Token next) {

        while (ops.size() > 0) {
            Token token = ops.peek();

            if (token.type ==Type.LPAREN) {
                if (next.type==Type.RPAREN) {
                    ops.pop();
                    break;
                } else {
                    break;
                }
            } else {
                if (precedence.get(token.type) >= precedence.get(next.type)) {
                    ops.pop();
                    int y = values.pop();
                    int x = values.pop();
                    values.push(calc(token, x, y));
                } else {
                    break;
                }
            }
        }
    }

    public int shift(String data) throws Exception {
        Tokenizer tokenizer = new Tokenizer(data);

        while (true) {
            Token token = tokenizer.token();
            //System.out.println(token);
            if (token.type ==Type.END) {
                reduce(token);
                break;
            }

            if (token.type == Type.ADD ||
                    token.type ==Type.SUBTRACT ||
                    token.type == Type.MULTIPLY ||
                    token.type == Type.DIVIDE) {
                reduce(token);
                ops.push(token);
            } else if (token.type == Type.LPAREN)
                ops.push(token);
            else if (token.type == Type.RPAREN) {
                reduce(token);
            } else {
                values.push(token.value);
            }
        }
        return values.pop();
    }

    public static void main(String[] args) {
        String test = " 3 + 4 * 3 + (45 / (5 + 4)) * 3 - 12";

        Shift eval = new Shift();

        try {
            int result = eval.shift(test);
            System.out.printf("%s = %d\n", test, result);

        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
