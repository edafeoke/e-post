import tkinter as tk
from gui.frames import MainFrame


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('My App')
        self.main_frame = MainFrame(self)
        
    def pack(self, *args, **kwargs):
        super().pack(fill='both', expand=True, *args, **kwargs)
        self.main_frame.pack(fill='both', expand=True)


class LabelFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text='Hello, World!')
        self.label.pack()
        
    def set_label_text(self, text):
        self.label.config(text=text)


class ButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.button = tk.Button(self, text='Click Me!', command=self.on_button_click)
        self.button.pack()
        
    def on_button_click(self):
        self.master.master.main_frame.label_frame.set_label_text('Button Clicked!')
        

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label_frame = LabelFrame(self)
        self.button_frame = ButtonFrame(self)
        
    def pack(self, *args, **kwargs):
        super().pack(fill='both', expand=True, *args, **kwargs)
        self.label_frame.pack(fill='both', expand=True)
        self.button_frame.pack()
