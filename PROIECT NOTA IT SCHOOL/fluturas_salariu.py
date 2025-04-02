'''
Functia din cadrul acestui modul, genereaza fluturasul de salariu pentru un angajat. Functia isi ia ca si parametru lista_angajati (registrul nostru de angajati),
iar cautarea angajatului pentru care dorim sa generam un fluturas de salariu se va face prin introducerea CNP-ului aferent acestui angajat.
Calculele prin care ajungem la salariul net din salariul brut sunt in functie de cotele de impozitare din Romania, si anume 10% CAS, 25% CASS respectiv 10% IMPOZIT PE SALAR.
'''

def functie_fluturas_salariu(lista_angajati):

    cnp_cautat = input('Introduceti CNP-ul angajatului pentru care doriti generarea fluturasului de salariu : ')
    gasit = False
    fluturas_angajat = dict()

    for angajat in lista_angajati:
        if angajat['CNP'] == cnp_cautat:
            fluturas_angajat = angajat
            gasit = True
            break

    if not gasit:
        return (f'Nu a fost gasit nici un angajat cu CNP : {cnp_cautat} !')
    else:

        salariul_brut = fluturas_angajat.get('Salariu angajat')

        cas = salariul_brut * 0.10
        cass = salariul_brut * 0.25
        baza_impozit = salariul_brut - (cas + cass)
        impozit = baza_impozit * 0.10

        salariul_net = salariul_brut - (cas+cass+impozit)

        nume_angajat = fluturas_angajat.get('Nume angajat')
        prenume_angajat = fluturas_angajat.get('Prenume angajat')

        fluturas = (f'''
        FLUTURASUL DE SALARIU PENTRU ANGAJATUL:
        NUME: {nume_angajat}
        PRENUME : {prenume_angajat}
        CNP : {cnp_cautat}

        SALARIU BRUT : {salariul_brut} 
        
        CAS........................................{cas} (10%)
        CASS.......................................{cass} (25%)
        IMPOZIT....................................{impozit} (10% DIN BAZA IMPOZABILA : {baza_impozit})

        SALARIU NET: {salariul_net}

    ''')

        return fluturas


