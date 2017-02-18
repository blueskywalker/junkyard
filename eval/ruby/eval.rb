#!/usr/bin/env ruby

def basic(line)
  p line.scan(/\w+/)
end

#
#  Token Definition
#
class Tokendef
  def initialize(reg, name, funcdef = nil)
    @reg = reg
    @name = name
    @funcdef = funcdef
  end
end

#
# Calculator Lexer Class
#
class CLexer
  def initialize(definition)
    @tokendef = definition
  end
end

def main
  test = ' 1 + 3 - 5 * 3 +10 - (20 / 4 +3) * 3'
  mat = /^\d+/.match(test)
  p mat.post_match if mat
end

main
