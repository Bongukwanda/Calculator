from __future__ import annotations
from abc import ABC, abstractmethod


class CommandBase(ABC):
  def __init__(self, operation):
    super().__init__()
    self.operation = operation
  
  @abstractmethod
  def execute(self):
    ...

# ===========

class ClearCommand(CommandBase):
  def __init__(self, operation, clearance: str = ""):
    super().__init__(operation)
    self.clear = clearance
  
  def execute(self):
    self.operation.clear_basic(self.clear)

class NumberPressCommand(CommandBase):
  def __init__(self, operation, number: float):
    super().__init__(operation)
    self.num = number
  
  def execute(self):
    self.operation.press_number(self.num)

class OperationUpdate(CommandBase):
  def __init__(self, operation, key: str):
    super().__init__(operation)
    self.key = key
  
  def execute(self):
    return self.operation.press_operator(self.key)

class Resultant(CommandBase):
  def execute(self):
    return self.operation.press_equal()
