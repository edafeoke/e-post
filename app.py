import tkinter as tk
from gui.window import MainWindow


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.mainloop()
