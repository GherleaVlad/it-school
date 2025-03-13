
print('Bine ati venit! ')

lista_catalog = list()

# Pentru teste
lista_catalog = [{'Nume':'Gherlea','Prenume':'Vlad','Nota romana':10,'Nota matematica':9,'Nota engleza':10,'Media':9.5}]

# functie pentru introducerea datelor unui elev
def functie_introducere_elev(nume, prenume, nota_romana,nota_matematica,nota_engleza):
    nume = input('Numele elevului : ')
    prenume = input('Prenumele elevului : ')
    nota_romana = float(input('Nota pentru materia "Limba si literarura romana" : '))
    nota_matematica = float(input('Nota pentru materia "Matematica" : '))
    nota_engleza = float(input('Nota pentru materia "Engleza" : '))
    media = round(((nota_romana + nota_matematica + nota_engleza)/3),2)

    dict_catalog = {
        'Nume':nume,
        'Prenume':prenume,
        'Nota romana':nota_romana,
        'Nota matematica':nota_matematica,
        'Nota engleza':nota_engleza,
        'Media':media
    }

    return dict_catalog

# functie incompleta 
def functie_cautare_elev(nume,prenume):
    nume = input('Va rugam introduceti numele elevului dorit : ')
    prenume = input('Va rugam introduceti prenumele elevului dorit : ')

    for element in lista_catalog:
        if element['Nume'] == nume and element['Prenume'] == prenume:
            return print(element)
        
        else:
            return print(f'Nu a fost gasit nici un elev cu numele: {nume} si prenumele : {prenume}. Verificati datele! ')
#


while True:
    print('MENIU PRINCIPAL')
    print('Va rugam alegeti o optiune din meniul de mai jos si introduceti numarul aferent operatiunii dorite din meniu: ')
    print(
    '''
    1. Adaugare elev #done
    2. Afisarea elevi existenti #done
    3. Modificare informatii elev existent 
    4. Stergere elev
    5. Cautare elev dupa nume si prenume
    6. Afisare elevi in ordinea mediei
    7. Afisare elevi cu media peste 8
    8. Afisare elevi in ordine alfabetica (in functie de Nume)
    9. Iesire din program #done 
    ''')

    optiunea_aleasa_de_utilizator = int(input('Optiunea aleasa : ')) # utilizatorul trebuie sa introduca numarul aferent operatiunii dorite

    if optiunea_aleasa_de_utilizator == 1:
        x = True
        while x == True:
        
            print('Ati ales operatiunea "1. Adaugare elev"\nIntroduceti datele necesare:')

            date_elev = functie_introducere_elev('default','default',0,0,0)
        
            print(f'Datele introduse sunt urmatoarele: {date_elev} ! ') 
            commit_modificari = input('Doriti adaugarea lor in catalog? (Da/Nu) : ').lower() == 'da'

            if commit_modificari:
                lista_catalog.append(date_elev)
                print('Datele elevului au fost adaugate cu succes! ')
                
                continuare_introducere_elev = input('Doriti sa mai adaugati un alt elev? (Da/Nu) : ').lower() == 'da'

                if continuare_introducere_elev:
                    x = True
                else:
                    x = False
            else:
                print('Datele nu au fost introduse.')
                continuare_introducere_elev = input('Doriti sa mai adaugati un alt elev? (Da/Nu) : ').lower() == 'da'
                if continuare_introducere_elev:
                    x = True
                else:
                    x = False
            

    elif optiunea_aleasa_de_utilizator == 2:
        print('Ati ales operatiunea "2. Afisarea elevi existenti " ')
        print('Elevi existenti in catalog : ')
        while True:
            for element in lista_catalog:
                print(element)
            
            inchidere_previzualiare = input('Introduceti "x" in cazul in care doriti inchiderea previzualizarii catalogului : ').lower() == 'x'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 3:
        
        print('x')
    
    elif optiunea_aleasa_de_utilizator == 9:
        print('La nevedere!')
        break

            




