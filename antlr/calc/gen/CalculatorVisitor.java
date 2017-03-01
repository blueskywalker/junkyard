// Generated from /Users/jerrykim/workspace/github/junkyard/antlr/calc/src/main/antlr4/org/blueskywalker/antlr/calc/Calculator.g4 by ANTLR 4.6
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CalculatorParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CalculatorVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#input}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInput(CalculatorParser.InputContext ctx);
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#setVar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetVar(CalculatorParser.SetVarContext ctx);
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#plusOrMinus}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPlusOrMinus(CalculatorParser.PlusOrMinusContext ctx);
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#multOrDiv}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultOrDiv(CalculatorParser.MultOrDivContext ctx);
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#pow}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPow(CalculatorParser.PowContext ctx);
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#unaryMinus}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryMinus(CalculatorParser.UnaryMinusContext ctx);
	/**
	 * Visit a parse tree produced by {@link CalculatorParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(CalculatorParser.AtomContext ctx);
}