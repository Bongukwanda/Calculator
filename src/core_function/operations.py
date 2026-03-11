from abc import ABC, abstractmethod

class Operations:
  
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
  
  def power_of(self, number:float, raise_to_value:int) -> float:
    resultant = number ** raise_to_value
    return resultant
  
  def add_parenthesis(self) -> None:
    pass
  

class CalculateCommand(ABC):
  def __init__(self):
    self.calculator = Operations()
  
  @abstractmethod
  def execute(self):
    ...

class AdditionCommand(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculator.add(num_1, num_2)

class SubtractionCommand(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculator.subtract(num_1, num_2)

class MultiplicationCommand(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculator.multiply(num_1, num_2)

class DivideCommand(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.calculator.divide(num_1, num_2)

class PowerOfCommand(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, number, power_of):
    return self.calculator.power_of(number, power_of)

