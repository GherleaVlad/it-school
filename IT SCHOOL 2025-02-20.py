
# x = float(input('Introdu un numar : '))

# if x % 3 == 0 and x % 5 == 0: 
#     print('FIZZBUZZ')
# elif x % 3 == 0:
#     print('FIZZ')
# elif x % 5 == 0:
#     print('BUZZ')
# else:
#     print('Nu-i divizibil')

# x = "Nume: Daniel, Prenume: Neamtiu"

# y = x.split(' ')
# print(y)
# print(y[1].strip(','))
# print(y[3])

# x = "Ana are 10 mingi de fotbal intergalactic"
# # x[5] = '!'
# x = x.replace('Ana','Marcela')
# print(x)
# # y = x.replace('intergalactic','')
# # print(y)


# parola = input('Va rugam introduceti o parola : ')

# if len(parola) >= 10 and ' ' not in parola:
#     print('OK')
# if len(parola) < 10:
#     print('Parola nu are 10 caractere')
# if ' ' in parola:
#     print('Parola contine spatii')



# Password = input("Introdu parola:")
# Lungime_Password = len(Password)
# Spatiu_Password = Password.find(" ")

# if Lungime_Password < 10 and (Spatiu_Password != -1 or Spatiu_Password >= 0):
#     Mesaj = "Parola trebuie sa contina cel putin 10 caractere si sa nu contina spatii!"

# elif Lungime_Password < 10 and Spatiu_Password == -1:
#     Mesaj = "Parola trebuie sa contina cel putin 10 caractere!"

# elif Lungime_Password > 10 and (Spatiu_Password != -1 or Spatiu_Password >= 0):
#     Mesaj = "Parola nu treb uie sa contina spatii!"
# else:
#     Mesaj = "Ok."


# print(Mesaj)



'''
Se citeste un numar intreg de la tastatura. 
Sa se verifice daca numarul este palindrom(ex: 123321, 12321 - are aceeasi valoarea citit si dintr-o parte si din alta) 
si sa se afiseze un mesaj corespunzator.
'''

numar = 123321
numar = str(numar)

if (numar == numar[::-1]):
    print("Este polindrom")
else:
    print("Nu este polindrom")

