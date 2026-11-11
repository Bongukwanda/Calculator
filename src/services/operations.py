from constants.constants import FUNCTIONS, NUM_STRUCTURE

class Operations:
  
  def calculate_result(self, equation:list):
    print("equation = ",equation)
    result = []
    answer = 0
    opperation = ""
    for item in equation:
      if item.isnumeric():
        result.append(float(item))
      elif item in FUNCTIONS:
        opperation = item
      else:
        pass
      
      if opperation and len(result) > 1:
        latestCalculation = FUNCTIONS[opperation](result[0], result[1])
        result.clear()
        opperation = ""
        return latestCalculation
    
    return result
  
  # helpers
  
  def _organize_list(self, raw_list:list) -> list:
    for index, item in enumerate(raw_list):
      if item == ".":
        pass
  