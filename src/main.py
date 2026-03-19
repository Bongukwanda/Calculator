import tkinter as tk
from ui.main_window import MainWindow

def run_app():
  root = tk.Tk()
  app = MainWindow(root)
  root.mainloop()

if __name__ == "__main__":
  run_app()