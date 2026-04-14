import tkinter as tk
from tkinter import ttk

from commands.commands import (
  OperationUpdate,
  ClearCommand,
  NumberPressCommand,
  Resultant
)

from services.operations import Operations

class MainWindow():
  
  def __init__(self, root: tk.Tk | None = None):
    
    self.root = root
    self.root.geometry("200x280")
    self.root.title("Calculator")
    
    # ---- UI/UX ----
    self.working_equation = tk.StringVar()
    self.whole_equation = tk.StringVar()
    self.root.grid_columnconfigure(0, weight=1)
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    
    # ---- Services ----
    self.ops = Operations(self.operation, self.my_equation)
    
    # ---- Build UI ----
    self.build_ui()
  
  # =============================
  # UI/UX
  # =============================
  
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
    
    self._defualt_grid_column_weights(calculator_frame, 1)
    self._defualt_grid_row_weights(calculator_frame, 5)
    
    first_row = ttk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    one = ttk.Button(first_row, text="1", command=lambda : self.press_number(1), width="5")
    one.grid(column=0, row=0)
    two = ttk.Button(first_row, text="2", command=lambda : self.press_number(2), width="5")
    two.grid(column=1, row=0)
    three = ttk.Button(first_row, text="3", command=lambda : self.press_number(3), width="5")
    three.grid(column=2, row=0)
    equal_to = ttk.Button(first_row, text="=", command=self.press_equal, width="5")
    equal_to.grid(column=3, row=0)
    
    second_row = ttk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    four = ttk.Button(second_row, text="4", command=lambda : self.press_number(4), width="5")
    four.grid(column=0, row=0)
    five = ttk.Button(second_row, text="5", command=lambda : self.press_number(5), width="5")
    five.grid(column=1, row=0)
    six = ttk.Button(second_row, text="6", command=lambda : self.press_number(6), width="5")
    six.grid(column=2, row=0)
    plus = ttk.Button(second_row, text="+", command=lambda : self.press_operator("+"), width="5")
    plus.grid(column=3, row=0)
    
    third_row = ttk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    seven = ttk.Button(third_row, text="7", command=lambda : self.press_number(7), width="5")
    seven.grid(column=0, row=0)
    eight = ttk.Button(third_row, text="8", command=lambda : self.press_number(8), width="5")
    eight.grid(column=1, row=0)
    nine = ttk.Button(third_row, text="9", command=lambda : self.press_number(9), width="5")
    nine.grid(column=2, row=0)
    minus = ttk.Button(third_row, text="-", command=lambda : self.press_operator("-"), width="5")
    minus.grid(column=3, row=0)
    
    fourth_row = ttk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    c = ttk.Button(fourth_row, text="C", command=self.clear_basic, width="5")
    c.grid(column=0, row=1)
    ce = ttk.Button(fourth_row, text="CE", command=self.clear_equation, width="5")
    ce.grid(column=1, row=1)
    divide = ttk.Button(fourth_row, text="÷", command=lambda : self.press_operator("÷"), width="5")
    divide.grid(column=2, row=1)
    multiply = ttk.Button(fourth_row, text="x", command=lambda : self.press_operator("x"), width="5")
    multiply.grid(column=3, row=1)
    
    fifth_row = ttk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    open_bracket = ttk.Button(fifth_row, text="(",  command=lambda : self.press_operator("("), width="5")
    open_bracket.grid(column=0, row=0)
    close_bracket = ttk.Button(fifth_row, text=")",  command=lambda : self.press_operator(")"), width="5")
    close_bracket.grid(column=1, row=0)
    pi = ttk.Button(fifth_row, text="π", width="5")
    pi.grid(column=2, row=0)
    raise_to = ttk.Button(fifth_row, text="^", command=lambda : self.press_operator("^"), width="5")
    raise_to.grid(column=3, row=0)
  
  # =============================
  # FUNCTION 
  # =============================
  
  def press_number(self, number: int, event=None) -> None:
    NumberPressCommand(self.ops, number).execute()
    self._update_working_equation(str(number))
  
  def press_operator(self, key: str, event=None) -> None:
    OperationUpdate(self.ops, key).execute()
    self._update_whole_equation(key)
  
  def press_equal(self, event=None) -> None:    
    resultant = Resultant(self.ops).execute()
    self.clear_equation()
    self.equation_answered = True
    self.working_equation.set(resultant)
  
  def clear_basic(self, event=None) -> None:
    self.working_equation.set("")
    ClearCommand(self.ops).execute
  
  def clear_equation(self, event=None) -> None:
    self.whole_equation.set("")
    self.working_equation.set("")
    ClearCommand(self.ops, "all").execute
  
  # =============================
  # HELPER
  # =============================
  
  def _update_working_equation(self, execution:str, event=None) -> None:
    current_equation = self.working_equation.get().strip()
    current_equation += execution
    self.working_equation.set(current_equation)
  
  def _update_whole_equation(self, execution:str) -> None:
    working_equation = self.working_equation.get().strip()
    whole_equation = self.whole_equation.get()
    current_equation = ""
    execution = " " + execution + " "
    
    if not whole_equation:
      current_equation = working_equation + execution
    else:
      current_equation = whole_equation + working_equation + execution
    
    self.whole_equation.set(current_equation)
    self.working_equation.set("")
  
  def _defualt_grid_column_weights(self, frame:tk.Misc, columns:int) -> None:
    for column in range(columns):
      frame.grid_columnconfigure(column, weight=1)
  
  def _defualt_grid_row_weights(self, frame:tk.Misc, rows:int) -> None:
    for row in range(rows):
      frame.grid_rowconfigure(row, weight=1)
  
  # =============================
  # BUILD UI
  # =============================
  
  def build_ui(self) -> None:
    self.display_screen()
    self.build_buttons()