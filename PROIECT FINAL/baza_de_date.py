
'''
Modulul baza_de_date reprezinta fisierul .py in care sunt stocate toate operatiunile legate de baza de date si anume operatiunea de conectare, operatiunile de creare a structurii tabelei
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
                       nume TEXT,
                       prenume TEXT,
                       administrator INTEGER)''')
        conexiune.commit()

def creare_tabela_pacienti():
    '''
    Functia folosita pentru crearea tabelei unde vor fi stocati pacientii in baza de date.
    IdPacient este cheia primara a tabelei Pacienti. Restul coloanelor reprezinta entry-urile introduse de catre utilizator
    '''
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
                       sex TEXT,
                       sectie TEXT,
                       medic_trimitator TEXT,
                       bilte_trimitere TEXT,
                       medic_curant TEXT,
                       diagnostic TEXT)
                       ''')
        conexiune.commit()

def creare_tabela_sectii():
    '''
    Functia folosita pentru crearea tabelei Sectii in care vor fi stocate sectiile clinicii.
    '''
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sectii(
                       IdSectie INTEGER PRIMARY KEY AUTOINCREMENT,
                       denumire TEXT,
                       sef_sectie TEXT)''')
        conexiune.commit()

def creare_tabela_medici_trimitatori():
    '''
    Functia folosita pentru crearea tabelei Medici_Trimitatori in care vor fi stocati medicii trimitatori (nomenclator national de medici).
    '''
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medici_Trimitatori(
                       IdMedicTrimitator INTEGER PRIMARY KEY AUTOINCREMENT,
                       nume TEXT,
                       prenume TEXT,
                       parafa TEXT)''')
        conexiune.commit()

def creare_tabela_medici_curanti():
    '''
    Functia folosita pentru crearea tabelei Medici_Curanti in care vor fi medicii curanti (medicii din cadrul clinicii).
    '''
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medici_Curanti(
                       IdMedicCurant INTEGER PRIMARY KEY AUTOINCREMENT,
                       nume TEXT,
                       prenume TEXT,
                       parafa TEXT)''')
        conexiune.commit()

# Functii pentru operatiuni CRUD (create, read, update, delete) pentru tabelele pacienti si operatori


# Functia folosita pentru adaugarea pacientilor in baza de date
def adaugare_pacient():
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('''INSERT INTO Pacienti (nume, prenume, data_nastere, varsta, CNP, sex, sectie, medic_trimitator, bilet_trimitere, medic_curant, diagnostic)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       ''')
        conexiune.commit()

# Functia folosita pentru autentificarea in aplicatie
def cautare_operator(utilizator, parola): 
    with conectare_baza_date() as conexiune:
        cursor = conexiune.cursor()
        cursor.execute('SELECT * FROM Operatori WHERE utilizator = ? AND parola = ?',(utilizator,parola))
        return cursor.fetchone()


