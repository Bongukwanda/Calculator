import tkinter as tk
from tkinter import ttk

class MainWindow():
  
  def __init__(self, root: tk.Tk | None = None):
    self.root = root
    
    # ---- Basic UI Settings ---------
    self.root.geometry("300x350")
    self.root.title("Calculator")
    
    # ---- Grid Layout ---------------
    self.root.grid_columnconfigure(0, weight=1)
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    
    # ---- Build UI ------------------
    self.build_ui()
  
  # ----------------------------------------------------------
  # DESIGN CALCULATOR
  # ----------------------------------------------------------
  
  def display_screen(self) -> None:
    screen_frame = tk.Frame(self.root, borderwidth=5, relief="solid")
    
    resultant_value = tk.StringVar()
    display = tk.Message(self.root, background="white", justify="right", relief="solid", textvariable=resultant_value)
    display.grid(padx=5, pady=5, sticky="nsew")
    
    screen_frame.grid(column=0, row=0, padx=10,pady=10)
  
  def basic_function_buttons(self) -> None:
    calculator_frame = tk.Frame(self.root, relief="solid")
    
    # ----- Numbers ----------
    tk.Button(calculator_frame, text="1", relief="raised").grid(column=0, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="4", relief="raised").grid(column=0, row=2, padx=5, pady=5)
    tk.Button(calculator_frame, text="7", relief="raised").grid(column=0, row=1, padx=5, pady=5)
    
    tk.Button(calculator_frame, text="3", relief="raised").grid(column=2, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="6", relief="raised").grid(column=2, row=2, padx=5, pady=5)
    tk.Button(calculator_frame, text="9", relief="raised").grid(column=2, row=1, padx=5, pady=5)
    
    tk.Button(calculator_frame, text="2", relief="raised").grid(column=1, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="5", relief="raised").grid(column=1, row=2, padx=5, pady=5)
    tk.Button(calculator_frame, text="8", relief="raised").grid(column=1, row=1, padx=5, pady=5)
    
    # ----- Basic Operations --
    tk.Button(calculator_frame, text="=", relief="raised").grid(column=3, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="+", relief="raised").grid(column=3, row=2, padx=5, pady=5)
    tk.Button(calculator_frame, text="-", relief="raised").grid(column=3, row=1, padx=5, pady=5)
    
    tk.Button(calculator_frame, text="C", relief="raised").grid(column=0, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="CE", relief="raised").grid(column=1, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="/", relief="raised").grid(column=2, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="x", relief="raised").grid(column=3, row=0, padx=5, pady=5)
    
    calculator_frame.grid(column=0, row=1, padx=5, pady=5, sticky="nswe")
  
  # ----------------------------------------------------------
  # AMA-FUNCTIONS ALUPHINI KWAMANYE AMA-FUNCTIONS
  # ----------------------------------------------------------
  
  # ----------------------------------------------------------
  # HLANGANISA YONKINTO
  # ----------------------------------------------------------
  
  def build_ui(self) -> None:
    self.display_screen() # Add display screen
    self.basic_function_buttons() # Add calculator buttons

root = tk.Tk()
app = MainWindow(root)
root.mainloop()