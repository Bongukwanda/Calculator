import tkinter as tk
from tkinter import ttk
from services.button_controller import AddCommand

class MainWindow():
  
  SPECIAL_KEYS = ["=", "+", "-", "C", "CE", "x", "÷", "π", "^", "(", ")"]
  
  def __init__(self, root: tk.Tk | None = None):
    self.root = root
    
    # ---- Basic UI Settings ---------
    self.root.geometry("200x280")
    self.root.title("Calculator")
    
    # ---- Instance variables --------
    self.working_equation = tk.StringVar()
    self.whole_equation = tk.StringVar()
    self.parenthesis = True
    self.equation = []
    
    # ---- Services ------------------
    
    # ---- Grid Layout ---------------
    self.root.grid_columnconfigure(0, weight=1)
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    
    # ---- Build UI ------------------
    self.build_ui()
  
  # --------------- Design -----------------------------------
  
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
    
    button_number = 0
    special_key_position = 0
    
    for cal_frame in range(4, -1, -1):
      
      button_frame = ttk.Frame(calculator_frame)
      button_frame.grid(column=0, row=cal_frame, padx=4)
      text_value = ""
      
      for cal_button in range(4):
        if cal_frame > 1:
          if cal_button < 3:
            button_number += 1
            text_value = str(button_number)
            
            new_button = ttk.Button(button_frame, text=text_value, command=lambda button_number=button_number : self.press_number(button_number), width=5)
            new_button.grid(column=cal_button, row=0)
            
          else:
            text_value = self.SPECIAL_KEYS[special_key_position]
            special_key_position += 1
            
            new_button = ttk.Button(button_frame, text=text_value, command=lambda text_value=text_value: self.press_special_key(text_value), width=5)
            new_button.grid(column=cal_button, row=0)
        
        else:
          text_value = self.SPECIAL_KEYS[special_key_position]
          special_key_position += 1
          
          if text_value == "=":
            new_button = ttk.Button(button_frame, text=text_value, command=lambda text_value=text_value: self.press_special_key(text_value), width=5)
            new_button.grid(column=cal_button, row=0)
          else:
            new_button = ttk.Button(button_frame, text=text_value, command=lambda text_value=text_value: self.press_special_key(text_value), width=5)
            new_button.grid(column=cal_button, row=0)
  
  
  # -------------- Fucntions ---------------------------------
  
  def press_number(self, number_pressed: int, event=None) -> None:
    current_equation = self.working_equation.get()
    self.working_equation.set(current_equation + str(number_pressed))
    self.equation.append(number_pressed)
  
  def press_special_key(self, key: str, event=None) -> None:
    current_equation = self._update_equation(key)
    self.whole_equation.set(current_equation)
    self.clear_equation("C")
    
    if key != "(" or key != ")":
      self.equation.append(key)
  
  def press_equal(self) -> None:
    
    self.clear_equation("CE")
    self.equation.clear()
  
  def clear_equation(self, operation:str, event=None) -> None:
    if operation == "CE":
      self.whole_equation.set("")
      self.working_equation.set("")
    else:
      self.working_equation.set("")
  
  # -------------- Execution ---------------------------------
  
  def addition(self, event=None) -> None:
    result = AddCommand(self.equation).execute()
    self.clear_equation("CE")
    self.update_working_equation(str(result))
  
  # ----------------- Helpers --------------------------------
  
  def defualt_grid_column_weights(self, frame:tk.Misc, columns:int) -> None:
    for column in range(columns):
      frame.grid_columnconfigure(column, weight=1)
  
  def defualt_grid_row_weights(self, frame:tk.Misc, rows:int) -> None:
    for row in range(rows):
      frame.grid_rowconfigure(row, weight=1)
  
  def _update_equation(self, operation: str) -> str:
    working_equation = self.working_equation.get().strip()
    whole_equation = self.whole_equation.get()
    current_equation = ""
    
    if whole_equation == "" or whole_equation is None:
      current_equation = working_equation + " " + operation
    else:
      current_equation = " " + whole_equation + " " + working_equation + " " + operation
    
    return current_equation
  
  # ------------------ Build UI ------------------------------
  
  def build_ui(self) -> None:
    self.display_screen()
    self.build_buttons()