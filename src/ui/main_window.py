import tkinter as tk
from core_function.operations import Operations

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
    self.root.grid_rowconfigure(1, weight=2)
    
    # ---- Build UI ------------------
    self.build_ui()
  
  # ----------------------------------------------------------
  # AKHA ISIZIQU ZE-CALCULATOR
  # ----------------------------------------------------------
  
  def display_screen(self) -> None:
    screen_frame = tk.Frame(self.root, borderwidth=5, relief="solid")
    screen_frame.grid(column=0, row=0)
    
    tk.Message(self.root, background="white", justify="right", relief="solid", text=self.resultant_value).grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
  
  def basic_function_buttons(self) -> None:
    calculator_frame = tk.Frame(self.root, relief="solid")
    calculator_frame.grid(column=0, row=1, padx=2, pady=8)
    
    first_row = tk.Frame(calculator_frame)
    first_row.grid(column=0, row=4, sticky="nsew")
    tk.Button(first_row, text="1", relief="raised").grid(column=0, row=0, sticky="nsew")
    tk.Button(first_row, text="2", relief="raised").grid(column=1, row=0, sticky="nsew")
    tk.Button(first_row, text="3", relief="raised").grid(column=2, row=0, sticky="nsew")
    tk.Button(first_row, text="=", relief="raised").grid(column=3, row=0, sticky="nsew")
    
    second_row = tk.Frame(calculator_frame)
    second_row.grid(column=0, row=3, sticky="nsew")
    tk.Button(second_row, text="4", relief="raised").grid(column=0, row=0, padx=5, pady=5)
    tk.Button(second_row, text="5", relief="raised").grid(column=1, row=0, padx=5, pady=5)
    tk.Button(second_row, text="6", relief="raised").grid(column=2, row=0, padx=5, pady=5)
    tk.Button(second_row, text="+", relief="raised").grid(column=3, row=0, padx=5, pady=5)
    
    third_row = tk.Frame(calculator_frame)
    third_row.grid(column=0, row=2, sticky="ew")
    tk.Button(third_row, text="7", relief="raised").grid(column=0, row=0, padx=5, pady=5)
    tk.Button(third_row, text="8", relief="raised").grid(column=1, row=0, padx=5, pady=5)
    tk.Button(third_row, text="9", relief="raised").grid(column=2, row=0, padx=5, pady=5)
    tk.Button(third_row, text="-", relief="raised").grid(column=3, row=0, padx=5, pady=5)
    
    fourth_row = tk.Frame(calculator_frame)
    fourth_row.grid(column=0, row=1, sticky="ew")
    tk.Button(fourth_row, text="C", relief="raised").grid(column=0, row=1, padx=5, pady=5)
    tk.Button(fourth_row, text="CE", relief="raised").grid(column=1, row=1, padx=5, pady=5)
    tk.Button(fourth_row, text="/", relief="raised").grid(column=2, row=1, padx=5, pady=5)
    tk.Button(fourth_row, text="x", relief="raised").grid(column=3, row=1, padx=5, pady=5)
    
    fifth_row = tk.Frame(calculator_frame)
    fifth_row.grid(column=0, row=0, sticky="ew")
    tk.Button(fifth_row, text="(", relief="raised").grid(column=0, row=0, padx=5, pady=5)
    tk.Button(fifth_row, text=")", relief="raised").grid(column=1, row=0, padx=5, pady=5)
    tk.Button(fifth_row, text="÷", relief="raised").grid(column=2, row=0, padx=5, pady=5)
    tk.Button(fifth_row, text="pi", relief="raised").grid(column=3, row=0, padx=5, pady=5)
  
  # ----------------------------------------------------------
  # AMA-FUNCTIONS ALUPHINI KWAMANYE AMA-FUNCTIONS
  # ----------------------------------------------------------
  
  # ----------------------------------------------------------
  # HLANGANISA YONKINTO
  # ----------------------------------------------------------
  
  def build_ui(self) -> None:
    self.display_screen()
    self.basic_function_buttons()