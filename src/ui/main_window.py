import tkinter as tk
from tkinter import ttk

from commands.commands import (
  ClearCommand,
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
    self.ops = Operations()
    
    # ---- Build UI ----
    self.build_ui()
  
  # UI/UX
  
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
    self._defualt_grid_row_weights(calculator_frame, 6)
    
    negative_row = ttk.Frame(calculator_frame)
    negative_row.grid(column=0, row=5, padx=4)
    ttk.Button(negative_row, text="+/-", command=self.negate, width="5").grid(column=0, row=0)
    ttk.Button(negative_row, text="0", command=lambda : self.press_number("0"), width="5").grid(column=1, row=0)
    ttk.Button(negative_row, text=",", command=lambda : self.press_number(","), width="5").grid(column=2, row=0)
    ttk.Button(negative_row, text="=", command=self.press_equal, width="5").grid(column=3, row=0)
    
    first_row = ttk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    ttk.Button(first_row, text="1", command=lambda : self.press_number("1"), width="5").grid(column=0, row=0)
    ttk.Button(first_row, text="2", command=lambda : self.press_number("2"), width="5").grid(column=1, row=0)
    ttk.Button(first_row, text="3", command=lambda : self.press_number("3"), width="5").grid(column=2, row=0)
    ttk.Button(first_row, text="+", command=lambda : self.press_operator("+"), width="5").grid(column=3, row=0)
    
    second_row = ttk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    ttk.Button(second_row, text="4", command=lambda : self.press_number("4"), width="5").grid(column=0, row=0)
    ttk.Button(second_row, text="5", command=lambda : self.press_number("5"), width="5").grid(column=1, row=0)
    ttk.Button(second_row, text="6", command=lambda : self.press_number("6"), width="5").grid(column=2, row=0)
    ttk.Button(second_row, text="-", command=lambda : self.press_operator("-"), width="5").grid(column=3, row=0)
    
    third_row = ttk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    ttk.Button(third_row, text="7", command=lambda : self.press_number("7"), width="5").grid(column=0, row=0)
    ttk.Button(third_row, text="8", command=lambda : self.press_number("8"), width="5").grid(column=1, row=0)
    ttk.Button(third_row, text="9", command=lambda : self.press_number("9"), width="5").grid(column=2, row=0)
    ttk.Button(third_row, text="x", command=lambda : self.press_operator("x"), width="5").grid(column=3, row=0)
    
    fourth_row = ttk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    ttk.Button(fourth_row, text="C", command=lambda : self.clear_equation(1), width="5").grid(column=0, row=0)
    ttk.Button(fourth_row, text="CE", command=lambda : self.clear_equation(0), width="5").grid(column=1, row=0)
    ttk.Button(fourth_row, text="÷", command=lambda : self.press_operator("÷"), width="5").grid(column=2, row=0)
    ttk.Button(fourth_row, text="⌫ ", command=self.backspace, width="5").grid(column=3, row=0)
    
    fifth_row = ttk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    ttk.Button(fifth_row, text="(", command=lambda : self.press_operator("("), width="5").grid(column=0, row=0)
    ttk.Button(fifth_row, text=")", command=lambda : self.press_operator(")"), width="5").grid(column=1, row=0)
    ttk.Button(fifth_row, text="π", command=lambda : self.press_operator("π"), width="5").grid(column=2, row=0)
    ttk.Button(fifth_row, text="^", command=lambda : self.press_operator("^"), width="5").grid(column=3, row=0)
  
  # FUNCTION 
  
  def press_number(self, number: str, event=None) -> None:
    self._update_working_equation(number)
  
  def press_operator(self, operator: str, event=None) -> None:
    self._update_whole_equation(operator)
  
  def backspace(self, event=None) -> None:
    current_equation = self.working_equation.get()
    current_whole = self.whole_equation.get()
    
    if current_equation != "" and current_equation != None:
      self.working_equation.set(current_equation[:-1])
    
    elif current_whole != "" and current_whole != None:
      self.whole_equation.set(current_whole[:-2])
    
    else:
      return
  
  def negate(self, event=None) -> None:
    current_number = self.working_equation.get()
    if not current_number:
      return
    
    if current_number.startswith("-"):
      self.working_equation.set(current_number[1:].lstrip())
    else:
      self.working_equation.set("- " + current_number)
  
  def press_equal(self, event=None) -> None: 
    final_equation = self._update_final_equation()
    resultant = Resultant(self.ops, final_equation).execute()
    self._update_result(resultant)
  
  def clear_equation(self, clear_type: int, event=None) -> None:
    if clear_type:
      self.working_equation.set("")
    else:
      self.working_equation.set("")
      self.whole_equation.set("")
    
    ClearCommand(self.ops, clear_type).execute()
  
  # HELPER
  
  def _defualt_grid_column_weights(self, frame:tk.Misc, columns:int) -> None:
    for column in range(columns):
      frame.grid_columnconfigure(column, weight=1)
  
  def _defualt_grid_row_weights(self, frame:tk.Misc, rows:int) -> None:
    for row in range(rows):
      frame.grid_rowconfigure(row, weight=1)
  
  def _update_working_equation(self, execution:str, event=None) -> None:
    current_equation = self.working_equation.get().strip()
    current_equation += execution
    self.working_equation.set(current_equation)
  
  def _update_whole_equation(self, execution:str) -> None:
    working_equation = self.working_equation.get().strip()
    whole_equation = self.whole_equation.get()
    current_equation = ""
    execution = " " + execution
    
    if not whole_equation:
      current_equation = working_equation + execution
    elif working_equation:
      current_equation = whole_equation + working_equation + execution
    else:
      current_equation = whole_equation + execution
    
    self.whole_equation.set(current_equation)
    self.working_equation.set("")
  
  def _update_final_equation(self) -> str:
    whole = self.whole_equation.get()
    current = self.working_equation.get()
    if not current:
      return whole
    
    final_equation = whole + current
    self._update_whole_equation(final_equation)
    
    return final_equation
  
  def _update_result(self, result: float) -> None:
    self.clear_equation(0)
    self.working_equation.set(result)
  
  # UI SERVICES
  
  def bind_services(self) -> None:
    for i in range(10):
      self.root.bind(f"<KeyPress-{i}>", lambda e, num = i : self.press_number(f"{num}"))
    
    self.root.bind("<BackSpace>", self.backspace)
  
  def build_ui(self) -> None:
    self.display_screen()
    self.build_buttons()
    self.bind_services()
  