#!/usr/bin/python3


import tkinter as tk
from gui.views.view_manager import ViewManager

def main():
    root = tk.Tk()
    root.title("E-Post")
    root.geometry("500x300")

    view_manager = ViewManager(root)
    view_manager.show_login_view()

    root.mainloop()


if __name__ == '__main__':
    main()
