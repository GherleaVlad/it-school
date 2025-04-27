
import class_Angajat as ca
import functionalitati_baza_de_date as bd
from collections import Counter

'''
ACEST MODUL STOCHEAZA FUNCTIONALITATILE OPERATIUNILOR CARE POT FI EFECTUATE ASUPRA SI CU DATELE EXISTENTE IN BAZA DE DATE: 
OPERATIUNI DE MODIFICARE, STERGERE, MANIPULARE A DATELOR

CONTINE URMATOARELE FUNCTII:
- modificare_date_angajat -> ACEASTA METODA PERMITE MODIFICAREA ANUMITOR DATE LEGATE DE UN ANGAJAT
- cautare_angajat -> ACEASTA METODA ESTE FOLOSITA PENTRU CAUTARE UNUI ANGAJAT IN BAZA DE DATE SI RETURNAREA ACESTUIA PENTRU AFISARE
- stergere_angajat -> ACEASTA METODA PERMITE STERGEREA UNUI ANGAJAT DIN BAZA DE DATE
- fluturas_salariu -> ACEASTA METODA CALCULEAZA SI RETURNEAZA FLUTURASUL DE SALARIU AL UNUI ANGAJAT
- afisare_angajati_dupa_senioritate() -> ACEASTA METODA AFISEAZA DUPA GRADUL DE SENIORITATE TOTI ANGAJATI DIN COMAPANIE
- afisare_angajati_dupa_departament() -> ACEASTA METODA AFISEAZA DUPA DEPARTAMENT TOTI ANGAJATII DIN COMPANIE
- calcul_salarii_totale() -> ACEASTA METODA AFISEAZA SUMA TUTUROR SALARIILOR DIN COMPANIE
- cost_salarii_departament() -> ACEASTA METODA CALCULEAZA SI AFISEAZA IN FUNCTIE DE DEPARTAMENT SUMA SALARIILOR

'''


class Companie:
    
    def modificare_date_angajat():

        cnp_cautat = input('Introduceti CNP pentru angajatul dorit: ')

        if bd.BazaDeDate.verificare_existenta_angajat_dupa_cnp(cnp_cautat):
            
            baza_date = bd.BazaDeDate.get_angajati()
            angajat_de_modificat_dictionar = dict()

            for angajat_element in baza_date:
                if cnp_cautat == angajat_element.get('CNP'):
                    angajat_de_modificat_dictionar = angajat_element

            print('Datele angajatului cautat sunt urmatoarele : ')
            print('-'*50)
            for cheie, valoare in angajat_de_modificat_dictionar.items():
                print(f'{cheie} : {valoare}')
            print('-'*50)

            modificare_dorita_de_utilizator = input('Doriti modificarea datelor angajatului gasit? (Da/Nu) : ').lower() == 'da'

            if modificare_dorita_de_utilizator:
                optiune_modificare = int(input('''
Va rugam alegeti din optiunile de modificare de mai jos introducand cifra aferenta operatiunii dorite:
    1. Modificare nume
    2. Modificare prenume
    3. Modificare salariu
    4. Modificare departament 
    5. Modificare senioritate

    OPTIUNEA ALEASA : '''))
                
                match optiune_modificare:
                    case 1: 
                        nume_nou = input('Introduceti noul nume al angajatului : ').title()
                        index_dictionar = baza_date.index(angajat_de_modificat_dictionar)
                        angajat_de_modificat_dictionar.update({'NUME':nume_nou})
                        baza_date[index_dictionar] = angajat_de_modificat_dictionar
                        bd.BazaDeDate.set_angajati(baza_date)
                        print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                        print('---------------------------------------------')
                        for cheie, valoare in angajat_de_modificat_dictionar.items():
                            print(f'{cheie} : {valoare}')
                        print('---------------------------------------------')
                    case 2: 
                        prenume_nou = input('Introduceti noul prenume al angajatului : ').title()
                        index_dictionar = baza_date.index(angajat_de_modificat_dictionar)
                        angajat_de_modificat_dictionar.update({'PRENUME':prenume_nou})
                        baza_date[index_dictionar] = angajat_de_modificat_dictionar
                        bd.BazaDeDate.set_angajati(baza_date)
                        print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                        print('---------------------------------------------')
                        for cheie, valoare in angajat_de_modificat_dictionar.items():
                            print(f'{cheie} : {valoare}')
                        print('---------------------------------------------')
                    case 3: 
                        salariu_nou = input('Introduceti noul salariu al angajatului : ').title()
                        index_dictionar = baza_date.index(angajat_de_modificat_dictionar)
                        angajat_de_modificat_dictionar.update({'SALAR':salariu_nou})
                        baza_date[index_dictionar] = angajat_de_modificat_dictionar
                        bd.BazaDeDate.set_angajati(baza_date)
                        print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                        print('---------------------------------------------')
                        for cheie, valoare in angajat_de_modificat_dictionar.items():
                            print(f'{cheie} : {valoare}')
                        print('---------------------------------------------')
                    case 4: 
                        departament_nou = input('Introduceti noul salariu al angajatului : ').title()
                        index_dictionar = baza_date.index(angajat_de_modificat_dictionar)
                        angajat_de_modificat_dictionar.update({'DEPARTAMENT':departament_nou})
                        baza_date[index_dictionar] = angajat_de_modificat_dictionar
                        bd.BazaDeDate.set_angajati(baza_date)
                        print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                        print('---------------------------------------------')
                        for cheie, valoare in angajat_de_modificat_dictionar.items():
                            print(f'{cheie} : {valoare}')
                        print('---------------------------------------------')
                    case 5: 
                        senioritate_noua = input('Introduceti noul salariu al angajatului : ').title()
                        index_dictionar = baza_date.index(angajat_de_modificat_dictionar)
                        angajat_de_modificat_dictionar.update({'SENIORITATE':senioritate_noua})
                        baza_date[index_dictionar] = angajat_de_modificat_dictionar
                        bd.BazaDeDate.set_angajati(baza_date)
                        print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                        print('---------------------------------------------')
                        for cheie, valoare in angajat_de_modificat_dictionar.items():
                            print(f'{cheie} : {valoare}')
                        print('---------------------------------------------')

                        
            else:
                print('Operatiune anulata! Datele angajatului cautat nu au fost modificate! ')
        
        
        else:
            print(f'Nu a fost gasit nici un angajat cu CNP : {cnp_cautat}')        

    def cautare_angajat():

        cnp_cautat = input('Introduceti CNP pentru angajatul dorit: ')

        if bd.BazaDeDate.verificare_existenta_angajat_dupa_cnp(cnp_cautat):
            
            baza_date = bd.BazaDeDate.get_angajati()
            angajat_cautat = dict()

            for angajat_element in baza_date:
                if cnp_cautat == angajat_element.get('CNP'):
                    angajat_cautat = angajat_element

            print('Datele angajatului cautat sunt urmatoarele : ')
            print('-'*50)
            for cheie, valoare in angajat_cautat.items():
                print(f'{cheie} : {valoare}')
            print('-'*50)
        
        else:
            print(f'INFO: Nu a fost gasit nici un angajat in baza de date cu CNP : {cnp_cautat}')

    def stergere_angajat():
        cnp_cautat = input('Introduceti CNP pentru angajatul dorit: ')
        
        if bd.BazaDeDate.verificare_existenta_angajat_dupa_cnp(cnp_cautat):

            baza_date = bd.BazaDeDate.get_angajati()
            angajat_de_sters_dictionar = dict()

            for angajat_element in baza_date:
                if cnp_cautat == angajat_element.get('CNP'):
                    angajat_de_sters_dictionar = angajat_element

            print('Datele angajatului cautat sunt urmatoarele : ')
            print('-'*50)
            for cheie, valoare in angajat_de_sters_dictionar.items():
                print(f'{cheie} : {valoare}')
            print('-'*50)

            stergere_date_angajat = input('Doriti stergere datelor angajatului gasit? (Da/Nu) : ').lower() == 'da'
            
            if stergere_date_angajat:

                baza_date.remove(angajat_de_sters_dictionar)
                bd.BazaDeDate.set_angajati(baza_date)
                print('INFO: Operatiune efectuata cu succes! ')
            else:

                print('INFO: Operatiune anulata! Datele angajatului cautat nu au fost sterse. ')
        
        else:
            print(f'INFO: Nu a fost gasit nici un angajat cu CNP : {cnp_cautat}!')

    def fluturas_salariu():
        cnp_cautat = input('Introduceti CNP pentru angajatul dorit: ')
        
        if bd.BazaDeDate.verificare_existenta_angajat_dupa_cnp(cnp_cautat):

            baza_date = bd.BazaDeDate.get_angajati()
            fluturas_angajat = dict()

            for angajat_element in baza_date:
                if cnp_cautat == angajat_element.get('CNP'):
                    fluturas_angajat = angajat_element

            salariul_brut = fluturas_angajat.get('SALAR')
            cas = salariul_brut * 0.10
            cass = salariul_brut * 0.25
            baza_impozit = salariul_brut - (cas + cass)
            impozit = baza_impozit * 0.10
            salariul_net = salariul_brut - (cas+cass+impozit)
            nume_angajat = fluturas_angajat.get('NUME')
            prenume_angajat = fluturas_angajat.get('PRENUME')
            fluturas = (f'''
        FLUTURASUL DE SALARIU PENTRU ANGAJATUL:
        NUME: {nume_angajat}
        PRENUME : {prenume_angajat}
        CNP : {cnp_cautat}
        -----------------------------------------------------------------------
        SALARIU BRUT : {salariul_brut} 
        CAS: {cas} (10%)
        CASS: {cass} (25%)
        IMPOZIT: {impozit} (10% DIN BAZA IMPOZABILA : {baza_impozit})
        SALARIU NET: {salariul_net}
        -----------------------------------------------------------------------''')

            return fluturas


        else:
            return(f'INFO: Nu a fost gasit nici un angajat cu CNP : {cnp_cautat}!')

    def afisare_angajati_dupa_senioritate():
        baza_date = bd.BazaDeDate.get_angajati()
        baza_date_sortata = sorted(baza_date, key=lambda dictionar: dictionar['SENIORITATE'], reverse=False)

        for angajat in baza_date_sortata:
            print(50*'-')
            for cheie,valoare in angajat.items():
                print(f'{cheie} : {valoare}')
            print(50*'-')

    def afisare_angajati_dupa_departament():
        baza_date = bd.BazaDeDate.get_angajati()
        baza_date_sortata = sorted(baza_date, key=lambda dictionar: dictionar['DEPARTAMENT'], reverse=False)

        for angajat in baza_date_sortata:
            print(50*'-')
            for cheie,valoare in angajat.items():
                print(f'{cheie} : {valoare}')
            print(50*'-')

    def calcul_salarii_totale():
        
        baza_date = bd.BazaDeDate.get_angajati()
        salarii_totale_in_companie = 0

        for angajat_element in baza_date:
            salarii_totale_in_companie += angajat_element.get('SALAR',0)
                        
        print(f'Valoarea totala a salariilor din compania dumneavoastra este : {salarii_totale_in_companie}')

    def cost_salarii_departament():

        baza_date = bd.BazaDeDate.get_angajati()
        salarii_totale_per_departament = Counter()

        for angajat in baza_date:
            salarii_totale_per_departament[angajat["DEPARTAMENT"]] += angajat["SALAR"]

        for departament,salariu in dict(salarii_totale_per_departament).items():
            print(f'{departament} : {salariu}')

def main():

    print(Companie.fluturas_salariu())

if __name__ == "__main__":
    main()
