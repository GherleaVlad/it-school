
import class_Angajat as ca
import functionalitati_baza_de_date as bd

class Companie:
    
    def modificare_date_angajat():
        while True:
            while True:
                cnp_cautat = input('Introduceti CNP pentru angajatul dorit: ')
                if len(cnp_cautat) == 13 and cnp_cautat.isdigit():
                    cnp_cautat = cnp_cautat
                    break
                else:
                    print(f'EROARE: CNP introdus: {cnp_cautat} este eronat!')
                    print('INFO: CNP trebuie sa fie format din 13 cifre! Reinncercati!')

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


                else:
                    print('Operatiune anulata! Datele angajatului cautat nu au fost modificate! ')
            
            
            else:
                print(f'Nu a fost gasit nici un angajat cu CNP : {cnp_cautat}')        

def main():
    Companie.modificare_date_angajat()

if __name__ == "__main__":
    main()
