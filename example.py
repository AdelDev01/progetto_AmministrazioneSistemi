import tkinter as tk
from tkinter import ttk
import backup_func
from tkinter import filedialog
from tkcalendar import Calendar

class BackupApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("600x600")
        
        self.source_label = tk.Label(self, text="Source")
        # self.source_label.pack()
        self.source_entry = tk.Entry(self, width=50)
        self.source_entry.pack()
        self.source_button = tk.Button(self, text="Browse", command=self.browse_source)
        self.source_button.pack()
        
        self.destination_label = tk.Label(self, text="Destination")
        self.destination_label.pack()
        self.destination_entry = tk.Entry(self, width=50)
        self.destination_entry.pack()
        self.destination_button = tk.Button(self, text="Browse", command=self.browse_destination)
        self.destination_button.pack()

        self.calendar_label = tk.Label(self, text="Select Backup Date")
        self.calendar_label.pack()
        self.calendar = Calendar(self, selectmode='day', date_pattern='d/m/yy')
        self.calendar.pack()

        self.time_label = tk.Label(self, text="Select Backup Time")
        self.time_label.pack()
        self.time_combobox = ttk.Combobox(self, values=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"])
        self.time_combobox.pack()

        self.backup_button = tk.Button(self, text="Backup Now", command=self.backup_now)
        self.backup_button.pack()

    def browse_source(self):
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, filedialog.askdirectory())

    def browse_destination(self):
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, filedialog.askdirectory())

    def backup_now(self):
        src = self.source_entry.get()
        dst = self.destination_entry.get()
        selected_date = self.calendar.get_date()
        selected_time = self.time_combobox.get()
        #try:
        backup_func.schedule_backup(src, dst, selected_date, selected_time)
        #except ValueError:
        # If both formats fail, show an error message
            #tk.messagebox.showerror("Backup App", "Invalid date or time format. Please use DD/MM/YYYY HH:MM")
      

if __name__ == "__main__":
    app = BackupApp()
    app.mainloop()