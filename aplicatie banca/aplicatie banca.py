
import random as random
import json as json

class Client:
    def __init__(self,nume,prenume,CNP,IBAN,sold=0):
        self.numeclient = nume
        self.prenumeclient = prenume
        self.CNP = CNP
        self.IBAN= IBAN
        self.sold = sold

    def __str__(self):
        return f'Clientul :\nNume: {self.numeclient}\nPrenume: {self.prenumeclient}\nCNP : {self.CNP}\nIBAN : {self.IBAN}\nSold: {self.sold}'
    
    def client_to_dict(self):
         return {
            'nume': self.numeclient,
            'prenume': self.prenumeclient,
            'CNP': self.CNP,
            'IBAN': self.IBAN,
            'sold': self.sold
        }

class BazaDeDate:
    ''' In cadrul clasei sunt aduse date din fisiere json (pentru a vedea baza de date cu clientii) si sunt scrise in baza de date cu clientii noile inregistrari'''

    def get_clienti(fisier_json = r'C:\Users\vlad.gherlea\Desktop\aplicatie banca\clienti.json'):
        with open(fisier_json, 'r') as json_bd_clienti:
            baza_de_date_clienti = json.load(json_bd_clienti)
        return list(baza_de_date_clienti)

    def set_client(client,bd_clienti = r'C:\Users\vlad.gherlea\Desktop\aplicatie banca\clienti.json'):

        bd = BazaDeDate.get_clienti()

        client_dictionar = Client.client_to_dict(client)

        exista = False
        for clienti in bd:
            if client_dictionar.get('CNP') == clienti.get('CNP'):
                exista = True

        if exista:
            print('Clientul exista deja in baza de date! Operatiune anulata!')
        
        else:
            bd.append(client_dictionar)

            with open(bd_clienti, 'w') as json_bd_client:
                json.dump(bd,json_bd_client,indent=4)
            
            print(f'{client}\nA fost adaugat cu succes!')
        
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
                     
            return Client(nume,prenume,cnp,iban,sold)
             
    def cautare_client():
        
        cnp_cautat = input('Introduceti CNP pentru cautare: ')
        bd = BazaDeDate.get_clienti()

        exista = False
        for clienti in bd:
            if clienti.get('CNP') == cnp_cautat:

                exista = True
# aici am ramas
                if exista:
                    print('-'*50)
                    for client,date in clienti.items():
                        print(f'{client} : {date}')
                    print('-'*50)
            else:
                print(F'Nu a fost gasit un client in baza de date cu CNP : {cnp_cautat}')
                    


    
    def adaugare_bani():
        pass
    
    def retragere_bani():
        pass

class Rapoarte:
    pass

client = Banca.cautare_client()

