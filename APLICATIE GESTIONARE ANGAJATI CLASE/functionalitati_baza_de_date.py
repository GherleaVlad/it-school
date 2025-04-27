'''
ACEST MODUL ESTE UTILIZAT PENTRU DESCHIDEREA BAZEI DE DATE CU ANGAJATII, DINTR-UN FISIER JSON SI PENTRU SALVAREA ANGAJATILOR IN BAZA DE DATE (TOT INTR-UN)
FISIER DE TIP JSON

ACEST MODUL ARE URMATOARELE METODE/ FUNCTII: 
- get_angajati(fisier_json = ...) -> ACEASTA METODA ARE ROLUL DE A ADUCE DATELE DIN BAZA DE DATE (UN FISIER TIP JSON) IAR PENTRU ASTA ARE NEVOIE DE UN ARGUEMNT SI ANUME 
CALEA CATRE FISIERUL JSON
 - set_angajati(bd_noua,fisier_json) -> ACEASTA METODA ARE ROLUL DE A SETA BAZA DE DATE - ESTE UTILIZATA PENTRU SCRIEREA DATELOR IN BAZA DE DATE - IAR PENTRU FUNCTIONAREA EI ESTE
 NEVOIE DE DOUA ARGUMENTE BAZA DE DATE NOUA SI FISIERUL JSON (CALEA CATRE ACESTA) UNDE SA SCRIE ACESTE DATE
 - verificare_existenta_angajt_adaugare(angajta) -> ACEASTA METODA ARE ROLUL DE A VERIFICA EXISTENTA UNUI ANGAJAT IN BAZA DE DATE FIIND FOLOSITA 
 IN MOMENTUL ADAUGARII UNUI ANGAJAT IN BAZA DE DATE
 - verificare_existenta_angajat_dupa_cnp(cnp) -> ACEASTA METODA ESTE FOLOSITA PENTRU VERIFICARE EXISTENTEI UNUI ANGAJAT IN BAZA DE DATE SI ESTE FOLOSITA
 IN CADRUL MAJORITATII METODELOR DIN CADRUL CLASEI COMPANIE (IN MOMENTUL CAUTARII UNUI ANGAJAT DUPA CNP IN VEDEREA MODIFICARII DATELOR ACESTUIA SI IN MOMENTUL
 CAUTARII IN ALTE SCOPURI CUM AR FI CALCULAREA FLUTURASULUI DE SALARIU )
 
- get_cale_fisier_json() -> ACEASTA FUNCTIE RETURNEAZA CALEA FISIERULUI JSON PENTRU A FI FOLOSITA IN FUNCTIILE DE GET SI SET BD

'''

import class_Angajat
import json as json
import os as os

class BazaDeDate:
    def get_cale_fisier_json():

        director_curent = os.path.dirname(os.path.abspath(__file__))
        cale_json = os.path.join(director_curent, 'angajati.json')
        
        return cale_json

    def get_angajati(fisier_json = get_cale_fisier_json()):
        with open(fisier_json, 'r') as  json_angajati:
            return list(json.load(json_angajati))
    
    def set_angajati(bd_noua,fisier_json = get_cale_fisier_json()):
        with open(fisier_json, 'w') as json_angajati:
            json.dump(bd_noua,json_angajati,indent=4)
    
    def verificare_existenta_angajat_adaugare(angajat):

        baza_date = BazaDeDate.get_angajati()
        angajat_dictionar = class_Angajat.Angajat.angajat_to_dict(angajat)

        exista = False
        for angajat_element in baza_date:
            if angajat_dictionar.get('CNP') == angajat_element.get('CNP'):
                exista = True

        if exista:
            return True
        else:
            return False
    
    def verificare_existenta_angajat_dupa_cnp(cnp):
        baza_date = BazaDeDate.get_angajati()
        cnp_cautat = cnp

        exista = False
        for angajat_element in baza_date:
            if cnp_cautat == angajat_element.get('CNP'):
                exista = True

        if exista:
            return True
        else:
            return False

def main():

    print(BazaDeDate.get_angajati())
    angajat = class_Angajat.Angajat.citire_date_angajat()        

    if BazaDeDate.verificare_existenta_angajat_adaugare(angajat):
        print('ANGAJATUL EXISTA DEJA IN BAZA DE DATE')

    else:
        baza_date = BazaDeDate.get_angajati()
        angajat_dictionar = class_Angajat.Angajat.angajat_to_dict(angajat)
        baza_date.append(angajat_dictionar)
        BazaDeDate.set_angajati(baza_date)
        print(BazaDeDate.get_angajati())

if __name__ == "__main__":
    main()
