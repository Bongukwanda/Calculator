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
    self.screen_output = tk.StringVar()
    self.button_ops = ButtonController()
    
    # ---- Grid Layout ---------------
    self.root.grid_columnconfigure(0, weight=1)
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    
    # ---- Build UI ------------------
    self.build_ui()
  
  # ----------------------------------------------------------
  
  def display_screen(self) -> None:
    screen_frame = ttk.Frame(self.root, borderwidth=5, relief="flat")
    screen_frame.grid(column=0, row=0, padx=4, pady=4)
    
    cal_message = ttk.Entry(
      self.root,
      background="white",
      font=("Segoe UI", 10),
      justify="right", 
      textvariable=self.screen_output
    )
    cal_message.config(state="readonly")
    cal_message.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
  
  def build_buttons(self) -> None:
    calculator_frame = ttk.Frame(self.root)
    calculator_frame.grid(column=0, row=1, sticky="nsew")
    
    self.defualt_grid_column_weights(calculator_frame, 1)
    self.defualt_grid_row_weights(calculator_frame, 5)
    
    first_row = ttk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    one = ttk.Button(first_row, text="1", command=lambda : self.update_equation_display("1"), width="5")
    one.grid(column=0, row=0)
    two = ttk.Button(first_row, text="2", command=lambda : self.update_equation_display("2"), width="5")
    two.grid(column=1, row=0)
    three = ttk.Button(first_row, text="3", command=lambda : self.update_equation_display("3"), width="5")
    three.grid(column=2, row=0)
    equal_to = ttk.Button(first_row, text="=", width="5")
    equal_to.grid(column=3, row=0)
    
    second_row = ttk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    four = ttk.Button(second_row, text="4", command=lambda : self.update_equation_display("4"), width="5")
    four.grid(column=0, row=0)
    five = ttk.Button(second_row, text="5", command=lambda : self.update_equation_display("5"), width="5")
    five.grid(column=1, row=0)
    six = ttk.Button(second_row, text="6", command=lambda : self.update_equation_display("6"), width="5")
    six.grid(column=2, row=0)
    plus = ttk.Button(second_row, text="+", command=lambda : self.update_equation_display(" + "), width="5")
    plus.grid(column=3, row=0)
    
    third_row = ttk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    seven = ttk.Button(third_row, text="7", command=lambda : self.update_equation_display("7"), width="5")
    seven.grid(column=0, row=0)
    eight = ttk.Button(third_row, text="8", command=lambda : self.update_equation_display("8"), width="5")
    eight.grid(column=1, row=0)
    nine = ttk.Button(third_row, text="9", command=lambda : self.update_equation_display("9"), width="5")
    nine.grid(column=2, row=0)
    minus = ttk.Button(third_row, text="-", command=lambda : self.update_equation_display(" - "), width="5")
    minus.grid(column=3, row=0)
    
    fourth_row = ttk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    c = ttk.Button(fourth_row, text="C", command=self.clear_equation_display, width="5")
    c.grid(column=0, row=1)
    ce = ttk.Button(fourth_row, text="CE", width="5")
    ce.grid(column=1, row=1)
    divide = ttk.Button(fourth_row, text="÷", command=lambda : self.update_equation_display(" ÷ "), width="5")
    divide.grid(column=2, row=1)
    multiply = ttk.Button(fourth_row, text="x", command=lambda : self.update_equation_display(" x "), width="5")
    multiply.grid(column=3, row=1)
    
    fifth_row = ttk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    open_bracket = ttk.Button(fifth_row, text="(",  command=lambda : self.update_equation_display("("), width="5")
    open_bracket.grid(column=0, row=0)
    close_bracket = ttk.Button(fifth_row, text=")",  command=lambda : self.update_equation_display(")"), width="5")
    close_bracket.grid(column=1, row=0)
    pi = ttk.Button(fifth_row, text="π", width="5")
    pi.grid(column=2, row=0)
    raise_to = ttk.Button(fifth_row, text="^", command=lambda : self.update_equation_display("^"), width="5")
    raise_to.grid(column=3, row=0)
  
  def update_equation_display(self, execution:str, event=None) -> None:
    current_equation = self.screen_output.get().strip()
    current_equation += execution
    self.screen_output.set(current_equation)
  
  def clear_equation_display(self, event=None) -> None:
    self.screen_output.set("")
  
  # -----------------------------------------------
  
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