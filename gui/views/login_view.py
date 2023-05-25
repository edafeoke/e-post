#!/usr/bin/python3


import tkinter as tk
import sqlite3


class LoginView(tk.Frame):
    def __init__(self, master, register_callback, login_success_callback):
        super().__init__(master)
        self.register_callback = register_callback
        self.login_success_callback = login_success_callback

        # Create and configure widgets
        self.label = tk.Label(self, text="Login")
        self.email_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.register_button = tk.Button(
            self, text="Register", command=self.register_callback)

        # Pack widgets
        self.label.pack(pady=10)
        self.email_entry.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=5)
        self.register_button.pack(pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Perform login authentication logic
        # Replace this with your own authentication logic
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        try:
            # Execute the SELECT query with a parameterized query
            cursor.execute("SELECT email, password FROM users WHERE email=?", (email,))
            result = cursor.fetchone()

            if result:
                if password == result[1]:
                    print("Login successful!")
                    self.login_success_callback()
                    # Perform further actions upon successful login
                else:
                    print("Login failed!")
            else:
                print("User not found.")

        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            cursor.close()
            conn.close()
