from __future__ import annotations

import re
import math
from .calculations import Calculations

class Operations:
  
  FUNCTIONS = {
    "+" : "add", 
    "-" : "subtract",
    "x" : "multiply", 
    "÷" : "divide", 
    "^" : "exponentiate"
  }
  
  KEYS = {"π", "(", ")"}
  
  def __init__(self):
    self.calc = Calculations()
    
    # Calculation list
    self.operation = []
    self.equation = []
    
    # Calculation variables
    self._parenthesis = 0
    self.equation_answered = False
    self.equation_cleared = True
  
  # calculation
  
  def addition(self) -> float:
    return self.calc.add(self.equation)
  
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
    answer = self.calc.exponentiate(self.equation)
    return answer
  
  # calculator functions
  
  def clear_basic(self, clearance: str) -> None:
    if clearance:
      self.operation.clear()
      self.equation.clear()
    else:
      self.equation.clear()
  
  def press_number(self) -> None:
    if self.equation_answered:
      self.clear_basic()
      self.equation_answered = False
  
  def press_operator(self, key: str, entered_number: float) -> None:
    if self.equation_answered:
      number = float(entered_number)
      self.equation.append(number)
      self.equation_answered = False
    
    else:
      self.equation.append(entered_number)
    
    try:
      self.operation.append(self.FUNCTIONS[key])
    except Exception:
      return
  
  def press_key(self, key: str):
    if key not in self.KEYS:
      return
    
    if key == "(":
      self._parenthesis += 1
    
    elif key == ")":
      self._parenthesis -= 1
    
    else:
      self.equation.append(math.pi)
  
  def press_equal(self, entered_number: str | None = None) -> float:
    print("entered number: ", entered_number)
    if entered_number is not None:
      entered_number = self._remove_parenthesis(entered_number)
      self.equation.append(entered_number)
    
    if not self._checks():
      return
    
    resultant = 0
    
    if "add" in self.operation:
      resultant = self.addition()
    
    if "subtract" in self.operation:
      resultant = self.subtraction()
    
    if "multiply" in self.operation:
      resultant = self.mulitplication()
    
    if "divide" in self.operation:
      resultant = self.division()
    
    if "exponentiate" in self.operation:
      resultant = self.exponentiation()
    
    return resultant
  
  # helpers
  
  def function(self, key: str) -> None:
    if len(self.my_dict) == 0:
      self.my_dict[key] = [value for value in self.my_equation]
    else:
      temp_list = self.my_dict[key]
      for value in self.my_equation:
        temp_list.append(value)
      self.my_dict[key] = temp_list
  
  def _parenthesis_check(self) -> bool:
    if self._parenthesis == 0:
      return True
    
    return False
  
  def _checks(self) -> bool:
    
    if not len(self.operation):
      return False
    
    if not len(self.equation):
      return False
    
    return True
  
  def _remove_parenthesis(self, value: str) -> float:
    value_split = re.findall("[0-9]", value)
    new_value = ""
    for char in value_split:
      new_value += char
    
    return float(new_value)
  