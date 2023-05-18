import tkinter as tk
from tkinter import ttk


class MainView(tk.Frame):
    def __init__(self, master, logout_callback):
        super().__init__(master)
        self.logout_callback = logout_callback

        # Create and configure widgets
        self.label = tk.Label(self, text="Main Page")

        # Create menu bar
        self.menu_bar = tk.Menu(self.master)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Save")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Settings menu
        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Preferences")
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About")
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Pack menu bar
        self.master.config(menu=self.menu_bar)

        # Email client
        self.email_tab = ttk.Frame(self)
        self.tab_pane = ttk.Notebook(self.email_tab)
        self.inbox_tab = ttk.Frame(self.tab_pane)
        self.compose_tab = ttk.Frame(self.tab_pane)
        self.tab_pane.add(self.inbox_tab, text="Inbox")
        self.tab_pane.add(self.compose_tab, text="Compose")

        # Logout button
        self.logout_button = tk.Button(
            self, text="Logout", command=self.logout)

        # Pack widgets
        self.label.pack(pady=10)
        self.email_tab.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tab_pane.pack(fill=tk.BOTH, expand=True)
        self.logout_button.pack(pady=5)

    def logout(self):
        self.logout_callback()
