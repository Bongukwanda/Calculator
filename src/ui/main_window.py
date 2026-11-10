import tkinter as tk
from tkinter import ttk
from commands.commands import Resultant
from services.operations import Operations

class MainWindow():
  
  def __init__(self, root: tk.Tk | None = None):
    
    self.root = root
    self.root.geometry("200x280")
    self.root.title("Calculator")
    
    # ---- UI/UX ----
    
    self.equation: list = []
    self.equation_display = tk.StringVar()
    
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
    screen_frame.pack_propagate(False)
    whole_equation = ttk.Label(screen_frame, anchor="nw", background="white", textvariable=self.equation_display,)
    whole_equation.pack(fill="both", expand=True)
    
    def wrap_display(event):
      wrap_width = event.width - 10
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
    ttk.Button(negative_row, text="+/-", command=lambda : self.input_operator("neg"), width="5").grid(column=0, row=0)
    ttk.Button(negative_row, text="0", command=lambda : self.input_number("0"), width="5").grid(column=1, row=0)
    ttk.Button(negative_row, text=".", command=lambda : self.input_number("."), width="5").grid(column=2, row=0)
    ttk.Button(negative_row, text="=", command=self.output_answer, width="5").grid(column=3, row=0)
    
    first_row = ttk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    ttk.Button(first_row, text="1", command=lambda : self.input_number("1"), width="5").grid(column=0, row=0)
    ttk.Button(first_row, text="2", command=lambda : self.input_number("2"), width="5").grid(column=1, row=0)
    ttk.Button(first_row, text="3", command=lambda : self.input_number("3"), width="5").grid(column=2, row=0)
    ttk.Button(first_row, text="+", command=lambda : self.input_operator("+"), width="5").grid(column=3, row=0)
    
    second_row = ttk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    ttk.Button(second_row, text="4", command=lambda : self.input_number("4"), width="5").grid(column=0, row=0)
    ttk.Button(second_row, text="5", command=lambda : self.input_number("5"), width="5").grid(column=1, row=0)
    ttk.Button(second_row, text="6", command=lambda : self.input_number("6"), width="5").grid(column=2, row=0)
    ttk.Button(second_row, text="-", command=lambda : self.input_operator("-"), width="5").grid(column=3, row=0)
    
    third_row = ttk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    ttk.Button(third_row, text="7", command=lambda : self.input_number("7"), width="5").grid(column=0, row=0)
    ttk.Button(third_row, text="8", command=lambda : self.input_number("8"), width="5").grid(column=1, row=0)
    ttk.Button(third_row, text="9", command=lambda : self.input_number("9"), width="5").grid(column=2, row=0)
    ttk.Button(third_row, text="x", command=lambda : self.input_operator("x"), width="5").grid(column=3, row=0)
    
    fourth_row = ttk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    ttk.Button(fourth_row, text="(", command=lambda : self.input_operator("("), width="5").grid(column=0, row=0)
    ttk.Button(fourth_row, text=")", command=lambda : self.input_operator(")"), width="5").grid(column=1, row=0)
    ttk.Button(fourth_row, text="^", command=lambda : self.input_operator("^"), width="5").grid(column=2, row=0)
    ttk.Button(fourth_row, text="÷", command=lambda : self.input_operator("÷"), width="5").grid(column=3, row=0)
    
    fifth_row = ttk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    ttk.Button(fifth_row, text="%", command=lambda : self.input_operator("%"), width="5").grid(column=0, row=0)
    ttk.Button(fifth_row, text="√", command=lambda : self.input_operator("√"), width="5").grid(column=1, row=0)
    ttk.Button(fifth_row, text="C", command=self.clear_button, width="5").grid(column=2, row=0)
    ttk.Button(fifth_row, text="⌫", command=self.backspace_input, width="5").grid(column=3, row=0)
  
  def _defualt_grid_column_weights(self, frame:tk.Misc, columns:int) -> None:
    for column in range(columns):
      frame.grid_columnconfigure(column, weight=1)
  
  def _defualt_grid_row_weights(self, frame:tk.Misc, rows:int) -> None:
    for row in range(rows):
      frame.grid_rowconfigure(row, weight=1)
  
  # FUNCTION 
  
  def input_number(self, input: str, event=None) -> None:
    new_equation = self.equation_display.get() + input
    self.equation_display.set(new_equation)
  
  def input_operator(self, operator: str, event=None) -> None:
    number = self.equation_display.get()
    self._update_equation_list(True, number, operator)
    new_equation = number + " " + operator + " "
    self.equation_display.set(new_equation)
  
  def input_special_op(self, operator: str, event=None) -> None:
    pass
  
  def output_answer(self, event=None) -> None:
    self._get_last_input()
    result = Resultant(self.ops, self.equation).execute()
    self.equation_display.set(result)
    self.equation.clear()
  
  def backspace_input(self, event=None) -> None:
    current_equation = self.equation_display.get()
    if current_equation:
      if current_equation[-1] != " ":
        new_equation = current_equation[:-1]
        self.equation_display.set(new_equation)
        self._update_equation_list(add_item=False)
      else:
        new_equation = current_equation[:-1]
        self.equation_display.set(new_equation)
  
  def clear_button(self, event=None) -> None:
    self.equation_display.set("")
    self.equation.clear()
  
  def _get_last_input(self) -> None:
    last_operator = self.equation[-1]
    for index, char in enumerate(self.equation_display.get()[::-1]):
      if char == last_operator:
        last_input = self.equation_display.get()[index+1:].strip()
        self._update_equation_list(True, last_input)
  
  def _update_equation_list(self, add_item=True, *args) -> None:
    if add_item:
      for item in args:
        self.equation.append(item)
    else:
      if len(self.equation) != 0:
        self.equation.pop()
  
  # UI SERVICES
  
  def bind_services(self) -> None:
    self.root.bind("<BackSpace>", lambda e: self.backspace_input(e))
    self.root.bind("<Return>", lambda e: self.output_answer(e))
    self.root.bind("<equal>", lambda e: self.output_answer(e))
    # self.root.bind("<parenleft>", lambda e : self.input_operator("(", e))
    # self.root.bind("<parenright>", lambda e : self.input_operator(")", e))
    self.root.bind("<period>", lambda e : self.input_number(".", e))
    
    self.root.bind("<Shift-slash>", lambda e : self.input_operator("÷", e))
    self.root.bind("<Shift-asterisk>", lambda e : self.input_operator("x", e))
    self.root.bind("<plus>", lambda e : self.input_operator("+", e))
    self.root.bind("<minus>", lambda e : self.input_operator("-", e))
    self.root.bind("<Shift-percent>", lambda e : self.input_operator("%", e))
    self.root.bind("<asciicircum>", lambda e : self.input_operator("^", e))
    
    for i in range(10):
      self.root.bind(f"<KeyPress-{i}>", lambda e, num = i : self.input_number(f"{num}", e))
  
  def build_ui(self) -> None:
    self.display_screen()
    self.build_buttons()
    self.bind_services()
  