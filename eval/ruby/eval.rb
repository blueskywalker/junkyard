#!/usr/bin/env ruby

def basic(line)
  p line.scan(/\w+/)
end


ARGF.each do |line|
  basic line
end
