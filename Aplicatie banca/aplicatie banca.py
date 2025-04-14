
import random as random

class Client:
    def __init__(self,numeclient,prenumeclient,CNP,IBAN,sold=0):
        self.numeclient = numeclient
        self.prenumeclient = prenumeclient
        self.CNP = CNP
        self.IBAN= IBAN
        self.sold = sold

    def __str__(self):
        return f'Clientul :\nNume: {self.numeclient}\nPrenume: {self.prenumeclient}\nCNP : {self.CNP}\nIBAN : {self.IBAN}\nSold: {self.sold}'

class BazaDeDate:
    ''' In cadrul clasei sunt aduse date din fisiere json (pentru a vedea baza de date cu clientii) si sunt scrise in baza de date cu clientii noile inregistrari'''
    pass

class Banca:
    def generare_iban():
        '''Pentru clientii noi aceasta functie genereaza un IBAN (13 caractere)'''
        base = 'RO01BGV'
        cod = ''.join(str(random.randint(0, 9)) for _ in range(6))

        return base+cod

    def adaugare_client_nou():
        while True:
            nume = input("Introdu numele clientului: ").title()
            prenume = input("Introdu prenumele clientului: ").title()
            while True:
                cnp_introdus = input('Introduceti codul numeric al clientului: ')
                if len(cnp_introdus) == 13 and cnp_introdus.isdigit():
                    cnp = cnp_introdus
                    break
                else:
                    print('Codul numeric personal al clientului trebuie sa aiba 13 cifre! Reintroduceti CNP! ')
            iban = Banca.generare_iban()
            while True:
                sold_introdus = float(input("Soldului clientului: ") or 0)
                if sold_introdus >= 0:
                    sold = sold_introdus
                else:
                    print('Soldul clientului nu poate fi negativ!')
                break
            
            while True:
                adaugare = input(f'Datele clientului introdus sunt urmatoarele : {nume}, {prenume}, {cnp}, {iban}, {sold}. Doriti adaugare acestuia in registrul clientilor? (Da/Nu) : ').lower() == 'da'
                if adaugare:                
                    return Client(nume, prenume, cnp, iban, sold)
                else:
                    continuare_introducere = input(f'Clientul nu a fost adaugat. Doriti adaugarea unui alt client? (Da/Nu) : ').lower() == 'da'
                    if not continuare_introducere:
                        return f'Operatiune anulata! '
                    
                
    def cautare_client():
        pass
    
    def adaugare_bani():
        pass
    
    def retragere_bani():
        pass

class Rapoarte:
    pass



