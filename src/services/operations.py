from __future__ import annotations
from .calculations import Calculations

class Operations:
  
  def __init__(self, operation: list, equation: list):
    self.operation = operation
    self.equation = equation
    
    self.calc = Calculations()
  
  # calculation
  
  def addition(self) -> float:
    answer = self.calc.add(self.equation)
    return answer
  
  def subtraction(self) -> float:
    answer = self.calc.subtract(self.equation)
    return answer
  
  def mulitplication(self) -> float:
    answer = self.calc.mulitply(self.equation)
    return answer
  
  def division(self) -> float:
    answer = self.calc.divide(self.equation)
    return answer
  
  def exponentiation(self) -> float:
    answer = self.calc.exponentiate()
    return answer
  
  # calculator functions
  
  def press_operator(self, key: str) -> str:
    
    match key:
      case "+":
        self.operation.append("add")
        function_key = "add"
      case "-":
        self.operation.append("subtract")
        function_key = "subtract"
      case "x":
        self.operation.append("multiply")
        function_key = "multiply"
      case "÷":
        self.operation.append("divide")
        function_key = "divide"
      case "π":
        self.operation.append("pi")
        function_key = "pi"
      case "^":
        self.operation.append("exponentiate")
        function_key = "exponentiate"
      case "(":
        self._parenthesis += 1
      case ")":
        self._parenthesis -= 1
      case _:
        pass
    
    return function_key
  