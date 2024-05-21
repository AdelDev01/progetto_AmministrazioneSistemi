# Questa è una classe creata per descrivere una riga del file crontab. Contiene tutti i suoi attributi e i 
# metodi setter e getter, più qualche metodo per stampare gli attributi


class Lines:
    # Inizializzazione di una riga con questi attributi
    def __init__(self, minute, hour, dayofmonth, month, dayofweek, username, command):
        self.minute = minute
        self.hour = hour
        self.dayofmonth = dayofmonth
        self.month = month
        self.dayofweek = dayofweek
        self.username = username
        self.command = command

#-----------------------------metodi print------------------------------
    
    def printAttr(self, attribute):
        if hasattr(self, attribute):
            print(getattr(self, attribute))
        else:
            print(f"L'attributo {attribute} non esiste nella classe Lines.")


#metodo print di tutto
    def printAttributes(self):
        print(
            f"Minuto: {self.minute}, ",
            f"Ora: {self.hour}, "
            f"Giorno del mese: {self.dayofmonth}, "
            f"Mese: {self.month}, "
            f"Giorno della settimana: {self.dayofweek}, "
            f"Username: {self.username}, "
            f"Comando: {self.command}"
            )
    



#-----------------------------metodi getter------------------------------
    def getAttr(self, attribute):
        if hasattr(self, attribute):
            return getattr(self, attribute)
        else:
            print(f"L'attributo {attribute} non esiste nella classe Lines.")


#metodo getter di tutto
    def getAttributes(self):
        return [self.minute, self.hour, self.dayofmonth, self.month, self.dayofweek, self.username, self.command ]



#-----------------------------metodi setter------------------------------

    # Metodo specifico per cambiare il minuto
    def changeMinute(self, newMin):
        if type(newMin) is int and 0 <= newMin <= 59:
            self.minute = newMin
        else:
            raise ValueError("Il valore per i minuti deve essere un numero intero tra 0 e 59.")

    # Metodo specifico per cambiare l'ora
    def changeHour(self, newHour):
        if type(newHour) is int and 0 <= newHour <= 23:
            self.hour = newHour
        else:
            raise ValueError("Il valore per le ore deve essere un numero intero tra 0 e 23.")

    # Metodo specifico per cambiare il giorno del mese
    def changeDayOfMonth(self, newDayOfMonth):
        if type(newDayOfMonth) is int and 1 <= newDayOfMonth <= 31:
            self.dayofmonth = newDayOfMonth
        else:
            raise ValueError("Il valore per il giorno del mese deve essere un numero intero tra 1 e 31.")

    # Metodo specifico per cambiare il mese
    def changeMonth(self, newMonth):
        if type(newMonth) is int and 1 <= newMonth <= 12:
            self.month = newMonth
        else:
            raise ValueError("Il valore per il mese deve essere un numero intero tra 1 e 12.")

    # Metodo specifico per cambiare il giorno della settimana
    def changeDayOfWeek(self, newDayOfWeek):
        if type(newDayOfWeek) is int and 0 <= newDayOfWeek <= 6:
            self.dayofweek = newDayOfWeek
        else:
            raise ValueError("Il valore per il giorno della settimana deve essere un numero intero tra 0 e 6.")

    # Metodo specifico per cambiare l'username
    def changeUsername(self, newUsername):
        if type(newUsername) is str:
            self.username = newUsername
        else:
            raise ValueError("Il valore per il nome utente deve essere una stringa.")

    # Metodo specifico per cambiare il comando
    def changeCommand(self, newCommand):
        if type(newCommand) is str:
            self.command = newCommand
        else:
            raise ValueError("Il valore per il comando deve essere una stringa.")
