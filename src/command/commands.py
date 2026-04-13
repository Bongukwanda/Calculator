from __future__ import annotations
from abc import ABC, abstractmethod
from services.calculations import Calculations


class CommandBase(ABC):
  def __init__(self, operation):
    super().__init__()
    self.operation = operation
  
  @abstractmethod
  def execute(self):
    ...

# ===========

class Addition(CommandBase):
  def execute(self):
    return self.operation.addition()

class Subtraction(CommandBase):
  def execute(self):
    return self.operation.subtraction()

class Muliplication(CommandBase):
  def execute(self):
    return self.operation.mulitplication()

class Division(CommandBase):
  def execute(self):
    return self.operation.division()

class Exponentiation(CommandBase):
  def execute(self):
    return self.operation.exponentiation()

class Pi(CommandBase):
  def execute(self):
    return self.operation.pi_calculation()

# ===========

class OperationUpdate(CommandBase):
  def __init__(self, operation, key: str):
    super().__init__(operation)
    self.key = key
  
  def execute(self):
    return self.operation.press_operator(self.key)

class Resultant(CommandBase):
  def execute(self):
    return self.operation.output_resultant()
