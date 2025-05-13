
import tkinter

date_conectare = {'USER':'admin','PAROLA':'test'}

class FereastraLogIn:

    def __init__(self):
        self.login_window = tkinter.Tk() # Initierea ferestrei
        self.login_window.title('Fereastra LogIn') # Numele ferestrei

        # Dimensiunea ferestrei de login
        self.latime_fereastra_login = 250
        self.inaltime_fereastra_login = 250

        # Obtinem dimensiunile ecranului folosind metodele tkinter winfo_screenwidth si winfo_screenheight 
        self.latime_ecran = self.login_window.winfo_screenwidth()
        self.inaltime_ecran = self.login_window.winfo_screenheight()

        # Calculam pozitia x si y (in pixeli) pe ecran (cam pe unde ar veni fereastra - pentru a fi centrata)
        self.x_pozitie_ecran = (self.latime_ecran - self.latime_fereastra_login) // 2
        self.y_pozitie_ecran = (self.inaltime_ecran - self.inaltime_fereastra_login) // 2

        '''
        Setam geometry cu dimensiune + poziție, unde:

        latime_fereastra x intaltime_fereastra
        +x_pozitie_ecran si + y_pozitie_ecran seteaza pozitia pe ecran a aplicatiei cu geometria acesteia (+ nu se refera la adunare ci in cadrul
        geometry din tkinter se refera la pozitionare)

        '''
        self.login_window.geometry(f"{self.latime_fereastra_login}x{self.inaltime_fereastra_login}+{self.x_pozitie_ecran}+{self.y_pozitie_ecran}")
        self.login_window.resizable(False, False) # Fereastra de LogIn nu este modificabila din punct de vedere a marimii

        self.label_autentificare = tkinter.Label(self.login_window,text='')
        self.label_autentificare.grid(row=5,column=1,columnspan=3)

        # Label pentru nume si prenume
        self.label_utilizator = tkinter.Label(self.login_window, text='Utilizator: ')
        self.label_parola = tkinter.Label(self.login_window, text='Parola: ')

        # Entry pentru nume si prenume
        self.entry_utilizator = tkinter.Entry(self.login_window)
        self.entry_parola = tkinter.Entry(self.login_window,show='*')

        # Buton LogIN
        self.buton_login = tkinter.Button(self.login_window,text='Autentificare',height=2,width=10,command=self.actionare_logare)

        # Pozitionare
        tkinter.Label(self.login_window, text='    \n    \n    ').grid(row=0,column=0) # label gol pentru pozitionare
        self.label_utilizator.grid(row=2, column=1, padx=5,pady=5)
        self.entry_utilizator.grid(row=2,column=2, padx=5,pady=5)
        self.label_parola.grid(row=3, column=1, padx=5,pady=5)
        self.entry_parola.grid(row=3,column=2, padx=5,pady=5)
        self.buton_login.grid(row=4,column=1,columnspan=3,padx=5,pady=5)


        self.login_window.mainloop()
        

    def actionare_logare(self): # Functia folosita pentru logarea in aplicatie
        utilizator = self.entry_utilizator.get()
        parola = self.entry_parola.get()

        if utilizator == date_conectare.get('USER') and parola == date_conectare.get('PAROLA'):
            self.label_autentificare.config(text='Autentificare reusita!')
            self.login_window.destroy()
        
        else:
            self.label_autentificare.config(text='Utilizator sau parola incorecta !')

        
# Daca scriptul este rulat din fisierul main se executa (folosit pentru teste)
if __name__ == '__main__':
    
    ferastra_log_in = FereastraLogIn()


