#!/usr/bin/python3


import tkinter as tk


class LoginView(tk.Frame):
    def __init__(self, master, register_callback, login_success_callback):
        super().__init__(master)
        self.register_callback = register_callback
        self.login_success_callback = login_success_callback

        # Create and configure widgets
        self.label = tk.Label(self, text="Login")
        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.register_button = tk.Button(
            self, text="Register", command=self.register_callback)

        # Pack widgets
        self.label.pack(pady=10)
        self.username_entry.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=5)
        self.register_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform login authentication logic
        # Replace this with your own authentication logic

        if username == "admin" and password == "password":
            print("Login successful!")
            self.login_success_callback()
            # Perform further actions upon successful login
        else:
            print("Login failed!")
