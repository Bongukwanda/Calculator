from __future__ import annotations
import math
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
  
  def __init__(self):
    self.operation = []
    self.equation = []
    self.check_equation = ""
    self.equation_answered = 0
  
  # calculation
  
  def clear_equation(self, clear_type: int) -> None:
    if clear_type:
      self.equation.clear()
    else:
      self.operation.clear()
      self.equation.clear()
  
  def calculate_answer(self, equation: str):
    self._get_operational_equation(equation)
    
    if not self._checks():
      return ""
    
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
    
    return True
  
  def _check_parenthesis(self, string_equation: str) -> bool:
    parenthesis = 0
    new_equation = ""
    
    for char in string_equation:
      if char == "(":
        parenthesis += 1
      elif char == ")":
        parenthesis -= 1
      else:
        new_equation += char
    
    if parenthesis == 0 or parenthesis == 1:
      self.check_equation = new_equation
      return True
    else:
      return False
  
  def _check_symbols(self) -> None:
    new_equation = ""
    equation = self.check_equation.strip()
    
    if not equation:
      return 
    
    for i in range(len(equation)):
      char = equation[i]
      if char == "." or char == ",":
        new_equation += "."
      elif char == " ":
        pass
      elif char == "π":
        new_equation += str(math.pi)
      else:
        new_equation += char
    
    self.check_equation = new_equation.lstrip()
  
  def _get_operational_equation(self, string_equation: str) -> None:
    check_braces = self._check_parenthesis(string_equation)
    if not check_braces:
      return
    
    self._check_symbols()
    
    string_equation = self.check_equation.strip()
    actual_number = ""
    
    for i in range(len(string_equation)):
      char = string_equation[i]
      
      if char in self.FUNCTIONS:
        try:
          self.operation.append(self.FUNCTIONS[char])
          self.equation.append(float(actual_number))
          actual_number = ""
        except ValueError:
          print("Weh")
      
      elif i == (len(string_equation)-1):
        if char in self.NUMBERS:
          actual_number += char
        self.equation.append(float(actual_number))
        actual_number = ""
      
      else:
        actual_number += char
  