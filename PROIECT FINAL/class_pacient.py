
class Pacient:

    def __init__(self, numepacient, prenumepacient, cnp, sex, asigurat, datanasterii, varsta):
        self.numepacient = numepacient
        self.prenumepacient = prenumepacient
        self.cnp = cnp
        self.sex = sex
        self.asigurat = asigurat
        self.datanasterii = datanasterii
        self.varsta = varsta

    def prezentare_pacient(self):
        delimitator = 30 * '-'
        afisaj = f'\n{delimitator}\nNume: {self.numepacient}\nPrenume: {self.prenumepacient}\nCNP: {self.cnp}\nSex: {self.sex}\nAsigurat: {self.asigurat}\nData Nasterii: {self.datanasterii}\nVarsta: {self.varsta}\n{delimitator}'
        print(afisaj)


def main():
    
    pacient = Pacient('Gherlea','Vlad','1111','M','True','21.04.1999','26')
    print(pacient)
    Pacient.prezentare_pacient(pacient)

if __name__ == '__main__':
    main()


