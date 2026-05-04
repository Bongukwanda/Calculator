from __future__ import annotations

def add(equation: list) -> float:
  return sum(equation)

def subtract(equation: list) -> float:
  resultant = 0
  for index, value in enumerate(equation):
    if index == 0:
      resultant = value
    else:
      resultant -= value
  
  return resultant

def mulitply(equation: list) -> float:
  resultant = 0
  for index, value in enumerate(equation):
    if index == 0:
      resultant = value
    else:
      resultant *= value
  
  return resultant

def divide(equation: list) -> float:
  resultant = 0
  for index, value in enumerate(equation):
    if index == 0:
      resultant = value
    else:
      resultant /= value
  
  return resultant

def exponentiate(equation: list) -> float:
  resultant = 0
  for index, value in enumerate(equation):
    if index == 0:
      resultant = value
    else:
      resultant **= value
  
  return resultant

def pi_calculation(equation: list) -> str:
  raise NotImplementedError("Not implemented yet")

