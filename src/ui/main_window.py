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
    
    # new equation list
    self.equation: list = []
    self.equation_display = tk.StringVar()
    
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
    whole_equation = ttk.Label(screen_frame, anchor="se", background="white", textvariable=self.equation_display,)
    whole_equation.pack(fill="both", expand=True)
    
    def wrap_display(event):
      wrap_width = event.width - 20
      if wrap_width > 0:
        whole_equation.config(wraplength=wrap_width)
    
    screen_frame.bind("<Configure>", wrap_display)
  
  def build_buttons(self) -> None:
    calculator_frame = ttk.Frame(self.root)
    calculator_frame.grid(column=0, row=1, sticky="nsew")
    
    self._defualt_grid_column_weights(calculator_frame, 1)
    self._defualt_grid_row_weights(calculator_frame, 6)
    
    negative_row = ttk.Frame(calculator_frame)
    negative_row.grid(column=0, row=5, padx=4)
    ttk.Button(negative_row, text="0", command=lambda : self.update_display("0"), width="5").grid(column=1, row=0)
    ttk.Button(negative_row, text=",", command=lambda : self.update_display(","), width="5").grid(column=2, row=0)
    ttk.Button(negative_row, text="=", command=self.equal, width="5").grid(column=3, row=0)
    
    first_row = ttk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    ttk.Button(first_row, text="1", command=lambda : self.update_display("1"), width="5").grid(column=0, row=0)
    ttk.Button(first_row, text="2", command=lambda : self.update_display("2"), width="5").grid(column=1, row=0)
    ttk.Button(first_row, text="3", command=lambda : self.update_display("3"), width="5").grid(column=2, row=0)
    ttk.Button(first_row, text="+", command=lambda : self.update_display("+"), width="5").grid(column=3, row=0)
    
    second_row = ttk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    ttk.Button(second_row, text="4", command=lambda : self.update_display("4"), width="5").grid(column=0, row=0)
    ttk.Button(second_row, text="5", command=lambda : self.update_display("5"), width="5").grid(column=1, row=0)
    ttk.Button(second_row, text="6", command=lambda : self.update_display("6"), width="5").grid(column=2, row=0)
    ttk.Button(second_row, text="-", command=lambda : self.update_display("-"), width="5").grid(column=3, row=0)
    
    third_row = ttk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    ttk.Button(third_row, text="7", command=lambda : self.update_display("7"), width="5").grid(column=0, row=0)
    ttk.Button(third_row, text="8", command=lambda : self.update_display("8"), width="5").grid(column=1, row=0)
    ttk.Button(third_row, text="9", command=lambda : self.update_display("9"), width="5").grid(column=2, row=0)
    ttk.Button(third_row, text="x", command=lambda : self.update_display("x"), width="5").grid(column=3, row=0)
    
    fourth_row = ttk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    ttk.Button(fourth_row, text="C", command=self.clear_button, width="5").grid(column=0, row=0)
    ttk.Button(fourth_row, text="÷", command=lambda : self.update_display("÷"), width="5").grid(column=1, row=0)
    ttk.Button(fourth_row, text="⌫", command=self.backspace_button, width="5").grid(column=2, row=0)
    
    fifth_row = ttk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    ttk.Button(fifth_row, text="(", command=lambda : self.update_display("("), width="5").grid(column=0, row=0)
    ttk.Button(fifth_row, text=")", command=lambda : self.update_display(")"), width="5").grid(column=1, row=0)
    ttk.Button(fifth_row, text="π", command=lambda : self.update_display("π"), width="5").grid(column=2, row=0)
    ttk.Button(fifth_row, text="^", command=lambda : self.update_display("^"), width="5").grid(column=3, row=0)
  
  # FUNCTION 
  
  # This is a functional method
  def press_button(self, btnPress: str) -> None:
    self.equation.append(btnPress)
  
  # new clear functions
  def clear_button(self, event=None) -> None:
    self.equation_display.set("")
    self.equation.clear()
  
  # update display new function
  def update_display(self, pressed_button: str, event=None) -> None:
    new_equation = self.equation_display.get() + pressed_button + " "
    self.equation_display.set(new_equation)
    self.press_button(pressed_button)
  
  # new backspace function
  def backspace_button(self, event=None) -> None:
    current_equation = self.equation_display.get()
    if current_equation:
      new_equation = current_equation[:-2]
      self.equation_display.set(new_equation)
    
    if len(self.equation) != 0:
      self.equation.pop()
  
  """
    Equal method should then do the calculation,
    send the list, receive it back, and update 
    the display.
  """
  
  def equal(self, event=None) -> None: 
    final_equation = self._update_final_equation()
    resultant = Resultant(self.ops, final_equation).execute()
    self._output_result(resultant)
  
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
  
  def _output_result(self, result: float) -> None:
    self.clear(0)
    self.working_equation.set(result)
  
  # UI SERVICES
  
  def bind_services(self) -> None:
    self.root.bind("<BackSpace>", lambda e: self.backspace_button(e))
    self.root.bind("<Return>", self.equal)
    for i in range(10):
      self.root.bind(f"<KeyPress-{i}>", lambda e, num = i : self.update_display(f"{num}", e))
  
  def build_ui(self) -> None:
    self.display_screen()
    self.build_buttons()
    self.bind_services()
  