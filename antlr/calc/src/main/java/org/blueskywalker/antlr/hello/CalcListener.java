package org.blueskywalker.antlr.hello;

import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.blueskywalker.antlr.calc.CalculatorBaseListener;


/**
 * Created by jerrykim on 2/8/17.
 */
public class CalcListener extends CalculatorBaseListener {

    public CalcListener() {
    }

    @Override
    public void visitTerminal(@NotNull TerminalNode node) {
        super.visitTerminal(node);
        //System.out.println(node);
    }
}
