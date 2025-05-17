import tkinter
import baza_de_date
import utilities
from fereastra_autentificare import FereastraAutentificare

class MeniuPrincipal(tkinter.Tk):
    def __init__(self): # Initializare constructor pentru clasa MeniuPrincipal
        super().__init__()
        self.withdraw()
        self.autentificare = FereastraAutentificare(self)

    def deschide_meniu_principal(self):
        self.deiconify()  # Afiseaza fereastra principala (cu meniul) dupa ce utilizatorul se autentifica cu succes
        self.title("Meniu Principal")
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,400,400))
        self.resizable(False, False)

        tkinter.Label(self, text="Bun venit in meniul principal!").pack(pady=20)
        tkinter.Button(self, text="Iesire", command=self.destroy).pack()
