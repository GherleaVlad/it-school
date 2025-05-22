import tkinter
import utilities

'''
Modulul fereastra_sectii este destinat adaugarii/editarii sectiilor existente in program.
Atentie! Modificarea sau stergerea unei sectii este posibila doar daca nu a fost folosita, adica daca nu este atribuita unui utilizator din baza de date.
'''

class FereastraSectii(tkinter.Toplevel):
    def __init__(self, master): # Initializare constructor pentru clasa Fereastra Sectii (reprezinta tkinter.TopLevel - clasa copil pentru tkinter.Tk)
        super().__init__(master) # Initializare constructor pentru clasa parinte (adica pentru clasa MeniuPrincipal - care reprezinta tkinter.Tk (clasa principala - radacina))
        self.title('Sectii') # Numele ferestrei
        self.resizable(False, False) # Dimensiunea nu este modificabila
        self.update_idletasks() # Asteapta initializarea completa a aplicatiei si abia apoi o deschide
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,800,600)) # Setam geometria si centrarea pe ecran folosind functia pozitionare_fereastra_pe_ecran cu parametrii fiind dimensiunea dorita a ferestrei


