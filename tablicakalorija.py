from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

def run_tablicakalorija():
    tablicakalorija = Tk()
    tablicakalorija.geometry("1000x600")
    tablicakalorija.title("Tablica kalorija")

    # Povezivanje sa bazom i prikaz vrednosti
    def prikazVrednosti():
        conn = sqlite3.connect("tablicakalorija.db")
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM tablicakalorija
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        # Create a Treeview widget to display data
        tree = ttk.Treeview(tablicakalorija, columns=("Id", "Namirnica",
                                                    "Proteini", "Ugljenihidrati", "Masti"),
                                                    show="headings")

        # Define the columns and headings
        tree.heading("Id", text="Index")
        tree.heading("Namirnica", text="Namirnica")
        tree.heading("Proteini", text="Proteini")
        tree.heading("Ugljenihidrati", text="Ugljenihidrati")
        tree.heading("Masti", text="Masti")

        # Changind column width
        tree.column("Id", width=40, anchor='center')
        tree.column("Namirnica", width=70, anchor='center')
        tree.column("Proteini", width=50, anchor='center')
        tree.column("Ugljenihidrati", width=80, anchor='center')
        tree.column("Masti", width=40, anchor='center')

        # Insert data into the Treeview
        for row in data:
            tree.insert("", "end", values=row)
        
        tree.grid(row=6, column=0, columnspan=2)

    # Dodavanje podataka u bazu
    def adding_values_in_database():
        conn = sqlite3.connect("tablicakalorija.db")
        cursor = conn.cursor()
        query = '''INSERT INTO tablicakalorija (namirnica, proteini, ugljenihidrati, masti)
                    VALUES (?, ?, ?, ?)'''
        cursor.execute(query,
                    (namirnica_entry.get(),
                    float(proteini_entry.get()),
                    float(ugljenihidrati_entry.get()),
                    float(masti_entry.get())))
        conn.commit()
        cursor.close()
        conn.close()    
        messagebox.showinfo("Information", "Namirnica uspesno dodata!")
        namirnica_entry.delete(0, 'end')
        proteini_entry.delete(0, 'end')
        ugljenihidrati_entry.delete(0, 'end')
        masti_entry.delete(0, 'end')
        prikazVrednosti()

    # Izmena vrednosti u bazi
    def change_values_in_database():
        tablicakalorija = Tk()
        tablicakalorija.geometry("1000x600")
        tablicakalorija.title("Izmena vrednosti")

        conn = sqlite3.connect("tablicakalorija.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM tablicakalorija''')
        data = cursor.fetchall()
        # Create a Treeview widget to display data
        tree = ttk.Treeview(tablicakalorija, columns=("Id", "Namirnica",
                                                    "Proteini", "Ugljenihidrati", "Masti"),
                                                    show="headings")

        # Define the columns and headings
        tree.heading("Id", text="Index")
        tree.heading("Namirnica", text="Namirnica")
        tree.heading("Proteini", text="Proteini")
        tree.heading("Ugljenihidrati", text="Ugljenihidrati")
        tree.heading("Masti", text="Masti")

        # Changind column width
        tree.column("Id", width=40, anchor='center')
        tree.column("Namirnica", width=70, anchor='center')
        tree.column("Proteini", width=50, anchor='center')
        tree.column("Ugljenihidrati", width=80, anchor='center')
        tree.column("Masti", width=40, anchor='center')

        # Insert data into the Treeview
        for row in data:
            tree.insert("", "end", values=row)

        tree.grid(row=5, column=0, columnspan=2)

        # Labele za namirnicu i makronutrijente
        namirnica_label = Label(tablicakalorija, text="Namirnica:")
        proteini_label = Label(tablicakalorija, text="Proteini (g):")
        ugljenihidrati_label = Label(tablicakalorija, text="Ugljeni hidrati (g):")
        masti_label = Label(tablicakalorija, text="Masti (g):")

        # Entry polja za namirnicu i makronutrijente
        namirnica_entry = Entry(tablicakalorija)
        proteini_entry = Entry(tablicakalorija)
        ugljenihidrati_entry = Entry(tablicakalorija)
        masti_entry = Entry(tablicakalorija)


        # Pozicioniranje labela za namirnicu i makronutrijente
        namirnica_label.grid(row=0, column=0, padx=5, sticky='w')
        proteini_label.grid(row=1, column=0, padx=5, sticky='w')
        ugljenihidrati_label.grid(row=2, column=0, padx=5, sticky='w')
        masti_label.grid(row=3, column=0, padx= 5, sticky='w')

        # Pozicioniranje entry polja namirnicu i makronutrijente
        namirnica_entry.grid(row=0, column=1, padx=5)
        proteini_entry.grid(row=1, column=1, padx=5)
        ugljenihidrati_entry.grid(row=2, column=1, padx=5)
        masti_entry.grid(row=3, column=1, padx=5)

        ok_button = Button(tablicakalorija, text="OK")
        ok_button.grid(row=4, column=0, padx=5, pady=10, sticky='w')
        odustani_button = Button(tablicakalorija, text="Odustani")
        odustani_button.grid(row=4, column=0, sticky='e')

        def on_row_selected(event):
            selected_item = tree.focus()
            item_values = tree.item(selected_item, 'values')
            namirnica_entry.delete(0, 'end')
            namirnica_entry.insert(0, item_values[1])
            proteini_entry.delete(0, 'end')
            proteini_entry.insert(0, item_values[2])
            ugljenihidrati_entry.delete(0, 'end')
            ugljenihidrati_entry.insert(0, item_values[3])
            masti_entry.delete(0, 'end')
            masti_entry.insert(0, item_values[4])

        tree.bind('<ButtonRelease-1>', on_row_selected)

        cursor.close()
        conn.close()

    # Labele za namirnicu i makronutrijente
    namirnica_label = Label(tablicakalorija, text="Namirnica:")
    kalorije_label = Label(tablicakalorija, text="Kalorije (kcal):")
    proteini_label = Label(tablicakalorija, text="Proteini (g):")
    ugljenihidrati_label = Label(tablicakalorija, text="Ugljeni hidrati (g):")
    masti_label = Label(tablicakalorija, text="Masti (g):")

    # Entry polja za namirnicu i makronutrijente
    namirnica_entry = Entry(tablicakalorija)
    kalorije_entry = Entry(tablicakalorija)
    proteini_entry = Entry(tablicakalorija)
    ugljenihidrati_entry = Entry(tablicakalorija)
    masti_entry = Entry(tablicakalorija)


    # Pozicioniranje labela za namirnicu i makronutrijente
    namirnica_label.grid(row=0, column=0, padx=5, sticky='w')
    kalorije_label.grid(row=1, column=0, padx=5, sticky='w')
    proteini_label.grid(row=2, column=0, padx=5, sticky='w')
    ugljenihidrati_label.grid(row=3, column=0, padx=5, sticky='w')
    masti_label.grid(row=4, column=0, padx= 5, sticky='w')

    # Pozicioniranje entry polja namirnicu i makronutrijente
    namirnica_entry.grid(row=0, column=1, padx=5)
    kalorije_entry.grid(row=1, column=1, padx=5)
    proteini_entry.grid(row=2, column=1, padx=5)
    ugljenihidrati_entry.grid(row=3, column=1, padx=5)
    masti_entry.grid(row=4, column=1, padx=5)



    # Buttons
    dodajVrednosti_button = Button(tablicakalorija, text="Dodaj", command=adding_values_in_database)
    dodajVrednosti_button.grid(row=5, column=0, pady=10, sticky='w', padx=5)
    izmeniVrednost_button = Button(tablicakalorija, text="Izmeni", command=change_values_in_database)
    izmeniVrednost_button.grid(row=5, column=0, sticky='e')








    prikazVrednosti()
    tablicakalorija.mainloop()