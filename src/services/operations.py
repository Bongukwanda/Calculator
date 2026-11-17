from constants.constants import BODMAS, FUNCTIONS

class Operations:
  
  def calculate_result(self, equation:list):
    self.equation = equation
    print("equation: ", equation)
    cleanedList = self._apply_bodmas()
    print("equation cleaned: ", cleanedList)
    result = []
    opperation = ""
    
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
  
  def _apply_bodmas(self):
    shunt_equation = []
    moved_numbers = []
    
    shunt_equation_2 = []
    moved_numbers_2 = []
    
    myeq = self.equation
    myeq_2 = self.equation
    bodmas_list = self._find_bodmas()
    
    # for op in bodmas_list:
    #   if myeq[op[0]+1] == myeq[-1]:
    #     if myeq[op[0]+1] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]+1])
    #       moved_numbers.append(myeq[op[0]+1])
    #     if myeq[op[0]] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]])
    #       moved_numbers.append(myeq[op[0]])
    #     if myeq[op[0]-1] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]-1])
    #       moved_numbers.append(myeq[op[0]-1])
    #   elif myeq[op[0]-1] == myeq[0]:
    #     if myeq[op[0]-1] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]-1])
    #       moved_numbers.append(myeq[op[0]-1])
    #     if myeq[op[0]] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]])
    #       moved_numbers.append(myeq[op[0]])
    #     if myeq[op[0]+1] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]+1])
    #       moved_numbers.append(myeq[op[0]+1])
    #   else:
    #     if myeq[op[0]-1] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]-1])
    #       moved_numbers.append(myeq[op[0]-1])
    #     if myeq[op[0]] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]])
    #       moved_numbers.append(myeq[op[0]])
    #     if myeq[op[0]+1] not in moved_numbers:
    #       shunt_equation.append(myeq[op[0]+1])
    #       moved_numbers.append(myeq[op[0]+1])
    
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