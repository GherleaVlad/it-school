import tkinter
import utilities
from tkinter import ttk

class FereastraPacient(tkinter.Toplevel):
    def __init__(self, master): # Initializare constructor pentru clasa Fereastra Pacient (reprezinta tkinter.TopLevel - clasa copil pentru tkinter.Tk)
        super().__init__(master) # Initializare constructor pentru clasa parinte (adica pentru clasa MeniuPrincipal - care reprezinta tkinter.Tk (clasa principala - radacina))
        self.title('Pacient') # Numele ferestrei
        self.resizable(False, False) # Dimensiunea nu este modificabila
        self.update_idletasks() # Asteapta initializarea completa a aplicatiei si abia apoi o deschide
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,800,600)) # Setam geometria si centrarea pe ecran folosind functia pozitionare_fereastra_pe_ecran cu parametrii fiind dimensiunea dorita a ferestrei

        # MODIFICARE STIL TAB-URI
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[5, 5], font=('TkDefaultFont', 10))

        # NOTEBOOK PENTRU A PUTEA PUNE TABURI IN FEREASTRA
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both',padx=5,pady=5)

        # ADAUGAREA FRAMEURILOR DEFINITE IN CLASE IN TABUL AFERENT FIECAREI OPERATIUNI
        self.frame_date_pacient = DatePacient(self.notebook)
        self.frame_internare = Internare(self.notebook)

        # POZITIONARE EFECTIVA IN APLICATIE PENTRU TAB-URI
        self.notebook.add(self.frame_date_pacient, text='Date Pacient')
        self.notebook.add(self.frame_internare, text='Internare')

class DatePacient(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # FRAME-UL CARE CONTINE DATELE PERSONALE ALE PACIENTULUI
        self.frame_date_personale = tkinter.Frame(self)
        self.frame_date_personale.grid(column=0, row=0, padx=(10,20), pady=(10,10))

        # LABEL + ENTRY PENTRU NUMELE PACIENTULUI
        tkinter.Label(self.frame_date_personale,text='NUME: ').grid(column=0,row=0,padx=5,pady=5)
        self.entry_nume = tkinter.Entry(self.frame_date_personale)
        self.entry_nume.grid(column=1,row=0,padx=5,pady=5)

        # LABEL + ENTRY PENTRU PRENUMELE PACIENTULUI
        tkinter.Label(self.frame_date_personale,text='PRENUME: ').grid(column=0,row=1,padx=5,pady=5)
        self.entry_prenume = tkinter.Entry(self.frame_date_personale)
        self.entry_prenume.grid(column=1,row=1,padx=5,pady=5)

        # LABEL + ENTRY PENTRU DATA DE NASTERE A PACIENTULUI
        tkinter.Label(self.frame_date_personale,text='DATA NASTERE: ').grid(column=0,row=2,padx=5,pady=5)
        self.entry_varsta = tkinter.Entry(self.frame_date_personale)
        self.entry_varsta.grid(column=1,row=2,padx=5,pady=5)

        # LABEL PENTRU VARSTA PACIENTULUI (CALCULATA AUTOMAT IN FUNCTIE DE VARSTA)
        tkinter.Label(self.frame_date_personale,text='VARSTA: ').grid(column=0,row=3,padx=5,pady=5)
        tkinter.Label(self.frame_date_personale,text='DEFAULT').grid(column=1,row=3,padx=5,pady=5)

        # LABEL + ENTRY PENTRU DATA DE NASTERE A PACIENTULUI
        tkinter.Label(self.frame_date_personale,text='CNP: ').grid(column=0,row=4,padx=5,pady=5)
        self.entry_cnp = tkinter.Entry(self.frame_date_personale)
        self.entry_cnp.grid(column=1,row=4,padx=5,pady=5)

        # LABEL + ENTRY PENTRU DATA DE NASTERE A PACIENTULUI
        tkinter.Label(self.frame_date_personale,text='SEX: ').grid(column=0,row=5,padx=5,pady=5)
        self.entry_sex = tkinter.Entry(self.frame_date_personale)
        self.entry_sex.grid(column=1,row=5,padx=5,pady=5)


        # FRAME-UL CARE CONTINE DATELE DE INTERNARE ALE PACIENTULUI
        self.frame_date_internare = tkinter.Frame(self)
        self.frame_date_internare.grid(column=1,row=0, padx=(20,10), pady=(10,10))

        # LABEL + ENTRY PENTRU SECTIA PE CARE VA FI INTERNAT PACIENTUL
        tkinter.Label(self.frame_date_internare,text='SECTIE: ').grid(column=0,row=0,padx=5,pady=5)
        
        # LABEL + ENTRY PENTRU MEDICUL TRIMITATOR
        tkinter.Label(self.frame_date_internare,text='MEDIC TRIMITATOR: ').grid(column=0,row=1,padx=5,pady=5)

        # LABEL + ENTRY PENTRU BILETUL DE TRIMITERE
        tkinter.Label(self.frame_date_internare,text='BILET TRIMITERE: ').grid(column=0,row=2,padx=5,pady=5)
        self.entry_bilet_trimitere = tkinter.Entry(self.frame_date_internare)
        self.entry_bilet_trimitere.grid(column=1,row=2,padx=5,pady=5)

        # LABEL + ENTRY PENTRU MEDICUL CURANT
        tkinter.Label(self.frame_date_internare,text='MEDICUL CURANT: ').grid(column=0,row=3,padx=5,pady=5)

        # LABEL + ENTRY PENTRU DIAGNOSTIC INITIAL
        tkinter.Label(self.frame_date_internare,text='DIAGNOSTIC: ').grid(column=0,row=4,padx=5,pady=5)
        self.entry_diagnostic = tkinter.Entry(self.frame_date_internare)
        self.entry_diagnostic.grid(column=1,row=4,padx=5,pady=5)

class Internare(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # FRAME-UL CARE CONTINE DATELE PERSONALE ALE PACIENTULUI
        self.frame_date_personale = tkinter.Frame(self)
        self.frame_date_personale.grid(column=0, row=0, padx=(10,20), pady=(10,10))

