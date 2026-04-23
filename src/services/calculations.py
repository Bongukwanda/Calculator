from __future__ import annotations

class Calculations:
  
  BODMAS = {
    "PARENTHESIS":5,
    "DIVISION": 4,
    "MULTIPLICATION": 3,
    "ADDITION": 2,
    "SUBTRACTION": 1
  }
  
  def __init__(self):
    self.resultant = 0
  
  # ----- Calculation -----
  
  def add(self, equation: list) -> float:
    print(equation)
    return sum(equation)
  
  def subtract(self, equation: list) -> float:
    for index, value in enumerate(equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant -= value
    
    return self.resultant
  
  def mulitply(self, equation: list) -> float:
    for index, value in enumerate(equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant *= value
    
    return self.resultant
  
  def divide(self, equation: list) -> float:
    for index, value in enumerate(equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant /= value
    
    return self.resultant
  
  def exponentiate(self, equation: list) -> float:
    for index, value in enumerate(equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant **= value
    
    return self.resultant
  
  def pi_calculation(self, equation: list) -> str:
    raise NotImplementedError("Not implemented yet")
  
