from tkinter import *
from tkinter import ttk
import sqlite3

def dodaj_obrok():
    obroci = Tk()
    obroci.geometry("800x600")
    obroci.title("Obroci")

    # Povezivanje sa bazom podataka
    conn = sqlite3.connect("tablicakalorija.db")
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM tablicakalorija
    ''')
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Kreiranje Treeview widgeta za prikaz podataka
    tree = ttk.Treeview(obroci, columns=("Id", "Namirnica", "Kalorije",
                                         "Proteini", "Ugljenihidrati", "Masti"),
                                         show="headings")
    
    # Define the columns and headings
    tree.heading("Id", text="Index")
    tree.heading("Namirnica", text="Namirnica")
    tree.heading("Kalorije", text="Kalorije")
    tree.heading("Proteini", text="Proteini")
    tree.heading("Ugljenihidrati", text="Ugljenihidrati")
    tree.heading("Masti", text="Masti")

    # Changind column width
    tree.column("Id", width=40, anchor='center')
    tree.column("Namirnica", width=70, anchor='center')
    tree.column("Kalorije", width=50, anchor='center')
    tree.column("Proteini", width=50, anchor='center')
    tree.column("Ugljenihidrati", width=80, anchor='center')
    tree.column("Masti", width=40, anchor='center')

    # Insert data into the Treeview
    for row in data:
        tree.insert("", "end", values=row)

    tree.grid(row=0, column=0, padx=10)  


    obroci.mainloop()