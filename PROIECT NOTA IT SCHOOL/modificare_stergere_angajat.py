'''
Functiile din cadrul acestui modul sunt folosite in vederea modificarii, respectiv a stergerii unui angajat cautat in functie de CNP
Functii isi iau ca si parametru lista_angajati (registru nostru cu angajatii dintr-o companie).
In cazul functiei de modificare exista mai multe optiuni de modificare si anume: modificare nume, modificare prenume, modificare salariu, modificare departament si modificare senioritate.
CNP-ul nu este modificabil, deoarece este un tip de data unic, pentru anumite operatiuni ale aplicatiei este si un criteriu de cautare. In cazul in care desi se trece de validarea
datelor la introducere si utilizatorul introduce un CNP eronat,  atunci singura optiune este cautarea dupa nume prenume si stergerea ulterior dupa CNP eronat al acelui angajat

'''


def functie_modificare_angajat(lista_angajati):
    date_modificare = dict()
    cnp_cautat = input('Introduceti codul numeric personal al angajatului dorit: ')
    gasit = False

    for angajat in lista_angajati:
        if angajat['CNP'] == cnp_cautat:
            date_modificare = angajat
            gasit = True
            break
    
    if not gasit:
        print(f'Nu a fost gasit nici un angajat cu CNP : {cnp_cautat} !')

    else:
        print('Datele angajatului cautat sunt urmatoarele : ')
        print('---------------------------------------------')
        for cheie, valoare in date_modificare.items():
            print(f'{cheie} : {valoare}')
        print('---------------------------------------------')
        modificare_date_angajat = input('Doriti modificarea datelor angajatului gasit? (Da/Nu) : ').lower() == 'da'

        if modificare_date_angajat:
            optiune_modificare = int(input('''
    Va rugam alegeti din optiunile de modificare de mai jos introducand cifra aferenta operatiunii dorite:
        1. Modificare nume
        2. Modificare prenume
        3. Modificare salariu
        4. Modificare departament 
        5. Modificare senioritate
    
        OPTIUNEA ALEASA : '''))

            if optiune_modificare == 1:

                nume_nou = input('Introduceti noul nume al angajatului : ').title()
                index_dictionar = lista_angajati.index(date_modificare)
                date_modificare.update({'Nume angajat':nume_nou})
                lista_angajati[index_dictionar] = date_modificare
                print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                print('---------------------------------------------')
                for cheie, valoare in date_modificare.items():
                    print(f'{cheie} : {valoare}')
                print('---------------------------------------------')

            elif optiune_modificare == 2:

                prenume_nou = input('Introduceti noul prenume al angajatului : ').title()
                index_dictionar = lista_angajati.index(date_modificare)
                date_modificare.update({'Prenume angajat':prenume_nou})
                lista_angajati[index_dictionar] = date_modificare
                print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                print('---------------------------------------------')
                for cheie, valoare in date_modificare.items():
                    print(f'{cheie} : {valoare}')
                print('---------------------------------------------')

            elif optiune_modificare == 3:
                while True:
                    salariu_nou = float(input('Introduceti noul salariu al angajatului : '))
                    if salariu_nou < 4050:
                        print('Salariul introdus nu poate fi mai mic de 4050 lei!')
                    else:
                        break

                index_dictionar = lista_angajati.index(date_modificare)
                date_modificare.update({'Salariu angajat':salariu_nou})
                lista_angajati[index_dictionar] = date_modificare
                print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                print('---------------------------------------------')
                for cheie, valoare in date_modificare.items():
                    print(f'{cheie} : {valoare}')
                print('---------------------------------------------')

            elif optiune_modificare == 4:

                departament_nou = input('Introduceti noul departament in cadrul caruia activeaza angajatul : ')
                index_dictionar = lista_angajati.index(date_modificare)
                date_modificare.update({'Departament':departament_nou})
                lista_angajati[index_dictionar] = date_modificare
                print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                print('---------------------------------------------')
                for cheie, valoare in date_modificare.items():
                    print(f'{cheie} : {valoare}')
                print('---------------------------------------------')
                
            elif optiune_modificare == 5:
                
                senioritate_noua = input('Introduceti noul grad de senioritate al angajatului : ')
                index_dictionar = lista_angajati.index(date_modificare)
                date_modificare.update({'Senioritate':senioritate_noua})
                lista_angajati[index_dictionar] = date_modificare
                print('Modificarile au fost efectuate cu succes! Noile date ale angajatului sunt urmatoarele: ')
                print('---------------------------------------------')
                for cheie, valoare in date_modificare.items():
                    print(f'{cheie} : {valoare}')
                print('---------------------------------------------')         
            else:
                print('Nu ati ales o optiune valida')
                


        else:
            print('Operatiune anulata! Datele angajatului cautat nu au fost modificate! ')
        


def functie_stergere_angajat(lista_angajati):
    angajat_de_sters = dict()
    cnp_cautat = input('Introduceti codul numeric personal al angajatului dorit: ')
    gasit = False

    for angajat in lista_angajati:
        if angajat['CNP'] == cnp_cautat:
            angajat_de_sters = angajat
            gasit = True
            break
    
    if not gasit:
        print(f'Nu a fost gasit nici un angajat cu CNP : {cnp_cautat} !')

    else:
        print('Datele angajatului cautat sunt urmatoarele : ')
        print('---------------------------------------------')
        for cheie, valoare in angajat_de_sters.items():
            print(f'{cheie} : {valoare}')
        print('---------------------------------------------')

        stergere_date_angajat = input('Doriti stergere datelor angajatului gasit? (Da/Nu) : ').lower() == 'da'
        
        if stergere_date_angajat:

            lista_angajati.remove(angajat_de_sters)

            print('Operatiune efectuata cu succes! ')
        else:

            print('Operatiune anulata! Datele angajatului cautat nu au fost sterse')

