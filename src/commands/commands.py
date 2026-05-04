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
    self.receiever.clear_equation(self.clear)

class Resultant(CommandBase):
  def __init__(self, receiever, equation):
    super().__init__(receiever)
    self.equation = equation
  
  def execute(self):
    return self.receiever.calculate_answer(self.equation)
