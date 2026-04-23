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
  def __init__(self, receiever, clearance):
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
  def __init__(self, receiever, key, entered_number):
    super().__init__(receiever)
    self.key = key
    self.number = entered_number
  
  def execute(self):
    return self.receiever.press_operator(self.key, self.number)

class SpeacialKeyCommand(CommandBase):
  def __init__(self, receiever, key):
    super().__init__(receiever)
    self.key = key
  
  def execute(self):
    self.receiever.press_key(self.key)

class Resultant(CommandBase):
  def __init__(self, receiever, entered_number):
    super().__init__(receiever)
    self.number = entered_number
  
  def execute(self):
    return self.receiever.press_equal(self.number)
