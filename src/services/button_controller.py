from services.operations import Operations
from abc import ABC, abstractmethod


class ButtonController:
  
  def __init__(self):
    self.operation = Operations()
    
    self.equation = {
      "numbers": [],
      "function": ""
    }
  
  # -------------------------------------
  
  def power_of(self):
    pass
  
  
  def update_equation(self, equation_update, equation_value: str) -> None:
    if equation_value == "numbers":
      self.equation[equation_value].append(equation_update)
    elif equation_value == "function":
      self.equation[equation_value] = equation_update
    else:
      return

class EquationCommandBase(ABC):
  def __init__(self, controller):
    super().__init__()
    self.controller = controller
  
  @abstractmethod
  def execute(self):
    ...

class EquationUpdateCommand(EquationCommandBase):
  def __init__(self, controller, update, value):
    super().__init__(controller=controller)
    self.update = update
    self.value = value
  
  def execute(self):
    self.controller.update_equation(self.update, self.value)


class CommandBase(ABC):
  def __init__(self):
    super().__init__()
    self.ops = Operations()
  
  @abstractmethod
  def execute(self):
    ...

class AdditionCommand(CommandBase):
  def __init__(self):
    super().__init__()

  def execute(self, num_1, num_2):
    return self.ops.add(num_1, num_2)

class SubtractionCommand(CommandBase):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.ops.subtract(num_1, num_2)

class MultiplicationCommand(CommandBase):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.ops.multiply(num_1, num_2)

class DivideCommand(CommandBase):
  def __init__(self):
    super().__init__()
  
  def execute(self, num_1, num_2):
    return self.ops.divide(num_1, num_2)

class PowerOfCommand(CommandBase):
  def __init__(self):
    super().__init__()
  
  def execute(self, number, power_of):
    return self.ops.power_of(number, power_of)
