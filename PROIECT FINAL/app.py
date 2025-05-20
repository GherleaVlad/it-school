
import baza_de_date
from meniu_principal import MeniuPrincipal

if __name__ == '__main__':
    baza_de_date.creare_tabela_operatori()
    baza_de_date.creare_tabela_pacienti()
    app = MeniuPrincipal()
    app.mainloop()
