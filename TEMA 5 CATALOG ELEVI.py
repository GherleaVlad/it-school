
print('Bine ati venit! ')

lista_catalog = list()

# Pentru teste
# lista_catalog = [{'NUME': 'GHERLEA', 'PRENUME': 'VLAD', 'NOTA ROMANA': 10, 'NOTA MATEMATICA': 10, 'NOTA ENGLEZA': 10, 'MEDIA': 10},
#                  {'NUME': 'ION', 'PRENUME': 'POPESCU', 'NOTA ROMANA': 5, 'NOTA MATEMATICA': 5, 'NOTA ENGLEZA': 5, 'MEDIA': 5.0}]

# functie pentru introducerea datelor unui elev
def functie_introducere_elev(nume, prenume, nota_romana,nota_matematica,nota_engleza):
    nume = input('Numele elevului : ').upper()
    prenume = input('Prenumele elevului : ').upper()
    nota_romana = float(input('Nota pentru materia "Limba si literarura romana" : '))
    nota_matematica = float(input('Nota pentru materia "Matematica" : '))
    nota_engleza = float(input('Nota pentru materia "Engleza" : '))
    media = round(((nota_romana + nota_matematica + nota_engleza)/3),2)

    dict_catalog = {
        'NUME':nume,
        'PRENUME':prenume,
        'NOTA ROMANA':nota_romana,
        'NOTA MATEMATICA':nota_matematica,
        'NOTA ENGLEZA':nota_engleza,
        'MEDIA':media
    }

    return dict_catalog

# functie cautare elev
def functie_cautare_elev(nume,prenume):
    nume = input('Va rugam introduceti numele elevului dorit : ').upper()
    prenume = input('Va rugam introduceti prenumele elevului dorit : ').upper()

    rezultatul_cautarii = {}

    for element in lista_catalog:
        if element['NUME'] == nume and element['PRENUME'] == prenume:
            rezultatul_cautarii.update(element)
            break 

    if rezultatul_cautarii:
        return rezultatul_cautarii
    else:
        return False

def functie_sortare_dupa_medie(dictionar):
    return dictionar['MEDIA']

def functie_sortare_dupa_nume(dictionar):
    return dictionar['NUME']



while True:
    print('MENIU PRINCIPAL')
    print('Va rugam alegeti o optiune din meniul de mai jos si introduceti numarul aferent operatiunii dorite din meniu: ')
    print(
    '''
    1. Adaugare elev
    2. Afisarea elevi existenti
    3. Modificare informatii elev existent
    4. Stergere elev
    5. Cautare elev dupa nume si prenume
    6. Afisare elevi in ordinea mediei
    7. Afisare elevi cu media peste 8
    8. Afisare elevi in ordine alfabetica (in functie de Nume)
    9. Iesire din program
    ''')

    optiunea_aleasa_de_utilizator = int(input('Optiunea aleasa : ')) # utilizatorul trebuie sa introduca numarul aferent operatiunii dorite

    if optiunea_aleasa_de_utilizator == 1: # adaugare elev
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
            
    elif optiunea_aleasa_de_utilizator == 2: #Afisare elevi existenti
        print('Ati ales operatiunea "2. Afisarea elevi existenti " ')
        print('Elevi existenti in catalog : ')
        while True:
            for element in lista_catalog:
                print(element)
            
            inchidere_previzualiare = input('Introduceti "x" in cazul in care doriti inchiderea previzualizarii catalogului : ').lower() == 'x'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 3: #Modificare elev cautat in functie de nume si prenume
        while True:
            rezulatul_cautarii = functie_cautare_elev('default','default')

            if rezulatul_cautarii != False:

                print('Datele elevului cautat sunt urmatoarele : ')
                print(rezulatul_cautarii)
                modificare_date_elev = input('Doriti modificarea datelor elevului gasit? (Da/Nu) ').lower() == 'da'
                
                if modificare_date_elev:
                    
                    print('''
                    
                    1. Modificarea nume
                    2. Modificare prenume
                    3. Modificare nota romana
                    4. Modificare nota matematica
                    5. Modificare nota engleza
                    
                    ''')
                    tipul_modificarii = int(input('Selectati tipul modificarii, introducand numarul aferent operatiunii dorite: '))

                    if tipul_modificarii == 1:
                        
                        nume_nou = input('Introduceti noul nume al elevului : ').upper()

                        index_dictionar = lista_catalog.index(rezulatul_cautarii)

                        rezulatul_cautarii.update({'NUME':nume_nou})

                        lista_catalog[index_dictionar] = rezulatul_cautarii
                        print('Modificarile au fost efectuate cu succes! Noile date ale elevului sunt urmatoarele: ')
                        print(rezulatul_cautarii)

                    elif tipul_modificarii == 2:
                        prenume_nou = input('Introduceti noul prenume al elevului : ').upper()

                        index_dictionar = lista_catalog.index(rezulatul_cautarii)

                        rezulatul_cautarii.update({'PRENUME':prenume_nou})

                        lista_catalog[index_dictionar] = rezulatul_cautarii
                        print('Modificarile au fost efectuate cu succes! Noile date ale elevului sunt urmatoarele: ')
                        print(rezulatul_cautarii)

                    elif tipul_modificarii == 3:
                        nota_noua = float(input('Introduceti nota noua la materia "Limba si literatura romana" : '))

                        index_dictionar = lista_catalog.index(rezulatul_cautarii)

                        rezulatul_cautarii.update({'NOTA ROMANA':nota_noua})

                        nota_romana = rezulatul_cautarii['NOTA ROMANA']
                        nota_matematica = rezulatul_cautarii['NOTA MATEMATICA']
                        nota_engleza = rezulatul_cautarii['NOTA ENGLEZA']

                        media_recalculata = round(((nota_romana + nota_matematica + nota_engleza)/3),2)

                        rezulatul_cautarii.update({'MEDIA':media_recalculata})

                        lista_catalog[index_dictionar] = rezulatul_cautarii
                        print('Modificarile au fost efectuate cu succes! Noile date ale elevului sunt urmatoarele: ')
                        print(rezulatul_cautarii)

                    elif tipul_modificarii == 4:
                        nota_noua = float(input('Introduceti nota noua la materia "Matematica" : '))

                        index_dictionar = lista_catalog.index(rezulatul_cautarii)

                        rezulatul_cautarii.update({'NOTA MATEMATICA':nota_noua})
                        
                        nota_romana = rezulatul_cautarii['NOTA ROMANA']
                        nota_matematica = rezulatul_cautarii['NOTA MATEMATICA']
                        nota_engleza = rezulatul_cautarii['NOTA ENGLEZA']

                        media_recalculata = round(((nota_romana + nota_matematica + nota_engleza)/3),2)

                        rezulatul_cautarii.update({'MEDIA':media_recalculata})

                        lista_catalog[index_dictionar] = rezulatul_cautarii
                        print('Modificarile au fost efectuate cu succes! Noile date ale elevului sunt urmatoarele: ')
                        print(rezulatul_cautarii)

                    elif tipul_modificarii == 5:
                        nota_noua = float(input('Introduceti nota noua la materia "Engleza" : '))

                        index_dictionar = lista_catalog.index(rezulatul_cautarii)

                        rezulatul_cautarii.update({'NOTA ENGLEZA':nota_noua})

                        nota_romana = rezulatul_cautarii['NOTA ROMANA']
                        nota_matematica = rezulatul_cautarii['NOTA MATEMATICA']
                        nota_engleza = rezulatul_cautarii['NOTA ENGLEZA']

                        media_recalculata = round(((nota_romana + nota_matematica + nota_engleza)/3),2)

                        rezulatul_cautarii.update({'MEDIA':media_recalculata})
                        lista_catalog[index_dictionar] = rezulatul_cautarii
                        print('Modificarile au fost efectuate cu succes! Noile date ale elevului sunt urmatoarele: ')
                        print(rezulatul_cautarii)
                    else:
                        print('Nu ati introdus o operatiune valida. Reincercati!')

            else:
                print('Elevul cautat nu a fost gasit in catalog! Verificati datele introduse! ')
            
            iesire = input('Doriti sa mai efectuati o alta modificare? (Da/Nu - iesire in meniul principal) : ').lower()=='nu'
            if iesire:
                break

    elif optiunea_aleasa_de_utilizator == 4: #Stergere elev dupa nume si prenume
        
        while True: 
            rezulatul_cautarii = functie_cautare_elev('default','default')

            if rezulatul_cautarii != False:

                print('Datele elevului cautat sunt urmatoarele : ')
                print(rezulatul_cautarii)
                stergere_elev = input('Doriti stergerea elevului respectiv? (Da/Nu) ').lower() == 'da'
    
                if stergere_elev:
                    
                    lista_catalog.remove(rezulatul_cautarii)
                    
                    print('Datele elevului au fost sterse cu succes! ')
    
            else:
                print('Elevul cautat nu a fost gasit! Verificati datele introduse')

            iesire = input('Pentru iesirea in meniul principal introduceti "x" :').lower() == 'x'
            if iesire:
                break

    elif optiunea_aleasa_de_utilizator == 5: #Cautare elev dupa nume si prenume
        
        while True:
            print(functie_cautare_elev('default','default'))
            inchidere_previzualiare = input('Introduceti "x" in cazul in care doriti inchiderea previzualizarii datelor elevului cautat : ').lower() == 'x'
            if inchidere_previzualiare:
                break
    
    elif optiunea_aleasa_de_utilizator == 6: # Afisare elevi in ordinea mediei

        while True:
            lista_sortata = sorted(lista_catalog, key=functie_sortare_dupa_medie, reverse=True)

            print('Catalogul sortat in functie de media fiecarui elev este : ')

            for element in lista_sortata:
                print(element)
        
            inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 7: # Afisare elevi cu media peste 8
        while True:
            x = ''
            for element in lista_catalog:
                if element['MEDIA'] > 8:
                    print(element)

            inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 8: # Afisare elevi in ordine alfabetica (in functie de Nume)

        while True:
            lista_sortata = sorted(lista_catalog, key=functie_sortare_dupa_nume, reverse=False)

            print('Catalogul sortat in functie de numele fiecarui elev este : ')

            for element in lista_sortata:
                print(element)
        
            inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 9: #Iesire din aplicatie
        print('La nevedere!')
        break

            




