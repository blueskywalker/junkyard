package org.blueskywalker.antlr.hello;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.BaseErrorListener;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.RecognitionException;
import org.antlr.v4.runtime.Recognizer;
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.misc.Nullable;
import org.antlr.v4.runtime.tree.ParseTree;
import org.blueskywalker.antlr.calc.CalculatorLexer;
import org.blueskywalker.antlr.calc.CalculatorParser;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringBufferInputStream;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;

/**
 * Created by jerrykim on 2/8/17.
 */
public class Calc {

    public static void main(String[] args) throws IOException {

        //CalculatorLexer lexer = new CalculatorLexer(new ANTLRInputStream(System.in));
        String test = "3 + 4 - 5 * (12 / 4 + 5 -2) + 4 - 7 ";
        InputStream is = new ByteArrayInputStream(test.getBytes(StandardCharsets.UTF_8));
        CalculatorLexer lexer = new CalculatorLexer(new ANTLRInputStream(is));
        CalculatorParser parser = new CalculatorParser(new CommonTokenStream(lexer));

        parser.addErrorListener(new BaseErrorListener() {
            @Override
            public void syntaxError(@NotNull Recognizer<?, ?> recognizer, @Nullable Object offendingSymbol, int line, int charPositionInLine, @NotNull String msg, @Nullable RecognitionException e) {
                super.syntaxError(recognizer, offendingSymbol, line, charPositionInLine, msg, e);
                System.out.printf("%s,%d,%d,%s\n",offendingSymbol,line,charPositionInLine,msg);
            }
        });
        parser.addParseListener(new CalcListener());

        CalculatorBaseVisitorImpl visitor = new CalculatorBaseVisitorImpl();
        Double result = visitor.visit(parser.input());

        System.out.println(String.format("%s = %f",test,result));
    }
}
