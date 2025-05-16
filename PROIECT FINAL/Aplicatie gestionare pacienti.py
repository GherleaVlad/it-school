
import tkinter

date_conectare = {'USER':'admin','PAROLA':'test'}

def pozitionare_fereastra_pe_ecran(fereastra,latime_fereastra,inaltime_fereastra):
    latime = latime_fereastra
    inaltime = inaltime_fereastra

    latime_ecran = fereastra.winfo_screenwidth()
    inaltime_ecran = fereastra.winfo_screenheight()

    pozitie_x = (latime_ecran - latime) // 2
    pozitie_y = (inaltime_ecran - inaltime) // 2

    return (f"{latime}x{inaltime}+{pozitie_x}+{pozitie_y}")


class FereastraAutentificare(tkinter.Toplevel):
    def __init__(self, master): # Initializare constructor pentru clasa Fereastra Autentificare (reprezinta tkinter.TopLevel - clasa copil pentru tkinter.Tk)
        super().__init__(master) # Initializare constructor pentru clasa parinte (adica pentru clasa MeniuPrincipal - care reprezinta tkinter.Tk (clasa principala - radacina))
        self.title('Autentificare') # Numele ferestrei
        self.resizable(False, False) # Dimensiunea nu este modificabila
        self.geometry(pozitionare_fereastra_pe_ecran(self,350,180)) # Setam geometria si centrarea pe ecran folosind functia pozitionare_fereastra_pe_ecran cu parametrii fiind dimensiunea dorita a ferestrei

        # Label si Entry pentru autentificare utilizator + pozitionare
        tkinter.Label(self, text="Utilizator:").pack(pady=(10, 0))
        self.entry_utilizator = tkinter.Entry(self)
        self.entry_utilizator.pack()

        # Label si Entry pentru autentificare parola + pozitionare
        tkinter.Label(self, text="Parola:").pack(pady=(10, 0))
        self.entry_parola = tkinter.Entry(self, show='*')
        self.entry_parola.pack()

        # Label gol pentru afisare mesaj de eroare autentificare
        self.eroare_autentificare = tkinter.Label(self,text='')
        self.eroare_autentificare.pack(pady=(10, 0))

        # Buton pentru autentificare cu comanda de verificare date de autentificare
        tkinter.Button(self, text="Autentificare", command=self.verifica_login).pack(pady=10)


    def verifica_login(self):
        '''
        Functia verifica_login din cadrul clasei FereastraAutentificare are rolul de a verifica daca utilizatorul si parola sunt conform cu cele introduse in sistem
        '''

        utilizator = self.entry_utilizator.get()
        parola = self.entry_parola.get()


        if utilizator == 'admin' and parola == 'test':
            self.destroy()  # Inchide fereastra de login
            self.master.deschide_meniu_principal()  # Apeleaza metoda din aplicatia principala
        else:
            self.eroare_autentificare.config(text= 'Utilizator sau parola gresita!') # Mesajul de eroare afisat in cazul in care utilizatorul si parola nu se potrivesc

class MeniuPrincipal(tkinter.Tk):
    def __init__(self): # Initializare constructor pentru clasa MeniuPrincipal
        super().__init__()
        self.withdraw()
        self.autentificare = FereastraAutentificare(self)

    def deschide_meniu_principal(self):
        self.deiconify()  # Afiseaza fereastra principala (cu meniul) dupa ce utilizatorul se autentifica cu succes
        self.title("Meniu Principal")
        self.geometry(pozitionare_fereastra_pe_ecran(self,400,400))
        self.resizable(False, False)

        tkinter.Label(self, text="Bun venit in meniul principal!").pack(pady=20)
        tkinter.Button(self, text="Iesire", command=self.destroy).pack()


if __name__ == '__main__':
    app = MeniuPrincipal()
    app.mainloop()
