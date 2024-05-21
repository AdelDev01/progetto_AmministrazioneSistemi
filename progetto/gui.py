import tkinter as tk
from tkinter import ttk
from lines import Lines

class CrontabGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("800x400")

        # Create Treeview
        self.tree = ttk.Treeview(self, columns=('Minute', 'Hour', 'Day of Month', 'Month', 'Day of Week', 'Username', 'Command'), show='headings')
        
        # Define column widths
        self.tree.column('Minute', width=50, anchor=tk.CENTER)
        self.tree.column('Hour', width=50, anchor=tk.CENTER)
        self.tree.column('Day of Month', width=100, anchor=tk.CENTER)
        self.tree.column('Month', width=70, anchor=tk.CENTER)
        self.tree.column('Day of Week', width=100, anchor=tk.CENTER)
        self.tree.column('Username', width=100, anchor=tk.CENTER)
        self.tree.column('Command', width=330, anchor=tk.W)

        # Set column headings
        self.tree.heading('Minute', text='Minute')
        self.tree.heading('Hour', text='Hour')
        self.tree.heading('Day of Month', text='Day of Month')
        self.tree.heading('Month', text='Month')
        self.tree.heading('Day of Week', text='Day of Week')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Command', text='Command')

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.lineObjectsList = []
        
        self.readFile()
        self.populate_treeview()

    def readFile(self):
        with open("/etc/crontab", "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#") and not line.startswith("SHELL"):
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

    def populate_treeview(self):
        for line in self.lineObjectsList:
            attributes = line.getAttributes()
            self.tree.insert('', tk.END, values=attributes)

if __name__ == "__main__":
    app = CrontabGUI()
    app.mainloop()
