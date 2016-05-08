package org.blueskywalker.test;


import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Shift {

    static final String ADD="+";
    static final String SUBTRACT="-";
    static final String MULPLY="*";
    static final String DIVIDE="/";
    static final String LPAREN="(";
    static final String RPAREN=")";

    static final Map<String,Integer> precedence =
        new HashMap<String,Integer>();

    static {
        precedence.put(ADD,10);
        precedence.put(SUBTRACT,10);
        precedence.put(MULPLY,20);
        precedence.put(DIVIDE,20);
        precedence.put(LPAREN,5);
    }

    public class Tokenizer {
        final String input;
        int index;
        Pattern p = Pattern.compile("\\d+");

        public Tokenizer(String data) {
            this.input = data;
            this.index = 0;
        }

        public String token() throws Exception {
            if(index<input.length()) {
                switch(input.charAt(index)) {
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
                    index += m.end();
                    return m.group();
                case '+':
                    index++;
                    return ADD;
                case '-':
                    index++;
                    return SUBTRACT;
                case '*':
                    index++;
                    return MULPLY;
                case '/':
                    index++;
                    return DIVIDE;
                default:
                    throw new Exception("Syntax Error");
                }
            }
            return null;
        }
    }

    Stack<Integer> values;
    Stack<String> ops;

    public Shift() {
        values = new Stack<Integer>();
        ops = new Stack<String> ();
    }

    int calc(String op,int x, int y) {

        switch(op) {
        case ADD:
            return x + y;
        case SUBTRACT:
            return x - y;
        case MULPLY:
            return x * y;
        case DIVIDE:
            return x / y;
        }

        return 0;
    }

    public int reduce(String next) {

        while(ops.size()>0) {
            String token = ops.peek();

            if(token.equals(LPAREN)) {
                if (next.equals(RPAREN)) {
                    ops.pop();
                    break;
                } else {
                    break;
                }
            } else {
                if ( precedence.get(token) >= precedence.get(next)) {
                    ops.pop();
                    int y = values.pop();
                    int x = values.pop();
                    return calc(token,x,y);
                } else {
                    break;
                }
            }
        }
        return 0;
    }

    public int shift(String data) throws Exception {
        Tokenizer tokenizer = new Tokenizer(data);

        while(true) {
            String token = tokenizer.token();
            if (token==null)
                break;

            if (token.equals(ADD) ||
                token.equals(SUBTRACT) ||
                token.equals(MULPLY) ||
                token.equals(DIVIDE)) {
                reduce(token);
                ops.push(token);
            } else if (token.equals(LPAREN))
                ops.push(token);
            else if (token.equals(RPAREN)) {
                reduce(token);
            } else {
                values.push(Integer.valueOf(token));
            }
        }
        return 0;
    }

    public static void main(String [] args) {
        String test = " 3 + 4 * 3 + (45 / (5 + 4)) * 3 - 12";

        Shift eval = new Shift();

        try {
            int result = eval.shift(test);
            System.out.printf("%s = %d\n",test,result);

        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
