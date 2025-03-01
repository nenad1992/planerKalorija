from tkinter import *
import tablicakalorija

root = Tk()
root.geometry("800x600")
root.title("Racunanje kalorija")

# Pokretanje tablice kalorija
def tablicakalorija_run():
    tablicakalorija.run_tablicakalorija()

# Racunanje kalorija po Mifflin-St Jeor jednacini
def mifflin_st_equation():
    godine = godine_entry.get()
    pol_muski = selected_option.get()
    pol_zenski = selected_option.get()
    visina = visina_entry.get()
    tezina = tezina_entry.get()

    if pol_muski == 'M':
        # BMR za muski pol
        rezultatBMR = 10 * float(tezina) + 6.25 * float(visina) - 5 * float(godine) + 5
    elif pol_zenski == 'Z':
        # BMR za zenski pol
        rezultatBMR = 10 * float(tezina) + 6.25 * float(visina) - 5 * float(godine) - 161
    
    rezultatBMR_label.config(text=f"{rezultatBMR} kcal")

# Labele za unos podataka
godine_label = Label(root, text="Godine:")
pol_label = Label(root, text="Pol:")
visina_label = Label(root, text="Visina (cm):")
tezina_label = Label(root, text="Tezina (kg):")
rezultatBMR_label = Label(root)

selected_option = StringVar()
selected_option.set(None)

# Entry i Radio polja za unos podataka
godine_entry = Entry(root)
button_muski = Radiobutton(root, text="Muski", variable=selected_option, value='M')
button_zenski = Radiobutton(root, text="Zenski", variable=selected_option, value='Z')
visina_entry = Entry(root)
tezina_entry = Entry(root)

# Buttons
izracunaj_button = Button(root, text="Izracunaj BMR", command=mifflin_st_equation)
tablicakalorija_button = Button(root, text="Tablica kalorija", command=tablicakalorija_run)

godine_label.grid(row=0, column=0, sticky='w')
pol_label.grid(row=1, column=0, sticky='w')
visina_label.grid(row=2, column=0, sticky='w')
tezina_label.grid(row=3, column=0, sticky='w')

godine_entry.grid(row=0, column=1, columnspan=2)
button_muski.grid(row=1, column=1)
button_zenski.grid(row=1, column=2)
visina_entry.grid(row=2, column=1, columnspan=2)
tezina_entry.grid(row=3, column=1, columnspan=2)

izracunaj_button.grid(row=4, column=0, pady=10)
rezultatBMR_label.grid(row=4, column=1, pady=10, columnspan=2)

tablicakalorija_button.grid(row=5, column=0, pady=20)


root.mainloop()