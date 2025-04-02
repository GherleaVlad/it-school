'''
Acest modul contine functia pentru cautarea angajatului.
Functia creata in cadrul acestui modul isi ia ca parametru o lista - lista_angajati

Operatiunile disponibile in cadrul functiei sunt : cautare dupa CNP si cautarea dupa nume si prenume.

Functia poate returna fie un string ca si rezultat in cazul in care datele privind un angajat nu exista in lista_angajati, sau daca nu a fost introdusa o optiune corecta de cautare
din meniu, adica 1 (cautare dupa CNP) sau 2 (cautare dupa nume si prenume)

'''


def functie_cautare_angajati(lista_angajati):
    
    print(
    ''' 
    Ati selectat optiunea "2. Cautare angajat".
    Alegeti una dintre optiunile de mai jos de cautare:
    1. Cautare dupa CNP
    2. Cautare dupa nume si prenume angajat
    ''')
    try:
        optiune_cautare = int(input('Introduceti numarul aferent cautarii dorite (1/2): '))
    except ValueError:
        return 'Eroare: Introduceti o valoare numerica (1 sau 2) pentru a selecta tipul de cautare dorita'
        
    if optiune_cautare == 1:
        print('Ati selectat optiunea 1. Cautare dupa CNP! ')
        cnp_cautat = input('Introduceti codul numeric personal al angajatului dorit: ')
        
        for angajat in lista_angajati:
            if angajat['CNP'] == cnp_cautat:
                return angajat
        
        return 'Nu a fost gasit nici un angajat conform CNP introdus'


    elif optiune_cautare == 2:
        print('Ati selectat optiunea 2. Cautare dupa nume si prenume angajat! ')
        nume_angajat_cautat = input('Introduceti numele angajatului dorit: ').title()
        prenume_angajat_cautat = input('Introduceti prenumele angajatului dorit: ').title()
        for angajat in lista_angajati:
            if angajat['Nume angajat'] == nume_angajat_cautat and angajat['Prenume angajat'] == prenume_angajat_cautat:
                return angajat
                
        return f'Nu a fost gasit nici un angajat cu numele: {nume_angajat_cautat} si prenumele {prenume_angajat_cautat}! Va rugam verificati datele introduse! '


    else:
        return 'Nu ati selectat o optiune de cautare valida, reincercati! '
        

