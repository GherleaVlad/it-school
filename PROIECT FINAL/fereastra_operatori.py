import tkinter
import utilities
from tkinter import ttk

'''
Modulul fereastra_operatori este folosit pentru creare, editarea sau stergerea operatorilor existenti in aplicatie.

'''


class FereastraOperatori(tkinter.Toplevel):
    def __init__(self, master): # Initializare constructor pentru clasa Fereastra Operatori (reprezinta tkinter.TopLevel - clasa copil pentru tkinter.Tk)
        super().__init__(master) # Initializare constructor pentru clasa parinte (adica pentru clasa MeniuPrincipal - care reprezinta tkinter.Tk (clasa principala - radacina))
        self.title('Operatori') # Numele ferestrei
        self.resizable(False, False) # Dimensiunea nu este modificabila
        self.update_idletasks() # Asteapta initializarea completa a aplicatiei si abia apoi o deschide
        self.geometry(utilities.pozitionare_fereastra_pe_ecran(self,800,500)) # Setam geometria si centrarea pe ecran folosind functia pozitionare_fereastra_pe_ecran cu parametrii fiind dimensiunea dorita a ferestrei

        frame_tabel = tkinter.Frame(self)
        frame_tabel.grid(column=1,row=0,padx=(20,20),pady=(20,20))
        
        frame_date = tkinter.Frame(self)
        frame_date.grid(column=0,row=0,padx=(20,20),pady=(20,5))

        coloane = ('IdOperator', 'Utilizator', 'Parola','Nume', 'Prenume', 'Sectie')
        tabel_pacient = ttk.Treeview(frame_tabel, columns=coloane, show='headings')

        for coloana in coloane:
            tabel_pacient.heading(coloana,text=coloana)
            tabel_pacient.column(coloana,width=75)

        tabel_pacient.pack()
        
        # Butoane si Entry-uri pentru introducere operator
        # Entry si label pentru utilizator
        tkinter.Label(frame_date,text='UTILIZATOR: ').pack(padx=5,pady=5)
        entry_utilizator = tkinter.Entry(frame_date)
        entry_utilizator.pack(padx=5,pady=5)

        # Entry si label pentru nume utilizator
        tkinter.Label(frame_date,text='NUME: ').pack(padx=5,pady=5)
        entry_nume = tkinter.Entry(frame_date)
        entry_nume.pack(padx=5,pady=5)
        
        # Entry si label pentru prenume utilizator
        tkinter.Label(frame_date,text='PRENUME: ').pack(padx=5,pady=5)
        entry_prenume = tkinter.Entry(frame_date)
        entry_prenume.pack(padx=5,pady=5)
        
        # Entry si label pentru prenume utilizator
        tkinter.Label(frame_date,text='SECTIE: ').pack(padx=5,pady=5)
        entry_prenume = ttk.Combobox(frame_date,values=['Sectie1','Sectie2'], state='readonly')
        entry_prenume.pack(padx=5,pady=5)






