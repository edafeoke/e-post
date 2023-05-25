import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


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
        self.email_scrollbar = tk.Scrollbar(self.email_tab)
        self.email_list = tk.Listbox(
            self.email_tab, selectmode=tk.SINGLE, yscrollcommand=self.email_scrollbar.set)
        self.email_scrollbar.config(command=self.email_list.yview)

        self.email_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.email_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add sample email titles to the list
        email_titles = [
            "Email 1",
            "Email 2",
            "Email 3",
            "Email 4",
            "Email 5",
            "Email 6",
            "Email 7",
            "Email 8",
            "Email 9",
            "Email 10",
            "Email 11",
            "Email 12",
            "Email 13",
            "Email 14",
            "Email 15",
            "Email 16",
            "Email 17",
            "Email 18",
            "Email 19",
            "Email 20",
        ]

        for title in email_titles:
            self.email_list.insert(tk.END, title)

        self.email_list.bind("<<ListboxSelect>>", self.show_email_content)

        self.email_preview = scrolledtext.ScrolledText(
            self.email_tab, height=10, wrap=tk.WORD)
        self.email_preview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Logout button
        self.logout_button = tk.Button(
            self, text="Logout", command=self.logout)

        # Pack widgets
        # self.label.pack(pady=10)
        self.email_tab.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.logout_button.pack(pady=5)

    def show_email_content(self, event):
        selected_index = self.email_list.curselection()
        if selected_index:
            # Retrieve the selected email title
            selected_title = self.email_list.get(selected_index)

            # Replace this with your logic to fetch email content based on the selected title
            # For demonstration, simply display the title in the email preview pane
            self.email_preview.delete(1.0, tk.END)
            self.email_preview.insert(
                tk.END, f"Email Title: {selected_title}\n")

    def logout(self):
        self.logout_callback()
        self.menu_bar.destroy()
