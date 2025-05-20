
import tkinter
import baza_de_date
import utilities
from fereastra_autentificare import FereastraAutentificare
from meniu_principal import MeniuPrincipal

if __name__ == '__main__':
    baza_de_date.creare_tabela_operatori()
    baza_de_date.creare_tabela_pacienti()
    app = MeniuPrincipal()
    app.mainloop()


# admin    
