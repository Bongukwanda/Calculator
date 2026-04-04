from abc import ABC, abstractmethod
from services.operations import Operations


class CommandBase(ABC):
  def __init__(self, equation: list):
    super().__init__()
    self.controller = Operations(equation)
  
  @abstractmethod
  def execute(self):
    ...

class Resultant(CommandBase):
  def __init__(self, equation_list: list):
    super().__init__(equation_list)
  
  def execute(self):
    return self.controller.output_resultant()

class Addition(CommandBase):
  def __init__(self, equation_list: list):
    super().__init__(equation_list)
  
  def execute(self):
    return self.controller.add()

class Subtraction(CommandBase):
  def __init__(self, equation_list: list):
    super().__init__(equation_list)
  
  def execute(self):
    return self.controller.subtract()

class Muliplication(CommandBase):
  def __init__(self, equation_list: list):
    super().__init__(equation_list)
  
  def execute(self):
    return self.controller.mulitply()

class Division(CommandBase):
  def __init__(self, equation_list: list):
    super().__init__(equation_list)
  
  def execute(self):
    return self.controller.divide()

class Exponentiation(CommandBase):
  def __init__(self, equation_list: list):
    super().__init__(equation_list)
  
  def execute(self):
    return self.controller.exponentiate()
