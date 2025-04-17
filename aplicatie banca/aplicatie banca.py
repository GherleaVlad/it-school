
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

    def get_clienti(fisier_json = r'C:\Users\vladg\OneDrive\Documents\GitHub\it-school\aplicatie banca\clienti.json'):
        with open(fisier_json, 'r') as json_bd_clienti:
            baza_de_date_clienti = json.load(json_bd_clienti)
        return list(baza_de_date_clienti)

    def set_client_nou(client,bd_clienti = r'C:\Users\vladg\OneDrive\Documents\GitHub\it-school\aplicatie banca\clienti.json'):

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
    
    def set_client_modificari(bd_modificata, bd_clienti = r'C:\Users\vladg\OneDrive\Documents\GitHub\it-school\aplicatie banca\clienti.json'):
        with open(bd_clienti, 'w') as json_bd_client:
            json.dump(bd_modificata,json_bd_client,indent=4)
        
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
        for client in bd:
            if client.get('CNP') == cnp_cautat:
                client_cautat = client
                exista = True
        if exista:
            print('-'*50)
            for client,date in client_cautat.items():
                print(f'{client.upper()} : {date}')
            print('-'*50)
            
        if not exista:
            print(f'Nu a fost gasit un client in baza de date cu CNP : {cnp_cautat}')
                    
    def depunere_bani():
        bd = BazaDeDate.get_clienti()
        cnp_cautat = input('Introduceti CNP pentru cautare: ')
        exista = False
        for client in bd:
            if client.get('CNP') == cnp_cautat:
                date_modificare = client
                exista = True
                break

        if not exista:
            print(f'Nu a fost gasit un client in baza de date cu CNP : {cnp_cautat}')
        else:
            index_dict_client = bd.index(date_modificare)
            suma_depusa = float(input('Introduceti suma depusa: '))
            sold_nou = date_modificare.get('sold') + suma_depusa
            date_modificare.update({'sold': sold_nou})
            bd[index_dict_client] = date_modificare

            BazaDeDate.set_client_modificari(bd)
    
    def retragere_bani():
        bd = BazaDeDate.get_clienti()
        cnp_cautat = input('Introduceti CNP pentru cautare: ')
        exista = False
        for client in bd:
            if client.get('CNP') == cnp_cautat:
                date_modificare = client
                exista = True
                break

        if not exista:
            print(f'Nu a fost gasit un client in baza de date cu CNP : {cnp_cautat}')
        else:
            index_dict_client = bd.index(date_modificare)
            suma_retrasa = float(input('Introduceti suma depusa: '))
            sold_nou = date_modificare.get('sold') - suma_retrasa
            date_modificare.update({'sold': sold_nou})
            bd[index_dict_client] = date_modificare

            BazaDeDate.set_client_modificari(bd)

class Rapoarte:
    pass

def main():
    # Functionalitatea efectiva a programului

    while True:
        optiune = int(input('''
Selectati una dintre variantele de mai jos aferenta operatiunii dorite:
        1. Adaugare client nou
        2. Cautare client
        3. Depunere bani (pe baza CNP)
        4. Retragere bani (pe baza CNP)
        5. Iesire din program
                                
Optiune aleasa: '''))
        if optiune == 1:
            while True:
                client = Banca.adaugare_client_nou()
                BazaDeDate.set_client_nou(client)
                
                continuare_adaugare = input('Doriti adaugarea unui alt client? (Da/Nu) : ').lower() == 'da'

                if not continuare_adaugare:
                    break
        elif optiune == 2:
            while True:
                Banca.cautare_client()
                continuare_cautare = input('Doriti cautarea unui alt client? (Da/Nu) : ').lower() == 'da'

                if not continuare_cautare:
                    break
        elif optiune == 3:
            Banca.depunere_bani()
            continuare_depunere = input('Doriti efectuarea unei alte depuneri? (Da/Nu) : ').lower() == 'da'

            if not continuare_depunere:
                break
        
        elif optiune == 4:
            Banca.retragere_bani()
            continuare_retragere = input('Doriti efectuarea unei alte retrageri? (Da/Nu) : ').lower() == 'da'

            if not continuare_retragere:
                break
        elif optiune == 5:
            break
        else:
            print('Nu ati ales o optiune valida')

if __name__ == "__main__":
    main()

