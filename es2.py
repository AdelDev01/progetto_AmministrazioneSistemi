import tkinter as tk
from tkinter import ttk

class CrontabGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("600x600")

        self.listbox_frame = ttk.Frame(self)
        self.listbox_frame.pack(padx=10, pady=10)

        self.readFile()
        self.populate_listbox()

    def readFile(self):
        self.minutes = []
        self.hours = []
        self.users = []
        self.commands = []

        with open("/etc/crontab", "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) > 5:
                        self.minutes.append(parts[0])
                        self.hours.append(parts[1])
                        self.users.append(parts[5])
                        self.commands.append(" ".join(parts[6:]))

    def populate_listbox(self):
        for minute, hour, user, command in zip(self.minutes, self.hours, self.users, self.commands):
            formatted_text = f"Il comando: {command}, l'utente: {user}, l'ora e il minuto: {hour}:{minute}"
            label = tk.Label(self.listbox_frame, text=formatted_text)
            label.pack(anchor="w", pady=5)

if __name__ == "__main__":
    app = CrontabGUI()
    app.mainloop()
