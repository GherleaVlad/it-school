
'''
    Functia de mai jos este utilizata in scopul introducerii unui angajat in lista_angajati (care reprezinta registrul angajatilor).
    
    Functia ii cere utilizatorului aplicatiei sa introduca datele legate de un angajat: nume, prenume, cnp, varsta, salariu, departament si gradul de senioritate iar rezultatele
sunt stocate ulterior intr-un dictionar care va fi returnat prin aceasta functie. Dictionarul returnat, pe urma in cadrul codului principal va fi adaugat in lista_angajati.
    
    Exista cateva validari legate de datele introduse: 
    1.  CNP-ul introdus pentru un angajat sa fie format din 13 cifre.
    2.  Varsta angajatului sa fie cuprinsa in intervalul 18-65 de ani, unde 18 reprezinta varsta minima si 65 reprezinta varsta maxima a unui angajat
    3.  Salariul introdus nu poate sa fie mai mic decat salariul minim brut pe economie din Romania.
    
    Totodata gradul de senioritate a unui angajat este introdus de utilizator prin selectia numarului aferent senioritatii dorie dupa cum urmeaza:
    1 - Junior
    2 - Mid
    3 - Senior

'''

def functie_introducere_angajat(): 
    while True:
        try:
            dictionar_angajat_introdus = {}
            
            dictionar_angajat_introdus['Nume angajat'] = input('Introduceti numele angajatului: ').title()
            dictionar_angajat_introdus['Prenume angajat'] = input('Introduceti prenumele angajatului: ').title()
            
            while True:
                cnp = input('Introduceti codul numeric al angajatului: ')
                if len(cnp) == 13 and cnp.isdigit():
                    dictionar_angajat_introdus['CNP'] = cnp
                    break
                else:
                    print('Codul numeric personal al angajatului trebuie sa aiba 13 cifre! Reintroduceti CNP! ')


            while True:
                varsta_angajat = int(input('Introduceti varsta angajatului: '))
                if varsta_angajat< 18 or varsta_angajat > 65:
                    print('Varsta angajatului trebuie sa fie cuprinsa in intervalul 18 - 65 ani! Reintroduceti datele! ')
                else:
                    dictionar_angajat_introdus['Varsta angajat'] = varsta_angajat
                    break

            while True:
                salariu_angajat = float(input('Introduceti salariul brut al angajatului: '))

                if salariu_angajat >= 4050:
                    dictionar_angajat_introdus['Salariu angajat'] = salariu_angajat
                    break
                else:
                    print('Salariul brut nu poate fi mai mic de 4050 lei')
            
            dictionar_angajat_introdus['Departament'] = input('Introduceti departamentul in cadrul caruia lucreaza angajatul: ').title()

            
            while True:
                
                print('''
                Alegeti senioritatea angajatului introducand cifra aferenta acesteia:
                1. Junior
                2. Mid
                3. Senior
                ''')
                senioritate = int(input('Optiune senioritate: '))
                if senioritate == 1:
                    dictionar_angajat_introdus['Senioritate'] = 'Junior'
                    break
                elif senioritate == 2:
                    dictionar_angajat_introdus['Senioritate'] = 'Mid'
                    break
                elif senioritate == 3:
                    dictionar_angajat_introdus['Senioritate'] = 'Senior'
                    break
                else:
                    print('Nu ati ales o optiune valida! Reincercati! ')      
            break
        except ValueError:
            print('Ultimele date introduse nu sunt valide! Reintroduceti datele! ')
    return dictionar_angajat_introdus   
    


