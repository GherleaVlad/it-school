# TEMA 03.03.2025

# 21) Sa se numere de cate ori apare o litera intr-un cuvant. (folositi for si while)
# CU FOR
cuvant = 'paralelipiped'
x = 0
for element in cuvant:
    if element == 'p':
        x+=1
print(x)

# CU WHILE

while x < len(cuvant):
    x+=1
    if cuvant[x] == 'p':
        print(x)



# 22) Sa se afiseze toate numerele pare pana la 100
x=0
while x in range(0,101):
    x+=1
    if x % 2 == 0:
        print(x)

# 23) Sa se afiseze toate numerele impare pana la 50.
# CU FOR
for x in range(0,50):
    if x % 2 != 0 and x < 50:
        print(x)

# 24) Sa se afiseze toate puterile lui 2 mai mici decat 150.

x = 0
while 2 ** x < 150:
    print(f'{x} e o putere a lui 2 mai mica decat 150 deoarece {2 ** x} este rezultatul ridicarii lui 2 la puterea {x}')
    x += 1

# 25) Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.
x = 0
while True:
    if 3 ** x >= 200 and 3 ** x <= 300:
        print(f'{x} e o putere a lui 3 deoarece {3 ** x} este rezultatul ridicarii lui 3 la puterea {x}')
    x+=1

# 26) Se citeste un numar de la tastatura. Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)

numar = int(input('Baga aici un numar : '))
# CU FOR
y = numar + 1
x = 0
for element in range(0,y): 
    x += element
print(x)

# CU WHILE
z = 0
while x < numar:
    x+=1
    z+=x
    print(z)

#  27) Se citeste un numar de la tastatura. Sa se calculeze produsul numerelor de la 1 pana la numarul citit. (folositi for si while)
numar = int(input('Baga aici un numar : '))
# CU FOR
y = numar + 1
x = 1
for element in range(1,y): 
    x *= element
    print(x)

# CU WHILE
z = 1
while x < numar:
    x+=1
    z*=x
    print(z)

# 28) Se citeste un numar n de la tastatura. Sa se scrie un program care face o numaratoare inversa de la numarul respectiv pana la 0.

# 29) Se citeste un numar de la tastatura. Sa se afiseze toti divizorii acestuia. -- DONE
# CU WHILE
numar = int(input('Baga un numar : '))
x = 0
while True:
    x += 1
    if numar % x == 0:
        print(f'{x} este divizor a lui {numar}')

# 30) Se citeste un numar intreg de la tastatura. Sa se afiseze pe rand fiecare cifra a acestuia folosind un while. -- DONE

numar = int(input('Baga un numar : '))
numarconvertit = str(numar)
for x in numarconvertit:
    print(x)


