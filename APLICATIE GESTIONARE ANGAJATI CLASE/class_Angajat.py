
class Angajat:
    def __init__(self,numeangajat,prenumeangajat,CNP,varsta,salar,departament,senioritate):
        self.numeangajat = numeangajat
        self.prenumeangajat = prenumeangajat
        self.CNP = CNP
        self.varsta = varsta
        self.salar = salar
        self.departament = departament
        self.senioritate = senioritate

    def citire_date_angajat():
        while True:
            try:    
                numeangajat = input('Introduceti numele angajatului : ').title()
                prenumeangajat = input('Introduceti prenumele angajatului : ').title()

                while True:
                    cnp_introdus = input('Introduceti codul numeric personal al angajatului: ')
                    if len(cnp_introdus) == 13 and cnp_introdus.isdigit():
                        CNP = cnp_introdus
                        break
                    else:
                        print('EROARE: Codul numeric personal al angajatului trebuie sa fie format din 13 cifre!')
                        print('INFO: Reintroduceti codul numeric al angajatului! ')
                
                while True:
                    varsta_introdusa = int(input('Introduceti varsta angajatului: '))
                    if varsta_introdusa< 18 or varsta_introdusa > 65:
                        print('EROARE: Varsta angajatului trebuie sa fie cuprinsa in intervalul 18 - 65 ani! ')
                        print('INFO: Reintroduceti datele! ')
                    else:
                        varsta = varsta_introdusa
                        break

                while True:
                    salariu_introdus = float(input('Introduceti salariul brut al angajatului: '))

                    if salariu_introdus >= 4050:
                        salariu = salariu_introdus
                        break
                    else:
                        print('EROARE: Salariul brut nu poate fi mai mic de 4050 lei! ')
                        print('INFO: Reintroduceti datele! ')
                
                while True:

                    print('''
Alegeti departamentul angajatului introducand cifra aferenta acestuia: 
    1. Contabilitate
    2. Resurse umane
    3. Marketing
    4. IT
    5. Vanzari                     
                          ''')

                    departament_introdus = int(input('Optiune departament: '))

                    if departament_introdus == 1:
                        departament = 'Contabilitate'
                        break
                    elif departament_introdus == 2:
                        departament = 'Resurse umane'
                        break
                    elif departament_introdus == 3:
                        departament = 'Marketing'
                        break
                    elif departament_introdus == 4:
                        departament = 'IT'
                        break
                    elif departament_introdus == 5:
                        departament = 'Vanzari'
                        break
                    else:
                        print('EROARE: Nu ati introdus o optiune valida! ')
                        print('INFO: Reintroduceti o optiune! ')

                while True:
                    print('''
Alegeti senioritatea angajatului introducand cifra aferenta acesteia:
    1. Junior
    2. Middle
    3. Senior
                    ''')

                    senioritate__introdusa = int(input('Optiune senioritate: '))
                    
                    if senioritate__introdusa == 1:
                        senioritate = 'Junior'
                        break
                    elif senioritate__introdusa == 2:
                        senioritate = 'Middle'
                        break
                    elif senioritate__introdusa == 3:
                        senioritate = 'Senior'
                        break
                    else:
                        print('EROARE: Nu ati introdus o optiune valida! ')
                        print('INFO: Reintroduceti o optiune! ')

            except ValueError:
                print('EROARE: Ultimele date introduse nu sunt valide! ')
                print('INFO: Reintroduceti datele! ')   

            return Angajat(numeangajat,prenumeangajat,CNP, varsta,salariu,departament,senioritate)

    def prezentare_angajat(self):
        print(50 * '-')
        print(f'ANGAJATUL:\nNUME: {self.numeangajat}\nPRENUME: {self.prenumeangajat}\nCNP : {self.CNP}\nVARSTA : {self.varsta}\nSALAR: {self.salar}\nDEPARTAMENT: {self.departament}\nSENIORITATE: {self.senioritate}')
        print(50 * '-')

    def angajat_to_dict(self):
         return {
            'NUME': self.numeangajat,
            'PRENUME': self.prenumeangajat,
            'CNP': self.CNP,
            'VARSTA': self.varsta,
            'SALAR': self.salar,
            'DEPARTAMENT' : self.departament,
            'SENIORITATE' : self.senioritate
        }


def main():
    angajat = Angajat.citire_date_angajat()
    Angajat.prezentare_angajat(angajat)

if __name__ == "__main__":
    main()

