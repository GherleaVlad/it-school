
import tkinter

login_window = tkinter.Tk() # Initierea ferestrei
login_window.title('Fereastra LogIn') # Numele ferestrei
login_window.geometry('250x250') # Dimensiunea ferestrei de LogIn
login_window.resizable(False, False) # Fereastra de LogIn nu este modificabila din punct de vedere a marimii


date_conectare = {'USER': 'admin', 'PAROLA': 'test'} # Pentru teste ( inainte de interactiunea cu baza de date )


def actionare_logare(): # Functia folosita pentru logarea in aplicatie
    utilizator = entry_utilizator.get()
    parola = entry_paorla.get()

    if utilizator == date_conectare.get('USER') and parola == date_conectare.get('PAROLA'):
        label_autentificare.config(text='Autentificare reusita!')
        login_window.destroy()
    
    else:
        label_autentificare.config(text='Utilizator sau parola incorecta !')


label_autentificare = tkinter.Label(login_window,text='')
label_autentificare.grid(row=5,column=1,columnspan=3)

# Label pentru nume si prenume
label_utilizator = tkinter.Label(login_window, text='Utilizator: ')
label_parola = tkinter.Label(login_window, text='Parola: ')

# Entry pentru nume si prenume
entry_utilizator = tkinter.Entry(login_window)
entry_paorla = tkinter.Entry(login_window)

# Buton LogIN
buton_login = tkinter.Button(login_window,text='Autentificare',height=2,width=10, command=actionare_logare)

# Pozitionare
tkinter.Label(login_window, text='    \n    \n    ').grid(row=0,column=0) # label gol pentru pozitionare

label_utilizator.grid(row=2, column=1, padx=5,pady=5)
entry_utilizator.grid(row=2,column=2, padx=5,pady=5)
label_parola.grid(row=3, column=1, padx=5,pady=5)
entry_paorla.grid(row=3,column=2, padx=5,pady=5)
buton_login.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

# Daca scriptul este rulat din fisierul main se executa (folosit pentru teste)
if __name__ == '__main__':
    login_window.mainloop()


