#!/usr/bin/python3

import tkinter as tk


class RegisterView(tk.Frame):
    def __init__(self, master, login_callback):
        super().__init__(master)
        self.login_callback = login_callback

        # Create and configure widgets
        self.label = tk.Label(self, text="Register")
        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        self.register_button = tk.Button(
            self, text="Register", command=self.register)
        self.back_button = tk.Button(
            self, text="Back", command=self.login_callback)

        # Pack widgets
        self.label.pack(pady=10)
        self.username_entry.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.register_button.pack(pady=5)
        self.back_button.pack(pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform registration logic
        # Replace this with your own registration logic

        if username and password:
            print(f"Registered: username={username}, password={password}")
            # Perform further actions upon successful registration
        else:
            print("Registration failed: Please enter both username and password.")
