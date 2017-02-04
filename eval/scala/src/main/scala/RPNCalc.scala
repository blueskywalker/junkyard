import scala.collection.mutable.Stack
import scala.io.Source
import java.lang.Double.parseDouble

/*
 *   RPN Calculator
 *
 *
 */

object RPNCalc {
  // Maps an operator to a function
  val ops = Map("+" -> ((_:Double) +(_:Double)),"-" -> (-(_:Double) + (_:Double)),
    "*" ->((_:Double) * (_:Double)),"/"->(1/(_:Double) *(_:Double)))

  // Evaluate RPN expr (given as string of tokens)
  def evalTokens(tokens: Array[String]) : Double = {
    val stack = new Stack[Double]
    tokens.foreach(tok => {
      if (ops.contains(tok)) stack.push(ops(tok)(stack.pop,stack.pop))
      else stack.push(parseDouble(tok)) })
    stack.pop
  }

  def main(args: Array[String]) = {
    // Read line by line from stdin + tokenize line + evaluates line
    println("type RPN rule")
    Source.fromInputStream(System.in).getLines.foreach(l => printf("exp=%2.2f\n",evalTokens(l.split(" "))))
  }

}
