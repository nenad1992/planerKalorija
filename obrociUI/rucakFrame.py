from tkinter import *
from tkinter import ttk

def rucakFrame(root):
    # Frame rucak
    rucak_frame = LabelFrame(root, text="Rucak")
    rucak_frame.grid(row=3, column=3, rowspan=3, padx=50)

    # Dodavanje i pozicioniranje dugmeta za dodavanje i uklanje obroka za rucak
    rucak_dugme = Button(rucak_frame, text="Dodaj obrok")
    rucak_dugme.grid(row=0, column=0, pady=10)
    ukloni_rucak_dugme = Button(rucak_frame, text="Ukloni obrok")
    ukloni_rucak_dugme.grid(row=1, column=0, pady=10)

    # Kreiranje Treeview widgeta za prikaz podataka za rucak
    tree_rucak = ttk.Treeview(rucak_frame, columns=("Id", "Namirnica", "Kalorije",
                                                    "Proteini", "Ugljenihidrati", "Masti"),
                                                    show="headings", height=5)
    # Definisanje kolona i headinga
    tree_rucak.heading("Id", text="Index")
    tree_rucak.heading("Namirnica", text="Namirnica")
    tree_rucak.heading("Kalorije", text="Kalorije")
    tree_rucak.heading("Proteini", text="Proteini")
    tree_rucak.heading("Ugljenihidrati", text="Ugljenihidrati")
    tree_rucak.heading("Masti", text="Masti")

    # Podesavanje sirine kolone
    tree_rucak.column("Id", width=40, anchor='center')
    tree_rucak.column("Namirnica", width=70, anchor='center')
    tree_rucak.column("Kalorije", width=50, anchor='center')
    tree_rucak.column("Proteini", width=50, anchor='center')
    tree_rucak.column("Ugljenihidrati", width=80, anchor='center')
    tree_rucak.column("Masti", width=40, anchor='center')

    # Pozicioniranje Treeview widgeta
    tree_rucak.grid(row=0, column=1, padx=10, pady=10, rowspan=2)

    # Kreiranje Treeview widgeta za prikaz ukupnih vrednosti za rucak
    tree_rucak_ukupno = ttk.Treeview(rucak_frame, columns=("Id", "Namirnica", "Kalorije",
                                                           "Proteini", "Ugljenihidrati", "Masti"),
                                                           show="headings", height=1)
    # Definisanje kolona i headinga
    tree_rucak_ukupno.heading("Id", text="#")
    tree_rucak_ukupno.heading("Namirnica", text="#")
    tree_rucak_ukupno.heading("Kalorije", text="Kalorije")
    tree_rucak_ukupno.heading("Proteini", text="Proteini")
    tree_rucak_ukupno.heading("Ugljenihidrati", text="Ugljenihidrati")
    tree_rucak_ukupno.heading("Masti", text="Masti")

    # Podesavanje sirine kolone
    tree_rucak_ukupno.column("Id", width=40, anchor='center')
    tree_rucak_ukupno.column("Namirnica", width=70, anchor='center')
    tree_rucak_ukupno.column("Kalorije", width=50, anchor='center')
    tree_rucak_ukupno.column("Proteini", width=50, anchor='center')
    tree_rucak_ukupno.column("Ugljenihidrati", width=80, anchor='center')
    tree_rucak_ukupno.column("Masti", width=40, anchor='center')

    # Pozicioniranje Treeview widgeta za ukupne vrednosti
    tree_rucak_ukupno.grid(row=2, column=1, padx=10, pady=10)