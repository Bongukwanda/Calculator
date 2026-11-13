from constants.constants import BODMAS, FUNCTIONS
"""
the problem now is the calculate_result method
it cannot hold the resultant value and work on tope of that
it also may return the value early, if the formula/calculation
is long
"""

class Operations:
  
  def calculate_result(self, equation:list):
    print("equation: ", equation)
    self._organize_list(equation=equation)
    print("equation cleaned: ", equation)
    result = []
    opperation = ""
    
    while len(equation) > 1:
      if isinstance(equation[0], (int, float)):
        result.append(equation.pop(0))
      
      if isinstance(equation[0], str):
        opperation = equation.pop(0)
      
      while len(result) < 2:
        if isinstance(equation[0], (int, float)):
          result.append(equation.pop(0))
      
      if opperation:
        result = [FUNCTIONS[opperation](result[0], result[1])]
        opperation = ""
    
    return result[0]
  
  # helpers
  
  def _organize_list(self, equation:list) -> list:
    operators = []
    for index, item in enumerate(equation):
      if item in BODMAS:
        operators.append(index)
    
    
  