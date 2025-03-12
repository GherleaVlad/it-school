
print('Bine ati venit! ')

catalog = list()

# Pentru teste
catalog = [['Gherlea','Vlad',10,10,10,10],['Anca','Nechiti',8,7,8,8.7]]

# functie pentru introducerea datelor unui elev
def functie_introducere_elev(nume, prenume, nota_romana,nota_matematica,nota_engleza):
    nume = input('Numele elevului : ')
    prenume = input('Prenumele elevului : ')
    nota_romana = float(input('Nota pentru materia "Limba si literarura romana" : '))
    nota_matematica = float(input('Nota pentru materia "Matematica" : '))
    nota_engleza = float(input('Nota pentru materia "Engleza" : '))
    media = round(((nota_romana + nota_matematica + nota_engleza)/3),2)

    return nume,prenume,nota_romana,nota_matematica,nota_engleza,media


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

    if optiunea_aleasa_de_utilizator == 9:
        print('La nevedere!')
        break

    if optiunea_aleasa_de_utilizator == 1:
        x = True
        while x == True:
        
            print('Ati ales operatiunea "1. Adaugare elev"\nIntroduceti datele necesare:')

            lista_date_elev = list(functie_introducere_elev('default','default',0,0,0))
        
            print(f'Datele introduse sunt urmatoarele: {lista_date_elev} ! ') 
            commit_modificari = input('Doriti adaugarea lor in catalog? (Da/Nu) : ').lower() == 'da'

            if commit_modificari:
                catalog.append(lista_date_elev)
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
        previzualizare = True
        while previzualizare == True:
            for element in catalog:
                print(element)
            
            inchidere_previzualiare = input('Introduceti "x" in cazul in care doriti inchiderea previzualizarii catalogului : ').lower() == 'x'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 3:
        print('x')


            




