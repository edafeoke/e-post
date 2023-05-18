import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Configure button style
        self.configure(relief=tk.RAISED, bd=2, padx=10, pady=5)
