import tkinter as tk
from tkinter import ttk
from lines import *

class CrontabGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("600x600")

        self.listbox_frame = ttk.Frame(self)
        self.listbox_frame.pack(padx=10, pady=10)

        lineObjectsList = []
        
        self.readFile(lineObjectsList)
        self.populate_listbox()

        
    def readFile(self, lineObjectsList):
        with open("/etc/crontab", "r") as f:
            for line in f:
                lineObj = Lines()
                if line.strip() and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) > 5:
                        lineObj.changeMinute(parts[0])
                        lineObj.changeHour(parts[1])
                        lineObj.changeDayOfMonth(parts[2])
                        lineObj.changeMonth(parts[3])
                        lineObj.changeDayOfWeek(parts[4])
                        lineObj.changeUsername(parts[5])
                        lineObj.changeCommand(" ".join(parts[6:]))

                lineObjectsList.append(lineObj)
                    
        print(lineObjectsList)


    def populate_listbox(self):
        for minute, hour, user, command in zip(self.minutes, self.hours, self.users, self.commands):
            formatted_text = f"Il comando: {command}, l'utente: {user}, l'ora e il minuto: {hour}:{minute}"
            label = tk.Label(self.listbox_frame, text=formatted_text)
            label.pack(anchor="w", pady=5)

if __name__ == "__main__":
    app = CrontabGUI()
    app.mainloop()

