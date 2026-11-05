from constants.constants import FUNCTIONS, NUM_STRUCTURE

class Operations:
  
  def calculate_result(self, equation:list):
    result = 0.0
    for item in equation:
      if item.isnumeric():
        result += float(item)
    
    return result
  
  # helpers
  
  def _organize_list(self, raw_list:list) -> list:
    pass
  