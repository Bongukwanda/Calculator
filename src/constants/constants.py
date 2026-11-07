import math
import operator

FUNCTIONS = {
  "+" : operator.add, 
  "-" : operator.sub,
  "x" : operator.mul, 
  "÷" : operator.truediv, 
  "^" : operator.pow,
  "%" : operator.mod,
  "√" : lambda a: math.sqrt(a)
}

NUM_STRUCTURE = {
  "+/-" : operator.inv,
  "(" : "paren left",
  ")" : "paren right"
}
