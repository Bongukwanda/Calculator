from .core_function.calculate import CalculateAddition, CalculateSubtraction, CalculateMultiplication, CalculateDivide

class Calculator:
  
  def run_calculator(self):
    
    num_1 = 0
    num_2 = 0
    
    while True:
      if num_1.lower() == "stop":
        break
      
      num_1 = int(input("Enter first number: "))
      num_2 = int(input("Enter second number: "))
      
      print("""
            Select Operator Next from list:
            Add -> 1
            Subtract -> 2
            Multiply -> 3
            Divide -> 4
            """)
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
          num_1 = "stop"
          return "Incorrect Option Selected"
      
      if num_1 != "stop":
        resultant_string = f"Equation = {str(num_1)} + {operation} + {str(num_2)}\nResultant = {resultant}"
        print(resultant_string)

cal = Calculator()
cal.run_calculator()
