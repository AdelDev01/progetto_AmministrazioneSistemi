import tkinter as tk
from tkinter import ttk
from lines import Lines

class CrontabGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("600x600")

        self.listbox_frame = ttk.Frame(self)
        self.listbox_frame.pack(padx=10, pady=10)

        self.lineObjectsList = []
        
        self.readFile()
        self.populate_listbox()

        
    def readFile(self):
        with open("/etc/crontab", "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) > 5:
                        lineObj = Lines(
                            minute=parts[0],
                            hour=parts[1],
                            dayofmonth=parts[2],
                            month=parts[3],
                            dayofweek=parts[4],
                            username=parts[5],
                            command=" ".join(parts[6:])
                        )
                        self.lineObjectsList.append(lineObj)
                    
        return self.lineObjectsList

    def populate_listbox(self):
        for line in self.lineObjectsList:
            formatted_text = f"Il comando: {line.command}, l'utente: {line.username}, l'ora e il minuto: {line.hour}:{line.minute}"
            label = tk.Label(self.listbox_frame, text=formatted_text)
            label.pack(anchor="w", pady=5)

if __name__ == "__main__":
    app = CrontabGUI()
    app.mainloop()
