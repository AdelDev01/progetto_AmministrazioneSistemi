import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from lines import Lines
import os

class CrontabGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("1000x400")

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
        self.tree.column('#0', width=70, anchor=tk.CENTER)

        # Set column headings
        self.tree.heading('Minute', text='Minute')
        self.tree.heading('Hour', text='Hour')
        self.tree.heading('Day of Month', text='Day of Month')
        self.tree.heading('Month', text='Month')
        self.tree.heading('Day of Week', text='Day of Week')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Command', text='Command')
        self.tree.heading('#0', text='Edit')

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.lineObjectsList = []
        self.original_lines = []
        
        self.readFile()
        self.populate_treeview()

        # Add save button
        self.save_button = tk.Button(self, text="Salva", command=self.update_crontab_file)
        self.save_button.pack(pady=10)

        # Add add button
        self.add_button = tk.Button(self, text="Aggiungi", command=self.add_new_entry)
        self.add_button.pack(pady=10)

    def readFile(self):
        with open("/etc/crontab", "r") as f:
            self.original_lines = f.readlines()
            for line in self.original_lines:
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
        for idx, line in enumerate(self.lineObjectsList):
            attributes = line.getAttributes()
            self.tree.insert('', tk.END, text='Modifica', values=attributes, tags=(idx,))
            self.tree.tag_bind(idx, '<Double-1>', lambda event, idx=idx: self.edit_line(idx))

    def edit_line(self, idx):
        line = self.lineObjectsList[idx]
        EditDialog(self, line)
        self.update_treeview()

    def add_new_entry(self):
        new_line = Lines("*", "*", "*", "*", "*", "root", "")
        self.lineObjectsList.append(new_line)
        EditDialog(self, new_line)
        self.update_treeview()

    def update_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.populate_treeview()

    def update_crontab_file(self):
        if not os.geteuid() == 0:
            messagebox.showerror("Errore", "Permessi di amministratore richiesti per modificare il file crontab.")
            return

        updated_lines = []
        original_line_index = 0
        line_index = 0

        while original_line_index < len(self.original_lines) or line_index < len(self.lineObjectsList):
            if original_line_index < len(self.original_lines):
                original_line = self.original_lines[original_line_index]
                if original_line.strip() and not original_line.startswith("#") and not original_line.startswith("SHELL"):
                    if line_index < len(self.lineObjectsList):
                        lineObj = self.lineObjectsList[line_index]
                        new_line = f"{lineObj.minute} {lineObj.hour}\t{lineObj.dayofmonth}\t{lineObj.month}\t{lineObj.dayofweek}\t{lineObj.username}\t{lineObj.command}\n"
                        updated_lines.append(new_line)
                        line_index += 1
                    else:
                        updated_lines.append(original_line)
                    original_line_index += 1
                else:
                    updated_lines.append(original_line)
                    original_line_index += 1
            else:
                if line_index < len(self.lineObjectsList):
                    lineObj = self.lineObjectsList[line_index]
                    new_line = f"{lineObj.minute} {lineObj.hour}\t{lineObj.dayofmonth}\t{lineObj.month}\t{lineObj.dayofweek}\t{lineObj.username}\t{lineObj.command}\n"
                    updated_lines.append(new_line)
                    line_index += 1

        try:
            with open("/etc/crontab", "w") as f:
                f.writelines(updated_lines)
            messagebox.showinfo("Info", "Modifiche salvate con successo!")
        except PermissionError:
            messagebox.showerror("Errore", "Non hai i permessi per modificare questo file.")

class EditDialog(simpledialog.Dialog):

    def __init__(self, parent, line):
        self.line = line
        super().__init__(parent, title="Edit Line")

    def body(self, master):
        self.entries = {}
        labels = ['Minute', 'Hour', 'Day of Month', 'Month', 'Day of Week', 'Username', 'Command']
        attributes = self.line.getAttributes()
        
        for i, label in enumerate(labels):
            tk.Label(master, text=label).grid(row=i, column=0)
            entry = tk.Entry(master)
            entry.insert(0, attributes[i])
            entry.grid(row=i, column=1)
            self.entries[label] = entry

    def apply(self):
        new_values = [self.entries[label].get() for label in self.entries]
        self.line.minute, self.line.hour, self.line.dayofmonth, self.line.month, self.line.dayofweek, self.line.username, self.line.command = new_values

if __name__ == "__main__":
    app = CrontabGUI()
    app.mainloop()
