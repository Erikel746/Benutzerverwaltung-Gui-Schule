#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import re

Abteilungen = [
    "Abteilungen",
    "Buchhaltung und Finanzen",
    "Forschung und Entwicklung",
    "Geschäftsleitung",
    "IT und EDV",
    "Kundendienst",
    "Marketing",
    "Personalwesen",
    "Produktion"
]

def pruefe_passwort(string):
    if not re.search(r"[A-Z]", string):
        return False

    if not re.search(r"[a-z]", string):
        return False

    if not re.search(r"\d", string):
        return False

    if len(string) <= 12:
        return False

    return True

def selbes_passwort(pw1, pw2):
    if pw1 == pw2:
        return True
    else:
        return False

def submit_action():
    vorname = firstname_entry.get()
    nachname = lastname_entry.get()
    abteilung = combo.get()
    passwort = password_entry.get()

    if abteilung == "Abteilungen" or vorname == "" or nachname == "" or passwort == "":
        messagebox.showinfo("Fehler", "Bitte füllen sie alle Felder aus.")
        return

    elif not pruefe_passwort(passwort):
        messagebox.showinfo("Fehler", "Passwort entspricht nicht den Regeln:\n"
                                      "- mindestens ein kleiner Buchstabe\n"
                                      "- mindestens ein großer Buchstabe\n"
                                      "- mindestens eine Zahl\n"
                                      "- mindestens 12 Zeichen")
        return
    else:
        benutzername = f"{nachname}.{vorname[0]}"
        # Schicke Vorname, Nachmane, Benutzername, Abteilung und hashed Passwort an das Backend
        ma_id = "1"
        mitarbeiter_id_label.config(text=f"Mitarbeiter_ID = {ma_id}")
        benutzername_label.config(text=f"Benutzername = {benutzername}")

root = Tk()
root.title("Benutzerverwaltung")
root.resizable(False, False)
large_font = ('Arial', 14)

Label(root, text="Vorname", font=large_font).grid(row=0, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Nachname", font=large_font).grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Abteilung", font=large_font).grid(row=2, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Passwort", font=large_font).grid(row=3, column=0, sticky=W, padx=10, pady=5)

firstname_entry = Entry(root, font=large_font)
lastname_entry = Entry(root, font=large_font)
combo = StringVar()
combo.set(Abteilungen[0])
drop = OptionMenu(root, combo, *Abteilungen)
password_entry = Entry(root, show="*", font=large_font)

firstname_entry.grid(row=0, column=1, sticky=W, padx=10, pady=5)
lastname_entry.grid(row=1, column=1, sticky=W, padx=10, pady=5)
drop.grid(row=2, column=1, sticky=W, padx=10, pady=5)
password_entry.grid(row=3, column=1, sticky=W, padx=10, pady=5)

submit_button = Button(root, text="Abschicken", command=submit_action)
submit_button.grid(row=7, column=1, pady=10)

exit_button = Button(root, text="Beenden", command=root.destroy)
exit_button.grid(row=7, column=0, pady=10)

mitarbeiter_id_label = Label(root, text="")
mitarbeiter_id_label.grid(row=5, column=0, columnspan=2)

benutzername_label = Label(root, text="")
benutzername_label.grid(row=6, column=0, columnspan=2)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

mainloop()
