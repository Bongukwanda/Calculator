from __future__ import annotations
from . import calculations as calc

class Operations:
  
  FUNCTIONS = {
    "+" : "add", 
    "-" : "subtract",
    "x" : "multiply", 
    "÷" : "divide", 
    "^" : "exponentiate"
  }
  NUMBERS = {"1","2","3","4","5","6","7","8","9","0"}
  BRACES = {"(": 1, ")": -1}
  
  def __init__(self):
    self.operation = []
    self.equation = []
    
    self._parenthesis = 0
    self.equation_answered = 0
  
  # calculation
  
  def clear_equation(self, clear_type: int) -> None:
    if clear_type:
      self.equation.clear()
    else:
      self.operation.clear()
      self.equation.clear()
  
  def calculate_answer(self, equation: str) -> float | int:
    self._get_operational_equation(equation)
    
    if not self._checks():
      return
    
    resultant = 0
    
    if "add" in self.operation:
      resultant = calc.add(self.equation)
    
    if "subtract" in self.operation:
      resultant = calc.subtract(self.equation)
    
    if "multiply" in self.operation:
      resultant = calc.mulitply(self.equation)
    
    if "divide" in self.operation:
      resultant = calc.divide(self.equation)
    
    if "exponentiate" in self.operation:
      resultant = calc.exponentiate(self.equation)
    
    if resultant % 1 == 0:
      resultant = int(resultant)
    
    return resultant
  
  # helpers
  
  def _checks(self) -> bool:
    
    if not len(self.operation):
      return False
    
    if not len(self.equation):
      return False
    
    if not self._parenthesis == 0:
      return False
    
    return True
  
  def _get_operational_equation(self, string_equation: str) -> None:
    string_equation = string_equation.strip()
    actual_number = ""
    
    for i in range(len(string_equation)):
      char = string_equation[i]
      
      if char in self.BRACES:
        self._parenthesis += self.BRACES[char]
      
      elif char in self.FUNCTIONS:
        self.operation.append(self.FUNCTIONS[char])
        self.equation.append(float(actual_number))
        actual_number = ""
      
      elif i == (len(string_equation)-1):
        if char in self.NUMBERS:
          actual_number += char
        
        self.equation.append(float(actual_number))
        actual_number = ""
      
      elif char == "." or char == ",":
        actual_number += "."
      
      elif char in self.NUMBERS:
        actual_number += char
      
      else:
        pass
  
  