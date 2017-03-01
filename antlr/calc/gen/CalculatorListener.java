// Generated from /Users/jerrykim/workspace/github/junkyard/antlr/calc/src/main/antlr4/org/blueskywalker/antlr/calc/Calculator.g4 by ANTLR 4.6
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalculatorParser}.
 */
public interface CalculatorListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#input}.
	 * @param ctx the parse tree
	 */
	void enterInput(CalculatorParser.InputContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#input}.
	 * @param ctx the parse tree
	 */
	void exitInput(CalculatorParser.InputContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#setVar}.
	 * @param ctx the parse tree
	 */
	void enterSetVar(CalculatorParser.SetVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#setVar}.
	 * @param ctx the parse tree
	 */
	void exitSetVar(CalculatorParser.SetVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#plusOrMinus}.
	 * @param ctx the parse tree
	 */
	void enterPlusOrMinus(CalculatorParser.PlusOrMinusContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#plusOrMinus}.
	 * @param ctx the parse tree
	 */
	void exitPlusOrMinus(CalculatorParser.PlusOrMinusContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#multOrDiv}.
	 * @param ctx the parse tree
	 */
	void enterMultOrDiv(CalculatorParser.MultOrDivContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#multOrDiv}.
	 * @param ctx the parse tree
	 */
	void exitMultOrDiv(CalculatorParser.MultOrDivContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#pow}.
	 * @param ctx the parse tree
	 */
	void enterPow(CalculatorParser.PowContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#pow}.
	 * @param ctx the parse tree
	 */
	void exitPow(CalculatorParser.PowContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#unaryMinus}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(CalculatorParser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#unaryMinus}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(CalculatorParser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculatorParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(CalculatorParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculatorParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(CalculatorParser.AtomContext ctx);
}