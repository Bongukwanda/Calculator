
class Operations:
  
  def add(self, *numbers:list[float]) -> float:
    result = 0
    for number in numbers:
      result += number
    return result
  
  def subtract(self, *numbers:list[float]) -> float:
    result = numbers[0]
    for number in range(1, len(numbers)):
      result -= number
    return result
  
  def multiply(self, number_1:float, number_2:float) -> float:
    multiplication_result = number_1 * number_2
    return multiplication_result
  
  def divide(self, number_1:float, number_2:float) -> float:
    dividend = number_1 / number_2
    return dividend
  
  def power_of(self, number:float, raise_to_value:int) -> float:
    resultant = number ** raise_to_value
    return resultant
  
  def add_parenthesis(self) -> None:
    pass
  
  def equal_to(self) -> float:
    return 0
  
