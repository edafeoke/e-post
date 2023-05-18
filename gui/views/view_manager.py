#!/usr/bin/python3

import tkinter as tk
from gui.views.login_view import LoginView
from gui.views.register_view import RegisterView
from gui.views.main_view import MainView


class ViewManager:
    def __init__(self, master):
        self.master = master

    def show_login_view(self):
        self.clear_frame()
        login_view = LoginView(
            self.master, self.show_register_view, self.show_main_view)
        login_view.pack(fill=tk.BOTH, expand=True)

    def show_register_view(self):
        self.clear_frame()
        register_view = RegisterView(self.master, self.show_login_view)
        register_view.pack(fill=tk.BOTH, expand=True)

    def show_main_view(self):
        self.clear_frame()
        main_view = MainView(self.master, self.show_login_view)
        main_view.pack(fill=tk.BOTH, expand=True)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
