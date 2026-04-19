from __future__ import annotations
from abc import ABC, abstractmethod

class CommandBase(ABC):
  def __init__(self, receiever):
    super().__init__()
    self.receiever = receiever
  
  @abstractmethod
  def execute(self):
    ...

# ===========

class ClearCommand(CommandBase):
  def __init__(self, receiever, clearance: str = ""):
    super().__init__(receiever)
    self.clear = clearance
  
  def execute(self):
    self.receiever.clear_basic(self.clear)

class NumberPressCommand(CommandBase):
  def __init__(self, receiever):
    super().__init__(receiever)
  
  def execute(self):
    self.receiever.press_number()

class OperationUpdate(CommandBase):
  def __init__(self, receiever, key: str, entered_number: float):
    super().__init__(receiever)
    self.key = key
    self.number = entered_number
  
  def execute(self):
    return self.receiever.press_operator(self.key, self.number)

class Resultant(CommandBase):
  def __init__(self, receiever, entered_number: float | None = None):
    super().__init__(receiever)
    self.number = entered_number
  
  def execute(self):
    return self.receiever.press_equal(self.number)
