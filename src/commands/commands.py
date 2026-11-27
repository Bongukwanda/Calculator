from abc import ABC, abstractmethod

class CommandBase(ABC):
  def __init__(self, receiever):
    super().__init__()
    self.receiever = receiever
  
  @abstractmethod
  def execute(self):
    ...

# ===========

class Resultant(CommandBase):
  def __init__(self, receiever, equation):
    super().__init__(receiever)
    self.equation = equation
  
  def execute(self):
    return self.receiever.calculate_result(self.equation) 

