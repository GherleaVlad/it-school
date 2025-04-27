import class_Angajat 
import class_Companie 
import functionalitati_baza_de_date as bd

'''

ACEST MODUL ESTE SCRIPTUL PRINCIPAL FOLOSIT PENTRU FUNCTIONAREA APLICATIEI DE GESTIONARE A ANGAJATILOR SI CENTRALIZEAZA TOATE FUNCTONALITATILE DIN 
CELELALTE MODULE

'''


def main():
    while True:
        try:
            print('''
        MENIUL PRINCIPAL:
                        
                Alegeti una dintre optiunile de mai jos introducand numarul operatiunii dorite:
                1.  Adaugare angajat
                2.  Cautare angajat
                3.  Modificare date angajat
                4.  Stergere angajat
                5.  Afisare angajati
                6.  Calculator cost total salarii
                7.  Calculator cost total salarii departament
                8.  Calculator fluturas salar angajat
                9.  Afisarea angajatilor (dupa senioritate)
                10. Afisarea angajatilor (dupa departament)
                11. Iesire
    ''')
            optiune_aleasa = int(input('Optiunea aleasa: '))

            match optiune_aleasa:
                case 1:
                    while True:
                        angajat = class_Angajat.Angajat.citire_date_angajat()
                        if bd.BazaDeDate.verificare_existenta_angajat_adaugare(angajat):
                            print('ANGAJATUL EXISTA DEJA IN BAZA DE DATE')
                        else: 
                            baza_date = bd.BazaDeDate.get_angajati()
                            angajat_dictionar = class_Angajat.Angajat.angajat_to_dict(angajat)
                            baza_date.append(angajat_dictionar)
                            bd.BazaDeDate.set_angajati(baza_date)
                            print('INFO: Angajatul a fost adaugat cu succes')
                        
                        continuare_adaugare = input('Doriti adaugarea unui alt angajat? (Da/Nu) : ').lower() == 'da'

                        if not continuare_adaugare:
                            break

                case 2:
                    while True:
                        class_Companie.Companie.cautare_angajat()

                        continuare_cautare = input('Doriti cautarea unui alt angajat? (Da/Nu) : ').lower() == 'da'

                        if not continuare_cautare:
                            break

                case 3:
                    while True:
                        class_Companie.Companie.modificare_date_angajat()
                        
                        continuare_modificare = input('Doriti modificarea datelor unui alt angajat? (Da/Nu) : ').lower() == 'da'

                        if not continuare_modificare:
                            break
                
                case 4: 
                    while True:
                        class_Companie.Companie.stergere_angajat()

                        continuare_stergere = input('Doriti stergerea unui alt angajat? (Da/Nu) : ').lower() == 'da'

                        if not continuare_stergere:
                            break

                case 5: 
                    while True:
                        baza_date = bd.BazaDeDate.get_angajati()

                        for angajat in baza_date:
                            print(50*'-')
                            for cheie, valoare in angajat.items():
                                print(f'{cheie} : {valoare}')
                            print(50*'-')

                        previzualizare = input('Pentru inchiderea previzualizarii registrului de angajati introduceti "x" : ').lower() == 'x'

                        if previzualizare:
                            break

                case 6:
                    while True:
                        class_Companie.Companie.calcul_salarii_totale()
                        previzualizare = input('Pentru inchiderea previzualizarii registrului de angajati introduceti "x" : ').lower() == 'x'

                        if previzualizare:
                            break
                
                case 7:
                    while True:
                        class_Companie.Companie.cost_salarii_departament()
                        previzualizare = input('Pentru inchiderea previzualizarii registrului de angajati introduceti "x" : ').lower() == 'x'

                        if previzualizare:
                            break

                case 8 : 
                    while True:
                        
                        print(class_Companie.Companie.fluturas_salariu())
                        
                        previzualizare = input('Pentru inchiderea previzualizarii registrului de angajati introduceti "x" : ').lower() == 'x'

                        if previzualizare:
                            break

                case 9:
                    while True:
                        class_Companie.Companie.afisare_angajati_dupa_senioritate()
                        previzualizare = input('Pentru inchiderea previzualizarii registrului de angajati introduceti "x" : ').lower() == 'x'

                        if previzualizare:
                            break

                case 10: 
                    while True:
                        class_Companie.Companie.afisare_angajati_dupa_departament()
                        previzualizare = input('Pentru inchiderea previzualizarii registrului de angajati introduceti "x" : ').lower() == 'x'

                        if previzualizare:
                            break

                case 11: break

        except ValueError:
                print('EROARE: Valoarea introdusa nu este valida. Introduceti o cifra din meniu aferenta operatiunii dorite!')
if __name__ == "__main__":
    main()