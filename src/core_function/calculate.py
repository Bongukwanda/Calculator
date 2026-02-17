

class Calculate:
  
  def __init__(self):
    self.total_resultant: float = 0
  
  def add(self, **numbers):
    if (len(numbers) < 2):
      return
    
    for number in numbers:
      self.total_resultant += number
    
    return self.total_resultant

class CalculateCommand:
  def __init__(self):
    self.calculate = Calculate()
  
  def execute(self):
    pass

class CalculateAddition(CalculateCommand):
  def __init__(self):
    super().__init__()
  
  def execute(self, **values):
    return self.calculate.add(values)

