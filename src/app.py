from .core_function.operations import (
  CalculateAddition,
  CalculateSubtraction,
  CalculateMultiplication,
  CalculateDivide
)

class Calculator:
  
  def run_calculator(self):
    
    while True:
      print("To Stop Calculator enter: '999' in num_1 entry box.")
      
      num_1 = int(input("Enter first number: "))
      if num_1 == 999:
        break
      
      num_2 = int(input("Enter second number: "))
      
      print("Select Operator Next from list:\nAdd -> 1\nSubtract -> 2\nMultiply -> 3\nDivide -> 4")
      operator = int(input("Enter operation selection from above options: "))
      operation = ""
      resultant = 0
      
      match operator:
        case 1:
          command = CalculateAddition()
          resultant = command.execute(num_1, num_2)
          operation = " + "
        case 2:
          command = CalculateSubtraction()
          resultant = command.execute(num_1, num_2)
          operation = " - "
        case 3:
          command = CalculateMultiplication()
          resultant = command.execute(num_1, num_2)
          operation = " x "
        case 4:
          command = CalculateDivide()
          resultant = command.execute(num_1, num_2)
          operation = " / "
        case _:
          num_1 = 999
          print("Incorrect Option Selected - Application closed")
      
      if num_1 == 999:
        break
      else:
        resultant_string = f"Equation = {str(num_1)} {operation} {str(num_2)}\nResultant = {resultant}"
        print(resultant_string)

cal = Calculator()
cal.run_calculator()
