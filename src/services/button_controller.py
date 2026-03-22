from services.operations import Operations
from abc import ABC, abstractmethod


class ButtonController:
  
  def __init__(self):
    self.operation = Operations()
  
  def add(self, equation: list) -> int:
    resultant = sum(equation)
    return resultant

class CommandBase(ABC):
  def __init__(self):
    self.controller = ButtonController()
  
  @abstractmethod
  def execute(self):
    ...

class AddCommand(CommandBase):
  def __init__(self, equation: list):
    super().__init__()
    self.equation = equation
  
  def execute(self):
    return self.controller.add(self.equation)
