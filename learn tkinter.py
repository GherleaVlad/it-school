import tkinter as tk

'''

PRIMA PARTE IN CARE AM INVATAT PLASAREA CU PACK SI GRID A BUTOANELOR A LABELURILOR A ENTRY-URILOR. UN LABEL ESTE UN TEXT, CEVA SIMPLU AFISAT IN APLICATIE, UN BUTON ESTE PENTRU APASARE SI ACTIONAREA UNEI COMENZI SAU INSTRUCTIUNI.
UN ENTRY ESTE SIMILAR CU INPUT - PENTRU INTODUCEREA TEXTULUI DE CATRE USER
EXISTA FUNCTIONALITATI MULTE CU PRIVIRE LA ATRIBUTE PE CARE POT SA LE AIBA LABELURILE, BUTOANELE SI ENTRY-URILE (FONT, CULOARE DE BACKGROUND, DIMENSIUNE (LATIME/LUNGIME (2D) SI INALTIME ), UMBRE, ETC. (GASESC PE NET CE SE POATE FACE CU FIECARE))
AM FACUT SI O FUNCTIE IN CARE SE EXECUTA O COMANDA SI O AFISEAZA PE ECRAN

# Creaza rama
root = tk.Tk()
root.geometry("600x600")
root.title('Aplicatia mea')


# Functia de salut (fg - font )
def conectare():
    label_salut = tk.Label(root, text=f'Salut {intrare_nume.get()} , {intrare_prenume.get()} !!!', fg='blue',bg='white', width= 30)
    label_salut.grid(row=6,column=2)

# LABEL NUME

label_antet_gol = tk.Label(root, text = '           ')
label_antet_gol.grid(row=0)

label_nume = tk.Label(root, text = 'NUME: ')
# label_nume.pack() -> metoda simpla de plasare folosind pack (puse vertical in aplicatie)
label_nume.grid(row=1,column=1)

# ENTRY NUME

intrare_nume = tk.Entry(root, width=25)
# intrare_nume.pack() -> metoda simpla de plasare folosind pack (puse vertical in aplicatie)
# intrare_nume.insert(0, 'Introduceti numele : ') -> metoda folosita ca sa iti insereze un text default in campul de entry
intrare_nume.grid(row=1,column=2)

# LABEL PRENUME 

label_prenume = tk.Label(root,text='PRENUME: ')
# label_prenume.pack() -> metoda simpla de plasare folosind pack (puse vertical in aplicatie)
label_prenume.grid(row=2,column=1)


# ENTRY PRENUME

intrare_prenume = tk.Entry(root, width=25) 

# intrare_prenume.pack() -> metoda simpla de plasare folosind pack (puse vertical in aplicatie)
# intrare_prenume.insert(0, 'Introduceti prenumele : ') -> metoda folosita ca sa iti insereze un text default in campul de entry

intrare_prenume.grid(row=2,column=2)

# BUTONUL

primul_buton = tk.Button(root,text='CONECTARE', command=conectare, fg='white', bg='black') # ,width=5 -> se poate folosi width si height pentru latime/lungime si inaltime
# primul_buton.pack() -> metoda simpla de plasare folosind pack (puse vertical in aplicatie)
primul_buton.grid(row=3,column=2)

# LABEL DE REZULTAT (AFISEAZA FUNCTIA SALUT + ENTRY.NUME + ENTRY.PRENUME)

label_rezultat = tk.Label(root,text='REZULTAT: ')
# primul_label.pack() -> metoda simpla de plasare folosind pack (puse vertical in aplicatie)

label_rezultat.grid(row=4,column=2)


#Aplicatia care ruleaza in bucla
root.mainloop()

'''

# Pentru buna practica pot sa le pun grupate (butoane, entry-uri, label - definirea lor si separat pozitionare) -> pentru a fi mai usor de vizualizat unde vin pozitionate in aplicatie


# Creaza rama
root = tk.Tk()
root.geometry("600x600")
root.title('Aplicatia mea')


class ComenziButoane:
    @staticmethod
    def apasa_buton1():
        label3 = tk.Label(root, text='Al treilea label! Apelat de functie si prin comanda', fg= 'black', bg='white', relief='ridge') # la culorile de font sau fundal se pot pune coduri de culoare
        label3.grid(row=2,column=0) 

    @staticmethod
    def apasa_buton2():
        label4 = tk.Label(root, text='Al patrulea label! Apelat de functie si prin comanda', fg= 'black', bg='white', relief='ridge')
        label4.grid(row=3,column=0)

# Definire labeluri
label1 = tk.Label(root, text='Primul label', fg= 'black', bg='white', relief='sunken')
label2 = tk.Label(root,text='Al doilea label',fg= 'black', bg='white', relief='flat')

# Definire butoane

buton1 = tk.Button(root, text='Primul buton',fg= 'black', bg='white',command=ComenziButoane.apasa_buton1)
buton2 = tk.Button(root, text='Al doilea buton',fg= 'black', bg='white',command=ComenziButoane.apasa_buton2)


# Afisaj label si butoane si entry-uri

label1.grid(row=0,column=0) 
label2.grid(row=1,column=0)
buton1.grid(row=0,column=1)
buton2.grid(row=1,column=1)


root.mainloop()



