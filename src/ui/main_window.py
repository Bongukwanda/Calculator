import tkinter as tk
from tkinter import ttk
from services.button_controller import ButtonController

class MainWindow():
  
  def __init__(self, root: tk.Tk | None = None):
    self.root = root
    
    # ---- Basic UI Settings ---------
    self.root.geometry("200x280")
    self.root.title("Calculator")
    
    # ---- Something ----------------
    self.working_equation = tk.StringVar()
    self.whole_equation = tk.StringVar()
    self.parenthesis = 0
    self.equation_answered = False
    
    self.equation = []
    self.operation = []
    
    # ---- Services -----------------
    self.button_ops = ButtonController()
    
    # ---- Grid Layout ---------------
    self.root.grid_columnconfigure(0, weight=1)
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    
    # ---- Build UI ------------------
    self.build_ui()
  
  # ----------------------------------------------------------
  
  def display_screen(self) -> None:
    screen_frame = ttk.Frame(self.root, border=2, borderwidth=5, relief="solid")
    screen_frame.grid(column=0, row=0, padx=8, pady=8, sticky="nsew")
    
    whole_equation = ttk.Label(screen_frame, anchor="se", background="white", textvariable=self.whole_equation)
    whole_equation.pack(fill="both", expand=True)
    current_equation = ttk.Label(screen_frame, anchor="se", background="white", textvariable=self.working_equation)
    current_equation.pack(fill="both", expand=True)
  
  def build_buttons(self) -> None:
    calculator_frame = ttk.Frame(self.root)
    calculator_frame.grid(column=0, row=1, sticky="nsew")
    
    self.defualt_grid_column_weights(calculator_frame, 1)
    self.defualt_grid_row_weights(calculator_frame, 5)
    
    first_row = ttk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    one = ttk.Button(first_row, text="1", command=lambda : self.press_number(1), width="5")
    one.grid(column=0, row=0)
    two = ttk.Button(first_row, text="2", command=lambda : self.press_number(2), width="5")
    two.grid(column=1, row=0)
    three = ttk.Button(first_row, text="3", command=lambda : self.press_number(3), width="5")
    three.grid(column=2, row=0)
    equal_to = ttk.Button(first_row, text="=", command=lambda : self.press_equal("="), width="5")
    equal_to.grid(column=3, row=0)
    
    second_row = ttk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    four = ttk.Button(second_row, text="4", command=lambda : self.press_number(4), width="5")
    four.grid(column=0, row=0)
    five = ttk.Button(second_row, text="5", command=lambda : self.press_number(5), width="5")
    five.grid(column=1, row=0)
    six = ttk.Button(second_row, text="6", command=lambda : self.press_number(6), width="5")
    six.grid(column=2, row=0)
    plus = ttk.Button(second_row, text="+", command=lambda : self.press_function("+"), width="5")
    plus.grid(column=3, row=0)
    
    third_row = ttk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    seven = ttk.Button(third_row, text="7", command=lambda : self.press_number(7), width="5")
    seven.grid(column=0, row=0)
    eight = ttk.Button(third_row, text="8", command=lambda : self.press_number(8), width="5")
    eight.grid(column=1, row=0)
    nine = ttk.Button(third_row, text="9", command=lambda : self.press_number(9), width="5")
    nine.grid(column=2, row=0)
    minus = ttk.Button(third_row, text="-", command=lambda : self.press_function("-"), width="5")
    minus.grid(column=3, row=0)
    
    fourth_row = ttk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    c = ttk.Button(fourth_row, text="C", command=lambda : self.clear_equation("C"), width="5")
    c.grid(column=0, row=1)
    ce = ttk.Button(fourth_row, text="CE", command=lambda : self.clear_equation("CE"), width="5")
    ce.grid(column=1, row=1)
    divide = ttk.Button(fourth_row, text="÷", command=lambda : self.press_function("÷"), width="5")
    divide.grid(column=2, row=1)
    multiply = ttk.Button(fourth_row, text="x", command=lambda : self.press_function("x"), width="5")
    multiply.grid(column=3, row=1)
    
    fifth_row = ttk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    open_bracket = ttk.Button(fifth_row, text="(",  command=lambda : self.press_function("("), width="5")
    open_bracket.grid(column=0, row=0)
    close_bracket = ttk.Button(fifth_row, text=")",  command=lambda : self.press_function(")"), width="5")
    close_bracket.grid(column=1, row=0)
    pi = ttk.Button(fifth_row, text="π", width="5")
    pi.grid(column=2, row=0)
    raise_to = ttk.Button(fifth_row, text="^", command=lambda : self.press_function("^"), width="5")
    raise_to.grid(column=3, row=0)
  
  # ----------------------------------------------------------
  
  def press_number(self, number: int, event=None) -> None:
    self.equation.append(number)
    current_equation = self.working_equation.get().strip()
    current_equation += str(number)
    self.working_equation.set(current_equation)
  
  def press_function(self, key: str, event=None) -> None:
    if not key:
      return
    
    match key:
      case "+":
        self.operation.append("add")
      case "-":
        self.operation.append("subtract")
      case "x":
        self.operation.append("multiply")
      case "÷":
        self.operation.append("divide")
      case "π":
        self.operation.append("pi")
      case "^":
        self.operation.append("raise_to")
      case "(":
        self.parenthesis += 1
      case ")":
        self.parenthesis -= 1
      case _:
        pass
    
    key_value = " " + key + " "
    self.update_whole_equation(key_value)
  
  def press_equal(self, event=None) -> None:    
    
    resultant = 0
    
    if not self.parenthesis_check():
      return
    
    if not len(self.operation):
      return
    
    if not len(self.equation):
      return
    
    if "add" in self.operation:
      resultant = sum(self.equation)
    
    if "subtract" in self.operation:
      for index, value in enumerate(self.equation):
        if index == 0:
          resultant += value
        else:
          resultant -= value
    
    if "multiply" in self.operation:
      for index, value in enumerate(self.equation):
        if index == 0:
          resultant += value
        else:
          resultant *= value
    
    if "divide" in self.operation:
      for index, value in enumerate(self.equation):
        if index == 0:
          resultant += value
        else:
          resultant /= value
    
    if "pi" in self.operation:
      for index, value in enumerate(self.equation):
        if index == 0:
          resultant += value
        else:
          resultant *= value
    
    if "raise_to" in self.operation:
      for index, value in enumerate(self.equation):
        if index == 0:
          resultant += value
        else:
          resultant **= value
    
    self.clear_equation("CE")
    self.working_equation.set(resultant)
  
  def clear_equation(self, operation:str, event=None) -> None:
    if operation == "CE":
      self.whole_equation.set("")
      self.working_equation.set("")
      self.operation.clear()
      self.equation.clear()
    else:
      self.working_equation.set("")
  
  def parenthesis_check(self) -> bool:
    if self.parenthesis == 0:
      return True
    
    return False
  
  def update_working_equation(self, execution:str, event=None) -> None:
    current_equation = self.working_equation.get().strip()
    current_equation += execution
    self.working_equation.set(current_equation)
  
  def update_whole_equation(self, execution:str) -> None:
    working_equation = self.working_equation.get().strip()
    whole_equation = self.whole_equation.get()
    current_equation = ""
    
    if whole_equation == "" or whole_equation is None:
      current_equation = working_equation + execution
    else:
      current_equation = whole_equation + working_equation + execution
    
    self.whole_equation.set(current_equation)
    self.clear_equation("C")
  
  # ----------------------------------------------------------
  
  def defualt_grid_column_weights(self, frame:tk.Misc, columns:int) -> None:
    for column in range(columns):
      frame.grid_columnconfigure(column, weight=1)
  
  def defualt_grid_row_weights(self, frame:tk.Misc, rows:int) -> None:
    for row in range(rows):
      frame.grid_rowconfigure(row, weight=1)
  
  # ----------------------------------------------------------
  
  def build_ui(self) -> None:
    self.display_screen()
    self.build_buttons()