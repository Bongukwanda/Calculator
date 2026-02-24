class Calculate:
  
  def add(self, number_1:float, number_2:float) -> float:
    addition_result = number_1 + number_2
    return addition_result
  
  def subtract(self, number_1:float, number_2:float) -> float:
    subtraction_result = number_1 - number_2
    return subtraction_result
  
  def multiply(self, number_1:float, number_2:float) -> float:
    multiplication_result = number_1 * number_2
    return multiplication_result
  
  def divide(self, number_1:float, number_2:float) -> float:
    dividend = number_1 / number_2
    return dividend

class CalculateCommand:
  pass

class CalculateAddition(CalculateCommand):
  def __init__(self):
    super().__init__()
    self.calculator = Calculate()
  
  def execute(self, num_1, num_2):
    return self.calculator.add(num_1, num_2)

class CalculateSubtraction(CalculateCommand):
  def __init__(self):
    super().__init__()
    self.calculator = Calculate()
  
  def execute(self, num_1, num_2):
    return self.calculator.subtract(num_1, num_2)

class CalculateMultiplication(CalculateCommand):
  def __init__(self):
    super().__init__()
    self.calculator = Calculate
  
  def execute(self, num_1, num_2):
    return self.calculator.multiply(num_1, num_2)

class CalculateDivide(CalculateCommand):
  def __init__(self):
    super().__init__()
    self.calculator = Calculate()
  
  def execute(self, num_1, num_2):
    return self.calculator.divide(num_1, num_2)

