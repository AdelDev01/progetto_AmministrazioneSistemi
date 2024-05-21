import tkinter as tk
from lines import *

class crontabGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Crontab")
        self.geometry("600x600")

        self.list = [] # inizializzo una lista vuota in cui inserirò le righe
        self.readFile()
        
        # Creazione della Listbox per mostrare gli elementi della lista
        self.listbox = tk.Listbox(self, width=100, height=30)
        self.listbox.pack(padx=10, pady=10)
        
        # Popolamento della Listbox con gli elementi della lista
        self.populate_listbox()

    def cleanOutput(self, line): # visto che l'output del crontab visualizzato in tkinter non compare correttamente, faccio una pulizia
        """Sostituisce i tab con quattro spazi e rimuove i caratteri di campanella."""
        cleaned = line.replace('\t', ' ' * 4)  # Sostituisce i tab con quattro spazi, sennò sarebbero delle freccie
        cleaned = cleaned.replace('\a', '')  # Rimuove eventuali caratteri di campanella
        return cleaned.strip()  # Rimuove spazi bianchi all'inizio e alla fine

    def readFile(self):
        with open("/etc/crontab", "r") as f:
            file = f.readlines()
            i = 18 # la riga 18 nel file crontab è la prima riga ufficiale, gli altri sono commenti
            while i < len(file):
                line = file[i].strip()
                if line and not line.startswith('#'):
                    cleaned_line = self.cleanOutput(line)
                    self.list.append(cleaned_line)
                i += 1

    def populate_listbox(self):
        for item in self.list:
            self.listbox.insert(tk.END, item)

if __name__ == "__main__":
    app = crontabGUI()
    app.mainloop()
