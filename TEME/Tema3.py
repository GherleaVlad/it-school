
print('Calculator')

def adunare(nr1,nr2):
    return nr1 + nr2
def scadere(nr1,nr2):
    return nr1 - nr2
def inmultire(nr1,nr2):
    return nr1 * nr2
def impartire(nr1,nr2):
    return nr1 / nr2


while True:

    calcul = input('Introduceti numerele si operatiunea dorita : ')

    if calcul.upper() == 'EXIT':
        break

    if len(calcul) < 5:
        print('Nu ati introdus date valide! Datele trebuie sa fie de forma "a + b" ! Reincercati! ')
    elif ' ' not in calcul:
        print('Nu ati introdus date valide! Datele trebuie sa fie de forma "a + b" ! Reincercati! ')
    else:
        impartirea_datelor = calcul.split(' ')
        nr1 = impartirea_datelor[0].strip()
        nr2 = impartirea_datelor[2].strip()
        operator = impartirea_datelor[1].strip()

        nr1 = float(nr1)
        nr2 = float(nr2)

        if operator == '+':
            print(adunare(nr1,nr2))
        elif operator == '-':
            print(scadere(nr1,nr2))
        elif operator == '*':
            print(inmultire(nr1,nr2))
        elif operator == '/':
            print(impartire(nr1,nr2))
        else:
            print('Nu ati introdus o operatiune matematica valida! Reincercati! ')



    
