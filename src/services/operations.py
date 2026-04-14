from __future__ import annotations
from .calculations import Calculations

class Operations:
  
  def __init__(self, operation: list, equation: list):
    self.calc = Calculations()
    
    # Calculation list
    self.operation = operation
    self.equation = equation
    
    # Calculation variables
    self._parenthesis = 0
    self.equation_answered = False
  
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
    answer = self.calc.exponentiate()
    return answer
  
  # calculator functions
  
  def clear_basic(self, clearance: str = "") -> None:
    if not clearance:
      self.operation.clear()
      self.my_equation.clear()
    else:
      self.my_equation.clear()
  
  def press_number(self, number: int) -> None:
    if self.equation_answered:
      self.clear_basic()
      self.equation_answered = False
    
    self.equation.append(number)
  
  def press_operator(self, key: str, previous_answer:float = 0) -> None:
    if self.equation_answered:
      number = float(previous_answer)
      self.equation.append(number)
      self.equation_answered = False
    
    match key:
      case "+":
        self.operation.append("add")
      case "-":
        self.operation.append("subtract")
      case "x":
        self.operation.append("multiply")
      case "÷":
        self.operation.append("divide")
      case "π":
        self.operation.append("pi")
      case "^":
        self.operation.append("exponentiate")
      case "(":
        self._parenthesis += 1
      case ")":
        self._parenthesis -= 1
      case _:
        pass
  
  def press_equal(self) -> float:
    if not self._checks():
      return
    
    resultant = 0
    
    print("Operations - self.operation: ", self.operation)
    
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
      
    print("Press Equal Operations = ", resultant)
    return resultant
  
  # helpers
  
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
  
  def function(self, key: str) -> None:
    if len(self.my_dict) == 0:
      self.my_dict[key] = [value for value in self.my_equation]
    else:
      temp_list = self.my_dict[key]
      for value in self.my_equation:
        temp_list.append(value)
      self.my_dict[key] = temp_list
  
  