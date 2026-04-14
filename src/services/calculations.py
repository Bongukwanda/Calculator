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
    print("Calculations - self.equation: ", equation)
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
    print("pi not calclulated yet")
    return 0
  
  
  # ----- Resultant -----
  
  def calculate_result(self, operation: dict) -> float:
    
    for ops, values in operation:
      match ops:
        case "add":
          self.resultant = sum(values)
        case _:
          pass
    
    return self.resultant
  
  # ----- Helper ----
  
  def is_number(self, value) -> bool:
    try:
      float(value)
      return True
    except ValueError:
      return False
  
