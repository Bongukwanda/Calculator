import tkinter as tk
from tkinter import ttk

class MainWindow():
  
  def __init__(self, root: tk.Tk | None = None):
    self.root = root
    
    # ---- Basic UI ---------
    self.root.geometry("300x350")
    
    # ---- Grid Layout ------
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=2)
    
    # ---- Build UI ---------
    self.build_ui()
  
  # ----------------------------------------------------------
  # DESIGN CALCULATOR
  # ----------------------------------------------------------
  
  def display_screen(self) -> None:
    screen_frame = tk.Frame(self.root, borderwidth=5, relief="solid")
    screen_frame.grid(column=0, row=0, padx=5,pady=5)
  
  def calculator_buttons(self) -> None:
    calculator_frame = tk.Frame(self.root, relief="solid")
    # calculator_frame.grid_columnconfigure()
    # calculator_frame.grid_rowconfigure()
    
    tk.Button(calculator_frame, text="1", relief="raised").grid(column=0, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="2", relief="raised").grid(column=1, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="3", relief="raised").grid(column=2, row=0, padx=5, pady=5)
    
    
    calculator_frame.grid(column=0, row=1, padx=5, pady=5)
  
  def number_buttons(self) -> None:
    button_frame = tk.Frame(self.root)
    button_frame.grid(column=0, row=1, padx=5, pady=5)
  
  # ----------------------------------------------------------
  # AMA-FUNCTIONS ALUPHINI KWAMANYE AMA-FUNCTIONS
  # ----------------------------------------------------------
  
  # ----------------------------------------------------------
  # HLANGANISA YONKINTO
  # ----------------------------------------------------------
  
  def build_ui(self) -> None:
    self.display_screen() # Add display screen
    self.calculator_buttons() # Add calculator buttons
  