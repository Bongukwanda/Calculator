from constants.constants import BODMAS, FUNCTIONS

class Operations:
  
  def calculate_result(self, equation:list):
    self.equation = equation
    result = []
    opperation = ""
    print("original: ", self.equation)
    print("reordered: ", self._reorder_equation())
    
    while len(self.equation) > 1:
      if isinstance(self.equation[0], (int, float)):
        result.append(self.equation.pop(0))
      
      if isinstance(self.equation[0], str):
        opperation = self.equation.pop(0)
      
      while len(result) < 2:
        if isinstance(self.equation[0], (int, float)):
          result.append(self.equation.pop(0))
      
      if opperation:
        result = [FUNCTIONS[opperation](result[0], result[1])]
        opperation = ""
    
    return result[0]
  
  # helpers
  
  def _find_bodmas(self) -> list:
    operators = []
    for index, item in enumerate(self.equation):
      if item in BODMAS:
        operators.append([index, BODMAS[item]])
    operators.sort(key=lambda x : x[1])
    return operators
  
  def _reorder_equation(self) -> list:
    bodmasList = self._find_bodmas()
    pracEquation = self.equation
    equationCounter = [x for x in range(len(pracEquation))]
    bodmasEquation = []
    
    for op in bodmasList:
      for x in range(-2, 2):
        curIndex = op[0] + x
        if curIndex in equationCounter:
          if pracEquation[curIndex] == '-' and x == -2:
            pracEquation[curIndex + 1] *= -1
            pracEquation[curIndex] = -1
          elif x != -2:
            if x != 0 and len(bodmasEquation) != 0 and pracEquation[curIndex] > -1:
              bodmasEquation.append('+')
            bodmasEquation.append(self.equation[curIndex])
            equationCounter[curIndex] = -1
          else:
            pass
    
    return bodmasEquation
  
  def _apply_bodmas(self):
    shunt_equation_2 = []
    moved_numbers_2 = []
    myeq_2 = self.equation
    bodmas_list = self._find_bodmas()
    
    for ops in bodmas_list:
      eq_item = ops[0]
      if len(shunt_equation_2) == 0:
        for i in range(1, -2, -1):
          shunt_equation_2.append(myeq_2[eq_item - i])
          moved_numbers_2.append(eq_item - i)
      else:
        shunt_equation_2.append(myeq_2[eq_item])
        moved_numbers_2.append(eq_item)
        
        if (eq_item-1) in moved_numbers_2:
          eq_item += 1
        elif (eq_item+1) in moved_numbers_2:
          eq_item -= 1
        
        shunt_equation_2.append(myeq_2[eq_item])
        moved_numbers_2.append(eq_item)
    
    return shunt_equation_2