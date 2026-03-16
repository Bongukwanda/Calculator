import tkinter as tk
from tkinter import ttk
from src.core_function.operations import Operations

class MainWindow():
  
  def __init__(self, root: tk.Tk | None = None):
    self.root = root
    
    # ---- Basic UI Settings ---------
    self.root.geometry("200x280")
    self.root.title("Calculator")
    
    # ---- Something ----------------
    self.resultant_value: tk.StringVar | None = None
    self.operator = Operations()
    
    # ---- Grid Layout ---------------
    self.root.grid_columnconfigure(0, weight=1)
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    
    # ---- Build UI ------------------
    self.build_ui()
  
  # ----------------------------------------------------------
  # AKHA ISIZIQU ZE-CALCULATOR
  # ----------------------------------------------------------
  
  def display_screen(self) -> None:
    screen_frame = tk.Frame(self.root, borderwidth=5, relief="solid")
    screen_frame.grid(column=0, row=0, padx=4, pady=4)
    
    tk.Message(self.root, background="white", justify="right", relief="solid", text=self.resultant_value).grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
  
  def basic_function_buttons(self) -> None:
    calculator_frame = tk.Frame(self.root)
    calculator_frame.grid(column=0, row=1, sticky="nsew")
    self.defualt_grid_column_weights(calculator_frame, 1)
    self.defualt_grid_row_weights(calculator_frame, 5)
    
    first_row = tk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, padx=4)
    ttk.Button(first_row, text="1", width="5").grid(column=0, row=0)
    ttk.Button(first_row, text="2", width="5").grid(column=1, row=0)
    ttk.Button(first_row, text="3", width="5").grid(column=2, row=0)
    ttk.Button(first_row, text="=", width="5").grid(column=3, row=0)
    
    second_row = tk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, padx=4)
    ttk.Button(second_row, text="4", width="5").grid(column=0, row=0)
    ttk.Button(second_row, text="5", width="5").grid(column=1, row=0)
    ttk.Button(second_row, text="6", width="5").grid(column=2, row=0)
    ttk.Button(second_row, text="+", width="5").grid(column=3, row=0)
    
    third_row = tk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, padx=4)
    ttk.Button(third_row, text="7", width="5").grid(column=0, row=0)
    ttk.Button(third_row, text="8", width="5").grid(column=1, row=0)
    ttk.Button(third_row, text="9", width="5").grid(column=2, row=0)
    ttk.Button(third_row, text="-", width="5").grid(column=3, row=0)
    
    fourth_row = tk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, padx=4)
    ttk.Button(fourth_row, text="C", width="5").grid(column=0, row=1)
    ttk.Button(fourth_row, text="CE", width="5").grid(column=1, row=1)
    ttk.Button(fourth_row, text="/", width="5").grid(column=2, row=1)
    ttk.Button(fourth_row, text="x", width="5").grid(column=3, row=1)
    
    fifth_row = tk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, padx=4)
    ttk.Button(fifth_row, text="(", width="5").grid(column=0, row=0)
    ttk.Button(fifth_row, text=")", width="5").grid(column=1, row=0)
    ttk.Button(fifth_row, text="÷", width="5").grid(column=2, row=0)
    ttk.Button(fifth_row, text="π", width="5").grid(column=3, row=0)
  
  # ----------------------------------------------------------
  # AMA-FUNCTIONS ALUPHINI KWAMANYE AMA-FUNCTIONS
  # ----------------------------------------------------------
  
  def defualt_grid_column_weights(self, frame:tk.Misc, columns:int) -> None:
    for column in range(columns):
      frame.grid_columnconfigure(column, weight=1)
  
  def defualt_grid_row_weights(self, frame:tk.Misc, rows:int) -> None:
    for row in range(rows):
      frame.grid_rowconfigure(row, weight=1)
  
  # ----------------------------------------------------------
  # HLANGANISA YONKINTO
  # ----------------------------------------------------------
  
  def build_ui(self) -> None:
    self.display_screen()
    self.basic_function_buttons()