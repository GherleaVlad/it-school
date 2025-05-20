import tkinter
import baza_de_date
import utilities
from fereastra_autentificare import FereastraAutentificare
from fereastra_pacienti import FereastraPacient
from fereastra_rapoarte import FereastraRapoarte
from fereastra_operatori import FereastraOperatori
from fereastra_sectii import FereastraSectii

class MeniuPrincipal(tkinter.Tk):
    def __init__(self): # Initializare constructor pentru clasa MeniuPrincipal
        super().__init__()
        self.title("Meniu Principal")
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,800,600))
        self.resizable(False, False)
        self.withdraw()
        self.autentificare = FereastraAutentificare(self)

    def deschide_meniu_principal_admin(self):
        self.deiconify()  # Afiseaza fereastra principala (cu meniul) dupa ce utilizatorul se autentifica cu succes
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,800,600))

        # Frame-ul care contine sigla si numele aplicatiei + pozitionare    
        frame_sigla = tkinter.Frame(self)
        frame_sigla.grid(row=0,column=0,padx=1,pady=(0,20))
        tkinter.Label(frame_sigla, text='+', font=("Arial", 120, "bold"), fg='red').pack(pady=2)
        tkinter.Label(frame_sigla, text='MEDICARE APP', font=("Arial", 15, "bold"), fg='red').pack(pady=2)

        frame_pacienti = tkinter.LabelFrame(self,text='Pacienti',font=("Arial", 10, "bold"))
        frame_pacienti.grid(row=1,column=0,padx=(20,0),pady=5)
        tkinter.Button(frame_pacienti,text='OPERATIUNI PACIENTI', command=lambda: FereastraPacient(self),width=25,height=3).pack(padx=20,pady=12)
        tkinter.Button(frame_pacienti,text='VIZUALIZARE INTERNARI',width=25,height=3).pack(padx=20,pady=12)
        tkinter.Button(frame_pacienti,text='RAPOARTE', command=lambda: FereastraRapoarte(self),width=25,height=3).pack(padx=20,pady=12)

        tkinter.Label(self).grid(row=1,column=1,padx=125,pady=5)

        frame_administrare = tkinter.LabelFrame(self,text='Administrare',font=("Arial", 10, "bold"))
        frame_administrare.grid(row=1,column=2,padx=(0,10),pady=5)
        tkinter.Button(frame_administrare,text='OPERATORI', command=lambda: FereastraOperatori(self),width=30,height=3).pack(padx=20,pady=12)
        tkinter.Button(frame_administrare,text='NOMENCLATOR MEDICI',width=30,height=3).pack(padx=20,pady=12)
        tkinter.Button(frame_administrare,text='SECTII', command= lambda: FereastraSectii(self),width=30,height=3).pack(padx=20,pady=12)

    def deschide_meniu_principal_operator(self):
        self.deiconify()  # Afiseaza fereastra principala (cu meniul) dupa ce utilizatorul se autentifica cu succes
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,800,600))

        # Frame-ul care contine sigla si numele aplicatiei + pozitionare    
        tkinter.Label(self).grid(row=0,column=0,padx=(130,130),pady=5)
        
        frame_sigla = tkinter.Frame(self)
        frame_sigla.grid(row=0,column=1,padx=(10,10),pady=(0,20))
        tkinter.Label(frame_sigla, text='+', font=("Arial", 120, "bold"), fg='red').pack(pady=2)
        tkinter.Label(frame_sigla, text='MEDICARE APP', font=("Arial", 15, "bold"), fg='red').pack(pady=2)

        frame_pacienti = tkinter.LabelFrame(self,text='Pacienti',font=("Arial", 10, "bold"))
        frame_pacienti.grid(row=1,column=1,padx=(10,10),pady=5)
        tkinter.Button(frame_pacienti,text='OPERATIUNI PACIENTI', command=lambda: FereastraPacient(self),width=25,height=3).pack(padx=20,pady=12)
        tkinter.Button(frame_pacienti,text='VIZUALIZARE INTERNARI',width=25,height=3).pack(padx=20,pady=12)
        tkinter.Button(frame_pacienti,text='RAPOARTE', command=lambda: FereastraRapoarte(self),width=25,height=3).pack(padx=20,pady=12)
