from tkinter import *
from tkinter import ttk

def veceraFrame(root):
    # Vecera Frame
    vecera_frame = LabelFrame(root, text="Vecera")
    vecera_frame.grid(row=7, column=3, rowspan=3, padx=50)

    # Dodavanje i pozicioniranje dugmeta za dodavanje i uklanje obroka za veceru
    vecera_dugme = Button(vecera_frame, text="Dodaj obrok")
    vecera_dugme.grid(row=0, column=0, pady=10)
    ukloni_vecera_dugme = Button(vecera_frame, text="Ukloni obrok")
    ukloni_vecera_dugme.grid(row=1, column=0, pady=10)

    # Kreiranje Treeview widgeta za prikaz podataka za veceru
    tree_vecera = ttk.Treeview(vecera_frame, columns=("Id", "Namirnica", "Kalorije",
                                                      "Proteini", "Ugljenihidrati", "Masti"),
                                                      show="headings", height=5)
    # Definisanje kolona i headinga
    tree_vecera.heading("Id", text="Index")
    tree_vecera.heading("Namirnica", text="Namirnica")
    tree_vecera.heading("Kalorije", text="Kalorije")
    tree_vecera.heading("Proteini", text="Proteini")
    tree_vecera.heading("Ugljenihidrati", text="Ugljenihidrati")
    tree_vecera.heading("Masti", text="Masti")

    # Podesavanje sirine kolone
    tree_vecera.column("Id", width=40, anchor='center')
    tree_vecera.column("Namirnica", width=70, anchor='center')
    tree_vecera.column("Kalorije", width=50, anchor='center')
    tree_vecera.column("Proteini", width=50, anchor='center')
    tree_vecera.column("Ugljenihidrati", width=80, anchor='center')
    tree_vecera.column("Masti", width=40, anchor='center')

    # Pozicioniranje Treeview widgeta
    tree_vecera.grid(row=0, column=1, padx=10, pady=10, rowspan=2)

    # Kreiranje Treeview widgeta za prikaz ukupnih vrednosti za veceru
    tree_vecera_ukupno = ttk.Treeview(vecera_frame, columns=("Id", "Namirnica", "Kalorije",
                                                             "Proteini", "Ugljenihidrati", "Masti"),
                                                             show="headings", height=1)
    # Definisanje kolona i headinga
    tree_vecera_ukupno.heading("Id", text="#")
    tree_vecera_ukupno.heading("Namirnica", text="#")
    tree_vecera_ukupno.heading("Kalorije", text="Kalorije")
    tree_vecera_ukupno.heading("Proteini", text="Proteini")
    tree_vecera_ukupno.heading("Ugljenihidrati", text="Ugljenihidrati")
    tree_vecera_ukupno.heading("Masti", text="Masti")

    # Podesavanje sirine kolone
    tree_vecera_ukupno.column("Id", width=40, anchor='center')
    tree_vecera_ukupno.column("Namirnica", width=70, anchor='center')
    tree_vecera_ukupno.column("Kalorije", width=50, anchor='center')
    tree_vecera_ukupno.column("Proteini", width=50, anchor='center')
    tree_vecera_ukupno.column("Ugljenihidrati", width=80, anchor='center')
    tree_vecera_ukupno.column("Masti", width=40, anchor='center')

    # Pozicioniranje Treeview widgeta za ukupne vrednosti
    tree_vecera_ukupno.grid(row=2, column=1, padx=10, pady=10)