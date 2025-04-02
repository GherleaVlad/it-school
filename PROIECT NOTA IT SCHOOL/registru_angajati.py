
import introducere_angajat # modulul care contine functia definita de mine pentru introducerea angajatilor in registrul de angajati (lista_angajati)
import cautare_angajat # modulul care contine functia pentru cautarea angajatilor
import modificare_stergere_angajat # modulul care contine functia de modificare si de stergere a unui angajat
import fluturas_salariu #modulul care contine functia de generare al fluturasului de salariu
from collections import Counter # modulul collection (modul predefinit in python), din cadrul modulului collections am folosit Counter pentru calculare salariilor in functie de departament 

lista_angajati = list()

def functie_sortare_dupa_senioritate(dictionar):
    return dictionar['Senioritate']

def functie_sortare_dupa_departament(dictionar):
    return dictionar['Departament']

# # pentru teste
# lista_angajati = [
#     {'Nume angajat':'Popescu', 'Prenume angajat':'Ion', 'CNP': '1990421055059', 'Varsta angajat': 41, 'Salariu angajat' : 10000, 'Departament':'Aprovizionare', 'Senioritate':'Junior'},
#     {'Nume angajat': 'Popescu', 'Prenume angajat': 'Ion', 'CNP': '1990421055059', 'Varsta angajat': 41, 'Salariu angajat': 10000, 'Departament': 'Aprovizionare', 'Senioritate': 'Junior'},
#     {'Nume angajat': 'Ionescu', 'Prenume angajat': 'Maria', 'CNP': '2920301045678', 'Varsta angajat': 35, 'Salariu angajat': 8000, 'Departament': 'Vanzari', 'Senioritate': 'Senior'},
#     {'Nume angajat': 'Georgescu', 'Prenume angajat': 'Alexandru', 'CNP': '1940503067894', 'Varsta angajat': 29, 'Salariu angajat': 12000, 'Departament': 'IT', 'Senioritate': 'Mid'},
#     {'Nume angajat': 'Dumitru', 'Prenume angajat': 'Elena', 'CNP': '1980122098765', 'Varsta angajat': 45, 'Salariu angajat': 9500, 'Departament': 'Resurse Umane', 'Senioritate': 'Senior'},
#     {'Nume angajat': 'Constantin', 'Prenume angajat': 'Andrei', 'CNP': '1870414085123', 'Varsta angajat': 33, 'Salariu angajat': 11000, 'Departament': 'Aprovizionare', 'Senioritate': 'Mid'}
#     ]

# Pentru conectarea in aplicatie va fi utilizat user-ul admin si parola test
date_conectare = {
    'User' : 'ADMIN',
    'Parola' : 'TEST'
}

while True:
    print('Pentru conectarea in aplicatie va rugam introduceti utilizatorul si parola! Pentru iesirea din aplicatie introduceti "EXIT" in campul user! ')
    user = input('Utilizator: ').upper()
    
    if user == 'EXIT':
        break
    parola = input('Parola: ').upper()

    if user != date_conectare['User'] or parola != date_conectare['Parola']:
        print('Utilizator sau parola invalida! Incercati din nou! ')
    else:

        while True:

            print('''
                MENIUL PRINCIPAL:
                
                Alegeti una dintre optiunile de mai jos introducand numarul operatiunii dorite:
                1.  Adaugare angajat -- done
                2.  Cautare angajat -- done
                3.  Modificare date angajat -- done
                4.  Stergere angajat -- done
                5.  Afisare angajati -- done 
                6.  Calculator cost total salarii -- done 
                7.  Calculator cost total salarii departament -- done 
                8.  Calculator fluturas salar angajat
                9.  Afisarea angajatilor (dupa senioritate)
                10. Afisarea angajatilor (dupa departament)
                11. Iesire
            ''')

            try:
                optiune_aleasa = int(input('Optiunea aleasa: '))

                if optiune_aleasa == 1:
                    print('Ati ales optiunea "1. Adaugare angajat!" Introduceti datele necesare! ')
                    continuare_introducere_date = True
                    while continuare_introducere_date != False:

                            date_intermediare = introducere_angajat.functie_introducere_angajat()
                            
                            gasit = False

                            for angajat in lista_angajati:
                                if angajat['CNP'] == date_intermediare['CNP']:
                                    print('Angajatul se afla deja in evidenta!')
                                    gasit = True
                                    break 

                            if gasit:
                                continuare_introducere_date = input('Doriti adaugarea unui alt angajat? (Da/Nu) : ').lower() == 'da'
                                continue 
                            
                            else:
                                print('Datele introduse sunt: ')
                                print('------------------------------------------')
                                for cheie,valoare in date_intermediare.items():
                                        print(f'{cheie} : {valoare}')
                                print('------------------------------------------')
                                commit_date = input('Doriti adaugarea datelor in lista de angajati? (Da/Nu) : ').lower() == 'da'

                                if commit_date:
                                    lista_angajati.append(date_intermediare)
                                    print('Datele au fost adaugate cu succes! ')

                                    continuare_introducere = input('Doriti adaugarea unui alt angajat? (Da/Nu) : ').lower() == 'da'

                                    if continuare_introducere:
                                        continuare_introducere_date = True
                                    else:
                                        continuare_introducere_date = False

                                else:
                                    print('Operatiune anulata! Datele nu au fost adaugate! ')

                                    continuare_introducere = input('Doriti adaugarea unui alt angajat? (Da/Nu) : ').lower() == 'da'

                                    if continuare_introducere:
                                        continuare_introducere_date = True
                                    else:
                                        continuare_introducere_date = False

                elif optiune_aleasa == 2: 
                    inchidere_previzualizare = False
                    while inchidere_previzualizare != True:

                        date_cautate=cautare_angajat.functie_cautare_angajati(lista_angajati)

                        if type(date_cautate) == dict:
                            print('------------------------------------------')
                            for angajat,date in date_cautate.items():
                                print(f'{angajat} : {date}')
                            print('------------------------------------------')
                        else:
                            print(date_cautate)
                        
                        cautare_alt_angajat = input('Doriti cautarea unui alt angajat? (Da/Nu) : ').lower() == 'da'

                        if cautare_alt_angajat:
                            inchidere_previzualizare = False
                        else:
                            inchidere_previzualizare = True

                elif optiune_aleasa == 3:

                    print('Ati ales optiunea "3. Modificare date angajat". Introduceti datele necesare! ')

                    inchidere_previzualizare = False
                    while inchidere_previzualizare == False:
                        
                        modificare_stergere_angajat.functie_modificare_angajat(lista_angajati)

                        continuare_alta_modificare = input('Doriti efectuarea unei alte modificari? (Da - efectuare alta modificare/ Nu - iesire in meniul princial) : ').lower() == 'da'

                        if continuare_alta_modificare:
                            inchidere_previzualizare = False
                        else:
                            inchidere_previzualizare = True
                   
                elif optiune_aleasa == 4:
                    print('Ati ales optiunea "4. Stergere angajat". Introduceti datele necesare! ')

                    inchidere_previzualizare = False
                    while inchidere_previzualizare == False: 
                        modificare_stergere_angajat.functie_stergere_angajat(lista_angajati)

                        continuare_stergere = input('Doriti efectuarea unei alte modificari? (Da - efectuare alta modificare/ Nu - iesire in meniul princial) : ').lower() == 'da'

                        if continuare_stergere:
                            inchidere_previzualizare = False
                        else:
                            inchidere_previzualizare = True

                elif optiune_aleasa == 5:
                    print('Ati ales optiunea "5. Afisare angajat". Registrul angajatilor este: ')
                    inchidere_previzualizare = False
                    while inchidere_previzualizare == False:
                        for angajat in lista_angajati:
                            print('--------------------------------------------------')
                            for cheie,valoare in angajat.items():
                                print(f'{cheie} : {valoare}')
                            print('--------------------------------------------------')
                        
                        iesire_afisare = input('Doriti inchiderea previzualizarii registrului de angajati si iesirea in meniul principal? (Da - iesire in meniul principal /Nu - continuare previzualizare registru) : ').lower() == 'da'

                        if iesire_afisare:
                            inchidere_previzualizare = True
                        else:
                            inchidere_previzualizare = False

                elif optiune_aleasa == 6:

                    print('Ati ales optiunea "6. Calculator cost total salarii" ')
                    inchidere_previzualizare = False
                    while inchidere_previzualizare == False:
                        
                        salarii_totale_in_companie = 0

                        for angajat in lista_angajati:
                            salarii_totale_in_companie += angajat.get('Salariu angajat',0)
                        
                        print(f'Valoarea totala a salariilor din compania dumneavoastra este : {salarii_totale_in_companie}')

                        close_previzualizare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ').lower() == 'da'

                        if close_previzualizare:
                            inchidere_previzualizare = True
                        else:
                            inchidere_previzualizare = False

                elif optiune_aleasa == 7:

                    print('Ati ales optiunea "7. Calculator cost total salarii departament" ')
                    inchidere_previzualizare = False
                    while inchidere_previzualizare == False:
                        
                        salarii_totale_per_departament = Counter()

                        for angajat in lista_angajati:
                            salarii_totale_per_departament[angajat["Departament"]] += angajat["Salariu angajat"]

                        for departament,salariu in dict(salarii_totale_per_departament).items():
                            print(f'{departament} : {salariu}')

                        close_previzualizare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ').lower() == 'da'
                        
                        if close_previzualizare:
                            inchidere_previzualizare = True
                        else:
                            inchidere_previzualizare = False
                    '''
                    In cadrul optiunii 7 unde se calculeaza salariile dintr-o companie in functie de departament am folosit counter()

                    Counter() - este o subclasa a dictionarelor si practic vine cu o anumita functionalitate de a aduna toate valoriile in functie de o cheie

                    Ce face mai sus mai exact acesta counter(): initializez o variabila salarii_totale_per_departament care contine aceasta subclasa a dictionarelor
                    Pe urma ma folosesc de aceasta variabila intr-un for pentru a lua fiecare dictionar din lista_angajati si pentru a cauta ulterior in fiecare angajat (dictionar)
                    dupa cheia Departament (ca sa vad ce departamente am).Prin functionalitatea counter(),face ca apoi fiecare valoare din cheia salariu angajat sa fie adunata 
                    cu o alta daca au acelasi departament.

                    counter pot sa il imaginez ca si cum ar fi un caiet gol, in care imi pun toate departamentele si dupa ma duc sa vad fiecare angajat 
                    ce salariu are si in ce departament lucreaza.
                    '''

                elif optiune_aleasa == 8:
                    while True:
                        print(fluturas_salariu.functie_fluturas_salariu(lista_angajati))

                        inchidere_previzualiare = input('Doriti inchiderea previzualizarii si revenirea in meniul principal? (Da/Nu - generare pentru alt angajat) : ').lower() == 'da'
                        if inchidere_previzualiare:
                            break    

                elif optiune_aleasa == 9:
                    while True:
                        print('Ati ales optiunea "9. Afisarea angajatilor (dupa senioritate)"')
                        print('Registrul sortat in functie de senioritatea angajatilor este urmatorul: ')

                        lista_sortata = sorted(lista_angajati, key=functie_sortare_dupa_senioritate, reverse=True)
                    
                        for angajat in lista_sortata:
                            print('--------------------------------------------------')
                            for cheie,valoare in angajat.items():
                                print(f'{cheie} : {valoare}')
                            print('--------------------------------------------------')

                        inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
                        if inchidere_previzualiare:
                            break

                elif optiune_aleasa == 10: 
                    while True:
                        print('Ati ales optiunea "10. Afisarea angajatilor (dupa departament)"')
                        print('Registrul sortat in functie de departament este urmatorul: ')

                        lista_sortata = sorted(lista_angajati, key=functie_sortare_dupa_departament, reverse=False)
                    
                        for angajat in lista_sortata:
                            print('--------------------------------------------------')
                            for cheie,valoare in angajat.items():
                                print(f'{cheie} : {valoare}')
                            print('--------------------------------------------------')

                        inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
                        if inchidere_previzualiare:
                            break

                elif optiune_aleasa == 11:
                    break
                else:
                    print('Nu ati ales o optiune valida! Reincercati! ')
            except ValueError:
                print('EROARE: Valoarea introdusa nu este valida. Introduceti o cifra din meniu aferenta operatiunii dorite!')