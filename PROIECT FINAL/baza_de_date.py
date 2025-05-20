
'''
Modulul baza_de_date reprezinta fisierul .py in care sunt stocate toate operatiunile legate de baza de date si anume operatiunea de conectare,
respectiv operatiunile CRUD (create, read, update, delete).

'''

import sqlite3

# Conectarea la baza de date
def conectare_baza_date():
    conn = sqlite3.connect('medicare.db')
    return conn

# Crearea tabelelor din baza de date

def creare_tabela_operatori():
    '''
    Functia folosita pentru crearea tabelei unde vor fi stocati utilizatorii in baza de date.
    IdOperator este cheia primata a tabelei Operatori. utilizator si parola reprezinta datele de acces in aplicatie. Administrator este o coloana
    care o sa accepte valori de tip 0 sau 1 pentru a determina daca un operator care se creaza sau logheaza este admin sau nu (folosim integer pentru ca
    in sqllite nu avem in baza de date valori de tip bit)
    '''
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Operatori(
                       IdOperator INTEGER PRIMARY KEY AUTOINCREMENT,
                       utilizator TEXT,
                       parola TEXT,
                       administrator INTEGER)''')
        conexiune.commit()


def creare_tabela_pacienti():
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pacienti(
                       IdPacient INTEGER PRIMARY KEY AUTOINCREMENT,
                       nume TEXT,
                       prenume TEXT,
                       data_nastere TEXT,
                       varsta INTEGER,
                       CNP INTEGER,
                       sectie TEXT)''')
        conexiune.commit()





# Functii pentru operatiuni CRUD (create, read, update, delete) pentru tabelele pacienti si operatori

# Functia folosita pentru autentificarea in aplicatie
def cautare_operator(utilizator, parola): 
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('SELECT * FROM Operatori WHERE utilizator = ? AND parola = ?',(utilizator,parola))
        return cursor.fetchone()


