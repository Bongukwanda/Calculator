import tkinter as tk
from tkinter import ttk

class MainWindow():
  
  def __init__(self, root: tk.Tk):
    self.root = root
    
    # ---- Basic UI --------
    self.root.geometry("450x350")
    
    # ---- Build UI ---------
    self.build_ui()
  
  def display_screen(self) -> None:
    screen_frame = ttk.Frame(self.root)
  
  
  def build_ui(self):
    pass
  