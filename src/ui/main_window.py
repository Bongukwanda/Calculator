import tkinter as tk
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
    
    tk.Message(self.root, background="white", justify="right", relief="solid", text=self.resultant_value).grid(padx=5, pady=5, sticky="nsew")
    
    screen_frame.grid(column=0, row=0, padx=10,pady=10)
  
  def basic_function_buttons(self) -> None:
    calculator_frame = tk.Frame(self.root, relief="solid")
    
    calculator_frame.grid_columnconfigure(0, weight=1)
    calculator_frame.grid_columnconfigure(1, weight=1)
    calculator_frame.grid_columnconfigure(2, weight=1)
    calculator_frame.grid_columnconfigure(3, weight=1)
    
    calculator_frame.grid_rowconfigure(0, weight=1)
    calculator_frame.grid_rowconfigure(1, weight=1)
    calculator_frame.grid_rowconfigure(2, weight=1)
    calculator_frame.grid_rowconfigure(3, weight=1)
    
    # ----- Numbers ----------
    tk.Button(calculator_frame, command=self._update_display(1), text="1", relief="raised").grid(column=0, row=4, padx=5, pady=5)
    tk.Button(calculator_frame, text="4", relief="raised").grid(column=0, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="7", relief="raised").grid(column=0, row=2, padx=5, pady=5)
    
    tk.Button(calculator_frame, text="3", relief="raised").grid(column=2, row=4, padx=5, pady=5)
    tk.Button(calculator_frame, text="6", relief="raised").grid(column=2, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="9", relief="raised").grid(column=2, row=2, padx=5, pady=5)
    
    tk.Button(calculator_frame, text="2", relief="raised").grid(column=1, row=4, padx=5, pady=5)
    tk.Button(calculator_frame, text="5", relief="raised").grid(column=1, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="8", relief="raised").grid(column=1, row=2, padx=5, pady=5)
    
    # ----- Basic Operations --
    tk.Button(calculator_frame, text="=", relief="raised").grid(column=3, row=4, padx=5, pady=5)
    tk.Button(calculator_frame, text="+", relief="raised").grid(column=3, row=3, padx=5, pady=5)
    tk.Button(calculator_frame, text="-", relief="raised").grid(column=3, row=2, padx=5, pady=5)
    
    tk.Button(calculator_frame, text="C", relief="raised").grid(column=0, row=1, padx=5, pady=5)
    tk.Button(calculator_frame, text="CE", relief="raised").grid(column=1, row=1, padx=5, pady=5)
    tk.Button(calculator_frame, text="/", relief="raised").grid(column=2, row=1, padx=5, pady=5)
    tk.Button(calculator_frame, text="x", relief="raised").grid(column=3, row=1, padx=5, pady=5)
    
    # ----- Operations --------
    tk.Button(calculator_frame, text="(", relief="raised").grid(column=0, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text=")", relief="raised").grid(column=1, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="÷", relief="raised").grid(column=2, row=0, padx=5, pady=5)
    tk.Button(calculator_frame, text="pi", relief="raised").grid(column=3, row=0, padx=5, pady=5)
    
    calculator_frame.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
  
  # ----------------------------------------------------------
  # AMA-FUNCTIONS ALUPHINI KWAMANYE AMA-FUNCTIONS
  # ----------------------------------------------------------
  
  def _update_display(self, update_value) -> None:
    current_text = self.resultant_value.get()
    self.resultant_value = current_text + str(update_value)
  
  # ----------------------------------------------------------
  # HLANGANISA YONKINTO
  # ----------------------------------------------------------
  
  def build_ui(self) -> None:
    self.display_screen() # Add display screen
    self.basic_function_buttons() # Add calculator buttons

# root = tk.Tk()
# app = MainWindow(root)
# root.mainloop()