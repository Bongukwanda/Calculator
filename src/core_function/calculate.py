

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
  def __init__(self):
    self.calculate = Calculate()
  
  def execute(self):
    pass

class CalculateAddition(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculate.add(num_1, num_2)

class CalculateSubtraction(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculate.subtract(num_1, num_2)

class CalculateMultiplication(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculate.multiply(num_1, num_2)

class CalculateDivide(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculate.divide(num_1, num_2)

