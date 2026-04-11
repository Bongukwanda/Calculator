class Operations:
  
  BODMAS = {
    "PARENTHESIS":5,
    "DIVISION": 4,
    "MULTIPLICATION": 3,
    "ADDITION": 2,
    "SUBTRACTION": 1
  }
  
  def __init__(self, equation: list):
    self.equation = equation
    self.resultant = 0
  
  # ----- Calculation -----
  
  def add(self) -> float:
    self.resultant = sum(self.equation)
    return self.resultant
  
  def subtract(self) -> float:
    for index, value in enumerate(self.equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant -= value
    
    return self.resultant
  
  def mulitply(self) -> float:
    for index, value in enumerate(self.equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant *= value
    
    return self.resultant
  
  def divide(self) -> float:
    for index, value in enumerate(self.equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant /= value
    
    return self.resultant
  
  def exponentiate(self) -> float:
    for index, value in enumerate(self.equation):
      if index == 0:
        self.resultant += value
      else:
        self.resultant **= value
    
    return self.resultant
  
  def pi_calculation(self) -> str:
    print("pi not calclulated yet")
    return 0
  
  # ----- BODMAS -----
  
  def operation_order(self, equation: dict):
    for bodmas_attribute in self.BODMAS:
      for key in equation:
        if key == bodmas_attribute:
          print(self.BODMAS[bodmas_attribute])
  
  # ----- Resultant -----
  
  def output_resultant(self, operation: dict) -> float:
    
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
  


'''
dict = {
  "add": [1],
  "parenthesis": [],
  "subtract": [9,5],
  "parenthesis": []
}
'''
