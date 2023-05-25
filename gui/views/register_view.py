#!/usr/bin/python3

import tkinter as tk
import sqlite3



class RegisterView(tk.Frame):
    def __init__(self, master, login_callback):
        super().__init__(master)
        self.login_callback = login_callback

        # Create and configure widgets
        self.label = tk.Label(self, text="Register")
        self.email_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        self.register_button = tk.Button(
            self, text="Register", command=self.register)
        self.back_button = tk.Button(
            self, text="Back", command=self.login_callback)

        # Pack widgets
        self.label.pack(pady=10)
        self.email_entry.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.register_button.pack(pady=5)
        self.back_button.pack(pady=5)

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        try:
            # Connect to the database (creates a new database file if it doesn't exist)
            conn = sqlite3.connect('test.db')

            # Create a cursor object to execute SQL commands
            cursor = conn.cursor()

            # Create a table to store users if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR UNIQUE,
                password VARCHAR
                )
            ''')

            # Perform registration logic

            if email and password:
                cursor.execute(
                    'INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
                conn.commit()
                print(f"Registered: email={email}, password={password}")
                # Perform further actions upon successful registration
            else:
                print("Registration failed: Please enter both email and password.")
        except sqlite3.Error as e:
            # Handle any errors that occur during execution
            print("An error occurred:", e)
        finally:
            # Close the cursor and the connection
            cursor.close()
            conn.close()
