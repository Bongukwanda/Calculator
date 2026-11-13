import math
import operator

BODMAS = {
  "b": 0,
  "÷": 1,
  "x": 2,
  "+": 3,
  "-": 4
}

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
  "(" : None,
  ")" : None
}
